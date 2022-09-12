from django.db import models

# Create your models here.

class Contact(models.Model):
    top = models.CharField(max_length=150, verbose_name = 'Топ')
    phone = models.CharField(max_length=64, verbose_name = 'Телефон')
    email = models.EmailField(max_length=254, )#**options)
    map1 = models.TextField(verbose_name = 'Карта1')
    gover = models.TextField(verbose_name = 'Правление', null=True, blank= True)
    audit = models.TextField(verbose_name = 'Ревизия', null=True, blank= True)
    finance = models.TextField(verbose_name = 'Финансы', null=True, blank= True)
    news = models.TextField(verbose_name = 'Новости', null=True, blank= True)
    power = models.TextField(verbose_name = 'Свет', null=True, blank= True)
    body = models.TextField(verbose_name = 'текст новости', null=True, blank= True)
    map2 = models.TextField(verbose_name='Карта2')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", null=True, blank= True)
    file = models.FileField(upload_to="file/%Y/%m/%d/", verbose_name="Файл", null=True, blank= True)
    date = models.DateField(verbose_name = 'изменен')#auto_now=True)
    def __str__(self):
        return self.top
    # def __dir__(self):
    #     return ['top','body','author','file','time_update','slug']
    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_slug': self.slug})
    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
