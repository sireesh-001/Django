from django import forms

class firstform(forms.Form):
    text=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' :'Enter todo e.g Grocery Shopping', 'aria-label' :'Todo', 'aria-describeby' : 'add-btn'}))