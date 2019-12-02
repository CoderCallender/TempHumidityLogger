import thingspeak
import time
import Adafruit_DHT
import logging
 
channel_id = 884199 # PUT CHANNEL ID HERE
write_key  = '11B4V75M25DQ5U8E' # PUT YOUR WRITE KEY HERE
read_key   = 'UQ0V7GGGINAJKBB6' # PUT YOUR READ KEY HERE
pin = 4
sensor = Adafruit_DHT.DHT22
 
def measure(channel):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        format(humidity, '.2f')
        format(temperature, '.2f')
       # print ('temp = 
        # write
        response = channel.update({'field1': temperature, 'field2': humidity})
        
        # read
        read = channel.get({})
        #print("Read:", read)
        logging.info("Update Success!")
        
    except:
        #print("connection failed")
        logging.error('connection failed')
 
 
if __name__ == "__main__":
    #channel = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
    #logging.basicConfig(format='%(asctime)s - %(message)s')
    logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s')
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(600) #update every 10 mins