import os


def get_my_files(dir_location):
    # setting working directory to the directory where my files are located
    os.chdir(dir_location)
    images = os.listdir()

    # creating a dynamic list in which i'll store all my file name
    # in special format to read actual data of my file.
    image_names = []

    # Loop to trivialise all my files and split name of each file by "-"
    # and create list for each file name. At the end we have 2D list/array in which
    # one list for all file names and other list for each file name.
    for names in images:
        image_names.append(names.split("-"))

    # Create List to save existing lists data after converting data to information
    new_image_name = []
    new_image_names = []

    # Adding third and forth to single index and other indexes of list remains same
    # and save them to new lists.
    # image_name -> new_image_names
    # image_names -> new_image_names
    for image_name in image_names:
        for index in range(0, len(image_name)):
            if index == 2:
                new_image_name.append(image_name[index] + image_name[index + 1])
            elif index > 3 or index < 2:
                new_image_name.append(image_name[index])
        new_image_names.append(new_image_name)
        new_image_name = []

    # Delete previous Lists to save memory and space
    image_name.clear()
    image_names.clear()

    # To get datetime stamp in actual format we will edit datetime stamp
    # which is embedded in file name.
    # 20220205000001 -> 2022-02-05 00:00:01
    for image_names in new_image_names:
        for image_name in image_names:
            if image_names.index(image_name) == 5:
                edit_index = 4
                for index in range(0, 20):
                    if index == edit_index and edit_index < 10:
                        image_name = image_name[:index] + "-" + image_name[index:]
                        edit_index += 3
                    elif index == edit_index and edit_index == 10:
                        image_name = image_name[:index] + " " + image_name[index:]
                        edit_index += 3
                    elif index == edit_index and 10 < edit_index < 19:
                        image_name = image_name[:index] + ":" + image_name[index:]
                        edit_index += 3
                    image_names[4] = image_name
                # print(image_name)
    for image_names in new_image_names:
        for image_name in image_names:
            if image_names.index(image_name) == 5:
                image_name = image_name.replace(".png", "")
                image_names[5] = image_name
    # print(new_image_names)
    return new_image_names, images
