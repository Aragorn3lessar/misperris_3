# Generated by Django 2.1.3 on 2018-11-28 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=45)),
                ('foto', models.ImageField(upload_to='media', verbose_name='Imágen')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Raza'),
        ),
    ]
