from modeltranslation.translator import translator, TranslationOptions
from .models import News, Article


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'description')


translator.register(News, NewsTranslationOptions)
translator.register(Article, ArticleTranslationOptions)
