from django.shortcuts import render, HttpResponse

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class Renderer(ABC):
    app_name: str

    def render(self, request, template: str, context: dict | None = None) -> HttpResponse:
        if context is None:
            context = {}

        return render(
            request=request,
            template_name=template,
            context=context
        )
    
    # def get_user_info(self, user_id: int):
