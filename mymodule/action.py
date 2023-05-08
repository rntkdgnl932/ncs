import time

import requests
import json
# import os
import sys
sys.path.append('C:/nightcrow/mymodule')

import variable as v_

die_count = 0
item_count = 0

def dead_die(cla):
    try:
        global die_count
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_
        from massenger import line_to_me

        dead_ = False

        full_path = "c:\\nightcrow\\imgs\\dead_die\\dead_die.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            dead_ = True
            die_count += 1
            print("dead_die", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            if die_count > 4:
                line_to_me(cla, "나크 5번째 죽었다.")
                die_count = 0

                time.sleep(1)

                out_ = False
                while out_ is False:
                    out_ = out_check(cla)
                    if out_ == False:
                        print("dead_clean")
                        clean_screen(cla)
                        line_to_me(cla, "죽은것 같은데 원인 파악하러 빨리 구경와라!!")
                    else:
                        dead_die_before(cla)
                    time.sleep(0.5)



        return dead_
    except Exception as e:
        print(e)

# 죽음 죽어 전에
def dead_die_before(cla):
    try:
        global die_count
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_
        from massenger import line_to_me

        die_count = 0

        full_path = "c:\\nightcrow\\imgs\\dead_die\\dead_die_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 0, 710, 82, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_die_2", imgs_)




            if v_.force_sub_quest == False:

                # 골드 파악후 50만 미만이면 강제로 서브퀘스트 실행
                bag_open(cla)

                die_x = imgs_.x
                die_y = imgs_.y
                click_pos_reg(imgs_.x, imgs_.y, cla)
                dead_die_ = False
                while dead_die_ is False:
                    die_count += 1
                    if die_count > 5:
                        dead_die_ = True
                        die_count = 0
                    full_path = "c:\\nightcrow\\imgs\\dead_die\\exp_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\nightcrow\\imgs\\dead_die\\exp_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(55, 120, 120, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(170, 940, cla)

                            full_path = "c:\\nightcrow\\imgs\\dead_die\\not_enough_gold.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dead_die_ = True
                                v_.force_sub_quest = True
                            else:
                                full_path = "c:\\nightcrow\\imgs\\dead_die\\not_enough_gold2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    dead_die_ = True
                                    v_.force_sub_quest = True
                        else:
                            dead_die_ = True
                            die_count = 0
                            click_pos_2(30, 205, cla)
                    else:
                        full_path = "c:\\nightcrow\\imgs\\dead_die\\jangbi_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dead_die_ = True
                        else:
                            click_pos_reg(die_x, die_y, cla)
                    time.sleep(0.5)
                dead_die_ = False
                while dead_die_ is False:
                    die_count += 1
                    if die_count > 5:
                        dead_die_ = True
                        die_count = 0
                    full_path = "c:\\nightcrow\\imgs\\dead_die\\jangbi_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\nightcrow\\imgs\\dead_die\\jangbi_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(55, 120, 120, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(170, 940, cla)

                            full_path = "c:\\nightcrow\\imgs\\dead_die\\not_enough_gold.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dead_die_ = True
                                v_.force_sub_quest = True
                            else:
                                full_path = "c:\\nightcrow\\imgs\\dead_die\\not_enough_gold.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    dead_die_ = True
                                    v_.force_sub_quest = True


                        else:
                            click_pos_2(25, 100, cla)
                            dead_die_ = True
                    else:
                        click_pos_2(30, 250, cla)
                    time.sleep(0.5)

        full_path = "c:\\nightcrow\\imgs\\clean_screen\\exit_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 100, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # clean_screen(cla)
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)


