# Generated by Django 4.1.2 on 2022-12-09 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('retuned', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.reader')),
            ],
        ),
    ]