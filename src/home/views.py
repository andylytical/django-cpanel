from django.shortcuts import render
from django.http import HttpResponse
import datetime

def homepage( request ):
    time_now = datetime.datetime.now()
    html_resp = f'''
        <html>
        <body>
        <h2>{time_now}</h2>
        </body>
        </html>
    '''
    return HttpResponse( html_resp )
