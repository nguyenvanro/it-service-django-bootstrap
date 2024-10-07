from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Tên khách hàng')
    email = models.EmailField(verbose_name='Email khách hàng')
    description =  models.CharField(max_length=1024, blank=True, null=True, verbose_name='Nội dung')
    
    def __str__(self):
        return str(self.name)


    class Meta:
        verbose_name_plural = '01. Liên hệ'
