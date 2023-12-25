from django.urls import path
from .views import (
    index,
    TopicListView, TopicCreateView, TopicUpdateView, TopicDeleteView,
    RedactorListView, RedactorCreateView, RedactorDeleteView, RedactorDetailView
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "topic/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "topic/create/",
        TopicCreateView.as_view(),
        name="topic-create",
    ),
    path(
        "topic/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update",
    ),
    path(
        "topic/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete",
    ),

    path("redactor/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"
    ),
    path("redactor/create/", RedactorCreateView.as_view(), name="redactor-create"),
    # path(
    #     "redactor/<int:pk>/update/",
    #     RedactorYearsExperienceUpdateView.as_view(),
    #     name="redactor-update",
    # ),
    # path(
    #     "redactor/<int:pk>/delete/",
    #     RedactorDeleteView.as_view(),
    #     name="redactor-delete",
    # ),

]

app_name = "newspaper_agency"
