from django.conf.urls import url
from django.conf.urls.static import static
from . import views
# from .views import Gauge

urlpatterns = [
    #url(r'^landing/', views.landing_repository, name='landing_repository'),
    url(r'^test/$', views.landing, name='landing'),
    url(r'^arborlive/$', views.getarbor, name='getarbor'),
    url(r'^ajax/ArborData/$', views.ArborData, name='ArborData'),
    url(r'^ajax/DeviceData/$', views.DeviceData, name='DeviceData'),
#     url(r'^data', Gauge.as_view()),
    # url(r'^lionel', views.test2, name='test2'),

    ]

