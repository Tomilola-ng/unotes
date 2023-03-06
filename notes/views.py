from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Note
from .forms import CustomUserCreationForm
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def me(request):
    notes = Note.objects.filter(user = request.user)
    context = {
        'notes' : notes
    }
    return render(request, 'core/dashboard.html', context)


def home(request):
    return render(request, 'core/home.html')


def register(request):
    if request.method == 'GET':
        context = {
            'form': CustomUserCreationForm,
            'formname': 'Sign Up'
        }
        return render(request, 'core/form.html', context )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('meView'))
    
    context = {
        'form': CustomUserCreationForm,
        'formname': 'Sign Up'
    }
    return render(request, 'core/form.html', context )


class NoteCreate(LoginRequiredMixin , CreateView):
    model = Note
    template_name = 'core/form.html'
    fields = ['title', 'content']

    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['formname'] = 'New Notes'
        return context 

    def form_valid(self, form):
        form.instance.user = self.request.user        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('meView')


class NoteUpdate(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
    model = Note
    template_name = 'core/form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

    def get_success_url(self):
        return reverse('meView')

    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['formname'] = 'Update Note'
        return context 
        

class NoteDelete(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Note
    template_name = 'core/confirm.html'

    def get_success_url(self):
        return reverse('meView')

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'core/detail.html'