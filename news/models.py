from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Новая новость')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Статья')
    data = models.DateField('Дата публикации')
    def __str__(self):
        return self.title
    class Mets:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'




