# flash micropython
read -p "bring GPIO0 low, reset device, and press enter"
esptool.py --port /dev/ttyUSB0 erase_flash
read -p "bring GPIO0 low, reset device, and press enter"
esptool.py -p /dev/ttyUSB0 --baud 450800 --chip esp8266 write_flash 0x00000 microhomie-esp8266-v3.0.2.bin
read -p "reset device and press enter"
# upload files
echo "sleeping"
sleep 5
echo "putting files on device"
ampy -p /dev/ttyUSB0 put main.py
python -m mpy_cross settings.py
ampy -p /dev/ttyUSB0 put settings.mpy
python -m mpy_cross bme680.py
ampy -p /dev/ttyUSB0 put bme680.mpy
read -p "reset device and press enter"
echo "done!"
