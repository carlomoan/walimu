from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('user/me', CurrentUserView.as_view(), name="userme"),
    path('users/', UsersProfileView.as_view(), name="profile"),
    path('users/<int:pk>', UserView.as_view(), name='userview'),
    path('profiles/<int:pk>', UserProfileView.as_view(), name="profiles"),
    path('mitaala_list', ListMitaalaView.as_view(), name='mitaala'),
    path('mitaala', mtaalalist.as_view(), name='mitaalalist'),
    path('mitaala_list/<int:pk>', MitaalaDetail.as_view(), name='mtaaladetail'),
    path('darasa_list', ListDarasaView.as_view(), name='madarasa'),
    path('darasa_list/<int:pk>', DarasaDetail.as_view(), name='darasadetail'),
    path('umahiri_list', ListUmahiriView.as_view(), name='umahiri'),
    path('umahiri_list/<int:pk>', UmahiriDetail.as_view(), name='umahiridetail'),
    path('umahsusi_list', ListUmahsusiView.as_view(), name='umahsusi'),
    path('umahsusi_list/<int:pk>', UmahsusiDetail.as_view(), name='umahsusidetail'),
    path('muhula_list', ListMuhulaView.as_view(), name='muhula'),
    path('muhula_list/<int:pk>', MuhulaDetail.as_view(), name='muhuladetail'),
    path('juma_list', ListJumaView.as_view(), name='juma'),
    path('juma_list/<int:pk>', JumaDetail.as_view(), name='jumadetail'),
    path('siku_list', ListSikuView.as_view(), name='siku'),
    path('siku_list/<int:pk>', SikuDetail.as_view(), name='sikudetail'),
    path('shughuli_list', ListShughuliView.as_view(), name='shughuli'),
    path('shughuli_list/<int:pk>', ShughuliDetail.as_view(), name='shughulidetail'),
    path('vipindi_list', ListVipindiView.as_view(), name='vipindi'),
    path('vipindi_list/<int:pk>', VipindiDetail.as_view(), name='vipindidetail'),
    path('mtaalaheader_list', ListMtaalaHead.as_view(), name='mtaalacontent'),
    path('mtaalaheader_list/<int:pk>', MtaalaHeadDetail.as_view(), name='mtaalacontentdetail'),
    path('mtaalaarticle_list', ListMtaalaArticle.as_view(), name='mtaalaarticle'),
    path('mtaalaarticle_list/<int:pk>', MtaalaArticlesDetail.as_view(), name='mtaalaarticledetail'),
    path('register', RegisterView,name="register")
]
