# Generated by Django 5.0.3 on 2024-03-30 22:40

import dirtyfields.dirtyfields
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRevenueData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sell_count', models.PositiveIntegerField(default=0)),
                ('sell_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_daily_revenue', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
