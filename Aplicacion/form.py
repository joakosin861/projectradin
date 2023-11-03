from django import forms


class AgregarFactura(forms.Form):
    detalle = forms.CharField(label='Detalle',
                              widget=forms.TextInput(attrs={'class':'form-control'}))
    num_factura = forms.IntegerField(label='Numero de factura',
                                     widget=forms.TextInput(attrs={'class':'form-control'}))
