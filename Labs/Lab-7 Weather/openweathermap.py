import socket
import ujson
import urequests

def getforecast(CityID='2960316', APIKey='126c5aa86fcedeb3bb3876202a8afc7c'):
    #load information for location 
    url = 'https://api.openweathermap.org/data/2.5/forecast/?id={}&appid={}&units=metric&cnt=3'.format(CityID, APIKey)
    #print(url)
    try: 
        #ask for forecast
        response = urequests.get(url)
        #extract the json , and convert it to a dict in one go
        forecast = response.json()
    except:
        print('Could not retrieve the weather forecast')
        #todo error handling
    finally:
        response.close() 

    try: 
        country = forecast['city']['country']
        city = forecast['city']['name']
        weather = forecast['list'][0]['weather'][0]['main']
        return country, city, weather
    except:
        return "unknown","unknown","unknown"

def getcurrentweather(CityID='2960316', APIKey='126c5aa86fcedeb3bb3876202a8afc7c'):
    #load information for location 
    url = 'https://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric'.format(CityID, APIKey)
    try: 
        #ask for forecast
        response = urequests.get(url)
        #extract the json , and convert it to a dict in one go
        info = response.json()
    except:
        print('Could not retrieve the weather forecast')
        #todo error handling
    finally:
        response.close() 
    
    country,city,weather,temp = "unknown","unknown","unknown",-999
    try: 
        country = info['sys']['country']
        city = info['name']
        temp = float(info['main']['temp'])
        weather = info['weather'][0]['main']
    except:
        pass
    return country,city,weather,temp
