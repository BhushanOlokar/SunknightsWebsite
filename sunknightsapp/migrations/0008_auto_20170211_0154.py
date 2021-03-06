# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 01:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0007_auto_20170210_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('permed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuestBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build', models.CharField(max_length=500)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='builds', to='sunknightsapp.Quest')),
            ],
        ),
        migrations.CreateModel(
            name='QuestTankMultiplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiplier', models.DecimalField(decimal_places=2, default=1, max_digits=4)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multipliers', to='sunknightsapp.Quest')),
                ('tank', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sunknightsapp.DiepTank')),
            ],
        ),
        migrations.CreateModel(
            name='QuestTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.PositiveSmallIntegerField(choices=[(1, 'Tier 1'), (2, 'Tier 2'), (3, 'Tier 3'), (4, 'Bonus')], default=1)),
                ('questtext', models.CharField(max_length=500)),
                ('deleted', models.BooleanField(default=False)),
                ('points', models.PositiveSmallIntegerField(default=0)),
                ('cooldown', models.PositiveIntegerField(default=24)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='sunknightsapp.Quest')),
            ],
        ),
        migrations.CreateModel(
            name='QuestTaskUserConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sunknightsapp.QuestTask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='DailyQuest',
        ),
        migrations.AddField(
            model_name='pointsinfo',
            name='permquestcd',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicuserpointsubmission',
            name='proof',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='eventquestsubmission',
            name='proof',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='mastery',
            name='tier',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tier 1'), (2, 'Tier 2'), (3, 'Tier 3'), (4, 'Tier 4'), (5, 'Tier 5')]),
        ),
        migrations.AlterField(
            model_name='oneononefightsubmission',
            name='proof',
            field=models.CharField(max_length=300),
        ),
        migrations.AddField(
            model_name='eventquestsubmission',
            name='questtask',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventquest', to='sunknightsapp.QuestTask'),
        ),
        migrations.AlterUniqueTogether(
            name='questtaskuserconnector',
            unique_together=set([('task', 'user')]),
        ),
    ]
