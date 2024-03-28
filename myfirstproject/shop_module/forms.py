from django import forms

from shop_module.models import UserUploadFile


class TestForm(forms.ModelForm):
    class Meta:
        model = UserUploadFile
        fields = '__all__'
