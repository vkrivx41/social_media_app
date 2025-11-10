from django import forms


class DescriptionForm(forms.Form):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Talk to the world...", "cols": 0, "rows": 0}
        ),
        label=""
    )

    def clean_description(self):
        description = self.cleaned_data.get("description")

        if len(description) > 500:
            raise forms.ValidationError(message="Description can't have more than 100 characters")
        
        return description


class PostImageForm(forms.Form):
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={"id": "custom-image-input", "hidden": True}
        ),
        label=""
    )
