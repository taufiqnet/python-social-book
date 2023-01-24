from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import (
    ListView,
    FormView,
    TemplateView,
    DetailView,
    UpdateView,
    RedirectView,
    DeleteView
)
from .models import Invoice
from .forms import InvoiceForm
# Create your views here.


class InvoiceListView(ListView):
    model = Invoice
    template_name = "inovices/invoice_list.html"  # default invoice_list.html

    # paginate_by
    context_object_name = 'qs'



