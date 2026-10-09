from django.contrib import admin
from .models import Skill, Hero

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "generation", "health", "attack_research", "attack_expedition")
    list_filter = ("generation",)
    search_fields = ("name",)
    filter_horizontal = ("research_skills", "expedition_skills")