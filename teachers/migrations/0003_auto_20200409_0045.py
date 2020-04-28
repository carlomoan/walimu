# Generated by Django 3.0.2 on 2020-04-08 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200409_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mitaala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'mitaala',
            },
        ),
        migrations.CreateModel(
            name='MtaalaArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.CharField(blank=True, choices=[('parent', 'PARENT'), ('Level_1_child', 'LEVEL_1_CHILD'), ('Level_2_child', 'LEVEL_2_CHILD')], max_length=50, null=True)),
                ('parent', models.ManyToManyField(blank=True, null=True, related_name='_mtaalaarticles_parent_+', to='teachers.MtaalaArticles')),
            ],
            options={
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='MtaalaHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField()),
                ('articles', models.ManyToManyField(to='teachers.MtaalaArticles')),
                ('mtaala', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Mitaala')),
            ],
        ),
        migrations.RemoveField(
            model_name='darasa',
            name='mtaala',
        ),
        migrations.DeleteModel(
            name='MtaalaArticle',
        ),
        migrations.AddField(
            model_name='darasa',
            name='mitaala',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Mitaala'),
        ),
        migrations.AlterField(
            model_name='umahiri',
            name='mtaala',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Mitaala'),
        ),
    ]
