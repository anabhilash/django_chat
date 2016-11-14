from django.db import IntegrityError
from django.db import transaction
from django.shortcuts import render, redirect
import haikunator
from django.contrib.auth.models import User
from .models import Room
from django.http import HttpResponse
from django.contrib.auth import login,authenticate


def landing(request):

    if request.user.is_authenticated():
        room_object = Room.objects.all()
        return render(request, "landing/index.html", context={"is_it": "YES", "rooms": room_object})
    else:
        return render(request, "landing/index.html", context={"is_it": "NO"})


def new_room(request):
    """
    Randomly create a new room, and redirect to it.
    """
    if request.method == 'POST':
        if request.user.is_authenticated():
            try:
                room = Room.objects.create(label=request.POST['label_name'],user=request.user)
                room.save()
            except IntegrityError:
                return HttpResponse('not')
            return HttpResponse('created')
        else:
            return HttpResponse('not authenticated')


def chatroom(request, label):
    room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chat/room.html",context= {
        'room': room,
        'messages': messages,
        'name' : request.user.username
    })


def clientregister(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        try:
            user=User.objects.create_superuser(username,email,password)
            user.save()
        except IntegrityError:
            return HttpResponse('INVALID')
        return HttpResponse('valid')


def clientlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('valid')
        else:
            return HttpResponse('invalid')
