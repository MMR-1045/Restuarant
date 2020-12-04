
from django.urls import path,include

from . import views

app_name='home'

urlpatterns = [
    path('', views.home,name='home'),
    # path('<int:id>',views.post_detail,name='post_detail'),
    
]