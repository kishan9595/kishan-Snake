from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs) 
        
        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class':'input'})   