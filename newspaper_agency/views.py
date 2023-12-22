from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Topic


@login_required
def index(request):
    """View function for the home page of the site."""

    num_topics = Topic.objects.count()
    # num_cars = Car.objects.count()
    # num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_topic": num_topics,
        # "num_cars": num_cars,
        # "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1,
    }
    return render(request, "newspaper_agency/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper_agency/topic_list.html"
    paginate_by = 5

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(TopicListView, self).get_context_data(**kwargs)
    #     name = self.request.GET.get("name", "")
    #     context["search_form"] = TopicSearchForm(
    #         initial={"name": name}
    #     )
    #     return context
    #
    # def get_queryset(self):
    #     queryset = Topic.objects.all()
    #     form = TopicSearchForm(self.request.GET)
    #     if form.is_valid():
    #         return queryset.filter(name__icontains=form.cleaned_data["model"])
    #     return queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper_agency:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper_agency:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper_agency:topic-list")


