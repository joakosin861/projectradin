from django.urls import path
from Aplicacion import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('agregar_factura', views.AgregarFactura.as_view(), name='agregar_factura'),
    path('lista_facturas/', views.ListaFacturas.as_view(), name='lista_facturas'),
    path('eliminar_factura/<int:pk>', views.EliminarFactura.as_view(), name='eliminar_factura'),
    path('apicheck/', views.consultapi, name='apicheck'),
]
