# Generated by Django 4.1.7 on 2023-04-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('meal_kcal', models.IntegerField(default=0)),
                ('meal_protein', models.IntegerField(default=0)),
                ('meal_fat', models.IntegerField(default=0)),
                ('meal_carbs', models.IntegerField(default=0)),
                ('meal_video', models.URLField(blank=True, max_length=100, null=True)),
                ('meal_img', models.ImageField(blank=True, null=True, upload_to='meal/%Y/%m/%d/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('foods', models.ManyToManyField(related_name='meals', to='foods.food')),
            ],
        ),
    ]
