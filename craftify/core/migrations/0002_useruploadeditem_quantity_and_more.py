# Generated by Django 4.2.4 on 2023-09-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useruploadeditem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='useruploadeditem',
            name='description',
            field=models.TextField(),
        ),
    ]