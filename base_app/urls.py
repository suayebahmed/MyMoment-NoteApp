from django.urls import path
from .views import HomePageView, MomentDetailView, AddMomentView, EditMomentView, DeleteMomentView

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("moment/<int:pk>", MomentDetailView.as_view(), name="moment-detail-page"),
    path("add_moment/", AddMomentView.as_view(), name="add-moment-page"),
    path("moment/edit/<int:pk>", EditMomentView.as_view(), name="edit-moment-page"),
    path("moment/<int:pk>/delete", DeleteMomentView.as_view(), name="delete-moment-page"),
]
