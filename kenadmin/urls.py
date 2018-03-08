from django.conf.urls import url, include
from kenadmin import views

urlpatterns = [
    url(r'^$', views.index, name="table_index"),
    url(r'^(\w+)/(\w+)/$', views.display_table_objs, name="table_objs"),
    url(r'^(\w+)/(\w+)/add/$', views.table_obj_add, name="table_obj_add"),
    url(r'^test/$', views.display_test, name="test"),
]
