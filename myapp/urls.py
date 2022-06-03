from unicodedata import name
from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.InsertPageView,name="insertpage"),
    path("insert/",views.InsertData,name="insert"),
    path("showtable/",views.ShowTable,name="showtable"),
    path("editpage/<int:pk>",views.EditPage,name="editpage"),
    path("update/<int:pk>",views.UpdateData,name="update"),
    path("delete/<int:pk>",views.DeleteData,name="delete"),

   
]