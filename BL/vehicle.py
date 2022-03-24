class Vehicle:
    def __init__(self, gate_location, camera_direction, date_time, vehicle_class):
        """
        This function automatically calls when the object created
        :param gate_location: gate number of DHA
        :param camera_direction: Camera Direction (Entry / Exit)
        :param date_time: datetime string
        :param vehicle_class: it takes type of vehicle
        """
        self.dha_phase = None
        self.dha_location = None
        self.video_path = None
        self.image = None
        self.gate_location = gate_location
        self.camera_direction = camera_direction
        self.date_time = date_time
        self.vehicle_class = vehicle_class

    def for_db_insertion(self, dha_location, dha_phase, gate_location, camera_direction, date_time, vehicle_class, image, video_path):
        """
        This function is used for making object of vehicle to insert into database.
        all the data bellow is generated by function -> "get_my_files()" in "file_name_splitter.py"
        :param dha_location: it is like DHAI
        :param dha_phase: the phase number. like phase-1
        :param gate_location: like gate-1
        :param camera_direction: like (Entry / Exit)
        :param date_time: like (yyyy-mm-dd HH:MM:SS)
        :param vehicle_class: like (bike / car / truck)
        :param image: absolute path to image
        :param video_path: absolute path of video generated by function -> "get_video_name()" in "video_name.py"
        """
        self.dha_location = dha_location
        self.dha_phase = dha_phase
        self.gate_location = gate_location
        self.camera_direction = camera_direction
        self.date_time = date_time
        self.vehicle_class = vehicle_class
        self.image = image
        self.video_path = video_path
        # insertData(gate_location, camera_direction, date_time, vehicle_class,image, video_path)
