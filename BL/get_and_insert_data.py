from file_name_splitter import get_my_files
from vehicle import Vehicle
from video_name import get_video_name
from DB.db_functions import insert_data


# This function will get folder name where your images' data are located
# and data will send into database.
# This function also have code for progressbar running into main GUI window

def folder_to_database_data_insertion(folder_path: str, progress_bar):
    """
    This function will get folder name where your images' data are located and data will send into database.
    This function also have code for progressbar running into main GUI window
    :param folder_path: path to folder where data located
    :param progress_bar: type ttk.Progressbar
    """
    files = get_my_files(folder_path)
    #
    file = files[0]
    images = files[1]

    vehicle_data = Vehicle

    # progress bar code
    value = 100 / len(file)

    for data, image in zip(file, images):
        vehicle_data.for_db_insertion(vehicle_data, str(data[0]), str(data[1]), str(data[2]), str(data[3]),
                                      str(data[4]), str(data[6]), image, get_video_name(image, data[5]))
        insert_data(vehicle_data)

        # progress bar code
        progress_bar['value'] += value
        progress_bar.update()
        print(value)
