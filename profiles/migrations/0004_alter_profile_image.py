# Generated by Django 4.2 on 2024-06-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/avatar_ndcfzk.png', upload_to='images/'),
        ),
    ]
