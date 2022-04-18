from django.shortcuts import render
from django.views.generic import TemplateView


def account_registrasion(request):
    boshsahifa = "REGISTRASION"
    return render(request, "account/registrasion.html", context={
        "page_title": boshsahifa
    })

 