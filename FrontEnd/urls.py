from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('Home/',views.index, name = 'dashboard-index'),
    path('cars/',views.cars, name = 'dashboard-cars'),
    path('cars/delete/<int:pk>/',views.cars_delete, name = 'dashboard-cars-delete'),
    path('cars/update/<int:pk>/',views.cars_update, name = 'dashboard-cars-update'),
    path('staff/',views.staff, name = 'dashboard-staff'),
    path('staff/details/<int:pk>/',views.staff_details, name = 'dashboard-staff-details'),
    path('order/',views.order, name = 'dashboard-order'),
]