from django.shortcuts import render, HttpResponse
import json


def ajax_test(request):
    if request.method == "POST":
        req = json.loads(request.body)
        cmd = req['cmd']
        if cmd == "1":
            return HttpResponse(json.dumps({"msg": "haha"}))
        elif cmd == "2":
            from random import random
            data_list = {}
            for x in req["index"]:
                data_list[x]= random()
            return HttpResponse(json.dumps(data_list))
    name_list = ["alice", "bob", "oscar"]
    name_json = []
    for idx, name in enumerate(name_list):
        name_json.append({"id": idx+1, "name": name})
    return render(request, "index.html", {"msg": "Hello, World", "names": name_json})
