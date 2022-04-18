from django.contrib import messages
from django.shortcuts import render, redirect
from main.models import Ism
from .form import IsmForm

def main_index(request):
    boshsahifa = "INDEX"
    return render(request, 'main/index.html', context={
        "page_title": boshsahifa,
        "ismlar": Ism.objects.all()
    })


def main_add(request):
    form = IsmForm(data=request.POST)

    if request.method == "POST":
        if form.is_valid():
            Ism(ism=form.cleaned_data['Ismingizni_kiriting'],
                familiya=form.cleaned_data['Familiyangizni_kiriting'],
                ty=form.cleaned_data['Tugilgan_yilingizni_kiriting']).save()


            messages.success(request,  "Ism muffaqiyatli qo'shildi")


            return redirect("index")

    boshsahifa = "ISM QO'SHISH"
    return render(request, "main/add.html", context={
        "page_title": boshsahifa,
        "form": form
    })

    
def main_about(request):
    boshsahifa = "ABOUT"
    return render(request, "main/about.html", context={
        "page_title": boshsahifa
    })


def main_delete(request):
    id = request.GET.get("id")

    Ism.objects.filter(id=id).delete()
    messages.error(request, "O'chirildi")
    return redirect("index")