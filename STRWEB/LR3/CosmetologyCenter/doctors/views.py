from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Doctor

# Create your views here.
def index(request):
    doctors = Doctor.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        doctors = doctors.filter(
            first_name__icontains=search_query
        ) | doctors.filter(
            last_name__icontains=search_query
        )

    return render(request, 'doctors/doctors-list.html', context={'doctors': doctors})

def contacts(request):
    doctors = Doctor.objects.all().order_by('last_name', 'first_name')
    return render(request, 'doctors/contacts.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        data = request.POST
        doctor = Doctor(
            last_name=data.get('last_name'),
            first_name=data.get('first_name'),
            image=data.get('image'),
            category=data.get('category'),
            phone=data.get('phone'),
            email=data.get('email'),
        )
        doctor.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctors/doctor-detail.html'
    context_object_name = 'doctor'
