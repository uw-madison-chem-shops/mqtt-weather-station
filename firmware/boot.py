import esp
esp.osdebug(None)
#import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
from machine import RTC
gc.collect()
