# Generated by Django 4.2.4 on 2023-09-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_useruploadeditem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useruploadeditem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]