# Generated by Django 2.2 on 2019-04-14 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190414_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='news_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.News'),
        ),
    ]
