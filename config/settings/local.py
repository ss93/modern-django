from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='dqb3(66pzed_+)t)gqa9h7%2+x5jo)=1jg#!ob!qwshk6xabcq')
DEBUG = env.bool('DJANGO_DEBUG', default=True)