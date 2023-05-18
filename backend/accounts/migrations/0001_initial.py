# Generated by Django 4.1.7 on 2023-05-16 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBodyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('activity', models.CharField(max_length=50)),
                ('general', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BodyInfoRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('activity', models.CharField(max_length=50)),
                ('general', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_body_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='accounts.userbodyinfo')),
            ],
        ),
    ]
