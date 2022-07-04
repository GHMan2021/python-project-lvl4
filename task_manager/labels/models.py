from django.db import models


class Label(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=20,
        null=False,
        unique=True,
    )
    date_created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Label'
        verbose_name_plural = 'Labels'
