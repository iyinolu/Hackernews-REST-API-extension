from rest_framework.pagination import PageNumberPagination

class BasicPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page'
    max_page_size = 5