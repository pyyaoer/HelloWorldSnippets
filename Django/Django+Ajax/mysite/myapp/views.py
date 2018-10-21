from django.shortcuts import render, HttpResponse
import json


def ajax_test(request):
    if request.method == "POST":
        cmd = request.POST.get('cmd')
        return HttpResponse(json.dumps({"msg": "haha"}))
    return render(request, "index.html", {"msg": "Hello, World"})
