from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Enquiry
import json


@csrf_exempt
def enquiry(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)

            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            message = data.get("message")

            # Save enquiry to database
            Enquiry.objects.create(
                name=name,
                phone=phone or "",
                email=email,
                message=message
            )

            # Send email to you
            send_mail(
                subject=f"New Portfolio Enquiry from {name}",
                message=f"""
You received a new enquiry from your portfolio website.

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
""",
                from_email=None,
                recipient_list=["anshifck249@gmail.com"],
                fail_silently=False,
            )

            return JsonResponse({
                "success": True,
                "message": "Enquiry sent successfully"
            })

        except Exception as e:
            return JsonResponse({
                "success": False,
                "error": str(e)
            }, status=400)

    return render(request, "contact.html")


def success(request):
    return render(request, "success.html")
