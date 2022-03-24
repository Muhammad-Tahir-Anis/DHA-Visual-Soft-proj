def get_video_name(image_name, date):
    """
    This function takes two argument and generate path to video which is used on local computer where you are taking data
    :param image_name: it takes an absolute path to image
    :param date: it takes date on which image captured
    :return: it returns an absolute path of video
    """
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
