"""
Created on Wed Feb 23 18:48:48 2022

@author: muham
"""


def get_video_name(image_name, date):
    name = []
    video_name = ""
    image_name = image_name.split("-")
    for index in range(len(image_name)):
        if index == 0 or index == 2:
            name.append(image_name[index] + "-" + image_name[index + 1])
        elif index > 3:
            name.append(image_name[index])
    for index in range(len(name)):
        if index == 2:
            video_name += date.split(" ", 1)[0] + "\\"
        if index < 3:
            video_name += name[index] + "\\"
        elif index == 3:
            video_name += name[index] + ".mp4"
        # print(video_name)
    return video_name
