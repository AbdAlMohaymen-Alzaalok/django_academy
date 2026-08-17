from django.shortcuts import render,redirect
from . import models,forms
from courses.models import Course


def make_order(request,cid):
    course = Course.objects.get(pk=cid)
    if request.method=='POST':
        if request.POST.get('status')=='success':
            if models.Payment.objects.filter(
                    user=request.user,
                    course=course
            ).exists():
                return redirect('course', course.id)
            models.Payment.objects.create(
                amount=course.price,
                course=course,
                user=request.user,
                status=models.Status.completed
            )
    return redirect('right',cid=cid)

def my_courses(request):
    payments=models.Payment.objects.filter(
        user=request.user,
        status=models.Status.completed
    )
    courses=[payment.course for payment in payments]
    for course in courses:
        course.purchased=models.Payment.objects.filter(
            user=request.user,
            course=course,
            status=models.Status.completed
        ).exists() if request.user.is_authenticated else False
    return render(request,'courses/index.html',{
        'courses':courses
    })


