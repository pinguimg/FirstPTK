from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views import generic
from sorrie.models import Dentist, Category, Post
from django.utils import timezone


class IndexView(generic.ListView):
    model = Dentist
    template_name = 'sorrie/index.html'
    context_object_name = 'latest_dentist_list'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dentists'] = Dentist
        context['posts'] = Post.objects.all()

        return context

    def get_queryset(self):
        """Return the last five published questions."""
        return Dentist.objects.order_by('-pub_date')[:8]



class DetailView(generic.DetailView):
    def get_queryset(self):
        model = Dentist
        template_name = 'sorrie/detail.html'
        return Dentist.objects.filter(pub_date__lte=timezone.now())
        """
        Excludes any questions that aren't published yet.
        """


class ResultsView(generic.DetailView):
        model = Dentist
        template_name = 'sorrie/results.html'