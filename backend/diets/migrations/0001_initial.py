# Generated by Django 4.1.7 on 2023-06-12 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_alter_bodyinforecord_user_alter_userbodyinfo_user'),
        ('meals', '0001_initial'),
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('kcal', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('carbs', models.IntegerField(default=0)),
                ('meal_count', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.foodcategory')),
                ('meals', models.ManyToManyField(to='meals.meal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeekDiet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('kcal', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('carbs', models.IntegerField(default=0)),
                ('meal_count', models.IntegerField(default=0)),
                ('bodyinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userbodyinfo')),
                ('categories', models.ManyToManyField(to='foods.foodcategory')),
                ('diets', models.ManyToManyField(to='diets.diet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultiURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('WeekDiet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diets.weekdiet')),
            ],
        ),
    ]
