"""
Configuration file for py.test
"""

import os
import django


def pytest_configure():
    from django.conf import settings
    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "test.sqlite3",
            },
            'wordpress': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.environ.get('WP_NAME', 'wordpress_test'),
                'USER': os.environ.get('WP_USER', 'root'),
                'PASSWORD': os.environ.get('WP_PASSWORD', ''),
                'HOST': os.environ.get('WP_HOST', 'localhost'),
            },
        },
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "wordpress",
        ],
        MIDDLEWARE_CLASSES=[],
        SITE_ID=1,
        ROOT_URLCONF="wordpress.urls",
    )
    print(django.VERSION)
    django.setup()
