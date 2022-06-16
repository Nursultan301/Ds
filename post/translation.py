from modeltranslation.translator import register, TranslationOptions

from post.models import IssykKul, Naryn, Chui, Talas


@register(IssykKul)
class IssykKulTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(Naryn)
class NarynTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(Chui)
class ChuiTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(Talas)
class TalasTranslation(TranslationOptions):
    fields = ('title', 'description')
