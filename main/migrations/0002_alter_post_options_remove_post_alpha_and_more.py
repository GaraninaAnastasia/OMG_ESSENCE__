# Generated by Django 4.2 on 2023-04-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "Данные", "verbose_name_plural": "Данные"},
        ),
        migrations.RemoveField(
            model_name="post",
            name="alpha",
        ),
        migrations.RemoveField(
            model_name="post",
            name="current_value_c1",
        ),
        migrations.RemoveField(
            model_name="post",
            name="current_value_c2",
        ),
        migrations.RemoveField(
            model_name="post",
            name="current_value_c3",
        ),
        migrations.RemoveField(
            model_name="post",
            name="current_value_c4",
        ),
        migrations.RemoveField(
            model_name="post",
            name="current_value_c5",
        ),
        migrations.RemoveField(
            model_name="post",
            name="current_value_c6",
        ),
        migrations.RemoveField(
            model_name="post",
            name="current_value_c7",
        ),
        migrations.RemoveField(
            model_name="post",
            name="current_value_c8",
        ),
        migrations.AddField(
            model_name="post",
            name="komanda",
            field=models.IntegerField(default=0, verbose_name="Команда"),
        ),
        migrations.AddField(
            model_name="post",
            name="programmnaya_sistema",
            field=models.IntegerField(default=0, verbose_name="Программная система"),
        ),
        migrations.AddField(
            model_name="post",
            name="rabota",
            field=models.IntegerField(default=0, verbose_name="Работа"),
        ),
        migrations.AddField(
            model_name="post",
            name="tehnologiya_raboty",
            field=models.IntegerField(default=0, verbose_name="Технология работы"),
        ),
        migrations.AddField(
            model_name="post",
            name="trebovaniya",
            field=models.IntegerField(default=0, verbose_name="Требования"),
        ),
        migrations.AddField(
            model_name="post",
            name="vosmojnost",
            field=models.IntegerField(default=0, verbose_name="Возможность"),
        ),
        migrations.AddField(
            model_name="post",
            name="zainteresovannye_storony",
            field=models.IntegerField(
                default=0, verbose_name="Заинтересованные стороны"
            ),
        ),
    ]
