from django.urls import path
from .views import index, produto, prod

urlpatterns = [
    path('', index, name='index'),
    path('produto/', produto, name='produto'),
    path('prod/<int:pk>', prod, name='prod')
]
