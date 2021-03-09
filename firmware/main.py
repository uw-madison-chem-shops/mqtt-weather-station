import settings

import sys
import machine
from machine import Pin, I2C, WDT
import network
import time
import struct

import mqtt_as
mqtt_as.MQTT_base.DEBUG = True


from bme680 import *

from homie.constants import FALSE, TRUE, BOOLEAN, FLOAT, STRING
from homie.device import HomieDevice
from homie.node import HomieNode
from homie.property import HomieNodeProperty

from uasyncio import get_event_loop, sleep_ms

class BME680(HomieNode):

    def __init__(self, name="bme680", device=None):
        super().__init__(id="bme680", name=name, type="sensor")
        self.device = device
        self.i2c = I2C(scl=Pin(5), sda=Pin(4))
        self.bme680 = BME680_I2C(i2c=self.i2c)
        self.temperature = HomieNodeProperty(
            id="temperature",
            name="temperature",
            unit="°C",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.temperature)
        self.humidity = HomieNodeProperty(
            id="humidity",
            name="humidity",
            unit="%",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.humidity)
        self.pressure = HomieNodeProperty(
            id="pressure",
            name="pressure",
            unit="Pa",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.pressure)
        self.gas = HomieNodeProperty(
            id="voc",
            name="voc",
            unit="ohm",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.gas)
        self.uptime = HomieNodeProperty(
            id="uptime",
            name="uptime",
            settable=False,
            datatype=STRING,
            default="PT0S"
        )
        self.add_property(self.uptime)
        loop = get_event_loop()
        loop.create_task(self.update_data())
        self.led = Pin(0, Pin.OUT)
        self.online_led = Pin(12, Pin.OUT)
        self.online_led.off()
        self.last_online = time.time()
        self.start = time.time()

    async def update_data(self):
        # wait until connected
        for _ in range(60):
            await sleep_ms(1_000)
            if self.device.mqtt.isconnected():
                break
        # loop forever
        while True:
            while self.device.mqtt.isconnected():
                self.last_online = time.time()
                self.online_led.on()
                self.led.value(0)  # illuminate onboard LED
                self.temperature.data = str(self.bme680.temperature)
                self.humidity.data = str(self.bme680.humidity)
                self.pressure.data = str(self.bme680.pressure)
                self.gas.data = str(self.bme680.gas)
                self.uptime.data = self.get_uptime()
                self.led.value(1)  # onboard LED off
                await sleep_ms(15_000)
            while not self.device.mqtt.isconnected():
                if time.time() - self.last_online > 300:   # 5 minutes
                    machine.reset()
                self.online_led.off()
                self.led.value(0)  # illuminate onboard LED
                await sleep_ms(100)
                self.led.value(1)  # onboard LED off
                await sleep_ms(1000)
            machine.reset()  # if lost connection, restart

    def get_uptime(self):
        diff = int(time.time() - self.start)
        out = "PT"
        # hours
        if diff // 3600:
            out += str(diff // 3600) + "H"
            diff %= 3600
        # minutes
        if diff // 60:
            out += str(diff // 60) + "M"
            diff %= 60
        # seconds
        out += str(diff) + "S"
        return out

def main():
    # homie
    print("homie main")
    homie = HomieDevice(settings)
    homie.add_node(BME680(device=homie))
    homie.run_forever()

if __name__ == "__main__":
    main()
