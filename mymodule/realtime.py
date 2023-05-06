import time

import requests
import json
# import os
import sys
sys.path.append('C:/nightcrow/mymodule')

import variable as v_


def mystatus_check():
    try:
        from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2
        from action import menu_open, dead_die_before
        from get_item import get_items, get_upjuk
        from jadong_crow import jadong_play

        import numpy as np
        import pyautogui
        import cv2

        cla = "one"

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960



        dead_die_before(cla)

        get_upjuk(cla)


    except Exception as e:
        print(e)


def moogi_(cla):
    try:
        from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2, drag_pos
        from action import menu_open, dead_die_before
        from get_item import get_items, get_upjuk
        from jadong_crow import jadong_play

        import numpy as np
        import pyautogui
        import cv2

        moo_1 = False
        moo_count = 0
        while moo_1 is False:
            moo_count += 1
            if moo_count > 3:
                moo_1 = True
            full_path = "c:\\nightcrow\\imgs\\check\\moogi_sooglyun_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("moogi_title", imgs_)
                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 410, 250, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    moo_1 = True
                    print("point : moo_1", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)

                    moo_2 = False
                    while moo_2 is False:
                        moo_count += 1
                        if moo_count > 4:
                            moo_2 = True
                        full_path = "c:\\nightcrow\\imgs\\check\\moogi_sooglyun_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 330, 560, 380, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\nightcrow\\imgs\\check\\none_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(640, 700, 715, 735, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("none")

                                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(110, 400, 200, 690, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("point : moo_2", imgs_)
                                    click_pos_reg(imgs_.x + 100, imgs_.y + 20, cla)


                            else:
                                print("무언가 있다.")
                                full_path = "c:\\nightcrow\\imgs\\check\\moogi_sooglyun_4.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 590, 615, 625, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    moo_2 = True
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                full_path = "c:\\nightcrow\\imgs\\check\\moogi_sooglyun_3.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(750, 695, 850, 735, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)


                        else:
                            print("진행중")
                        time.sleep(0.3)
                    click_pos_2(930, 60, cla)
                    time.sleep(0.3)
                    click_pos_2(930, 60, cla)

                else:
                    drag_pos(130, 900, 130, 500, cla)
            else:
                menu_open(cla)

                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 110, 820, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("무기숙련 있다?", imgs_)
                    click_pos_2(790, 140, cla)
                else:
                    print("무기숙련 없다?")
                    moo_1 = True
                    click_pos_2(930, 60, cla)
            time.sleep(0.5)
        full_path = "c:\\nightcrow\\imgs\\check\\moogi_sooglyun_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(930, 60, cla)
    except Exception as e:
        print(e)

def soojib(cla):
    try:
        from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2, drag_pos
        from action import menu_open, dead_die_before
        from get_item import get_items, get_upjuk
        from jadong_crow import jadong_play

        import numpy as np
        import pyautogui
        import cv2

        collection_ = False

        col_1 = False
        while col_1 is False:
            full_path = "c:\\nightcrow\\imgs\\check\\collection_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("collection_1", imgs_)

                full_path = "c:\\nightcrow\\imgs\\check\\confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_1 : collection", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 70, 480, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point : col_1", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(0.3)
                    full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(220, 130, 620, 990, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point : collection", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                        time.sleep(0.5)
                        click_pos_2(830, 950, cla)
                        time.sleep(0.5)
                    full_path = "c:\\nightcrow\\imgs\\check\\confirm_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm_1 : collection", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)


                else:
                    col_2 = False
                    while col_2 is False:
                        full_path = "c:\\nightcrow\\imgs\\check\\collection_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("collection_1", imgs_)
                            click_pos_2(930, 60, cla)
                        else:
                            col_1 = True
                            col_2 = True
            else:
                menu_open(cla)
                click_pos_2(930, 140, cla)
            time.sleep(0.5)

        if collection_ == True:
            col_1 = False
            while col_1 is False:
                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(220, 130, 620, 990, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point : collection", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                    time.sleep(0.5)
                    click_pos_2(830, 950, cla)
                    full_path = "c:\\nightcrow\\imgs\\check\\confirm_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm_1 : collection", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)
