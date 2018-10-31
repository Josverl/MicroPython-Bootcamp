import _thread, network, ujson, ubinascii, machine
#from m5stack import lcd, buttonA, buttonC, m5button
import utime as time

wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)
#lcd.setColor(0xCCCCCC, 0)
#lcd.rect(0, 210, 320, 30, #lcd.BLACK, #lcd.BLACK)
message = 'reconnect'
#lcd.text(62 - int(#lcd.textWidth(message) / 2), 235 - #lcd.fontSize()[1], message)
message = 'set wifi'
#lcd.text(253 - int(#lcd.textWidth(message) / 2), 235 - #lcd.fontSize()[1], message)


def do_connect(ntwrk_ssid, netwrk_pass):
	#lcd.setCursor(0, 0)
	#lcd.rect(0, 0, 320, 200, #lcd.BLACK, #lcd.BLACK)
	if not wlan_sta.isconnected():
		wlan_sta.active(True)
		print('Connect WiFi: SSID:'+ntwrk_ssid+' PASSWD:'+netwrk_pass+' network...')
		#lcd.println('Connect WiFi: \r\nWiFi SSID:'+ntwrk_ssid)
		wlan_sta.connect(ntwrk_ssid, netwrk_pass)
		#lcd.print('Connecting.')
		a=0
		while not wlan_sta.isconnected() | (a > 20) :
			time.sleep_ms(500)
			a+=1
			print('.', end='')
			#lcd.print('.',wrap=1)
		if wlan_sta.isconnected():
			print('\nConnected. Network config:', wlan_sta.ifconfig())
			#lcd.println("Connected! \r\nNetwork config:\r\n"+wlan_sta.ifconfig()[0]+', '+wlan_sta.ifconfig()[3])
			return (True)
		else : 
			#lcd.println('.',wrap=1)
			print('\nProblem. Not Connected to :'+ntwrk_ssid)
			#lcd.println('Problem. Not Connected to :'+ntwrk_ssid)
			return (False)
	return (True)


def auto_connect():
	try:
		if not wlan_sta.isconnected():
			with open("modeconfig.json") as f:
				jdata = ujson.loads(f.read())
				ssid = jdata['wifi']['ssid']
				passwd = jdata['wifi']['password']
				if ssid == '' and passwd == '':
					raise OSError
			if do_connect(ssid, passwd):
				return (True)
			print('connect fail!')

			if not wlan_sta.isconnected():
				import wificonfig
				wificonfig.webserver_start()
		else:
			return (True)
	except OSError:
		# Web server for connection manager
		import wificonfig
		wificonfig.webserver_start()


def isconnected():
	return wlan_sta.isconnected()
