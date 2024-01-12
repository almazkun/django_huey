from huey.contrib.djhuey import task
from emailer.usecases.email import send_email


@task()
def send_email_task(email):
    send_email(email)
