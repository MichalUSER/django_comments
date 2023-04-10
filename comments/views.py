from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import Comment


def index(request):
    comments = Comment.objects.all()
    timezone_name = request.COOKIES.get("timezone_name")
    if timezone_name:
        context = {"comments": comments, "user_timezone": str(timezone_name)}
    else:
        context = {"comments": comments}

    return render(request, "index.html", context)


def add_comment(request):
    new_comment = Comment(content=request.POST["comment"], date=timezone.now())
    new_comment.save()
    return HttpResponseRedirect("/")


def delete_comments(request):
    Comment.objects.all().delete()
    return HttpResponseRedirect("/")
