from django.conf.urls import url
from meiduo_admin.views import users

urlpatterns = [
    url(r'^authorizations/$', users.AdminAuthorizeView.as_view()),
]
