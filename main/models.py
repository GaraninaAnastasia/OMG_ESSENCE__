from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
#
#
class Post(models.Model):
    # alpha = models.CharField("Сущности", max_length=50)
    # cycle = models.IntegerField("Цикл", default=1)
    zainteresovannye_storony = models.IntegerField("Заинтересованные стороны", default=0)
    vosmojnost = models.IntegerField("Возможность", default=0)
    trebovaniya = models.IntegerField("Требования", default=0)
    programmnaya_sistema = models.IntegerField("Программная система", default=0)
    rabota = models.IntegerField("Работа", default=0)
    komanda = models.IntegerField("Команда", default=0)
    tehnologiya_raboty = models.IntegerField("Технология работы", default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Est(models.Model):
    # alpha = models.CharField("Сущности", max_length=50)
    cycle = models.IntegerField("Цикл", default=1)
    zainteresovannye_storony = models.IntegerField("Заинтересованные стороны", default=0)
    vosmojnost = models.IntegerField("Возможность", default=0)
    trebovaniya = models.IntegerField("Требования", default=0)
    programmnaya_sistema = models.IntegerField("Программная система", default=0)
    rabota = models.IntegerField("Работа", default=0)
    komanda = models.IntegerField("Команда", default=0)
    tehnologiya_raboty = models.IntegerField("Технология работы", default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Данные_"
        verbose_name_plural = "Данные_"
