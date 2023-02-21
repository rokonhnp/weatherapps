from django.shortcuts import render

import requests
from bs4 import BeautifulSoup as bs


def get_weather_data(city):
    city = city.replace(' ','+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.9"
    COOKIE = 'HSID=ALZs_MP2T5ZYQYwSU; SSID=AIq4opvOQr3b2-hd1; APISID=c5M1r0yPoPzxC69Z/A9M_qbnzdYX65vRKb; SAPISID=z0IMad28sDXKeOt7/Au3RqGF0K3zlBD-Wy; __Secure-1PAPISID=z0IMad28sDXKeOt7/Au3RqGF0K3zlBD-Wy; __Secure-3PAPISID=z0IMad28sDXKeOt7/Au3RqGF0K3zlBD-Wy; SID=TwgioSUt85uY57fHXV3Ooo8lESju-HVznET1WKq-yGfeYA5Vfyh3RNipQRBxkrC0T_6reg.; __Secure-1PSID=TwgioSUt85uY57fHXV3Ooo8lESju-HVznET1WKq-yGfeYA5VHBanNEofyCLBzqM9HMuN1g.; __Secure-3PSID=TwgioSUt85uY57fHXV3Ooo8lESju-HVznET1WKq-yGfeYA5VtFV1UDnPRnF9jxfBJsMctA.; OTZ=6899736_32_32__32_; SEARCH_SAMESITE=CgQIzZcB; AEC=ARSKqsIS_cp7kU3NMnx5UzvyJv2-KMYyv5gbF1HTZjfjuntC2p4ECr1uh48; 1P_JAR=2023-02-21-06; NID=511=oVvlfLs43AmtjgORD_7_k4tfmKgt7Bt3vrEZf78AiddUEPrjzFQT8MMTXRofFbRSywK70FBIttYZmm8EIcoCyX2lLMsI0ckvJ7yrYbU2Yl4uR0WqxeYy6O8ZiLw-8quhTdjcGpGexGxtRWXStV7ExAr0IrtFukRpo5QW19EwtkAgWLJjV1cwaT0C_sjuRV5JqzX2oYTjfcDUINiTHGpR8kwCrabZnY9R2YmwgD8ZXGiUtVFoX5sw95uEVpgBouAoWqlts-Xx9bdwQ3JyvSODpIvE06psLvC5uVhMQYIukAfOueDSvDyzcyMLU72k_YxnKRdKfVF46Sw; DV=47P7XKv-VYBf4NvUndzzyhmtt4UrZ1iVc7QAoi46LgIAAIBHfY3ypUEulAAAAPCSFA-qpoSSKgAAAKaqsXzyEc3TEAAAAA; SIDCC=AFvIBn-_zJCgHkPzAyK_eqivBkqqE6qn1j1hE-G6tei3jDfKujOWrAKRIhHFbKMq5WOhpIMCWqvB; __Secure-1PSIDCC=AFvIBn-SoKqk52xCC8MY_96ix3TxaSQtnB5nfPsa1N7yLcgpm1VrJFuW6rBBRH_hXDSXdtt2WnHf; __Secure-3PSIDCC=AFvIBn9b1-bl0tz980AE_lbvORecB9E7N8VO_CLTUqfLKQtUkFyMDzjfCK9aBI3n50CTbTfTb8oz'

    session = requests.Session()
    session.headers['user-agent'] = USER_AGENT
    session.headers['accept-language'] = LANGUAGE
    session.headers['cookie'] = COOKIE
    response = session.get(url)
    soup = bs(response.text, 'html.parser')
    # Extract Region
    results = {}
    results['region'] = soup.find('span','BBwThe').text
    results['day_time'] = soup.find('div', attrs={'id':'wob_dts'}).text
    results['weather'] = soup.find('span', attrs={'id':'wob_dc'}).text
    results['temp'] = soup.find('span', attrs={'id':'wob_tm'}).text
    
    return results

# Create your views here.

def home_view(request):
    if request.method == "GET" and 'city' in request.GET:
        city = request.GET.get('city')
        results = get_weather_data(city)
        context = {'results':results}

    else:
        context={}
    return render(request, 'home.html', context)
