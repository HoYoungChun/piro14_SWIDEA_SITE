from django.db import models

# Create your models here.
class Idea(models.Model):
    title = models.CharField(verbose_name='아이디어명', max_length=100)
    image = models.ImageField(verbose_name='대표 사진', blank=True, null=True)
    content = models.TextField(verbose_name='아이디어 설명')
    interest = models.IntegerField(verbose_name='아이디어 관심도', default=0)
    devtool = models.CharField(verbose_name='예상 개발툴', max_length=100)

    def __str__(self):
        return self.title