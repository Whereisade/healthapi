from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Blog
from .serializers import BlogSerializer

#doctors only
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "doctor":
            raise ValidationError("Only doctors can create blogs.")
        serializer.save(author=self.request.user)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        blog = self.get_object()
        if self.request.user != blog.author:
            raise ValidationError("You can only edit your own blogs.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise ValidationError("You can only delete your own blogs.")
        instance.delete()
