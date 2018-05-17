import socket
import ujson
import urequests

def getforecast(lat='49.53892899',lng='6.12860155'):
    #load information for location 
    url = 'http://api.wunderground.com/api/35bb891b4697284b/geolookup/forecast/q/{},{}.json'.format(lat,lng)
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
        country = forecast['location']['country_name']
        city = forecast['location']['city']
        #Just one day 
        day=forecast['forecast']['txt_forecast']['forecastday'][0]
        forecast = day['icon']
        return country,city,forecast
    except:
        return "unknown","unknown","unknown"

def getcurrentweather(lat='49.53892899',lng='6.12860155'):
    #load information for location 
    url = 'http://api.wunderground.com/api/35bb891b4697284b/geolookup/conditions/q/{},{}.json'.format(lat,lng)
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
    
    try: 
        country = info['location']['country_name']
        city = info['location']['city']
        weather = info['current_observation']['weather']
        return country,city,weather
    except:
        return "unknown","unknown","unknown"

        

