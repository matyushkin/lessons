import requests
from bs4 import BeautifulSoup

def get_html(url):
    """Забирает html для конкретного url"""
    response = requests.get(url)
    return response.text

def get_all_event_divs(page_html):
    """Забирает блоки, содержащие мероприятия"""
    soup = BeautifulSoup(page_html, 'lxml')
    event_blocks = soup.find_all('div', class_='event-list-item')
    return event_blocks

def get_event_info(block):
    """Забирает информацию из блоков, содержащих мероприятия"""
    soup = BeautifulSoup(str(block), 'lxml')
    event_type = soup.find('div', class_='event-list-item__type')
    return event_type

# url = 'https://it-events.com/'
# blocks = get_all_event_divs(get_html(url))
# for block in blocks:
#     print(get_event_info(block))

def result(n):
    print(2/3*2**n - 1/6*(-1)**n - 1/2)

result(6)

# html = """<div class="event-list-item">
# <div class="row">
# <div class="col-2">
# <a class="event-list-item__image" href="/events/11251" style="background-image: url(/system/events/logos/000/011/251/original/%D1%82%D0%B0%D1%80%D0%B3%D0%B5%D1%82-%D0%B2-%D1%81%D0%BE%D1%86.-%D1%81%D0%B5%D1%82%D1%8F%D1%85.jpg?1571141846)"></a>
# </div>
# <div class="col-10">
# <div class="event-list-item__type">
# Курс / Платное
# </div>
# <a class="event-list-item__title" href="/events/11251">
# Таргетированная реклама в социальных сетях
# </a>
# <div class="event-list-item__info">
#  3 февраля 2020 - 21 марта 2020
# </div>
# <div class="event-list-item__info event-list-item__info_location">
# Москва, Россия
# </div>
# </div>
# </div>
# </div>"""

# soup = BeautifulSoup(html, 'lxml')
# event_type = soup.find('div', class_='event-list-item__type')

# print(event_type)