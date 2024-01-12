from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import FormView
from emailer.forms import SendEmailForm
from django.contrib import messages


# Create your views here.
class SendEmailView(FormView):
    form_class = SendEmailForm
    template_name = "emailer/send_email.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, f"Email sent successfully to {form.cleaned_data['email']}"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, f"Email failed to send to {form.cleaned_data['email']}"
        )
        return super().form_invalid(form)

    def get_template_names(self) -> Any:
        if self.request.htmx:
            return "emailer/includes/send_email.html"
        return "emailer/send_email.html"
