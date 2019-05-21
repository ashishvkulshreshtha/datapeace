from django.core.exceptions import FieldDoesNotExist
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from users.models import User
from .serializers import UserSerializer


# This function will check if field exist in given model or not.
def is_field_exist(model, field):
    try:
        model._meta.get_field(field)
        return True
    except FieldDoesNotExist:
        print("Field Does not exist")
        return False


# Custom Pagination class
class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 1000


# List and Create API View class
class UserListApiView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = User.objects.all()

        # name search field starts here.
        name = self.request.GET.get('name', None)
        if name:
            queryset = queryset.filter(Q(last_name__icontains=name) | Q(first_name__icontains=name))

        # ----------------Ordering Filter starts here.-------------------------
        order_by = self.request.GET.get('sort', None)
        # Check ordering is ascending or descending order.
        if order_by:
            if order_by[0] == '-':
                # remove minus sign if ordering is descending.
                field = order_by[1:]
            else:
                field = order_by
            # Check if field exist in model or not.
            if is_field_exist(User, field):
                queryset = queryset.order_by(order_by)
        # ----------------Ordering Filter ends here.-------------------------
        return queryset


# Retrieve, Update, Destroy User data APIView
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
