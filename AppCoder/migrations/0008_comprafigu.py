# Generated by Django 4.1 on 2022-10-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_avatar_delete_avatares'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraFigu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oferta', models.TextField(max_length=240)),
            ],
        ),
    ]