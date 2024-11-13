from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        label = {
        "title" : "Car model",
        "description" : "Price",
        }

        widgets ={
        "title" : forms.TextInput(attrs={"placeholder":"Add unit here"}),
        "description" : forms.TextInput(attrs={"placeholder":"Add Price"}), 
        }