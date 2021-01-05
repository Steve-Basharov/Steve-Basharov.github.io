from django.db import models

class job(models.Model):
    tg = models.CharField('Telegram', max_length=50)
    cash = models.CharField('Размер оплаты', max_length=50)
    tex_zad = models.TextField('О проекте')
    def __str__(self):
        return self.cash
