from modeltranslation.translator import translator, TranslationOptions
from .models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

class ArticleTranslationOptions(TranslationOptions):
    fields = ()

translator.register(News, NewsTranslationOptions)
