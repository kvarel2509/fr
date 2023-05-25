from rest_framework import viewsets, views

from clients.repository import ClientRepository
from mailing.logic.mailing_report.services import MailingReporter
from mailing.repository import MailingRepository
from .serializers import ClientSerializer, MailingSerializer


class ClientAPIView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    repo = ClientRepository()

    def get_queryset(self):
        return self.repo.all_clients()


class MailingAPIView(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    repo = MailingRepository()

    def get_queryset(self):
        return self.repo.all_mailings()


class MailingReportAPIView(views.APIView):
    repo = MailingRepository()

    def get(self, request, mailing_id=None):
        reporter = MailingReporter(self.repo)
        report = reporter.get_report(mailing_id)
        return views.Response({'response': report})
