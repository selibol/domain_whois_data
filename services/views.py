# -*- coding: utf-8 -*-
from django.http import JsonResponse
from whois import tld_regexpr, whois
from whois._2_parse import get_tld_re
from services.models import WhoIsData, WhoIsDataHeader


def index(request):
    domains_txt = open('static/domain.txt', 'r')
    domains = domains_txt.read().splitlines()
    res_list = []
    for domain in domains:
        tld_regexpr.tr = {
            'extend': 'com'
        }
        get_tld_re('tr')
        res = whois(domain)
        domain_name = res['domain_name']
        created = res['creation_date']
        expire_date = res['expiration_date']
        if domain.endswith('tr'):
            registrant_name = res['registrant_name'].split('\n')[0]
        else:
            registrant_name = res['registrar']

        data = WhoIsData.objects.create(domain_name=domain_name, registrant_name=registrant_name, create_date=created, expire_date=expire_date)
        data_header = WhoIsDataHeader.objects.create(name=domain_name)
        data_header.whois_data.add(data)
        res_list.append(res)

    return JsonResponse({'data': res_list})





