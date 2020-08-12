import os
import cv2


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
                
def add_image_to_dir(image,dir):
    img_location = os.path.join(os.getcwd(),'resources/')
    direct_location = os.path.join(img_location,dir)
    next = get_next_photo_number(direct_location)
    new_file_location = os.path.join(direct_location,f'{dir}{next}.png')
    cv2.imwrite(new_file_location, image)

def reset_labels(label_ids, conf_counter):
    for key in label_ids:
        # conf_counter[key] = delay_value * (picture_list.count(key)-1) + 1
        conf_counter[key] = 1
    conf_counter[-1] = 1 # -1 stands for unknown person
    # print(label_ids, picture_list, conf_counter)