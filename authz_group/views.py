from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from authz_group.models import Crowd, Person, CrowdOwner
import json


@login_required
def demo_page(request):
    return render(request, "crowds_demo.html", {})


@login_required
def group_data(request):
    crowds = Crowd.get_crowds_for_user(request.user.username)

    all_objects = []
    for crowd in crowds:
        all_objects.append(crowd.json_data_structure())

    all_backend_sources = []
    for backend in Crowd.get_crowd_backends():
        all_backend_sources.append(backend.json_data_structure())

    data = {
        'crowds': all_objects,
        'source_types': all_backend_sources,
    }

    return HttpResponse(json.dumps(data), {
        "Content-type": "application/json; charset=utf-8"})