def item_open(cla):
    try:
        global item_count
        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import bag_open, clean_screen, menu_open

        import os
        import numpy as np
        import cv2

        result_bag = bag_open(cla)
        if result_bag == True:

            click_pos_2(935, 265, cla)
            time.sleep(0.2)

            # 스킬북
            full_path = "c:\\nightcrow\\imgs\\item_1\\skillbook_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\nightcrow\\imgs\\item_1\\skillbook_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            # 탈것_1
            dir_path = "C:\\nightcrow"
            file_path = dir_path + "\\items\\item_open\\talgut.txt"
            ###
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='UTF8') as file:
                    box_ = file.read().splitlines()
                    print("box_", box_)
            ###
            print("탈것 시작")
            for i in range(len(box_)):
                full_path = "c:\\nightcrow\\imgs\\item_1\\" + box_[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("탈것 있", box_[i])
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    time.sleep(0.5)
                    full_path = "c:\\nightcrow\\imgs\\item_1\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("max.PNG")
                        time.sleep(0.2)
                        click_pos_2(585, 460, cla)
                        time.sleep(0.1)
                        click_pos_2(585, 460, cla)

                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)

                    tal_1 = False
                    tal_1_2 = False
                    while tal_1 is False:
                        item_count += 1
                        print("item_count", item_count)
                        if item_count > 20:
                            item_count = 0
                            tal_1 = True
                        full_path = "c:\\nightcrow\\imgs\\item_1\\exit_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            tal_last = False
                            while tal_last is False:
                                full_path = "c:\\nightcrow\\imgs\\item_1\\exit_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    tal_1 = True
                                    tal_1_2 = True
                                    tal_last = True
                        else:
                            full_path = "c:\\nightcrow\\imgs\\item_1\\y_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 700, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\nightcrow\\imgs\\item_1\\get_clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    if tal_1_2 == True:

                        tal_3 = False
                        while tal_3 is False:
                            full_path = "c:\\nightcrow\\imgs\\clean_screen\\talgut.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 40, 140, 75, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                talgut_ing_(cla)
                                tal_3 = True
                            else:
                                menu_open(cla)
                                time.sleep(0.1)
                                click_pos_2(795, 260, cla)
                                time.sleep(1)

                    bag_open(cla)
                    time.sleep(0.2)
                    click_pos_2(935, 265, cla)
                    time.sleep(0.2)
                else:
                    print("탈것 없 => ", box_[i])

            # 무기_2
            dir_path = "C:\\nightcrow"
            file_path = dir_path + "\\items\\item_open\\moogi.txt"
            ###
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='UTF8') as file:
                    box_ = file.read().splitlines()
                    print("box_", box_)
            ###
            print("무기 시작")
            for i in range(len(box_)):
                full_path = "c:\\nightcrow\\imgs\\item_1\\" + box_[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("무기 있", box_[i])
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    time.sleep(0.5)
                    full_path = "c:\\nightcrow\\imgs\\item_1\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("max.PNG")
                        time.sleep(0.2)
                        click_pos_2(585, 460, cla)
                        time.sleep(0.1)
                        click_pos_2(585, 460, cla)

                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)

                    tal_1 = False
                    tal_1_2 = False
                    while tal_1 is False:
                        item_count += 1
                        print("item_count3", item_count)
                        if item_count > 20:
                            item_count = 0
                            tal_1 = True
                        full_path = "c:\\nightcrow\\imgs\\item_1\\exit_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            tal_last = False
                            while tal_last is False:
                                full_path = "c:\\nightcrow\\imgs\\item_1\\exit_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    tal_1 = True
                                    tal_1_2 = True
                                    tal_last = True
                        else:
                            full_path = "c:\\nightcrow\\imgs\\item_1\\y_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 700, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\nightcrow\\imgs\\item_1\\get_clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    if tal_1_2 == True:
                        tal_3 = False
                        while tal_3 is False:
                            full_path = "c:\\nightcrow\\imgs\\clean_screen\\moogioutlook.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 40, 140, 75, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                talgut_ing_(cla)
                                tal_3 = True
                            else:
                                menu_open(cla)
                                click_pos_2(880, 260, cla)
                                time.sleep(1)

                    bag_open(cla)
                    time.sleep(0.2)
                    click_pos_2(935, 265, cla)
                    time.sleep(0.2)
                else:
                    print("무기_ 없 => ", box_[i])
            # 음식
            x_reg = 0
            y_reg = 0
            full_path = "c:\\nightcrow\\imgs\\item_1\\umsik_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("음식 있")
                tal_1 = False
                while tal_1 is False:
                    item_count += 1
                    print("item_count3", item_count)
                    if item_count > 20:
                        item_count = 0
                        tal_1 = True
                    full_path = "c:\\nightcrow\\imgs\\item_1\\umsik_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 400, 630, 550, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\nightcrow\\imgs\\item_1\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\nightcrow\\imgs\\item_1\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            tal_1 = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_2(935, 265, cla)
                    else:
                        full_path = "c:\\nightcrow\\imgs\\item_1\\umsik_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("음식 있")
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            if x_reg != 0:
                                click_pos_reg(x_reg, y_reg, cla)

                    time.sleep(0.3)
            else:
                print("음식 없")
            # 상자

            dir_path = "C:\\nightcrow"
            file_path = dir_path + "\\items\\item_open\\bag_item.txt"
            ###
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='UTF8') as file:
                    box_ = file.read().splitlines()
                    print("box_", box_)
            ###
            for i in range(len(box_)):
                x_reg = 0
                y_reg = 0
                full_path = "c:\\nightcrow\\imgs\\item_1\\" + box_[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("상자 있", box_[i])
                    tal_1 = False
                    while tal_1 is False:
                        item_count += 1
                        print("item_count3", item_count)
                        if item_count > 20:
                            item_count = 0
                            tal_1 = True

                        full_path = "c:\\nightcrow\\imgs\\item_1\\ganghwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("ganghwa.PNG 111111111111111111111111111111111111111111111111", box_[i])
                            tal_1 = True
                            bag_open(cla)
                            time.sleep(0.2)
                            click_pos_2(935, 265, cla)
                            time.sleep(0.2)

                        full_path = "c:\\nightcrow\\imgs\\item_1\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("max.PNG")
                            time.sleep(0.2)
                            click_pos_2(585, 460, cla)
                            time.sleep(0.1)
                            click_pos_2(585, 460, cla)

                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.3)
                            full_path = "c:\\nightcrow\\imgs\\item_1\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                tal_1 = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                click_pos_2(935, 265, cla)
                        else:
                            full_path = "c:\\nightcrow\\imgs\\item_1\\" + box_[i] + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("상자 있")
                                x_reg = imgs_.x
                                y_reg = imgs_.y
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                if x_reg != 0:
                                    click_pos_reg(x_reg, y_reg, cla)

                        time.sleep(0.3)
                        full_path = "c:\\nightcrow\\imgs\\item_1\\get_clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    print("상자 없")

            # 골드상자
            x_reg = 0
            y_reg = 0
            full_path = "c:\\nightcrow\\imgs\\item_1\\gold_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("골드 상자 있", imgs_)
                tal_1 = False
                while tal_1 is False:
                    item_count += 1
                    print("item_count3", item_count)
                    if item_count > 20:
                        item_count = 0
                        tal_1 = True
                    full_path = "c:\\nightcrow\\imgs\\item_1\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\nightcrow\\imgs\\item_1\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            tal_1 = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_2(935, 265, cla)

                        time.sleep(0.3)
                    else:
                        full_path = "c:\\nightcrow\\imgs\\item_1\\gold_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("골드 상자 있", imgs_)
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                        else:
                            full_path = "c:\\nightcrow\\imgs\\item_1\\gold_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("골드 상자 사용 있", imgs_)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                print("x_reg", x_reg)
                                if x_reg != 0:
                                    click_pos_reg(x_reg, y_reg, cla)

                    time.sleep(0.3)

            else:
                print("골드 상자 없")
        # 튜토육성 체크 후 클린스크린
        print("item_open_cleanscreen 1")
        clean_screen(cla)
        print("item_open clean end")
    except Exception as e:
        print(e)

