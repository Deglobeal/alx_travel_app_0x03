from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import uuid
import requests
from django.conf import settings
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer   # we’ll create these next


# ---------- API ViewSets ----------
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# ---------- Chapa Payment ----------
CHAPA_URL = "https://api.chapa.co/v1"
HEADERS   = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}


@api_view(['POST'])
def initiate_payment(request):
    booking = get_object_or_404(Booking, pk=request.data['booking_id'])
    tx_ref = str(uuid.uuid4())

    Payment.objects.create(
        booking=booking,
        amount=request.data.get('amount', booking.listing.price),
        tx_ref=tx_ref,
    )

    payload = {
        "amount": str(booking.listing.price),
        "currency": "ETB",
        "email": booking.user.email,
        "first_name": booking.user.first_name or "User",
        "last_name":  booking.user.last_name  or "",
        "tx_ref": tx_ref,
        "callback_url": request.build_absolute_uri('/payments/verify/'),
        "return_url":   request.build_absolute_uri('/payments/success/'),
    }

    resp = requests.post(f"{CHAPA_URL}/transaction/initialize",
                         json=payload, headers=HEADERS)
    if resp.status_code == 200:
        return Response({"checkout_url": resp.json()["data"]["checkout_url"]})
    return Response(resp.json(), status=400)


@api_view(['GET'])
def verify_payment(request):
    tx_ref = request.GET.get("tx_ref")
    payment = get_object_or_404(Payment, tx_ref=tx_ref)

    resp = requests.get(f"{CHAPA_URL}/transaction/verify/{tx_ref}", headers=HEADERS)
    data = resp.json()

    if data.get("status") == "success":
        payment.status = Payment.COMPLETED
        payment.transaction_id = data["data"]["id"]
        payment.save()
        return Response({"message": "Payment successful"})
    else:
        payment.status = Payment.FAILED
        payment.save()
        return Response({"message": "Payment failed"}, status=400)