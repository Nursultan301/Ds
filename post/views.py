from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.utils.translation import ugettext_lazy as _

from post.forms import FeedbackForm
from post.models import IssykKul, Naryn, Chui, Talas, Gallery


class Areas(TemplateView):
    template_name = "post/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = []
        regions = [
            {'name': _('Иссык-кульская область'), '_class': IssykKul, 'id': 'issykkul'},
            {'name': _('Нарынская область'), '_class': Naryn, 'id': 'naryn'},
            {'name': _('Чуйская область'), '_class': Chui, 'id': 'chui'},
            {'name': _('Таласская область'), '_class': Talas, 'id': 'talas'},
        ]
        for region in regions:
            context['regions'].append({
                "name": region['name'],
                "objects": region['_class'].objects.all(),
                'id': region['id']
            })
        return context


class ContactForm(FormView):
    form_class = FeedbackForm
    template_name = "post/contact.html"
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(ContactForm, self).form_valid(form)


class GalleryView(TemplateView):
    template_name = "post/gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["galleries"] = Gallery.objects.all()
        return context

