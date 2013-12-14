import sae
import sys,os
import django.core.handlers.wsgi

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, response_headers)
    return ['<strong>Welcome to SAE!</strong>']

#application = sae.create_wsgi_app(app)


os.environ['DJANGO_SETTINGS_MODULE'] = 'smart_contacts.settings'
application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())