from machine import Pin
from utime import sleep_ms
from umqtt.simple import MQTTClient
import network

led = Pin(23,Pin.OUT)

wifi_ssid = "Wokwi-GUEST"
wifi_pwd = ""

MQTT_BROKER = "mqtt.netpie.io"  
MQTT_CLIENT = "xxx" # Client ID
MQTT_USER = "xxx" # Token
MQTT_PWD = "xxx" # Secret

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wifi_ssid, wifi_pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def sub_callback(topic, msg):
    print((topic, msg))
    if topic == b'@msg/led':
        if msg == b'ledon':
            led.on()
        elif msg == b'ledoff':
            led.off()

def init_client():
    global client
    print("Trying to connect to MQTT Broker.")
    try:
        client = MQTTClient(MQTT_CLIENT, MQTT_BROKER, port=1883, user=MQTT_USER,password=MQTT_PWD)
        client.connect()
        print("Connected to ",MQTT_BROKER)
        topic_sub = b"@msg/led"
        client.set_callback(sub_callback)
        client.subscribe(topic_sub)
    except:
        print("Trouble to init mqtt.") 

wifi_connect()  # connect to WiFi network
init_client()

while True:
    client.check_msg()
    sleep_ms(500)

