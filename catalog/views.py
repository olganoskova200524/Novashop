from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .forms import ProductForm
from .models import Product, Category
from .services import get_products_by_category


class ProductUnpublishView(PermissionRequiredMixin, View):
    permission_required = "catalog.can_unpublish_product"

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()
        return redirect(reverse("catalog:detail", args=[pk]))


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:detail', args=[self.object.pk])


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    raise_exception = True

    def get_success_url(self):
        return reverse('catalog:detail', args=[self.object.pk])

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:index')
    raise_exception = True

    def test_func(self):
        product = self.get_object()
        user = self.request.user

        return product.owner == user or user.has_perm('catalog.delete_product')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category').all()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class CategoryProductsView(ListView):
    model = Product
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = Category.objects.get(pk=category_id)
        return context
