import os
import json
import cv2
from facerecognitionpy.files import *


def get_next_photo_number(dir):
    number_list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            base = os.path.basename(path)
            number_list.append(int(os.path.splitext(base)[0][-1]))
    if not number_list:
        return 0
    else:
        return max(number_list) + 1


def add_image_to_dir(image, dir):
    img_location = get_full_path('resources')
    direct_location = os.path.join(img_location, dir)
    next = get_next_photo_number(direct_location)
    new_file_location = os.path.join(direct_location, f'{dir}{next}.png')
    cv2.imwrite(new_file_location, image)


def reset_labels(label_ids, conf_counter):
    for key in label_ids:
        # conf_counter[key] = delay_value * (picture_list.count(key)-1) + 1
        conf_counter[key] = 1
    conf_counter[-1] = 1  # -1 stands for unknown person
    # print(label_ids, picture_list, conf_counter)


def idOfName(name, label_ids):
    for key, value in label_ids.items():
        if(value == name):
            return key
    return None


def change_conf():
    conf_min, conf_max = input(
        "New Minimum Conf: "), input("New Maximum Conf: ")
    old_delay = None
    with open("config.json", "r") as f:
        data = json.load(f)
        old_delay = data.get("delay")
    with open("config.json", "w") as f:
        new_dict = {}
        new_dict["conf_min"] = conf_min
        new_dict["conf_max"] = conf_max
        new_dict["delay"] = old_delay
        json.dump(new_dict, f)


def change_delay():
    new_delay = input("New delay: ")
    old_conf_min = None
    old_conf_max = None
    with open("config.json", "r") as f:
        data = json.load(f)
        old_conf_min = data.get("conf_min")
        old_conf_max = data.get("conf_max")
    with open("config.json", "w") as f:
        new_dict = {}
        new_dict["conf_min"] = old_conf_min
        new_dict["conf_max"] = old_conf_max
        new_dict["delay"] = new_delay
        json.dump(new_dict, f)


def read_values():
    with open("config.json", "r") as f:
        data = json.load(f)
        return int(data.get("conf_min")), int(data.get("conf_max")), int(data.get("delay"))
