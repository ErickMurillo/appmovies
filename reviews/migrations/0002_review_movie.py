# Generated by Django 2.2.5 on 2019-09-02 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.Movie'),
            preserve_default=False,
        ),
    ]
