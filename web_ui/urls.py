from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from . import views

app_name = 'web_ui'
urlpatterns = [
    path('', views.MainRedirectView.as_view()),
    path('mailings/', include([
        path('', views.MailingsView.as_view(), name='mailings'),
        path('create/', views.MailingCreateView.as_view(), name='mailing_create'),
        path('<int:mailing_id>/', include([
            path('', views.MailingView.as_view(), name='mailing'),
            path('update/', views.MailingUpdateView.as_view(), name='mailing_update'),
            path('delete/', views.MailingDeleteView.as_view(), name='mailing_delete'),
        ])),
    ])),
    path('mailings-report/', include([
        path('', views.MailingReportView.as_view(), name='mailings_report'),
        path('<int:mailing_id>/', views.MailingReportView.as_view(), name='mailing_report')
    ])),
    path('accounts/', include([
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
    ])),
]
