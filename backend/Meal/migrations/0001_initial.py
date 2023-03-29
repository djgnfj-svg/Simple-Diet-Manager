# Generated by Django 4.1.7 on 2023-03-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('total_kcal', models.IntegerField()),
                ('tital_protein', models.IntegerField()),
                ('total_fat', models.IntegerField()),
                ('total_carbs', models.IntegerField()),
                ('meal_video', models.URLField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('foods', models.ManyToManyField(related_name='meals', to='food.food')),
            ],
        ),
    ]