# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 18:09:42 2022

@author: muham
"""


def digital_to_binary(image_name):
    # Convert digital data to binary format
    with open(image_name, 'rb') as file:
        binary_data = file.read()
    return binary_data


def binary_to_digital(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
