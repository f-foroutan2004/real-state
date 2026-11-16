from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title',
            'description',
            'property_type',
            'status',
            'price',
            'area',
            'rooms',
            'address',
            'city',
            'amenities',
        ]

        labels = {
            'title': 'عنوان ملک',
            'description': 'توضیحات',
            'property_type': 'نوع ملک',
            'status': 'نوع معامله',
            'price': 'قیمت',
            'area': 'متراژ',
            'rooms': 'تعداد اتاق',
            'address': 'آدرس',
            'city': 'شهر',
            'amenities': 'امکانات',
        }