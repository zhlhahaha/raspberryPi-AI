import paho.mqtt.client as mqtt
def public_info():
    print("start get....")
    client = mqtt.Client()
    #broker = args.broker
    client.connect("10.169.182.19")
    client.publish('handRecon', "OFF")

if __name__ == '__main__':
    public_info()

