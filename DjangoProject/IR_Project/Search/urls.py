from django.urls import path
from .views import home, search_page, upload_page

app_name = "Search"

urlpatterns = [
    path('', home),
    path('results/', search_page, name="search-page"),
    path('upload-page/', upload_page, name="upload-page"),
]
