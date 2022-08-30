from django.conf import settings

from landlord.views import akeray_detail
from landlord.models import Akeray

class Gofor(object):
    def __init__(self, request):
        self.session = request.session
        gofor = self.session.get(settings.GOFOR_SESSION_ID)

        if not gofor:
            gofor = self.session[settings.GOFOR_SESSION_ID] = {}

        self.gofor = gofor 

    def __iter__(self):
        akeray_ids = self.gofor.keys()        
        akeray_clean_ids = []

        for p in akeray_ids:
            akeray_clean_ids.append(p)

            self.gofor[str(p)]['akeray'] = Akeray.objects.get(pk=p)

        for item in self.gofor.values():
            item['quantity'] =  item['quantity']

            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.gofor.values())

    def add(self, akeray, quantity=1, update_quantity=False):
        akeray_id = str(akeray.id)
        price = akeray.price 

        if akeray_id not in self.gofor:
            self.gofor[akeray_id] = {'quantity':0, 'price': price, 'id': akeray_id}

        if update_quantity:
            self.gofor[akeray_id]['quantity'] = quantity

        else:
           self.gofor[akeray_id]['quantity'] = self.gofor[akeray_id]['quantity'] + 1

        self.save()
    
    def remove(self, akeray_id):
        if akeray_id in self.gofor:
            del self.gofor[akeray_id]
            self.save()

    def save(self):
        self.session[settings.GOFOR_SESSION_ID] = self.gofor 
        self.session.modefied = True

        