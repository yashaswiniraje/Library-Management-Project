"""
URL configuration for LibraryManagement project.
"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("gettoken/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
     path("register/",views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("api/books/", views.view_books_api, name="books-list"),
    path("books/create/", views.create_book_api, name="create_book"),
    path("books/update/<int:book_id>/", views.update_book_api, name="update_book"),
    path("books/delete/<int:book_id>/", views.delete_book_api, name="delete_book"),
]
