from django.db import models

class Review(models.Model):
    name = models.CharField('Имя', max_length=32)
    text = models.CharField('Отзыв', max_length=512)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name = 'Изображение')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name