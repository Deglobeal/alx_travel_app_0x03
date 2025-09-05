from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(customer_email, listing_title, check_in, check_out):
    subject = f"Booking confirmed – {listing_title}"
    message = (
        f"Hi!\n\nYour booking for '{listing_title}' "
        f"from {check_in} to {check_out} has been received.\n\n"
        "We will contact you shortly.\n\n"
        "– TravelApp team"
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL or 'noreply@travelapp.com',
        [customer_email],
        fail_silently=False,
    )