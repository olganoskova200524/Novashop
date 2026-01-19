from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductUnpublishView, CategoryProductsView

from django.conf import settings
from django.views.decorators.cache import cache_page

app_name = 'catalog'

product_detail_view = ProductDetailView.as_view()

if settings.CACHE_ENABLED:
    product_detail_view = cache_page(60 * 5)(product_detail_view)

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>/', product_detail_view, name='detail'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('product/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='unpublish'),
]
