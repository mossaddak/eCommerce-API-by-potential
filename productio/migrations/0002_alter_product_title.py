# Generated by Django 5.0.3 on 2024-03-31 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
