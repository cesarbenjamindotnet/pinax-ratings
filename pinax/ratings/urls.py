from django.urls import re_path

from pinax.ratings import views

app_name = "pinax_ratings"


urlpatterns = [
    re_path(r"^(?P<content_type_id>\d+)/(?P<object_id>\d+)/rate/$", views.RateView.as_view(), name="rate"),
]
