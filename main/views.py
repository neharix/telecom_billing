from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import *
from .utils import *


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
        if request.GET.get("query", False):
            query = request.GET["query"]
            clients = (
                Client.objects.filter(phone_number__contains=query)
                | Client.objects.filter(full_name__contains=query)
                if query != ""
                else None
            )
            return render(
                request,
                "views/search_results.html",
                {"clients": clients},
            )
        else:
            return redirect("home")
    else:
        return redirect("home")


def about_sub(request: HttpRequest, client_id: int):
    if exists_by_id(client_id, Client):
        client = Client.objects.get(id=client_id)
    else:
        return redirect("home")

    return render(
        request,
        "views/about_sub.html",
        {
            "client": client,
            "client_packages": ClientPackage.objects.filter(
                client=client,
                ends_at__gte=datetime.datetime.now(pytz.timezone("Asia/Ashgabat")),
            ),
            "client_services": client.services.all(),
            "packages": Package.objects.all(),
            "appraisals": Appraisal.objects.all(),
            "services": Service.objects.all(),
        },
    )


def logout_view(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")


def get_pack(request: HttpRequest, package_id: int, client_id: int):
    if exists_by_id(client_id, Client):
        client = Client.objects.get(id=client_id)
    else:
        return redirect("home")

    if exists_by_id(package_id, Package):
        package = Package.objects.get(id=package_id)
    else:
        return redirect("home")

    if client.balance >= package.price:
        ClientPackage.objects.create(
            package=package,
            client=client,
            ends_at=datetime.datetime.now(pytz.timezone("Asia/Ashgabat"))
            + datetime.timedelta(days=30),
        )
        client.balance -= package.price
        client.save()
    return redirect(about_sub, client_id=client_id)


def set_appraisal(request: HttpRequest, appraisal_id: int, client_id: int):
    if exists_by_id(client_id, Client):
        client = Client.objects.get(id=client_id)
    else:
        return redirect("home")

    if exists_by_id(appraisal_id, Appraisal):
        appraisal = Appraisal.objects.get(id=appraisal_id)
    else:
        return redirect("home")

    if client.balance >= appraisal.price:
        client.balance -= appraisal.price
        client.appraisal = appraisal
        client.save()
    return redirect(about_sub, client_id=client_id)


def toggle_service(request: HttpRequest, client_id: int, service_id: int):
    if exists_by_id(client_id, Client):
        client = Client.objects.get(id=client_id)
    else:
        return redirect("home")

    if exists_by_id(service_id, Service):
        service = Service.objects.get(id=service_id)
    else:
        return redirect("home")

    if service in client.services.all():
        client.services.remove(service)
    else:
        client.services.add(service)
        client.balance -= service.price

    client.save()
    return redirect(about_sub, client_id=client_id)
