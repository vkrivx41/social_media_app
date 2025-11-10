from django.shortcuts import redirect, HttpResponse

from app_contents.models import Post

from app_contents.forms import DescriptionForm, PostImageForm


from app.abstract.Renderer import Renderer
from app.enums.HttpMethods import HttpMethod

class ContentsRenderer(Renderer):
    def home(self, request) -> HttpResponse:
        # redirect from / to posts/
        if request.get_full_path() == "/":
            return redirect(to="app_contents:home")

        posts = Post.objects.all()

        context: dict = {
            'user': request.user,
            'posts': posts,
        }
        
        return self.render(request, "contents/home.html", context)

    def create(self, request) -> HttpResponse:
        user = request.user

        form1 = DescriptionForm()
        form2 = PostImageForm()

        if request.method == HttpMethod.POST:
            form1 = DescriptionForm(request.POST)
            form2 = PostImageForm(request.POST, request.FILES)

            if form1.is_valid() and form2.is_valid():
                form1_data = form1.cleaned_data
                form2_data = form2.cleaned_data

                post = Post(
                    user=user,
                    description=form1_data.get("description"),
                    image=form2_data.get("image"),
                )

                post.save()

                return redirect("app_contents:home")

        context: dict = {
            'user': user,
            'form1': form1,
            'form2': form2,
        }
        
        return self.render(request, "contents/create.html", context)

    def delete(self, request, id: int) -> HttpResponse:
        try:
            post = Post.objects.get(id=id)
            post_author = post.user
        except Post.DoesNotExist:
            return redirect("app_contents:home")
        
        if request.user != post.user:
            return redirect("app_contents:home")

        delete_confirmation: bool = request.GET.get("confirm") == "1"

        if delete_confirmation:
            post.delete()
            return redirect("app_contents:home")
        
        context: dict = {
            'user': post_author,
            'post': post,
        }

        return self.render(request, "contents/delete.html", context)

    def update(self, request, id: int) -> HttpResponse:
        try:
            post = Post.objects.get(id=id)
            post_author = post.user
        except Post.DoesNotExist:
            return redirect("app_contents:home")
        
        if request.user != post.user:
            return redirect("app_contents:home")

        form1 = DescriptionForm(prefix="desc", initial={"description": post.description})
        form2 = PostImageForm(prefix="image", initial={"image": post.image})

        if request.method == HttpMethod.POST:
            form1 = DescriptionForm(request.POST, prefix="desc", initial={"description": post.description})
            form2 = PostImageForm(request.POST, request.FILES, prefix="image", initial={"image": post.image})

            if form1.is_valid() and form2.is_valid():
                form1_data = form1.cleaned_data
                form2_data = form2.cleaned_data

                post.description = form1_data.get("description")
                post.image = form2_data.get("image")

                post.save()

                return redirect("app_contents:home")
            
        context: dict = {
            'user': post_author,
            'form1': form1,
            'form2': form2,
        }
        
        return self.render(request, "contents/update.html", context)
