from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login' ),
    path('addnote/', views.addnote, name="addnote"),
    path('note/updatenote/<int:pk/', views.update_note, name="updatenote"),
    # path('note/update/<int:pk/', views.delete_note, name="updatenote1"),
]