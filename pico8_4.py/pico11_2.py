import urequests as requests
from tools import connect,reconnect
from machine import WDT,Timer,ADC,RTC
import time


def alert(t:float):
    print('要爆炸了!')
    rtc = RTC()
    date_tuple = rtc.datetime()
    year = date_tuple[0]
    month = date_tuple[1]
    day = date_tuple[2]
    hour = date_tuple[4]
    minites = date_tuple[5]
    second = date_tuple[6]
    date_str = f'{year}-{month}-{day} {hour}:{minites}:{second}'
    get_url = f'https://hook.us1.make.com/自已的token?name=我家雞場&date={date_str}&temperature={t}'
    try:
        response = requests.get(get_url)
    except:
        reconnect()
    else:
        if response.status_code == 200:
            print("傳送成功")
        else:
            print("server有錯誤訊息")
            print(f'status_code:{response.status_code}')
        response.close()