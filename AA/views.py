from django.shortcuts import render, HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponseRedirect("/poll/")


# def handler404(request):
#     return render(request, "404.html")
#
#
# def handler400(request):
#     return render(request, "400.html")
#
#
# def handler403(request):
#     return render(request, "403.html")
#
#
# def handler500(request):
#     return render(request, "500.html")
