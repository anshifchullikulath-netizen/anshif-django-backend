from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Enquiry
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def enquiry(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)

            name = data.get("name")
            email = data.get("email")
            message = data.get("message")

            Enquiry.objects.create(
                name=name,
                phone="",
                email=email,
                message=message
            )

            return JsonResponse({"success": True})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return render(request, "contact.html")


def success(request):
    return render(request, "success.html")
