from django.urls import path
from games import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'games'


urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('game/<int:game_id>/', views.game_info, name='game_info'),
    path('buy/<int:game_id>/', views.buy_game, name='buy_game'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)