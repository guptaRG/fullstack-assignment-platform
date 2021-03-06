# Generated by Django 2.2.5 on 2019-11-24 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bucket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=256)),
                ('bucket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bucket.Bucket')),
            ],
            options={
                'verbose_name': 'To Do',
                'verbose_name_plural': 'ToDos',
                'db_table': 'to_do',
            },
        ),
    ]
