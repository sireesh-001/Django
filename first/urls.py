from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.form_view,name='add'),
    path('completed/<first_id>',views.completed,name='completed'),
    path('delete',views.deleted,name='delete'),
    path('deleteall',views.deleteall,name='deleteall')
]
