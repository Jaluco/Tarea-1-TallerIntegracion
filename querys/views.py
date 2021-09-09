# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests


def index(request):
    response = ["start"]
    page = 1
    users = []
    while len(response) > 0:
        response = requests.get(
            "https://us-central1-taller-integracion-310700.cloudfunctions.net/" +
            "tarea-1-2021-2/30951/users?_page="+str(page)
        ).json()
        users.extend(response)
        # print(response)
        page += 1

    template = loader.get_template("querys/index.html")
    context = {
        "response": users,
    }
    return HttpResponse(template.render(context, request))
