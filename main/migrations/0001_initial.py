# Generated by Django 2.1.2 on 2018-10-21 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Competitor')),
            ],
        ),
        migrations.CreateModel(
            name='RatingTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.RatingTable'),
        ),
    ]