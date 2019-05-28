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
        context['rootcategories'] = Category.objects.root_nodes()
        roots = context['rootcategories']
        #context['subcategories'] = Category.objects.add_related_count(IndexView.category_node.get_children(), Post, 'category', 'question_counts')
        x = 1
        for i in roots:

            context['subcategories' + str(x)] = Category.objects.get(name=i).get_children()
            x += 1

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