from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate



def home(request):
    notes = Note.objects.all().order_by('-created_at')
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['note']
        image = request.FILES['image']
        send = Note(title=title, content=content, image=image)
        send.save()
    return render(request, 'index.html', {"notes": notes})


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 :
            user = User.objects.create_user(email, username, password1)
            user.save()
            auth.login(request, user)
            return redirect('home')
        return redirect(request, 'nouser.html', {'wrong password': 'please sign up again'} )
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error_message = 'invalid username or password'
            return render(request, 'nologin.html', {'error_message': error_message})
    return render(request, 'Login.html')

# def update_note(request, pk):
#     mynote = get_object_or_404(Note, pk=pk)
#     if request.method == 'POST':
#         new_note = request.POST['newtitle']
#         mynote.send = new_note
#         mynote.save()
#         return redirect('updatenote')

#     return render(request,'update_note.html', {'mynote': mynote} )

# def delete_note(request, pk):
#     mynote_delete =get_object_or_404(Note, pk=pk)

#     return render(request, 'delete_note.html', {'mynote_delete': mynote_delete})


def addnote(request):
    return render (request, 'Addnote.html')




# Create your views here.
