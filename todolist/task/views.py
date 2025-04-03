from django.shortcuts import render, redirect
from django.views import View
from . models import Task, Customer
from . forms import TaskForm, CustomRegistrationForm, CreateCustomerProfileForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView 
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import JsonResponse
from django.db import IntegrityError

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

def home(request):
    return render(request, 'task/base.html') 

@method_decorator(login_required, name="dispatch")
class TaskView(View):
    def get(self, request):
        # Ensure only logged-in users can access tasks
        if not request.user.is_authenticated:
            return redirect("login")  # Redirect to login page

        task = Task.objects.filter(user=request.user)  # ✅ Safe way to filter tasks
        return render(request, "task/tasks.html", locals())
    
class TaskDetailView(View):
    def get(self, request,pk):
        task= Task.objects.get(pk=pk)
        return render(request, 'task/taskdetails.html', locals())
    
class TaskAddView(CreateView):
    model= Task
    form_class= TaskForm 
    template_name = 'task/addtask.html'
    success_url= reverse_lazy('task')
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the current user
        return super().form_valid(form)
    
class TaskUpdateView(UpdateView):
    model= Task
    form_class= TaskForm 
    template_name = 'task/updatetask.html'
    def get_success_url(self):
        return reverse('taskdetails', kwargs={'pk': self.object.pk}) 
    
class TaskDeleteView(DeleteView):
    model= Task
    template_name = 'task/deletetask.html'
    success_url= reverse_lazy('task')
    
    
class CustomerRegistrationView(View):
    def get(self,request):
        form= CustomRegistrationForm()
        return render( request, 'task/customregistration.html', locals())
    def post(self,request):
        form= CustomRegistrationForm(request.POST)
        if form.is_valid():# if all data is valid then save the data in database
             form.save() 
             messages.success(request, "Congratulationn! User Registration Succesfully")
        else:
            messages.warning(request,"Invalid input data")
        return render( request, 'task/customregistration.html', locals())
    
class CreateCustomerProfileView(CreateView):
    model= Customer
    form_class= CreateCustomerProfileForm 
    template_name = 'task/createcustomerprofile.html'
    success_url= reverse_lazy('profile')
    # def get_success_url(self):
    #     return reverse('profile', kwargs={'pk': self.object.pk}) 
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # 🔹 Assign the logged-in user
        return super().form_valid(form)
    
    
class CustomerProfileView(View):
    def get(self, request):
        customer= Customer.objects.filter(user= request.user)
        return render(request, 'task/profile.html', locals())
    
class UpdateCustomerProfileView(UpdateView):
    model= Customer
    form_class =CreateCustomerProfileForm
    template_name = 'task/updatecustomerprofile.html'
    success_url= reverse_lazy('profile')
    
    
class DeleteCustomerProfileView(DeleteView):
    model= Customer
    template_name = 'task/deletecustomerprofile.html'
    success_url= reverse_lazy('profile')