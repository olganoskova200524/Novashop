from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
