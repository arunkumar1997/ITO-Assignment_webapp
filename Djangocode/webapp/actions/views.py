from django.shortcuts import render ,HttpResponseRedirect
from .forms import CarRegistration
from .models import Car
from django.contrib import messages

# Create your views here.
#for adding and shoing car
def show_add(request):
	fm= None
	fmclass = CarRegistration
	if request.method == 'POST':
		fm = fmclass(request.POST or None)
		if fm.is_valid():
			fm.save()
			fm = fmclass()
		else:
			fm = fmclass()
	allcar = Car.objects.all()
	return render(request,'actions/showandadd.html',{'form':fm,'ac': allcar })



#for updating
def update_car(request,id):
	pi = None
	fm  = None
	if request.method == 'POST':
		pi = Car.objects.get(pk=id)
		fm = CarRegistration(request.POST, instance=pi)
		if fm.is_valid():
			fm.save()
		else:
			pi = Car.objects.get(pk=id)
			fm = CarRegistration(instance=pi)
	return render(request, 'actions/updatecar.html',{'form':fm})


#For deliting car
def delete_car(request,id):
	pi = None
	if request.method == 'POST':
		pi = Car.objects.get(pk=id)
		pi.delete()
		return HttpResponseRedirect('/')


#for searching

