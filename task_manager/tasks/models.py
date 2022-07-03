from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser


class Task(models.Model):
    name = models.CharField(
        'Имя',
        max_length=150,
        db_index=True
    )
    description = models.TextField('Описание')
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name='Статус'
    )
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Исполнитель',
        related_name='executor'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='author'
    )
    # label = models.CharField('Метка', max_length=20)
    date_created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
