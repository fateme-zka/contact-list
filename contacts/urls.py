from django.urls import path
from django.contrib.auth.views import LoginView

from .views import *

urlpatterns = [
    path('register/', RegisterCustom.as_view(), name='register'),
    path('login/', LoginCustom.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', Contacts.as_view(), name='contacts-list'),
    path('contact/<int:pk>/', ContactProfile.as_view(), name='contact-profile'),
    path('contact-create/', ContactCreate.as_view(), name='contact-create'),
    path('contact-edit/<int:pk>/', ContactEdit.as_view(), name='contact-edit'),
    path('contact-delete/<int:pk>/', ContactDelete.as_view(), name='contact-delete'),

]
