# Generated by Django 3.1.4 on 2020-12-05 21:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('petsnew', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='test',
            field=models.CharField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsnew.pet'),
        ),
    ]
