# Generated by Django 3.2 on 2021-05-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_socialicon_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='maps',
            field=models.TextField(),
        ),
    ]
