from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'clients', views.ClientAPIView, basename='clients')
router.register(r'mailings', views.MailingAPIView, basename='mailings')

urlpatterns = [
    path('', include(router.urls)),
    path('mailing-report/', views.MailingReportAPIView.as_view()),
    path('mailing-report/<int:mailing_id>/', views.MailingReportAPIView.as_view())
]
