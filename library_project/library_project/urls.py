from django.contrib import admin
from django.urls import path, include
from library.swagger import schema_view
from rest_framework.routers import DefaultRouter
from library.views import  RegisterView, LoginView ,BookAuthorsRetrieveUpdateDestroyView,BookAuthorsListCreateView, AuthorListCreateView,AuthorRetrieveUpdateDestroyView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='token_obtain_pair'),  # JWT login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger-json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    # Books
    path('api/books/',BookAuthorsListCreateView .as_view(), name='book-list'),  # GET: Retrieve all books, POST: Create new book (protected)
    path('api/books/<int:id>/', BookAuthorsRetrieveUpdateDestroyView.as_view(), name='book-detail'),  # GET: Retrieve a specific book, PUT: Update book, DELETE: Delete book (protected)

    # Authors
    path('api/authors/', AuthorListCreateView.as_view(), name='author-list'),  # GET: Retrieve all authors, POST: Create new author (protected)
    path('api/authors/<int:id>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),  # GET: Retrieve a specific author, PUT: Update author, DELETE: Delete author (protected)
]