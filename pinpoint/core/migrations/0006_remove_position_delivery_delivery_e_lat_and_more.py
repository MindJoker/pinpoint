# Generated by Django 5.0.3 on 2024-04-14 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_delivery_delivery_end_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='delivery',
        ),
        migrations.AddField(
            model_name='delivery',
            name='e_lat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_lat', to='core.position'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='e_long',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_long', to='core.position'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='position_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position_id', to='core.position'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='s_lat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s_lat', to='core.position'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='s_long',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s_long', to='core.position'),
        ),
        migrations.AddField(
            model_name='operator',
            name='now_lat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='now_lat', to='core.position'),
        ),
        migrations.AddField(
            model_name='operator',
            name='now_long',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='now_long', to='core.position'),
        ),
    ]
