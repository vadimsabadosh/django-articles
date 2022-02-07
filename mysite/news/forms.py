from django import forms

from .models import Category, News
import re


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=100, label="Назва", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label="Контент", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
#     is_published = forms.BooleanField(label="Опубліковано", initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категорія", empty_label="Виберіть категорію",  widget=forms.Select(attrs={'class': 'form-select'}))
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise forms.ValidationError('Назва не повинна починатися з цифри')
        return title
