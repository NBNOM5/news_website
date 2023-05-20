from django import template
from article.models import Post
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('tags/lastest_postes.html')
def lastest_postes():
    posts = Post.objects.filter(status='active').order_by('-created_at')[:5]
    return {'posts': posts}

@register.inclusion_tag('tags/most_comments.html')
def most_comments(count=8):
    comments = Post.objects.annotate(total_comments=Count('comments')).\
        order_by('-total_comments')[:count]
    return {'comments': comments}

@register.inclusion_tag('tags/most_view.html')
def most_view():
    posts = Post.objects.filter(status = 'active').order_by('-see')[:5]

    return{'posts':posts}

