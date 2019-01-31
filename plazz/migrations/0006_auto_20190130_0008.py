# Generated by Django 2.1.5 on 2019-01-29 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plazz', '0005_auto_20190129_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='max',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='min',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plazz.Form'),
        ),
    ]