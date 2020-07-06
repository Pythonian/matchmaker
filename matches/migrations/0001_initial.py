# Generated by Django 3.0.8 on 2020-07-06 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hidden', models.BooleanField(default=False)),
                ('liked', models.NullBooleanField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_decimal', models.DecimalField(decimal_places=8, default=0.0, max_digits=16)),
                ('questions_answered', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_user_a', to=settings.AUTH_USER_MODEL)),
                ('user_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_user_b', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LocationMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hidden', models.BooleanField(default=False)),
                ('liked', models.NullBooleanField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployerMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hidden', models.BooleanField(default=False)),
                ('liked', models.NullBooleanField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Employer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
