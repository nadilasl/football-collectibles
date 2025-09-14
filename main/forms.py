from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"
                  ,"stock", "brand", "release_year", "size", "edition_type", "condition", 
                  "authenticity_certificate", "rarity_level"
                ]