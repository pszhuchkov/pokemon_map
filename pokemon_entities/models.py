from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('название (рус.)', max_length=200)
    title_en = models.CharField(
        'название (англ.)', max_length=200, null=True, blank=True
    )
    title_jp = models.CharField(
        'название (яп.)', max_length=200, null=True, blank=True
    )
    image = models.ImageField('изображение', null=True, blank=True)
    description = models.TextField('описание', blank=True)
    previous_evolution = models.ForeignKey(
        'Pokemon', models.SET_NULL, 'next_evolutions',
        verbose_name='из кого эволюционировал', null=True, blank=True
    )

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE,
        verbose_name='покемон'
    )
    lat = models.FloatField('широта', null=True, blank=True)
    lon = models.FloatField('долгота', null=True, blank=True)
    appeared_at = models.DateTimeField('появился в', null=True, blank=True)
    disappeared_at = models.DateTimeField('исчез в', null=True, blank=True)
    level = models.IntegerField('уровень', null=True, blank=True)
    health = models.IntegerField('здоровье', null=True, blank=True)
    strength = models.IntegerField('сила', null=True, blank=True)
    defence = models.IntegerField('защита', null=True, blank=True)
    stamina = models.IntegerField('выносливость', null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon.title_ru} ({self.pokemon.id})"
