from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),    
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('jobs',views.jobs,name='jobs'),
    path('jobs/<str:name>',views.jobsviews,name='jobs'),
    path('jobs/<str:cname>/<str:dname>',views.job_details,name='job_details')
]