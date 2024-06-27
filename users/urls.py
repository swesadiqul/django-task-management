from django.urls import path
from users import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('account/verify', views.verify_account, name='verify_account'),
]
