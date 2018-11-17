from django.conf.urls import url
from bio import views

urlpatterns = [
    url(r'^bio/perfil/$', views.PerfilList.as_view()), 
    url(r'^bio/perfil/(?P<pk>[0-9]+)/$', views.PerfilDetail.as_view()),
    url(r'^bio/denuncia/$', views.DenunciaList.as_view()), 
    url(r'^bio/denuncia/(?P<pk>[0-9]+)/$', views.DenunciaDetail.as_view()),   
    url(r'^bio/usuario/$', views.UsuarioList.as_view()), 
    url(r'^bio/usuario/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),   
]