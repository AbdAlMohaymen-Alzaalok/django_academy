from django.shortcuts import render,redirect
from . import models,forms
from django.views.generic import CreateView
from django.urls import reverse,reverse_lazy
from checkout.models import Payment,Status


def index(request):
    courses=models.Course.objects.all()
    for course in courses:
        course.purchased=Payment.objects.filter(
            user=request.user,
            course=course,
            status=Status.completed
        ).exists() if request.user.is_authenticated else False
    return render(request,'courses/index.html',{
        'courses':courses
    })

def course(request,cid):
    course=models.Course.objects.get(pk=cid)
    comments=course.comment_set.filter(reply__isnull=True)
    return render(request,'courses/course.html',{
        'course':course,
        'comments':comments
    })

def checkout(request,cid):
    course = models.Course.objects.get(pk=cid)
    return render(request,'courses/checkout.html',{
        'course':course
    })

def wrong(request,cid):
    course=models.Course.objects.get(pk=cid)
    return render(request,'courses/wrong.html',{
        'course':course
    })

def right(request,cid):
    course=models.Course.objects.get(pk=cid)
    return render(request,'courses/right.html',{
        'course':course
    })

def add_comment(request,cid):
    course = models.Course.objects.get(pk=cid)
    if request.method=='POST':
        content=request.POST.get('content')
        models.Comment.objects.create(
            course=course,
            user=request.user,
            content=content
        )
        return redirect('course',course.id)
    return redirect('course',course.id)

def add_reply(request,cmid):
    comment=models.Comment.objects.get(pk=cmid)
    if request.method=='POST':
        content=request.POST.get('content')
        models.Comment.objects.create(
            course=comment.course,
            content=content,
            user=request.user,
            reply=comment
        )
    return redirect('course',comment.course.id)

