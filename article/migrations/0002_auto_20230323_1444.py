# Generated by Django 3.1 on 2023-03-23 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-created_at', 'status'), 'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',), 'verbose_name': 'Maqola', 'verbose_name_plural': 'Maqolalar'},
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='post matni'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='article.category', verbose_name='Kategoriya'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='post_photo/%Y/%m/%d/', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='see',
            field=models.PositiveIntegerField(default=1, verbose_name="ko'rishlar soni"),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deactive', 'Deactive')], default='active', max_length=20, verbose_name='Holati'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=250, verbose_name='Kichik sarlavha'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(max_length=25, verbose_name='TAG'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='post_videos/%Y/%m/%d/', verbose_name='video'),
        ),
    ]