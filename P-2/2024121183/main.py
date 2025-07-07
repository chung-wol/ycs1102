import time
import dht
from machine import Pin

file = open('./input.txt', 'r', encoding='EUC-KR')

for line in file:
  period = line.strip().split(' ')
  period = [int(i) for i in period]

period_index = 0
humidity_data = []
temperature_data = []
last_measure_time = time.ticks_ms()
print_flag = False

period_button = Pin(13, Pin.IN, Pin.PULL_UP)
print_button = Pin(18, Pin.IN, Pin.PULL_UP)
sensor = dht.DHT22(Pin(28))
led = Pin(0, Pin.OUT)

def period_button_callback(channel):
  global period_index
  period_index += 1

period_button.irq(period_button_callback, Pin.IRQ_FALLING)

def print_button_callback(channel):
  global print_flag
  print_flag = True

print_button.irq(print_button_callback, Pin.IRQ_FALLING)

while True:
  current_time = time.ticks_ms()
  time_diff = time.ticks_diff(current_time, last_measure_time)
  
  if time_diff >= period[period_index % 3] * 1000:
    led.value(1)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temperature_data.append(temp)
    humidity_data.append(hum)
    last_measure_time = current_time
  
  if time_diff >= period[period_index % 3] * 1000 / 2:
    led.value(0)

  if print_flag:
    print(f"측정 횟수: {len(temperature_data)}")
    print(f"온도 평균/최대: {(sum(temperature_data[-10:]) / len(temperature_data[-10:])):.2f}/{max(temperature_data[-10:]):.2f}")
    print(f"습도 평균/최대: {(sum(humidity_data[-10:]) / len(humidity_data[-10:])):.2f}/{max(humidity_data[-10:]):.2f}")
    print_flag = False
  time.sleep_ms(10)