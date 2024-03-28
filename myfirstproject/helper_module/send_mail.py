from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_mail_from_site(subject, template_message, context, receivers):
    try:
        template = render_to_string(template_message, context=context)
        plain_message = strip_tags(template)
        send_mail(
            subject,
            plain_message,
            settings.EMAIL_HOST_USER,
            receivers,
            html_message=template,
        )
    except:
        pass
