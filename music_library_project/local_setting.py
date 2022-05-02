# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%9)6+6(^8n3(&t5qzqz&_kf36i@no=xm%352er6ga-z#6^&h^b'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_database', 
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '91_Bravo746'
    }
}