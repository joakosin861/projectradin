from django.shortcuts import render
from django.urls import reverse_lazy
from .form import AgregarFactura
from .models import Facturas
from datetime import date
import requests
from django.views.generic import TemplateView, ListView, FormView, DeleteView


class Home(TemplateView):#home aca va el grafico con los datos de la DB
    template_name = 'home.html'


class AgregarFactura(FormView):
    template_name = 'agregar_factura.html'
    form_class = AgregarFactura
    success_url = 'lista_facturas/'

    def form_valid(self, form):
        factura = Facturas(
            detalle=form.cleaned_data['detalle'],
            num_factura=form.cleaned_data['num_factura'],
            agregado=date.today()
        )
        factura.save()
        return super().form_valid(form)


class ListaFacturas(ListView):
    model = Facturas
    context_object_name = 'facturas'
    template_name = 'facturaslista.html'


class EliminarFactura(DeleteView):
    model = Facturas
    success_url = reverse_lazy('lista_facturas')
    template_name = 'confirm_eliminar.html'


def consultapi(request):
    apikey = '930e1f93ca0489c588db0886e64c7296'
    url = 'https://api.stntrading.eu/GetKeyPrices/v1'
    respuesta = requests.get(url, params={'apikey': apikey}).json()
    buy = respuesta['result']['pricing']['buyPrice']
    sell = respuesta['result']['pricing']['sellPrice']
    return render(request, 'response_api.html',
                  {'buykey': round(buy * 0.11111, 2), 'sellkey': round(sell * 0.11111, 2)})
