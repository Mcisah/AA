from django.shortcuts import render, HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponseRedirect("/poll/")