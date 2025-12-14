from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('confirm/', views.confirm_page, name='confirm'),
    path('confirm-order/', views.confirm_order, name='confirm_order'),
]