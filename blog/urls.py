from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit,name='post_edit'),
    path('cv/',views.cv_view,name='cv_view'),
    path('cv/education',views.cv_education,name='cv_education'),
    path('cv/<int:pk>/ed/edit', views.cv_education_edit,name='cv_education_edit'),
    path('cv/work',views.cv_work,name='cv_work'),
    path('cv/<int:pk>/work/edit', views.cv_work_edit,name='cv_work_edit'),
]