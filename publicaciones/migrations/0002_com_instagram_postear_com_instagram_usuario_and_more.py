# Generated by Django 4.0 on 2022-01-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='com_instagram',
            name='postear',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='publicaciones.pub_instagram'),
        ),
        migrations.AddField(
            model_name='com_instagram',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auth.user'),
        ),
        migrations.AddField(
            model_name='pub_instagram',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='auth.user'),
        ),
    ]