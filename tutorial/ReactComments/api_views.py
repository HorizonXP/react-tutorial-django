from rest_framework import viewsets
from ReactComments import models

class CommentViewSet(viewsets.ModelViewSet):
    model = models.Comment

class AuthorViewSet(viewsets.ModelViewSet):
    model = models.Author
