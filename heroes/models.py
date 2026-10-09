from django.db import models
from django.core.validators import MinValueValidator


class Skill(models.Model):
    """Навык героя (для исследования или экспедиции)."""
    name = models.CharField(
        max_length=100,
        verbose_name="Название навыка"
    )
    description = models.TextField(
        verbose_name="Описание навыка"
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Hero(models.Model):
    """Герой игры."""

    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    generation = models.PositiveIntegerField(
        verbose_name="Поколение",
        validators=[MinValueValidator(1)]
    )

    # Характеристики на исследовании
    attack_research = models.IntegerField(
        verbose_name="Атака на исследовании",
        default=0
    )
    defense_research = models.IntegerField(
        verbose_name="Защита на исследовании",
        default=0
    )
    health = models.IntegerField(
        verbose_name="Здоровье",
        default=100,
        validators=[MinValueValidator(0)]
    )

    # Характеристики на экспедиции
    attack_expedition = models.IntegerField(
        verbose_name="Атака на экспедиции",
        default=0
    )
    defense_expedition = models.IntegerField(
        verbose_name="Защита на экспедиции",
        default=0
    )

    # Списки навыков (M2M)
    research_skills = models.ManyToManyField(
        Skill,
        related_name="heroes_research",
        blank=True,
        verbose_name="Навыки исследования"
    )
    expedition_skills = models.ManyToManyField(
        Skill,
        related_name="heroes_expedition",
        blank=True,
        verbose_name="Навыки экспедиции"
    )

    # Изображение персонажа
    image = models.ImageField(
        upload_to="heroes/images/",
        blank=True,
        null=True,
        verbose_name="Изображение персонажа"
    )

    class Meta:
        verbose_name = "Герой"
        verbose_name_plural = "Герои"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} (поколение {self.generation})"