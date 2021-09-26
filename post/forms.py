from django import forms

class ComentarioForm(forms.Form):
    autor = forms.CharField()
    comentario = forms.CharField()