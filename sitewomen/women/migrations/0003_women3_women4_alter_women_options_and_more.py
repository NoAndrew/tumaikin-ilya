# Generated by Django 4.2.1 on 2024-08-15 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_women2_remove_women_cat_alter_women_title1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Women3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=255)),
                ('text1', models.CharField(max_length=255)),
                ('text2', models.CharField(max_length=255)),
                ('text3', models.CharField(max_length=255)),
                ('title5', models.CharField(max_length=255)),
                ('title6', models.CharField(max_length=255)),
                ('title2', models.CharField(max_length=255)),
                ('card1', models.CharField(max_length=255)),
                ('card2', models.CharField(max_length=255)),
                ('card3', models.CharField(max_length=255)),
                ('text_card1', models.CharField(max_length=255)),
                ('text_card2', models.CharField(max_length=255)),
                ('text_card3', models.CharField(max_length=255)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(max_length=255)),
                ('content3', models.CharField(max_length=255)),
                ('content4', models.CharField(max_length=255)),
                ('content5', models.CharField(max_length=255)),
                ('content6', models.CharField(max_length=255)),
                ('content7', models.CharField(max_length=255)),
                ('content8', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Достижение учеников',
                'verbose_name_plural': 'Страница сайта "Достижение учеников"',
            },
        ),
        migrations.CreateModel(
            name='Women4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=255)),
                ('title2', models.CharField(max_length=255)),
                ('title3', models.CharField(max_length=255)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(max_length=255)),
                ('content3', models.CharField(max_length=255)),
                ('name_pages', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Главная',
                'verbose_name_plural': 'Страница сайта "Главная"',
            },
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'verbose_name': 'Материал', 'verbose_name_plural': 'Страница сайта "Материал"'},
        ),
        migrations.AlterModelOptions(
            name='women2',
            options={'verbose_name': 'Обо мне', 'verbose_name_plural': 'Страница сайта "Обо мне"'},
        ),
        migrations.RemoveField(
            model_name='women2',
            name='text',
        ),
    ]
