from django import forms 
from .models import Item

class ItemForm(forms.ModelForm) :
    class Meta :
        model = Item
        fields=["item_name", "item_desc", "item_price", "items_image"]
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'item_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
