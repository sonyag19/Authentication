from rest_framework import serializers
from .models import *

class personForm(serializers.ModelSerializer):
    class Meta:
        model=person
        fields='__all__'
