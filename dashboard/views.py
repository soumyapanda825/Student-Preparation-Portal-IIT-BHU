#from pyexpat.errors import messages
from django.shortcuts import redirect, render
from . forms import *
from django.contrib import messages
from django.views import generic

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form =NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        #messages.success(request,f"Notes Added from {request,user.username} Successfully!")
        messages.success(request,f"Notes Added from {request.user.username} Successfully!")
    else:
        form = NotesForm()
    notes= Notes.objects.filter(user=request.user)
    context ={'notes' : notes, 'form':form}
    return render(request,'dashboard/notes.html',context)

def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

class NotesDetailView(generic.DetailView):
    model =  Notes

def assignment(request):
    assignment = Assignments.objects.filter(user=request.user)
    context={'assignments': assignment}
    return render(request, 'dashboard/assignment.html', context)