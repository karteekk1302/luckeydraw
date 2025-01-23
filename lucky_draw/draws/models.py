from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class DrawResult(models.Model):
    date = models.DateField()
    time = models.TimeField()
    royal = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)]
    )
    deluxe = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)]
    )
    casino = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)]
    )
    express = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)]
    )
    gold_play = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)]
    )
    name = models.CharField(max_length=100, default='laxmi')

    def __str__(self):
        return f"{self.date} {self.time} - Royal: {self.royal}, Deluxe: {self.deluxe}, Casino: {self.casino}, Express: {self.express}, Gold Play: {self.gold_play}"