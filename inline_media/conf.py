#-*- coding: utf-8 -*-

from django.conf import settings

# Defaulted to Django 1.4 path
ADMIN_IMAGES_PATH = getattr(settings, 
                            "ADMIN_IMAGES_PATH", 
                            "%s/admin/img" % settings.STATIC_URL)

# Defines custom picture sizes for app_label.model and size_type combinations.
# It's a 2-level depth dictionary with 'app_label.model' as keys for the 
# 1st level and 'size_type' as keys for the 2nd level. There are 5 size_types
# (mini, small, medium, large and full) that you can customize in two ways.
# One way is by just adjusting the sizes declaring this setting. Another way
# consist of declaring templates in 'templates/inline_media' directory with
# names '<app_label>.<model>.<size_type>.html'. The default template
# <app_label>.<model>.default.html will be used as a fallback.
# Size values may be just an int, a tuple or anything else. When the size is 
# an int it represents the width of the thumbnail for the picture. When the
# size is a tuple it represents the geometry (width, height) for the thumbnail.
CUSTOM_SIZES = getattr(settings,
                       'INLINE_MEDIA_CUSTOM_SIZES',
                       {'inline_media.picture':
                            {'mini': 80,
                             'small': 150,
                             'medium': 200,
                             'large': 250,
                             'full': 'full'},
                        'inline_media.pictureset':
                            {'mini': (80, 80),
                             'small': (150, 150),
                             'medium': (200, 200),
                             'large': (250, 250),
                             'full': (380, 280)}
                        })

# Default size in case the entry corresponding to an app_label.model and 
# size_type does not exist in INLINE_MEDIA_CUSTOM_SIZES
DEFAULT_SIZE = getattr(settings, 'INLINE_MEDIA_DEFAULT_SIZE', 200)

# Quick way to site-wide change attributes of TextareaWithInlines widget
TEXTAREA_ATTRS = getattr(settings, 
                         'INLINE_MEDIA_TEXTAREA_ATTRS', 
                         {})

