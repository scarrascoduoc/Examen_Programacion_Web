# Generated by Django 4.0.4 on 2022-07-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_login_id_alter_login_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_pat', models.CharField(max_length=50)),
                ('apellido_mat', models.CharField(max_length=50)),
                ('montos', models.IntegerField(choices=[(1000, '1000'), (5000, '5000'), (10000, '10000'), (20000, '20000')], null=True)),
                ('monto', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
