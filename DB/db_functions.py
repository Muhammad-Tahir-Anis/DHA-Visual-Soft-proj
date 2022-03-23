from datetime import datetime, timedelta

from BL.vehicle import Vehicle
from BL.img_convert import digital_to_binary
from db_connector import connect_db

db = connect_db()

conn = db[0]
cursor = db[1]

vehicle_data = Vehicle


# insertData is a function which is used to insert data from application to database.
def insert_data(vehicle):
    vehicle.image = digital_to_binary(vehicle.image)
    data = [vehicle.dha_location, vehicle.dha_phase, vehicle.gate_location, vehicle.camera_direction, vehicle.date_time,
            vehicle.vehicle_class,
            vehicle.image, vehicle.video_path]
    statement = """INSERT INTO dha_table (dha_location, dha_phase, gate_location, camera_direction, date_time,
                vehicle_class, image, video_path) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
    try:
        print('execute')
        cursor.execute(statement, data)
        conn.commit()
        print("data inserted")
    except:
        conn.rollback()


# "showData" is a function which is used to get data from database and show on console
def show_data():
    # To store data from database we will use "data-list" in which objects of Class "vehicleData" stored in.
    data_list: list = []
    # sql query for retrieving specified data from database
    statement = "select gate_location, camera_direction, date_time, vehicle_class  from dha_table;"
    # exception handling in case of any exception while retrieving data from database
    try:
        cursor.execute(statement)
        db_data = cursor.fetchall()
    except:
        print("except")
    # for loop is used here to create objects from data of rows from database
    # 1 object is representing one row.
    # and all objects stored in "data-list"
    for index in db_data:
        vehicle = Vehicle(index[0], index[1], index[2], index[3])
        data_list.append(vehicle)
    return data_list


def count_exit():
    statement = 'select count(*) from dha_table where camera_direction = "Exit";'
    try:
        cursor.execute(statement)
        exit_data = cursor.fetchall()
        print(exit_data)
    except:
        print("except")
    return exit_data[0][0]


def count_entry():
    statement = 'select count(*) from dha_table where camera_direction = "Entry";'
    try:
        cursor.execute(statement)
        entry_data = cursor.fetchall()
        print(entry_data)
    except:
        print("except")
    return entry_data[0][0]


def data_of_day_by_hours_exit(start_date, phase=None):
    exit_hours_data = []
    if phase is None:
        for hour in range(0, 24):
            statement = f'select count(*) from dha_table where camera_direction = "exit" and ' \
                        f'date_time between "{start_date} {str(hour)}:00:00" and "{start_date} {str(hour + 1)}:00:00"'
            try:
                cursor.execute(statement)
                hours_data = cursor.fetchall()
                exit_hours_data.append(hours_data[0][0])
            except:
                print("except")
    else:
        for hour in range(0, 24):
            statement = f'select count(*) from dha_table where camera_direction = "exit" and dha_phase = "{phase}" and ' \
                        f'date_time between "{start_date} {str(hour)}:00:00" and "{start_date} {str(hour + 1)}:00:00"'
            try:
                cursor.execute(statement)
                hours_data = cursor.fetchall()
                exit_hours_data.append(hours_data[0][0])
            except:
                print("except")
    return exit_hours_data


def data_of_day_by_hours_entry(start_date, phase=None):
    entry_hours_data = []
    if phase is None or phase == "" or phase == "None":
        for hour in range(0, 24):
            statement = f'select count(*) from dha_table where camera_direction = "entry" and ' \
                        f'date_time between "{start_date} {str(hour)}:00:00" and "{start_date} {str(hour + 1)}:00:00"'
            try:
                cursor.execute(statement)
                hours_data = cursor.fetchall()
                entry_hours_data.append(hours_data[0][0])
            except:
                print("except")
    else:
        for hour in range(0, 24):
            statement = f'select count(*) from dha_table where camera_direction = "entry" and dha_phase = "{phase}" and ' \
                        f'date_time between "{start_date} {str(hour)}:00:00" and "{start_date} {str(hour + 1)}:00:00"'
            try:
                cursor.execute(statement)
                hours_data = cursor.fetchall()
                entry_hours_data.append(hours_data[0][0])
            except:
                print("except")
    return entry_hours_data


def data_of_week_by_days_entry(start_date, phase=None):
    start_date = datetime.strptime(str(start_date), "%Y-%m-%d")
    entry_days_data = []
    if phase is None or phase == "" or phase == "None":
        for days in range(0, 7):
            statement = f'select count(*) from dha_table where camera_direction = "entry" and ' \
                        f'date_time between "{start_date + timedelta(days=days)}" and "{start_date + timedelta(days=days + 1)}"'
            try:
                cursor.execute(statement)
                hours_data = cursor.fetchall()
                entry_days_data.append(hours_data[0][0])
            except:
                print("except")
    else:
        for days in range(0, 7):
            statement = f'select count(*) from dha_table where camera_direction = "entry" and dha_phase = "{phase}" and ' \
                        f'date_time between "{start_date + timedelta(days=days)}" and "{start_date + timedelta(days=days + 1)}"'
            try:
                cursor.execute(statement)
                hours_data = cursor.fetchall()
                entry_days_data.append(hours_data[0][0])
            except:
                print("except")
    return entry_days_data


def data_of_week_by_days_exit(start_date, phase=None):
    start_date = datetime.strptime(str(start_date), "%Y-%m-%d")
    exit_days_data = []
    if phase is None or phase == "" or phase == "None":
        for days in range(0, 7):
            statement = f'select count(*) from dha_table where camera_direction = "exit" and ' \
                        f'date_time between "{start_date + timedelta(days=days)}" and "{start_date + timedelta(days=days + 1)}"'
            try:
                cursor.execute(statement)
                days_data = cursor.fetchall()
                exit_days_data.append(days_data[0][0])
            except:
                print("except")
    else:
        for days in range(0, 7):
            statement = statement = f'select count(*) from dha_table where camera_direction = "exit" and dha_phase = "{phase}" and ' \
                                    f'date_time between "{start_date + timedelta(days=days)}" and "{start_date + timedelta(days=days + 1)}"'
            try:
                cursor.execute(statement)
                days_data = cursor.fetchall()
                exit_days_data.append(days_data[0][0])
            except:
                print("except")
    return exit_days_data


def data_of_week_by_hours_entry(start_date, phase=None):
    start_date = datetime.strptime(str(start_date), "%Y-%m-%d").date()
    entry_days_data = []
    date_time_stamps = []
    day: int = 0
    hour: int = 0
    if phase is None:
        for day in range(0, 7):
            for hour in range(0, 24):
                statement = f'select count(*) from dha_table where camera_direction = "entry" and ' \
                            f'date_time between "{start_date + timedelta(days=day)} {str(hour)}:00:00" and ' \
                            f'"{start_date + timedelta(days=day)} {str(hour + 1)}:00:00"'
                try:
                    cursor.execute(statement)
                    hours_data = cursor.fetchall()
                    entry_days_data.append(hours_data[0][0])
                    date_time_stamps.append(f"{start_date + timedelta(days=day)} {str(hour)}:00:00")
                except:
                    print("except")
    else:
        for day in range(0, 7):
            for hour in range(0, 24):
                statement = f'select count(*) from dha_table where camera_direction = "entry" and dha_phase = "{phase}" and ' \
                            f'date_time between "{start_date + timedelta(days=day)} {str(hour)}:00:00" and ' \
                            f'"{start_date + timedelta(days=day)} {str(hour + 1)}:00:00"'
                try:
                    cursor.execute(statement)
                    hours_data = cursor.fetchall()
                    entry_days_data.append(hours_data[0][0])
                    date_time_stamps.append(f"{start_date + timedelta(days=day)} {str(hour)}:00:00")
                except:
                    print("except")
    return entry_days_data, date_time_stamps


def data_of_week_by_hours_exit(start_date, phase=None):
    start_date = datetime.strptime(str(start_date), "%Y-%m-%d").date()
    exit_days_data = []
    day: int = 0
    hour: int = 0
    if phase is None:
        for day in range(0, 7):
            for hour in range(0, 24):
                statement = f'select count(*) from dha_table where camera_direction = "exit" and ' \
                            f'date_time between "{start_date + timedelta(days=day)} {str(hour)}:00:00" and ' \
                            f'"{start_date + timedelta(days=day)} {str(hour + 1)}:00:00"'
                try:
                    cursor.execute(statement)
                    hours_data = cursor.fetchall()
                    # print(hours_data)
                    # print(start_date + timedelta(days=day))
                    exit_days_data.append(hours_data[0][0])
                except:
                    print("except")
    else:
        for day in range(0, 7):
            for hour in range(0, 24):
                statement = f'select count(*) from dha_table where camera_direction = "exit" and dha_phase = "{phase}" and ' \
                            f'date_time between "{start_date + timedelta(days=day)} {str(hour)}:00:00" and ' \
                            f'"{start_date + timedelta(days=day)} {str(hour + 1)}:00:00"'
                try:
                    cursor.execute(statement)
                    hours_data = cursor.fetchall()
                    # print(hours_data)
                    # print(start_date + timedelta(days=day))
                    exit_days_data.append(hours_data[0][0])
                except:
                    print("except")
    return exit_days_data

# print(data_of_week_by_hours_exit('2022-1-15'))
# print(data_of_week_by_hours_entry('2022-1-15'))
