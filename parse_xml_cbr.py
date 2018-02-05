import requests
from datetime import datetime
from lxml import etree
from pandas import DataFrame

COMMON_URL = 'http://www.cbr.ru/scripts/'
INDEX_DAYLY = 'XML_daily.asp?'
INDEX_DYNAMIC = 'XML_dynamic.asp?'
ID_CURRENCY_USD = 'VAL_NM_RQ=R01235'
ID_CURRENCY_EUR = 'VAL_NM_RQ=R01239'
INDEX_DATE = 'date_req='
INDEX_DATE1 = 'date_req1='
INDEX_DATE2 = 'date_req2='
DATE_NOW = datetime.now().strftime('%d/%m/%Y')
DATE_START = '01/01/2000'
DATE_RANGE = (INDEX_DATE1 + DATE_START) + '&' + (INDEX_DATE2 + DATE_NOW) + '&'
EUR = 'EUR'
USD = 'USD'


def get_xml_data(id_currency):
    url = COMMON_URL + INDEX_DYNAMIC + DATE_RANGE + id_currency
    xml_feed = requests.get(url)
    return xml_feed


def get_xml_content(xml_feed):
    xml_content = xml_feed.content
    list_rate = etree.fromstring(xml_content)
    return list_rate


def get_data(content, currency):
    list_data = []
    for element in content.xpath('//Record'):
        date = element.attrib['Date']
        rate = element.getchildren()[1].text
        rate_dict = {'rate': rate, 'date': date, 'currency': currency}
        list_data.append(rate_dict)
    return list_data


def output():
    list_currency = [{'currency': EUR, 'id_currency': ID_CURRENCY_EUR},
                     {'currency': USD, 'id_currency': ID_CURRENCY_USD}]
    for currency in list_currency:
        xml_feed = get_xml_data(currency['id_currency'])
        content = get_xml_content(xml_feed)
        list_data = get_data(content, currency['currency'])
        df = DataFrame(list_data, columns=['date', 'currency', 'rate'])
        df.to_csv('rate_{}.csv'.format(currency['currency']))


if __name__ == '__main__':
    output()
