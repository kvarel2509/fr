from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from mailing.logic.mailing_report.services import MailingReporter
from mailing.repository import MailingRepository
from .forms import MailingFrom


class MailingsMixin(LoginRequiredMixin):
    pk_url_kwarg = 'mailing_id'
    ordering = 'start_date'
    repo = MailingRepository()

    def get_queryset(self):
        return self.repo.all_mailings()


class MainRedirectView(generic.RedirectView):
    url = reverse_lazy('web_ui:mailings')


class MailingsView(MailingsMixin, generic.ListView):
    template_name = 'web_ui/mailings.html'


class MailingView(MailingsMixin, generic.DetailView):
    template_name = 'web_ui/mailing.html'


class MailingCreateView(MailingsMixin, generic.CreateView):
    template_name = 'web_ui/mailing_form.html'
    form_class = MailingFrom


class MailingUpdateView(MailingsMixin, generic.UpdateView):
    template_name = 'web_ui/mailing_form.html'
    form_class = MailingFrom

    def get_success_url(self):
        return reverse_lazy('web_ui:mailing', kwargs={'mailing_id': self.object.pk})


class MailingDeleteView(MailingsMixin, generic.DeleteView):
    template_name = 'web_ui/mailing_form.html'
    success_url = reverse_lazy('web_ui:mailings')


class MailingReportView(MailingsMixin, generic.TemplateView):
    template_name = 'web_ui/mailings_report.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        mailing_id = self.kwargs.get('mailing_id')
        reporter = MailingReporter(self.repo)
        report = reporter.get_report(mailing_id)
        ctx['report'] = report
        return ctx
