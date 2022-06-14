from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Contact
from .forms import ContactForm


class LoginCustom(LoginView):
    # form_class = UserCreationForm
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('contacts-list')


class RegisterCustom(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('contacts-list')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterCustom, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('contacts-list')
        return super(RegisterCustom, self).get(*args, **kwargs)


# -----------------------------------------------
# CRUD views


class Contacts(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'index.html'
    context_object_name = 'contacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Contacts, self).get_context_data(**kwargs)
        # context['contacts']= context['contacts'].filter(user=self.request.user)
        search_input = self.request.GET.get('search-area')
        if search_input:
            context['contacts'] = context['contacts'].filter(full_name__icontains=search_input)
            context['search_input'] = search_input
        else:
            context['search_input'] = ' '
        return context


class ContactProfile(LoginRequiredMixin, DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'contact-profile.html'


class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'new.html'

    # def form_valid(self, form):
    #     full_name = form.full_name
    #     relationship = form.relationship
    #     email = form.email
    #     phone_number = form.phone_number
    #     address = form.address

    def get_success_url(self):
        return reverse('contact-profile', kwargs={'pk': self.object.pk})


class ContactEdit(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'edit.html'
    context_object_name = 'contact'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contact-profile', kwargs={'pk': self.object.pk})


class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    context_object_name = 'contact'
    success_url = reverse_lazy('contacts-list')
