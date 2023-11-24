from django.db import models


# Create your models here.
class Books(models.Model):
    title = models.CharField(verbose_name='Название', max_length=120,null=False)
    author = models.CharField(verbose_name='Автор', max_length=60,null=False)
    year = models.DateField(verbose_name='Дата издания', auto_now_add=True)
    isbn = models.BigIntegerField(verbose_name='Книжный номер',default=0)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
    
    def __str__(self):
        return f'{self.title}'
    
