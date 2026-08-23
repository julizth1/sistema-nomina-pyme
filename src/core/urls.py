from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nomina.views import ver_factura, modulo_nomina, EmpleadoViewSet, FacturaNominaViewSet,cargar_excel_marcaciones

router = DefaultRouter()
router.register(r'api/empleados', EmpleadoViewSet)
router.register(r'api/facturas', FacturaNominaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('factura/', ver_factura, name='ver_factura'),
    path('nomina-gestion/', modulo_nomina, name='modulo_nomina'),
    path('cargar-excel/', cargar_excel_marcaciones, name='cargar_excel'),
    path('', include(router.urls)),
]