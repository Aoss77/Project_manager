from django.shortcuts import render, redirect
from Projects.models import Projects, Task
from Projects.forms import ProjectCreateForm, ProjectUpdateForm
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from . import models, forms


# Create your views here.
class ProjectListView(ListView):
    model = models.Projects
    template_name = "project/list.html"


class ProjectCreateView(CreateView):
    model = models.Projects
    form_class = forms.ProjectCreateForm
    template_name = "project/create.html"
    success_url = reverse_lazy('project_list')


class ProjectUpdateView(UpdateView):
    model = models.Projects
    form_class = forms.ProjectUpdateForm
    template_name = "project/update.html"
    success_url = reverse_lazy('project_list')

    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])


class ProjectDeleteView(DeleteView):
    model = models.Projects
    template_name = "project/delete.html"
    success_url = reverse_lazy('project_list')


class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskDeleteView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])