def talgut_ing_(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        full_path = "c:\\nightcrow\\imgs\\get_item\\talgut_checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 130, 700, 170, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("talgut_checked", imgs_)
            click_pos_2(930, 60, cla)
        else:

            # 탈것
            go_1 = False
            go_2 = False
            full_path = "c:\\nightcrow\\imgs\\clean_screen\\talgut.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 40, 90, 75, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                go_1 = True

            full_path = "c:\\nightcrow\\imgs\\clean_screen\\glider.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 40, 130, 75, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                go_1 = True

            full_path = "c:\\nightcrow\\imgs\\clean_screen\\moogioutlook.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 40, 130, 75, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                go_2 = True



            if go_1 == True:
                print("talgut_ing___", imgs_)
                click_pos_2(740, 200, cla)
                time.sleep(0.3)
                click_pos_2(870, 1010, cla)
                time.sleep(0.3)
                click_pos_2(870, 1010, cla)
                time.sleep(0.3)
                click_pos_2(930, 60, cla)
            if go_2 == True:
                click_pos_2(660, 200, cla)
                time.sleep(0.3)
                click_pos_2(870, 1010, cla)
                time.sleep(0.3)
                click_pos_2(870, 1010, cla)
                time.sleep(0.3)
                click_pos_2(930, 60, cla)


    except Exception as e:
        print(e)




def bag_open(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, imgs_set_
        from massenger import line_to_me

        go_ = False

        full_path = "c:\\nightcrow\\imgs\\check\\bag_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            go_ = True
        else:
            while go_ is False:
                out_result = out_check(cla)
                if out_result == True:
                    click_pos_2(840, 60, cla)
                    go_ = True
                    time.sleep(0.5)

                else:
                    print("bag open clean_screen")
                    clean_screen(cla)
                time.sleep(0.2)

        if go_ == True:
            # 골드 파악 후 강제노역 시키기
            my_gold_bloon = False
            my_gold_count = 0
            while my_gold_bloon is False:
                my_gold_count += 1
                if my_gold_count > 3:
                    my_gold_bloon = True
                my_money = text_check_get(830, 880, 892, 900, cla)

                print("내 골드?", my_money)
                my_money = int_put_(my_money)
                money_bool = my_money.isdigit()
                if money_bool == True:
                    my_money = int(my_money)
                    if my_money > 0:
                        my_gold_bloon = True

                        onFG_ = int_put_(v_.onForceGold)
                        onFG = int(onFG_) * 10000
                        if my_money < onFG:
                            print("강제로 서브퀘스트 수행하기, 기준골드 : ", v_.onForceGold)
                            if v_.force_sub_quest != True:
                                v_.force_sub_quest = True
                                mg_ = str(my_money) + "골드 있다. 거지다. ㅠㅠ"
                                line_to_me(cla, mg_)
                        else:
                            print("기준골드보다 돈 많다 강제노역 해제하기, 기준골드 : ", v_.onForceGold)
                            v_.force_sub_quest = False
                time.sleep(1)

        return go_
    except Exception as e:
        print(e)

def menu_open(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, imgs_set_

        go_ = False

        while go_ is False:
            out_result = out_check(cla)
            if out_result == True:

                full_path = "c:\\nightcrow\\imgs\\check\\pvp_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("pvp_1", imgs_)
                else:
                    click_pos_2(930, 60, cla)
                go_ = True
                time.sleep(0.5)
            else:
                print("menu open clean_screen")
                clean_screen(cla)

        return go_
    except Exception as e:
        print(e)

def clean_screen(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2
        from schedule import myQuest_play_add

        print("<< clean_screen >>")

        out_ = False

        # 메인퀘스트 및 서브퀘스트일 경우 스케쥴 추가
        if v_.now_ing_schedule != "none":
            full_path = "c:\\nightcrow\\imgs\\dead_die\\dead_die.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("/////////////////////////////////////", v_.now_ing_schedule)

                if v_.force_sub_quest == True:
                    v_.force_sub_quest = False

                elif v_.now_ing_schedule == "메인퀘스트" or v_.now_ing_schedule == "서브퀘스트":
                    myQuest_play_add(cla, v_.now_ing_schedule)
                    v_.now_ing_schedule = "none"
                    time.sleep(2)
                # click_pos_reg(imgs_.x, imgs_.y, cla)
                dead_die(cla)
                time.sleep(3)
                full_path = "c:\\nightcrow\\imgs\\dead_die\\dead_die.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

        else:
            print("none?", v_.now_ing_schedule)




        # skip
        full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 45, 960, 130, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # skip
        full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\skip_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(580, 880, 680, 920, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skip_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\nightcrow\\imgs\\clean_screen\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)



        full_path = "c:\\nightcrow\\imgs\\clean_screen\\exit_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 0, 960, 120, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("exit_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\nightcrow\\imgs\\clean_screen\\exit_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 0, 960, 600, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("exit_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\nightcrow\\imgs\\clean_screen\\exit_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 0, 960, 600, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("exit_3", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\nightcrow\\imgs\\item_1\\exit_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\nightcrow\\imgs\\clean_screen\\setting_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 800, 960, 1030, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("setting_1", imgs_)
            click_pos_2(930, 60, cla)

        while out_ is False:

            full_path = "c:\\nightcrow\\imgs\\clean_screen\\setting_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 800, 960, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("setting_1", imgs_)
                click_pos_2(930, 60, cla)

            re_1 = go_auto_ing_(cla)
            re_2 = go_quest_ing_(cla)
            if re_1 == True or re_2 == True:
                out_ = True
                full_path = "c:\\nightcrow\\imgs\\check\\pvp_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("pvp_1", imgs_)
                    click_pos_2(930, 60, cla)
            else:

                # skip
                full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\skip_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 45, 960, 130, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("skip_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                # skip
                full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\skip_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(580, 880, 680, 920, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("skip_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\nightcrow\\imgs\\clean_screen\\confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\nightcrow\\imgs\\clean_screen\\setting_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 800, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("setting_1", imgs_)
                    click_pos_2(930, 60, cla)

                full_path = "c:\\nightcrow\\imgs\\clean_screen\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 0, 960, 120, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("exit_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\nightcrow\\imgs\\clean_screen\\exit_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 0, 960, 600, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("exit_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\nightcrow\\imgs\\clean_screen\\exit_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 0, 960, 600, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("exit_3", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\nightcrow\\imgs\\check\\bag_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\nightcrow\\imgs\\clean_screen\\exit_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(900, 70, 960, 200, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)


        return out_
    except Exception as e:
        print(e)

def out_check(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_

        out_ = False

        re_1 = go_auto_ing_(cla)
        re_2 = go_quest_ing_(cla)
        if re_1 == True or re_2 == True:
            out_ = True

        return out_
    except Exception as e:
        print(e)


def go_quest_ing_(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        go_ = False

        #퀘스트 진행중인지 여부
        full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\quest_ing_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 820, 945, 860, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("quest_ing_1", imgs_)
            go_ = True

        return go_

    except Exception as e:
        print(e)

def go_auto_ing_(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        go_ = False

        # 자동사냥 진행중인지 여부
        full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\auto_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 820, 945, 860, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("auto_1", imgs_)
            go_ = True
        full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\auto_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 820, 945, 860, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("auto_1", imgs_)
            go_ = True
        full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\auto_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 820, 945, 860, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("auto_1", imgs_)
            go_ = True

        return go_

    except Exception as e:
        print(e)

def skill_check_(cla):
    try:
        import numpy as np
        import cv2
        from function import imgs_set_, click_pos_reg, click_pos_2
        from action import menu_open
        # 기술서 적용 체크
        in_skill_all = False
        in_skill_all_count = 0
        in_skill_1 = False
        in_skill_2 = False
        while in_skill_all is False:
            in_skill_all_count += 1
            if in_skill_all_count > 10:
                in_skill_all = True
            full_path = "c:\\nightcrow\\imgs\\dungeon\\refresh_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 980, 130, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\nightcrow\\imgs\\dungeon\\in_skill_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(25, 115, 80, 180, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("스킬이 등록되어 있다", imgs_)
                    full_path = "c:\\nightcrow\\imgs\\dungeon\\skill_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 930, 50, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        in_skill_1 = True
                        print("반복사용 체크 완료")
                    else:
                        full_path = "c:\\nightcrow\\imgs\\dungeon\\skill_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 930, 50, 960, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("반복사용 체크 중")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    full_path = "c:\\nightcrow\\imgs\\dungeon\\skill_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 900, 140, 940, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        in_skill_2 = True
                        print("자동사용 켬 완료")
                    else:
                        full_path = "c:\\nightcrow\\imgs\\dungeon\\skill_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 900, 140, 940, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("자동사용 켜는 중")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    if in_skill_1 == True and in_skill_2 == True:
                        in_skill_last_count = 0
                        in_skill_last = False
                        while in_skill_last is False:
                            in_skill_last_count += 1
                            if in_skill_last_count > 10:
                                in_skill_last = True
                            full_path = "c:\\nightcrow\\imgs\\dungeon\\skill_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 900, 760, 960, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                in_skill_last2 = False
                                in_skill_last2_count = 0
                                while in_skill_last2 is False:
                                    in_skill_last2_count += 1
                                    if in_skill_last2_count > 10:
                                        in_skill_last2 = True
                                    full_path = "c:\\nightcrow\\imgs\\dungeon\\skill_7.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(900, 70, 960, 130, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        print("스킬 세팅 완료")
                                        in_skill_last = True
                                        in_skill_last2 = True
                                        v_.skill_checked_ = True
                                        in_skill_all = True
                                    time.sleep(0.2)
                            else:
                                full_path = "c:\\nightcrow\\imgs\\dungeon\\skill_6.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(700, 900, 760, 960, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    print("스킬이 등록 되지 않았다.")
                    y_gob = 40
                    for i in range(4):
                        click_pos_2(55, 155 + (y_gob * i), cla)
                        time.sleep(0.1)
                        click_pos_2(55, 155 + (y_gob * i), cla)
                        time.sleep(0.1)
                    y_gob = 60
                    for i in range(4):
                        click_pos_2(715, 160 + (y_gob * i), cla)
                        time.sleep(0.1)
                        click_pos_2(715, 160 + (y_gob * i), cla)
                        time.sleep(0.1)


            else:
                full_path = "c:\\nightcrow\\imgs\\dungeon\\skill_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 900, 760, 960, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open(cla)
                    click_pos_2(885, 60, cla)
            time.sleep(0.3)

    except Exception as e:
        print(e)