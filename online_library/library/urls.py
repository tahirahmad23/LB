from django.urls import path
from . import views
app_name = "library"

urlpatterns = [
    path("new-material/<course>",views.CreateMaterial.as_view(),name="creatematerial"),
    path("edit-material/<int:pk>",views.UpdateMaterial.as_view(),name="updatematerial"),
    path("delete-material/<int:pk>",views.DeleteMaterial.as_view(),name="deletematerial"),
    path("courses",views.CourseList.as_view(),name="courselist"),
    path("course/<int:pk>/",views.CourseDetail.as_view(),name="coursedetail"),
    path("course/material/<int:pk>/review",views.add_review,name="add_review"),
    path("search/",views.search_course,name="search"),
    path("courses/filtered",views.filter,name="filter")
]
