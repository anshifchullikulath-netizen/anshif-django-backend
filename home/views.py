from django.shortcuts import render, redirect
from .models import Enquiry


def enquiry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Enquiry.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )

        return redirect("success")

    return render(request, "contact.html")


def success(request):
    return render(request, "success.html")