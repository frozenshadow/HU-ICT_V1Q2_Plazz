# Generated by Django 2.1.5 on 2019-01-28 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOption',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('disabled', models.BooleanField()),
                ('selected', models.BooleanField()),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('enabled', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('label', models.CharField(max_length=255)),
                ('required', models.BooleanField()),
                ('fieldtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plazz.FieldType')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plazz.Form', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='fieldoption',
            name='formfield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plazz.FormField', unique=True),
        ),
    ]
