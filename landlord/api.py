import json
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from gofor.gofor import Gofor
from landlord.models import Akeray


def api_add_new_rent(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    title = data['title']
    location = data['location']
    subcity = data['subcity']
    kebele = data['kebele']
    price = data['price']
    summary = data['summary']
    phone = data['phone']

    a = Akeray.objects.create(title = title, location = location, subcity = subcity, kebele = kebele, price = price, summary = summary, phone = phone)

    return JsonResponse(jsonresponse)

def api_add_to_gofor(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    akeray_id = data['akeray_id']
    update = data['update']
    quantity = data['quantity']

    gofor = Gofor(request)

    akeray = get_object_or_404(Akeray, pk=akeray_id)

    if not update:
        gofor.add(akeray=akeray, quantity=1, update_quantity=False)
    else:
        gofor.add(akeray=akeray, quantity=quantity, update_quantity=True)
    
    return JsonResponse(jsonresponse)

def api_remove_from_gofor(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    akeray_id = data['akeray_id']

    gofor = Gofor(request)

    gofor.remove(akeray_id)

    return JsonResponse(jsonresponse)