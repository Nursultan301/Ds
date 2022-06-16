from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from post.models import IssykKul, Naryn, Chui, Talas, Feedback, Gallery


@admin.register(IssykKul)
class IssykKulAdmin(TranslationAdmin):
    list_display = ('title', 'get_photo')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="75">')


@admin.register(Naryn)
class NarynAdmin(TranslationAdmin):
    list_display = ('title', 'get_photo')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="75">')


@admin.register(Chui)
class ChuiAdmin(TranslationAdmin):
    list_display = ('title', 'get_photo')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="75">')


@admin.register(Talas)
class TalasAdmin(TranslationAdmin):
    list_display = ('title', 'get_photo')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="75">')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('get_photo', 'date')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="75">')