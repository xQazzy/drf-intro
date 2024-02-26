from django.urls import path
from .views import SensorCreate, SensorUpdate, MeasurementCreate, SensorList, SensorDetail

urlpatterns = [
    path('sensors/', SensorList.as_view(), name='sensor-list'),
    path('sensors/create/', SensorCreate.as_view(), name='sensor-create'),
    path('sensors/update/<int:pk>/', SensorUpdate.as_view(), name='sensor-update'),
    path('measurements/create/', MeasurementCreate.as_view(), name='measurement-create'),
    path('sensors/<int:pk>/', SensorDetail.as_view(), name='sensor-detail'),
]
