#-*- coding: utf-8 -*-

from django.forms.models import modelform_factory
from django.test import TestCase as DjangoTestCase
from django.utils import simplejson
from django.utils.html import conditional_escape

from inline_media.widgets import (TextareaWithInlines, InlinesDialogStr, 
                                  BaseInlinesDialogStr, build_imSizes_array)
from inline_media.tests.models import TestModel, AnotherTestModel


class TextareaWithInlinesWidgetAttrs(DjangoTestCase):
    def test_setting_textarea_attrs(self):
        ModelForm1 = modelform_factory(TestModel)
        ModelForm2 = modelform_factory(AnotherTestModel)
        defwidget = ModelForm1.base_fields['first_text'].widget
        widget1 = ModelForm1.base_fields['second_text'].widget
        widget2 = ModelForm2.base_fields['second_text'].widget
        # Model tests.TestModel has specific customized settings
        # for 'second_text' field (see: tests/settings.py)
        self.assertEqual(widget1.attrs['style'], 'font: 13px monospace')
        self.assertEqual(widget1.attrs['rows'], '20')
        # Model tests.AnotherTestModel doesn't have specific settings
        # but inherits 'style' as it's part of 'default' key of
        # settings.INLINE_MEDIA_TEXTAREA_ATTRS
        self.assertEqual(widget2.attrs['style'], 'font: 13px monospace')
        self.assertEqual(widget2.attrs['rows'], defwidget.attrs['rows'])


class AdminTextareaWithInlinesWidgetTestCase(DjangoTestCase):
    def test_render_textareawithinlines_widget(self):
        neilmsg = TestModel.objects.create(
            first_text="One small step for man", 
            second_text="One giant leap for mankind")
        widget = TextareaWithInlines()
        self.assert_(
            InlinesDialogStr("id_test").widget_string() in
            conditional_escape(widget.render("test", neilmsg.second_text)))


class IMSizesArrayTestsCase(DjangoTestCase):
    def test_imSizes_array_creation(self):
        default = ['mini', 'small', 'medium', 'large', 'full']
        expected = simplejson.dumps({
            'inline_media/picture': default,
            'inline_media/pictureset': ['medium', 'large', 'full'],
            'inline_media/tests/testmediamodel': default
        })
        self.assertEqual(expected, build_imSizes_array())
