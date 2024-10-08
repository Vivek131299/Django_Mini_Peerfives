# Generated by Django 5.1.1 on 2024-10-05 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RewardHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_stamp', models.DateTimeField(auto_now_add=True)),
                ('points', models.FloatField()),
                ('given_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='given_rewards', to='api.peeruser')),
                ('given_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='received_rewards', to='api.peeruser')),
            ],
        ),
    ]
