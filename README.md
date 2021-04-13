# MQTT weather station

Simple station for monitoring environmental conditions in the lab over MQTT.

Based on the Bosch's [BME280 humidity, pressure, and temperature sensor](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/).
Using Adafruit's [breakout board](https://www.adafruit.com/product/2652).

Designed to work with [mqtt.chem.wisc.edu](https://mqtt.chem.wisc.edu/).

## Repository

This is an open source hardware project licensed under the CERN Open Hardware Licence Version 2 - Permissive.
Please see the LICENSE file for the complete license.

This repository is being mirrored to several version control systems in an attempt to ensure maximum avaliability.

| name           | url                                                           |
| -------------- | ------------------------------------------------------------- |
| Chem (primary) | https://git.chem.wisc.edu/shop/mqtt-weather-station           |
| GitHub         | https://github.com/uw-madison-chem-shops/mqtt-weather-station |
| GitLab         | https://gitlab.com/uw-madison-chem-shops/mqtt-weather-station |

## PCB

This PCB was designed using KiCAD version 5.
Refer to `weather.pdf` for schematic.
PCB images generated with [tracespace](https://github.com/tracespace/tracespace) follow.

<img src="./weather-.top.svg" width="100%"/>
<img src="./weather-.bottom.svg" width="100%"/>

## Bill of Materials

| reference      | value            | manufacturer     | part number          | price  | vendors |
| :------------- | :--------------- | :--------------- | :------------------- | :----- | :------ |
| A1             | ESP8266 breakout | Adafruit         | 2471                 | $10.00 | [Adafruit](https://www.adafruit.com/product/2471) [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/2471/5355489) |
| C1             | 100u             | Illinois Cap.    | 107KXM025M           | $0.25  | [DigiKey](https://www.digikey.com/en/products/detail/illinois-capacitor/107KXM025M/5410757?s=N4IgTCBcDaIIwAYDsBpAGgWQWArBkAugL5A) |
| C2             | 10u              | Yageo            | CC1206KKX7R8BB106    | $0.25  | [DigiKey](https://www.digikey.com/en/products/detail/yageo/CC1206KKX7R8BB106/5195365?s=N4IgTCBcDaIMJwIxgAwDYDSGAaB2ASgBwBCxi6IAugL5A) |
| C3             | 22u              | Yageo            | CC1206MKX7R7BB226    | $0.75  | [DigiKey](https://www.digikey.com/en/products/detail/yageo/CC1206MKX7R7BB226/7071713?s=N4IgTCBcDaIMJwIxgAwDYCyBpAGgdgCU8AhYsMNEAXQF8g) |
| D1, D2         | red LED          | Lite-ON          | LTST-C230KRKT        | $0.50  | [DigiKey](https://www.digikey.com/en/products/detail/lite-on-inc/LTST-C230KRKT/386857?s=N4IgTCBcDaIDIBUDKCC0BhMBmADAaQCU8EQBdAXyA) |
| Q1, Q2         | MOSFET N-ENH     | Diodes Inc.      | 2N7002K-7            | $0.25  | [DigiKey](https://www.digikey.com/en/products/detail/diodes-incorporated/2N7002K-7/1934378?lang=en&s=N4IgTCBcDa4HIHYAMSwGkC0CQF0C%2BQA&site=us&x=17&y=13) [Mouser](https://www.mouser.com/ProductDetail/Diodes-Incorporated/2N7002K-7?qs=rGAXPo9uwV0%2Fp9r5KJ7huA%3D%3D) |
| U1             | BME280 breakout  | Adafruit         | 2652                 | $20.00 | [Adafruit](https://www.adafruit.com/product/2652) [DigiKey]() |

All prices are extended.
Assuming an order of 10 PCBs, the boards themselves should cost around $5 each.

## Firmware

This project uses [micropython](https://micropython.org/), specifically [microhomie](https://github.com/microhomie/microhomie).
Refer to the "firmware" directory in this repository for detailed instructions.

## Changelog

### Unprinted

### B

#### Added
- new hour long reset timer based on CD4060BM96

#### Changed
- SOT23 packages for all discrete transistors

### A

#### Added
- initial design
