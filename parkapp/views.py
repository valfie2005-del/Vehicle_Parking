from django.shortcuts import redirect, render
from .forms import ParkingForm
from .models import Parking
from rest_framework import viewsets
from .serializers import ParkSerializer

# Create your views here.
def parkFormView(request):
    form = ParkingForm()
    if request.method == 'POST':
        form = ParkingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'parking.html'
    context = {'form': form}
    return render(request, template_name, context)
def showView(request):
    obj = Parking.objects.all()
    template_name = 'show.html'
    context = {'obj': obj}
    return render(request, template_name, context)
def updateView(request, f_Pid):
    obj = Parking.objects.get(Pid=f_Pid)
    form = ParkingForm(instance=obj)
    if request.method == 'POST':
        form = ParkingForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'parking.html'
    context = {'form': form}
    return render(request, template_name, context)
def deleteView(request, f_Pid):
    obj = Parking.objects.get(Pid=f_Pid)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)


class ParkViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkSerializer