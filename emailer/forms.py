from django import forms
from emailer.tasks import send_email_task


class SendEmailForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "class": "form-control",
                "placeholder": "Enter email address here",
            }
        ),
    )

    def save(self, commit=True):
        send_email_task(self.cleaned_data["email"])
