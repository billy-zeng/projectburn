# Generated by Django 3.0.3 on 2020-02-21 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('bmr', models.IntegerField()),
                ('target_weight', models.IntegerField()),
                ('goal', models.CharField(choices=[('Lose weight', 'Lose weight'), ('Maintain weight', 'Maintain weight'), ('Bulk up', 'Bulk up')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Snacks', 'Snacks'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=10)),
                ('total_calories', models.FloatField(default=0)),
                ('total_carbs', models.FloatField(default=0)),
                ('total_fats', models.FloatField(default=0)),
                ('total_proteins', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('calories', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fats', models.FloatField()),
                ('proteins', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='burn.Meal')),
            ],
        ),
    ]
