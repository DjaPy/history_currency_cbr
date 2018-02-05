import requests
from datetime import datetime
from lxml import etree
from pandas import DataFrame

COMMON_URL = 'http://www.cbr.ru/scripts/'
INDEX_DAYLY = 'XML_daily.asp?'
INDEX_DYNAMIC = 'XML_dynamic.asp?'
ID_CURRENCY_USD = 'VAL_NM_RQ=R01235'
INDEX_DATE = 'date_req='
INDEX_DATE1 = 'date_req1='
INDEX_DATE2 = 'date_req2='
DATE_NOW = datetime.now().strftime('%d/%m/%Y')
DATE_START = '01/01/2000'
DATE_RANGE = (INDEX_DATE1 + DATE_START) + '&' + (INDEX_DATE2 + DATE_NOW) + '&' + ID_CURRENCY_USD


def get_courses_list():
    url = COMMON_URL + INDEX_DYNAMIC + DATE_RANGE
    xml_feed = requests.get(url)
    xml_content = xml_feed.content
    list_rate = etree.fromstring(xml_content)
    element_list = []

    for attr in list_rate.xpath('//Record[@Date]'):
        element_list.append(attrib

    # for element in list_rate.xpath('//Record'):
    #     # date = element.Date
    #     rate = element.getchildren()[1].text
    #     rate_dict = {'rate': rate}
    #                  # 'date': date}
    #     element_list.append(rate_dict)

    return element_list


if __name__ == '__main__':
    print(get_courses_list())
