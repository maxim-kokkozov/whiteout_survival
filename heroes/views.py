from django.shortcuts import render, get_object_or_404
from .models import Hero


def hero_list(request):
    """Список всех героев (карточки: имя + картинка)."""
    heroes = Hero.objects.all()
    return render(request, "heroes/hero_list.html", {"heroes": heroes})


def hero_detail(request, pk):
    """Подробная информация о герое."""
    hero = get_object_or_404(
        Hero.objects.prefetch_related("research_skills", "expedition_skills"),
        pk=pk,
    )
    return render(request, "heroes/hero_detail.html", {"hero": hero})