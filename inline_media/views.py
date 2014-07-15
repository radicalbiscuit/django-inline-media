#-*- coding: utf-8 -*-

import simplejson

from django.http import HttpResponse
from django.conf import settings

from sorl.thumbnail import get_thumbnail

from inline_media.models import Picture


def render_inline(request, size, align, oid):
    try:
        picture = Picture.objects.get(pk=oid)
    except Picture.DoesNotExist:
        if settings.DEBUG:
            raise Picture.DoesNotExist, "Picture id '%s' does not exist"
        else:
            return ''
    im = get_thumbnail(picture.picture, size)
    json = simplejson.dumps({"src": im.url, 
                             "title": picture.title, 
                             "width": size, 
                             "align": align})
    return HttpResponse(json, mimetype='application/json')
