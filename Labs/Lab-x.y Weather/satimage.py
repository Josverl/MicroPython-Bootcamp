"""
    retrieve the satelite weather forcast map for a location 
    convert that from png to jpg 
    display this on the M5 display in a window

    uses : 
        - weather underground API 
            - free API Key, needs registration 
        - filestack 
            - initial free plan (500 conversions) 
"""
import urequests, uos as os, gc

def urlencode(string =""):
    '''
    poor mans urlencode
    :   Separate protocol (http) from address       %3B     Y
    /   Separate domain and directories             %2F     Y
    #   Separate anchors                            %23     Y
    ?   Separate query string                       %3F     Y
    &   Separate query elements                     %24     No
    @   Separate username and password from domain  %40     Y
    %   Indicates an encoded character              %25     No
    +   Indicates a space                           %2B     Y
    <space> Not recommended in URLs            %20 or +     Y
    '''
    url = string.replace(':','%3A').replace('/','%2F')#.replace('#','%23').replace('?','%3F').replace('+','%2B').replace(' ','+').replace('@','%40')
    #.replace('&','%24').replace('%','%25')
    return url

def write(text):
    "Log text to REPL and to Display"
    print(text)
    tft.text(tft.LASTX ,tft.LASTY,'{}\r\n'.format(text),tft.RED) 
#=========================================
city='Pijnacker'
header('Satellite {}'.format(city))
mainwindow()

tft.text(0,0,"Retrieving map from\n\r") 
tft.text(tft.LASTX ,tft.LASTY,"Weather Underground\n\r") 

wunderground_APIKey='0c1c0d57eee9edf0'
satURL = 'http://api.wunderground.com/api/{}/satellite/q/KS/{}.png?width={}&height={}&basemap=1'.format(
                wunderground_APIKey,city,318,238)


PNGurl = urlencode(satURL)

Filestack_APIKey='AheOzuybQgupZOWlRIZ3Gz'
transform='output=format:jpg/resize=width:{}'.format(318)
#fixme : urequests does not like the url in HTTPS, so we are leaking the API Key 
jpgurl = "http://process.filestackapi.com/{}/{}/{}".format( Filestack_APIKey, transform, PNGurl)

filename = '/flash/satview.jpg'

try: 
    #ask for a PNG transformed to JPG 
    response = urequests.get(jpgurl)
    #todo: get errors out if there is no network connection 
    gc.collect()
    if response.status_code == 200: 
        #write that to a file 
        with open(filename,'wb') as file:
            _= file.write(response.content)
            file.close() 
    else: 
        write(b'HTTP Response {} {}'.format(response.status_code, response.reason) )
        
except OSError as exc:
    if exc.args[0] == 28:
        write('IO Error') #OSError: 28
    else:
        write('OS Error {}'.format(exc.args[0]) ) 
except MemoryError: 
    write('Ran out of memory')
except:
    write('Could not retrieve the map')
finally:
    response.close() 

tft.image(0, 0, filename )

try: 
    #remove the file to get some space back
    os.remove(filename)
except:
    pass

"""
    - Possible alternative : 
        https://cloudconvert.com/pricing - Free 
        https://api.cloudconvert.com/convert?apikey=oFI8RR73C8W7krLDgCOK0JG7tgS7u9kwiziDYhe20YfY0u1ZfIEjXNwh4bPGiqO6&inputformat=png&outputformat=jpg&input=download&file=http%3A%2F%2Fapi.wunderground.com%2Fapi%2F0c1c0d57eee9edf0%2Fsatellite%2Fq%2FKS%2Fpijnacker.png%3Fwidth%3D318%26height%3D238%26basemap%3D1&wait=true&download=true                
        #Testing
        jpgurl = 'http://api.cloudconvert.com/convert?apikey=oFI8RR73C8W7krLDgCOK0JG7tgS7u9kwiziDYhe20YfY0u1ZfIEjXNwh4bPGiqO6&inputformat=png&outputformat=jpg&input=download&file=http%3A%2F%2Fapi.wunderground.com%2Fapi%2F0c1c0d57eee9edf0%2Fsatellite%2Fq%2FKS%2Fpijnacker.png%3Fwidth%3D318%26height%3D238%26basemap%3D1&wait=true&download=true'
        >> urequests.py - NotImplementedError: Redirects not yet supported

"""