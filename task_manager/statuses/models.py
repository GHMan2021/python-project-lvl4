from django.db import models


class Status(models.Model):
    name = models.CharField(
        'Имя',
        max_length=20,
        db_index=True
    )
    date_created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
