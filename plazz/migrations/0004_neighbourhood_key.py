# Generated by Django 2.1.5 on 2019-01-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plazz', '0003_auto_20190129_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='key',
            field=models.CharField(max_length=255, null=True),
        ),
    ]