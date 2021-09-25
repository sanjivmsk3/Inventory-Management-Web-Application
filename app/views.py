from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView

from app.models import *
from app.forms import *
# Create your views here.


class Home(ListView):
    queryset = Product.objects.all()
    context_object_name = 'allProduct'
    template_name = 'home.html'

class Location(ListView):
    queryset = Location.objects.all()
    context_object_name = 'allLocation'
    template_name = 'all-locations.html'

class Movements(ListView):
    queryset = ProductMovement.objects.all()
    context_object_name = 'allProductMovement'
    template_name = 'movement.html'


class AddProduct(View):
    def get(self, request):
        form = ProductAddForm()
        return render(request, 'add-procduct.html', {'forms':form})

    def post(self, request):
        form = ProductAddForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')

class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductAddForm
    template_name = 'update-product.html'

    def form_valid(self, form):
        form.save()
        return redirect('home')

class UpdateLocations(UpdateView):
    model = Location
    form_class = LocationAddForm
    template_name = 'update-location.html'

    def form_valid(self, form):
        form.save()
        return redirect('all-location')

class AddLocation(View):
    def get(self, request):
        form = LocationAddForm()
        return render(request, 'add-location.html',{'forms':form})

    def post(self, request):
        form = LocationAddForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('all-location')




class AddProductMovement(View):
    def get(self,request):
        form = ProductMovementForm()
        return render(request,'add-productmovement.html',{'forms':form})

    def post(self, request):
        form = ProductMovementForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('all-productmovement')


class UpdateMovement(UpdateView):
    model = ProductMovement
    form_class = ProductMovementForm
    template_name = 'update-movement.html'

    def form_valid(self, form):
        form.save()
        return redirect('all-productmovement')

class Report(View):
    def get(self, request):
        context = {
            'allreport':ProductMovement.objects.all()
        }
        return render(request,'reports.html',context)