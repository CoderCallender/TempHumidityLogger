
import httplib
import urllib
import time
key = "EZ7IPRK3L3STGPRE"  # Put your API Key here
def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # $
        params = urllib.urlencode({'field1': temp, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept"$
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print temp
            print response.status, response.reason
            data = response.read()
            conn.close()
            time.sleep(30)
        except:
            print "connection failed"
        break
if __name__ == "__main__":
        while True:
                thermometer()
