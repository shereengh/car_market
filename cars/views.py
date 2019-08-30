from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Car
from .forms import CarForm
def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	#Complete Me
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save()
            messages.success(request, "Car created successfully!")
            return redirect(car)
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)




def car_update(request, car_id):
    car_obj = Car.objects.get(id=car_id)
    form = CarForm(instance=car_obj)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES,instance=car_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Car updated successfully!")
            return redirect(car_obj)
    context = {
        "form":form,
        "car": car_obj,
        
    }
    return render(request, 'update.html', context)

def car_delete(request, car_id):
	#Complete Me
    car_obj = Car.objects.get(id=car_id)
    car_obj.delete()
    messages.warning(request, "You deleted a car!")
    return redirect('car-list')
