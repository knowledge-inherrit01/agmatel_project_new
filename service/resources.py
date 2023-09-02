from import_export import resources
from .models import Data1



class DataResource(resources.ModelResource):
    class meta:
        model=Data1