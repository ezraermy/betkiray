from django.shortcuts import render
from .gofor import Gofor

# Create your views here.
def gofor_detail(request):
    gofor = Gofor(request)
    akeraysstring = ''

    for item in gofor:
        akeray = item['akeray']
        url = '/%s/' % (akeray.id)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'subcity': '%s', 'phone': '%s', 'url': '%s'}," % (akeray.id, 
        akeray.title, akeray.price, item['quantity'], 
        akeray.subcity, akeray.phone, url)

        akeraysstring = akeraysstring + b

    context = {
        'gofor': gofor,
        'akeraysstring': akeraysstring
    }

    return render(request, 'gofor.html', context)