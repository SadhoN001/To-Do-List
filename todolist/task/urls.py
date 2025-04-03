from django.urls import path
from . views import (home, TaskView, TaskAddView, TaskDetailView, TaskUpdateView, TaskDeleteView, CustomerRegistrationView,
                     CreateCustomerProfileView, CustomerProfileView, UpdateCustomerProfileView, DeleteCustomerProfileView,
                     )

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from django.contrib.auth.models import User
from . forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    path('home/', home),
    path('task/', TaskView.as_view(), name='task'),
    path('addtask/', TaskAddView.as_view(), name='addtask'),
    path('taskdetails/<int:pk>', TaskDetailView.as_view(), name='taskdetails'),
    path('taskupdate/<int:pk>', TaskUpdateView.as_view(), name='taskupdate'),
    path('taskdelete/<int:pk>', TaskDeleteView.as_view(), name='taskdelete'),
    
    path('profile/',CustomerProfileView.as_view(), name='profile'),
    path('create-profile/',CreateCustomerProfileView.as_view(), name='create-profile'),
    path('update-profile/<int:pk>/',UpdateCustomerProfileView.as_view(), name='update-profile'),
    path('delete-profile/<int:pk>/',DeleteCustomerProfileView.as_view(), name='delete-profile'),
    
    #Authentication part
    path('login/',auth_view.LoginView.as_view(template_name='task/login.html', authentication_form=LoginForm),name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page= 'login'), name='logout'),
    path('registration/', CustomerRegistrationView.as_view(), name='registration'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='task/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='task/passwordchangedone.html'), name='passwordchangedone'), 
    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name= 'task/password_reset.html', form_class= MyPasswordResetForm), name="password_reset"),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name= 'task/password_reset_done.html'), name="password_reset_done"),
    
    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name= 'task/password_reset_confirm.html', form_class= MySetPasswordForm), name="password_reset_confirm"),
    
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name= 'task/password_reset_complete.html', ), name="password_reset_complete"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
