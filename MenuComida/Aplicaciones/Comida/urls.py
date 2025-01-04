from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('platillos',views.platillos,name='platillos'),
    path('guardarPlatillo/',views.guardarPlatillo),
    path('verPlatillo/',views.verPlatillo,name='verPlatillo'),


    path('menu_filtrado/', views.menu_filtrado, name='menu_filtrado'),
    path('menu_filtrado/<str:tipo>/', views.menu_filtrado, name='menu_filtrado_tipo'),
    path('ocultar_platillo/<int:platillo_id>/', views.ocultar_platillo, name='ocultar_platillo'),

    path('platillo/<int:platillo_id>/', views.platillo_detalle, name='platillo_detalle'),
    path('editarPlatillo/<int:platillo_id>/', views.editarPlatillo, name='editar_platillo'),
    path('procesarEdicionPlatillo/',views.procesarEdicionPlatillo),
    path('eliminarPlatillo/<id>',views.eliminarPlatillo),
]