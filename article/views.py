from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from article.models import Category, Post, Comment
from .forms import ShareForm, CommentForm

from taggit.models import Tag

# Create your views here.

def listview(request, tag_slug=None):
    most_new = Post.objects.filter(status = 'active').first()
    last6_news = Post.objects.filter(status = 'active')[1:7]
    posts = Post.objects.filter(status ='active')
    videos = Post.objects.exclude(video__exact='').filter(status = 'active')[:6]

    categories = Category.objects.filter(status ='active')
  

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    # ----------- PAGEINATOR >>>>>
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # ----------- PAGEINATOR >>>>>

    context = {
        'most_new':most_new,
        'last6_news':last6_news,
        'maqolalar': posts,
        'page':page,
        'videos':videos,
        'categories':categories,
        'tag':tag,
        

    }
    return render(request,'article/list.html',context)


def detailview(request, id):
    post = get_object_or_404(Post, id=id)
    posts = Post.objects.filter(category=post.category, status = 'active')[:4]
    categories = Category.objects.filter(status ='active')

    # foydalanuvchilarga avval yozilgan commentlar ko'rinishi un ajratib olamiz
    comments = post.comments.filter(status=True)

    new_comment = None
    #frontend dan kelayotgan so'rov turi "POST" bo'lsa
    if request.method == 'POST':
        # front dan kelgan malumotdan 'CommentForm'ga to'ldirilgan ma'lumotlarni ajratib olamiz
        comment_form = CommentForm(data=request.POST)
        # agr frontend dan kelgan ma'lumotlar "to'g'ri to'ldirilgan bo'lsa"
        if comment_form.is_valid():
            # ma'lumotlarni vaqtincha o'zgaruvchiga saqlab turamiz
            new_comment = comment_form.save(commit=False)
            # bo'sh qolib ketgan CommentForm ni ichidagi 'post' maydoniga 👇
            new_comment.post = post # joriy 'post'ni biriktiramiz(28-qatordagi o'zgaruvchini)
            new_comment.save() # va comment ni bazaga saqlaymiz
    else:
        comment_form=CommentForm() # foydalanuvchi comment yozishi un unga formani jo'natamiz

    context = {
        'maqola': post, # joriy maqola
        'comments':comments,# avval yozilgan commentlar
        'new_comment':new_comment, # yangi yozilgan comment
        'comment_form':comment_form, # yangi forma yozish uchun yuborilayotgan forma
        'posts':posts,
        'categories':categories, 
        
        }

    return render(request,'article/detail.html', context)

def post_share(request, id):
    # id bo'yicha maqola olinadi
    post = get_object_or_404(Post, id=id)
    categories = Category.objects.filter(status = 'active')
    sent = False
    if request.method == 'POST': # GET, POST, 
        # forma saqlash  uchun yuboriladi
        form = ShareForm(request.POST)
        if form.is_valid():
            # barcha maydonlar tasdiqlandi
            cd = form.cleaned_data
            
            post_url = request.build_absolute_uri(post.get_absolute_url())
            email = cd['email']
            subject = f"{cd['name']}({cd['email']}) sizga {post.title} tafsiya qildi"
            message = f"{post.title} ni quidagi link orqali o'qing: {post_url}  Comment: {cd['comment']}"
            send_mail(subject, message, email, [cd['to']])
            sent = True
    else:
        form = ShareForm()

    context = {'post': post, 'form': form, 'sent': sent, 'categories':categories}

    return render(request, 'article/share.html', context)

def base_view(request, *args, **kwargs):
    categories = Category.objects.filter(status = 'active')

    context = {

        'categories':categories,
    }
    return render(request, 'base.html', context)

def category_list(request, id):
    category_object = get_object_or_404(Category, id=id)
    posts = Post.objects.filter(status='active', category = category_object.id)[:12]
    categories = Category.objects.filter(status = 'active')
    
    # ----------- PAGEINATOR >>>>>
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # ----------- PAGEINATOR >>>>>


    context = {
        'category_object': category_object, 
        'posts': posts,
        'categories':categories,
        }

    return render(request, 'article/category_list.html', context)


