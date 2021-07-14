from django import forms

class ContactForm(forms.Form):
   name = forms.CharField(label = "nombre",required=True,widget=forms.TextInput(
       attrs={'class':'form-control','placeholder':'Escribe tu nombre'}
       ),min_length=3,max_length=50)
   email =forms.EmailField(label = "Email",required=True,widget=forms.EmailInput(
       attrs={'class':'form-control','placeholder':'Escribe tu Email'}
       ))
   content =  forms.CharField(label = "Contenido",required=True,widget=forms.Textarea(
       attrs={'class':'form-control', 'rows':3,'placeholder':'Escribe tu mensaje'}
       ))