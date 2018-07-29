from rest_framework.pagination import PageNumberPagination


class PostListPagination(PageNumberPagination):
    page_size = 2
