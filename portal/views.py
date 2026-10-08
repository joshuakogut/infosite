from django.shortcuts import render, redirect
from django.http import HttpResponse
from portal import models


def index(request):
    return HttpResponse("Hello world")
