# Generated by Django 3.2.4 on 2021-07-13 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_alter_link_key'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name'], 'verbose_name': 'Enlace', 'verbose_name_plural': 'enlaces'},
        ),
    ]
