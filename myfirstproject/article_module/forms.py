from django import forms
from .models import ArticleComments


class CommentForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': "نام شما ...", }),
                           label='نام شما',
                           error_messages={
                               'required': 'نوشتن نام ضروری است',
                               'max_length': 'نام نباید خیلی طولانی باشد'
                           })
    text = forms.CharField(max_length=600,
                           widget=forms.Textarea(attrs={'placeholder': "متن پیام ...", 'rows': "11", 'id': 'text'}),
                           label='نظر شما',
                           error_messages={
                               'required': 'نوشتن نظر ضروری است',
                               'max_length': 'نظر نباید خیلی طولانی باشد',
                           })

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = ArticleComments
#         fields = '__all__'
#         widgets = {
#             'text': forms.Textarea(attrs={'placeholder': 'نظر خود را وارد کنید!', 'rows': 11})
#         }
