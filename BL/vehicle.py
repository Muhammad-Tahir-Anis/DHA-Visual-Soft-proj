# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:34:23 2022

@author: muham
"""


class Vehicle:
    def __init__(self, gate_location, camera_direction, date_time, vehicle_class):
        self.dha_phase = None
        self.dha_location = None
        self.video_path = None
        self.image = None
        self.gate_location = gate_location
        self.camera_direction = camera_direction
        self.date_time = date_time
        self.vehicle_class = vehicle_class

    def for_db_insertion(self, dha_location, dha_phase, gate_location, camera_direction, date_time, vehicle_class, image, video_path):
        self.dha_location = dha_location
        self.dha_phase = dha_phase
        self.gate_location = gate_location
        self.camera_direction = camera_direction
        self.date_time = date_time
        self.vehicle_class = vehicle_class
        self.image = image
        self.video_path = video_path
        # insertData(gate_location, camera_direction, date_time, vehicle_class,image, video_path)
