from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Topic, Redactor
from .forms import RedactorCreationForm


@login_required
def index(request):
    """View function for the home page of the site."""

    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    # num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_topic": num_topics,
        "num_redactors": num_redactors,
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


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor

    # context_object_name = "redactor_list"
    # template_name = "newspaper_agency/redactor_list.html"
    #
    # paginate_by = 5

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(RedactorListView, self).get_context_data(**kwargs)
    #     search_username = self.request.GET.get("username", "")
    #     context["search_form"] = RedactorSearchForm(
    #         initial={"username": search_username}
    #     )
    #     return context
    #
    # def get_queryset(self):
    #     queryset = Redactor.objects.all()
    #     form = RedactorSearchForm(self.request.GET)
    #     if form.is_valid():
    #         return queryset.filter(
    #             username__icontains=form.cleaned_data["username"]
    #         )
    #     return queryset


# class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
#     model = Redactor
#     queryset = Redactor.objects.all().prefetch_related("cars__manufacturer")


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper_agency:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper_agency:redactor-list")

