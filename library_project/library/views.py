# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.db.models import Q

from .models import Author, Book, Work, Series, Shelf, BookAuthors, BookShelves, BookRating
from .serializers.Register import RegisterSerializer
from .serializers.Login import LoginSerializer
from .serializers.Authors import AuthorSerializer
from .serializers.Books import BookSerializer
from .serializers.Works import WorkSerializer
from .serializers.Series import SeriesSerializer
from .serializers.Shelfs import ShelfSerializer
from .serializers.Book_authors import BookAuthorsSerializer
from .serializers.Book_shelves import BookShelvesSerializer
from .serializers.Book_ratings import BookRatingsSerializer


# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Book Views
class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('search', None)

        if search_query:
            # Filter by book title or author name
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(authors__name__icontains=search_query)
            ).distinct()

        return queryset


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Work Views
class WorkListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

# Series Views
class SeriesListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class SeriesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

# Shelf Views
class ShelfListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer

class ShelfRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer

# BookAuthors Views
class BookAuthorsListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = BookAuthors.objects.all()
    serializer_class = BookAuthorsSerializer

class BookAuthorsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookAuthors.objects.all()
    serializer_class = BookAuthorsSerializer

# BookShelves Views
class BookShelvesListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = BookShelves.objects.all()
    serializer_class = BookShelvesSerializer

class BookShelvesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookShelves.objects.all()
    serializer_class = BookShelvesSerializer

# BookRatings Views (Optional)
class BookRatingsListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookRating.objects.all()
    serializer_class = BookRatingsSerializer

class BookRatingsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookRating.objects.all()
    serializer_class = BookRatingsSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Create the user
        return Response({
            'username': user.username,
            'email': user.email,
        }, status=status.HTTP_201_CREATED)  # 201 Created

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Authenticate the user
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username,  # Return the username in the response
            }, status=201)  # 201 Created
        else:
            return Response({"detail": "Invalid credentials"}, status=400)    