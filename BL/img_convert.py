def digital_to_binary(image_name):
    """
    This function takes absolute image path and convert that image to BLOB which is binary form of image supported by
    database we used.
    :param image_name: takes absolute path of image
    :return: it returns the BLOB image
    """
    # Convert digital data to binary format
    with open(image_name, 'rb') as file:
        binary_data = file.read()
    return binary_data


def binary_to_digital(data, filename):
    """
    This function takes BLOB image and covert it into simple formate like PNG or JPGE.
    :param data: take blob image
    :param filename: takes absolute image file name where you want to store image.
    """
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
