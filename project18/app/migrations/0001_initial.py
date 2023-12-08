# Generated by Django 4.2.6 on 2023-12-08 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('capid', models.IntegerField()),
                ('capname', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('cname', models.CharField(max_length=100)),
                ('capname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.capital')),
            ],
        ),
    ]