import os
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import passengerDetail
import qrcode
from urllib.parse import urlparse

path = "./static/qrcode_image/"


def makeCode(url):
    image = qrcode.make(url)
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split("/")
    accessed_value = path_segments[-2]
    name = accessed_value + ".jpg"
    file_path = os.path.join(path, name)
    if not os.path.exists(file_path):
        image.save(file_path)
    else:
        pass


def show_latest_passenger(request):
    latest_passenger = passengerDetail.objects.last()
    if latest_passenger:
        return redirect("showPassenger", id=latest_passenger.id)
    else:
        # Handle case when there are no passengers
        return HttpResponse("No passengers found.")


def showPassenger(request, id):
    resultsdisplay = get_object_or_404(passengerDetail, id=id)
    full_url = request.build_absolute_uri()
    makeCode(full_url)
    context = {
        "results": resultsdisplay,
    }

    return render(request, "index.html", context)
