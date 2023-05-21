from django.shortcuts import render, redirect, get_object_or_404
from .models import BorderCrossing, Vaccine, VaccineRecord
from .forms import BorderCrossingForm, VaccineForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm


@login_required
def home(request):
    if request.method == 'POST':
        form = BorderCrossingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BorderCrossingForm()

    crossings = BorderCrossing.objects.all()

    return render(request, 'border/home.html', {'form': form, 'crossings': crossings})

def add_border_crossing(request):
    if request.method == 'POST':
        form = BorderCrossingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BorderCrossingForm()

    return render(request, 'border/add_border_crossing.html', {'form': form})

def view_vaccines(request, crossing_id):
    crossing = get_object_or_404(BorderCrossing, id=crossing_id)
    vaccines = Vaccine.objects.filter(border_crossing=crossing)

    return render(request, 'border/view_vaccines.html', {'crossing': crossing, 'vaccines': vaccines})

def add_vaccine(request, crossing_id):
    crossing = get_object_or_404(BorderCrossing, id=crossing_id)

    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            vaccine = form.save(commit=False)
            vaccine.border_crossing = crossing
            vaccine.save()
            return redirect('view_vaccines', crossing_id=crossing_id)
    else:
        form = VaccineForm()

    return render(request, 'border/add_vaccine.html', {'form': form, 'crossing': crossing})

def vaccination_records(request):
    records = VaccineRecord.objects.all()
    return render(request, 'border/records.html', {'records': records})

def login(request):
   
 
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})




def about(request):
    return render(request, 'border/about.html')