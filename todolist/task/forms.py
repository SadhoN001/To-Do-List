from django import forms
from . models import Task, Customer
from django.contrib.auth.forms import (AuthenticationForm, UsernameField, UserCreationForm ,PasswordChangeForm,
                                       PasswordResetForm, SetPasswordForm)
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'task_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-md', 'rows': 4}),
            'completed': forms.CheckboxInput(attrs={'class': 'h-5 w-5'}),
            'task_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 border rounded-md'}),
        }
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': 'True',
        'class': 'w-full p-3 text-lg border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
    }))
    
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'w-full p-3 text-lg border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
        })
    )
    
class CustomRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autofocus': 'True',
            'class': 'w-full p-3 text-lg border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'placeholder': 'Enter your username'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-3 text-lg border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'placeholder': 'Enter your email'
        })
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 text-lg border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'placeholder': 'Enter password'
        })
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 text-lg border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class CreateCustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'mobile', 'city', 'address', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none'}),
            'mobile': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none'}),
            'city': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none'}),
            'address': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none'}),
        } 
        
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password', 
        widget=forms.PasswordInput(attrs={
            'autofocus': 'True',
            'autocomplete': 'current-password',
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    new_password1 = forms.CharField(
        label='New Password', 
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    new_password2 = forms.CharField(
        label='Confirm Password', 
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'})
    )
    
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
            }
        )
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
            }
        )
    )