from django import forms

class ComentarioForm(forms.Form):
    autor = forms.CharField(label='Nome' ,min_length=4, max_length=50)
    comentario = forms.CharField(label="comentario", min_length=1, widget=forms.Textarea)