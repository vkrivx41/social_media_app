from django.shortcuts import render, HttpResponse

from decouple import config

from abc import ABC
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Renderer(ABC):
    app_name: str
    title_suffix: str = field(default=config("WEBSITE_NAME", default="FENOMENO"))

    def render(self, request, template: str, context: dict | None = None) -> HttpResponse:
        if context is None:
            context = {}

        # append the website name to the context before rendering
        context["website_name"] = config("WEBSITE_NAME", default="FENOMENO")

        if "title" not in context:
            context["title"] = config("WEBSITE_NAME", default="FENOMENO", cast=str)

        return render(
            request=request,
            template_name=template,
            context=context
        )
    
    # def get_user_info(self, user_id: int):
