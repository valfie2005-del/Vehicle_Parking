from django.urls import path
from parkapp import views
from rest_framework.routers import DefaultRouter
from .views import ParkViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'park', ParkViewSet)

urlpatterns = [
    path('', views.parkFormView, name='home'),
    path('pfv/', views.parkFormView, name='parking_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_Pid>/', views.updateView, name='update_url'),
    path('del/<int:f_Pid>/', views.deleteView, name='delete_url'),
    path('api/', include(router.urls))
]