from django.urls import re_path

from project import views

urlpatterns = [
    re_path(r'^profile/$', views.Profile.as_view(), name="profile"),
    re_path(r'^add-reservation/$', views.AddReservation.as_view(), name="add"),
    re_path(r'^login/$', views.Login.as_view(), name="login"),
    # re_path(r'^register/$', views.Register.as_view(), name="register"),
    re_path(r'^dashboard/$', views.dashboard, name="dashboard"),
    re_path(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    re_path(r'^view-reservations/$',
        views.view_reservations, name="view_reservations"),
    re_path(r'^update-reservation/(?P<pk>\d+)/$',
        views.UpdateReservation.as_view(), name="update_reservation"),
]
