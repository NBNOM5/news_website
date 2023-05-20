from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager

# Create your models here.

STATUS = (
    ('active',"Active"),
    ('deactive', "Deactive"),
)


class Category(models.Model):
    name = models.CharField(max_length=50)

    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ('-created_at','status')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('article:category_list', args=[self.id,])

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,\
                                  related_name='post_category', verbose_name="Kategoriya")
    title = models.CharField(max_length=120, verbose_name="Sarlavha")
    subtitle = models.CharField(max_length=250, verbose_name="Kichik sarlavha")
    body = models.TextField(verbose_name="post matni")
    video = models.FileField(upload_to='post_videos/%Y/%m/%d/', blank=True, \
                             null=True, verbose_name="video")
    photo = models.ImageField(upload_to='post_photo/%Y/%m/%d/', blank=True, \
                              null=True, verbose_name="photo")
    see = models.PositiveIntegerField(default=1, verbose_name="ko'rishlar soni")
    tags = TaggableManager()

    status = models.CharField(max_length=20, choices=STATUS, default='active', verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail', args=[self.id,])


    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    body = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ("-created_at",)

    def __str__(self):
        text = f"{self.name}  - {self.email}"
        return text
    



