import forms
from .models import Data1

class Data1Form(forms.Form):
    class meta:
        model=Data1
        fields='__all__'