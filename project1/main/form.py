from django import forms
from django.core.validators import MaxLengthValidator
class IsmForm(forms.Form):
    Ismingizni_kiriting  = forms.CharField(max_length=40, required=True, strip=True , validators=[MaxLengthValidator(10)])
    Familiyangizni_kiriting  = forms.CharField(max_length=40)
    Tugilgan_yilingizni_kiriting = forms.IntegerField(min_value=1970, max_value=2022)




