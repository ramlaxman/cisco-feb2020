#!/usr/bin/env python3

rainfall = {}

while True:
    city_name = input("City: ").strip()
    if not city_name:
        break

    mm_rain = input("Rain: ").strip()
    if mm_rain.isdigit():
        mm_rain = int(mm_rain)
        rainfall[city_name] = rainfall.get(city_name, 0) + mm_rain

for key, value in rainfall.items():
    print(f'{key}: {value}')
