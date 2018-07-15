#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = 'Jessie'

import re
import requests
from lxml import html
import xlwt

baseurl='https://www.watchguard.com/wgrd-products/appliances-compare'
file=r'.\result\result.csv'

def get_all_model():
    model_list = []
    print('requesting compare page...')
    page = requests.get(baseurl).text
    tree = html.etree.HTML(page)
    m_series = tree.xpath('//select[@id="p1"]/optgroup[contains(@label,"M Series")]/option')
    t_series = tree.xpath('//select[@id="p1"]/optgroup[contains(@label,"T Series")]/option')
    all_model = m_series + t_series
    model_list= [[mod.get('value'),mod.text] for mod in all_model]
    return model_list

def get_perf(model_list):
    for i in range(0, len(model_list), 3):
        appd_url = u'/%s/%s/%s' % (model_list[i][0],model_list[i+1][0],model_list[i+2][0])
        print('requesting compare detail page for %s...' % appd_url)
        page = requests.get(baseurl + appd_url).text
        tree = html.etree.HTML(page)
        for (model,index) in zip(model_list[i:i+3],range(2,5)):
            xpath1= '//div/table//tr/td[%d]' % index
            pf = tree.xpath(xpath1)
            model += [p.text for p in pf[8:14]]
    model_list=my_sort(model_list)
    model_list.insert(0, ['Code', 'Model', 'Firewall Throughput', 'VPN Throughput', 'AV Throughput',
                          'IPS Throughput', 'UTM Throughput', 'Concurrent Sessions*'])
    return model_list

def my_sort(m_list):
    pattern = r'([\d\.]+|[a-zA-Z]+)'
    print('sorted by Firewall Throughput ...')
    my_list = sorted(m_list, key=lambda l: float(re.findall(pattern, l[2])[0]))
    my_list = sorted(my_list, key=lambda l: re.findall(pattern, l[2])[1], reverse=True)
    return my_list

def write_csv(model_list):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('performance', cell_overwrite_ok=True)
    print('writing to %s...' % file)
    for i in range(len(model_list)):
        for j in range(len(model_list[i])-1):
            sheet.write(i, j, model_list[i][j+1])
    book.save(file)

def main():
    models=get_all_model()
    models_perf=get_perf(models)
    write_csv(models_perf)


if __name__=='__main__':
    main()