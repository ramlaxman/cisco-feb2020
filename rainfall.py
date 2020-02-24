#!/usr/bin/env python3

rainfall = {}

while True:
    city_name = input("City: ").strip()
    if not city_name:
        break

    mm_rain = input("Rain: ").strip()

    rainfall[city_name] = rainfall.get(city_name, 0) + mm_rain
