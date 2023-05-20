from django.urls import path
from .views import listview, detailview, post_share,category_list

app_name = 'article'

urlpatterns = [
    path('', listview, name='list'),
    path('tag/<slug:tag_slug>/',listview, name='post_list_by_tag'),
    path('<int:id>/share/', post_share, name='share'),
    path('<int:id>/', detailview, name='detail'),
    path('category/<int:id>/', category_list, name='category_list'),
]



