
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("<int:id>/delete", views.delete_post, name="delete_post"),
    path("new_post/", views.new_post, name="new_post"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<int:pk>", views.like, name="likes"),
    path("<int:id>/edit", views.edit_post, name="edit_post"),
    path("search_venues", views.search_venues, name="search-venues"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
