#!/usr/bin/python3.8
# -*- coding=utf-8 -*-


import random
first_code = random.randint(0, 255)
second_code = random.randint(0, 255)
third_code = random.randint(0, 255)
fourth_code = random.randint(0, 255)
random_ip = str(first_code) + '.' + str(second_code) + '.' + str(third_code) + '.' + str(fourth_code)
print(random_ip)
