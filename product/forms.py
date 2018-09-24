from django import forms
from product.models import Products

class ProductForms(forms.Form):

    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class' : 'product_title',
            'placeholder' : "Введите заголовок ..."
        })
    )

    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'product_description',
            'placeholder' : "Небольшое описание и как с вами связаться ..."
        })
    )

    city = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'product_city',
            'placeholder' : 'Введите ваш город ...'
        })
    )

    price = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class' : 'product_price',
            'placeholder' : "Информация о цене ..."
        })
    )


    # photo = forms.FileField(
    #     required=False,
    #     label='',
    #     widget=forms.FileInput(attrs={
    #         'class' : 'product_file'
    #     })
    # )


    # class Meta:
    #     model = Products
    #     fields = ('photo',)


    # img = forms.FileField(
    #     required=False,
    #     label='',
    #     widget=forms.FileInput(attrs={
    #         'class': 'product_file'
    #     })
    # )
