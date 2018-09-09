from django.conf.urls import url

from . import views

from app.Tutor.views import ListViewTutor

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^health', views.health, name='health'),
               url(r'^404', views.handler404, name='404'),
               url(r'^500', views.handler500, name='500'),
               url(r'^tutor/', ListViewTutor.as_view(), name = 'ListaTutores'),
               url(r'^asignatura/', ListViewAsignatura.as_view(), name = 'ListaAsignaturas'),
               ]
