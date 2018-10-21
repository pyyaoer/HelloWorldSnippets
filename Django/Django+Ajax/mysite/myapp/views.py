from django.shortcuts import render

def ajax_test(request):
    return render(request, "index.html", {"msg": "Hello, World"})
