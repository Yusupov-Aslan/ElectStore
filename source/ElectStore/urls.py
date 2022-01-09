from django.urls import path

from ElectStore.views import index_view

urlpatterns = [
    path('', index_view, name='index'),

]
