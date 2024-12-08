from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import *


@login_required(login_url="/admin/login/")
def main(request: HttpRequest):
    clients = Client.objects.all()
    return render(
        request,
        "views/main.html",
        {"current_page": "main", "clients": clients},
    )


@login_required(login_url="/admin/login/")
def search(request: HttpRequest):
    if request.method == "GET":
        # if request.GET.get("query", False):
        #     query = request.GET["query"]
        #     devices = Device.objects.filter(
        #         name__contains=query
        #     ) | Device.objects.filter(device_type__name__contains=query)
        return render(
            request,
            "views/search_results.html",
            {},
        )
    else:
        return redirect("home")


def logout_view(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")
