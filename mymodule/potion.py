import time

import requests
import json
# import os
import sys
sys.path.append('C:/nightcrow/mymodule')

import variable as v_


def potion_check(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, imgs_set_, click_pos_2, in_number_check, change_number
        from action import dead_die_before, bag_open
        from realtime import soojib

        if cla == "one":
            potion = v_.mypotion_1
        else:
            potion = v_.mypotion_2

        full_path = "c:\\nightcrow\\imgs\\potion\\out_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 950, 760, 1030, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("화면에 물약 존재한다", imgs_)


            potion_ready = text_check_get(730, 1004, 759, 1016, cla)
            print("전체4자리 potion_?", potion_ready)
            result_num_in = in_number_check(cla, potion_ready)
            if result_num_in == True:
                potion = change_number(potion_ready)
                potion_bloon = potion.isdigit()
                if potion_bloon == True:
                    potion = int(potion)
                    print("potion?", potion)
                    if cla == "one":
                        v_.mypotion_1 = potion
                    else:
                        v_.mypotion_2 = potion

                    if potion < 10:
                        v_.potion_count += 1
                        if v_.potion_count > 3:
                            v_.potion_count = 0
                            maul_potion(cla)
                    else:
                        v_.potion_count = 0
                else:
                    print("potion => 숫자 아님")
            else:
                potion_ready = text_check_get(733, 1004, 758, 1016, cla)
                print("전체4자리 potion_2?", potion_ready)
                result_num_in = in_number_check(cla, potion_ready)
                if result_num_in == True:
                    potion = change_number(potion_ready)
                    potion_bloon = potion.isdigit()
                    if potion_bloon == True:
                        potion = int(potion)
                        print("potion?", potion)
                        if cla == "one":
                            v_.mypotion_1 = potion
                        else:
                            v_.mypotion_2 = potion

                        if potion < 10:
                            v_.potion_count += 1
                            if v_.potion_count > 5:
                                v_.potion_count = 0
                                maul_potion(cla)
                        else:
                            v_.potion_count = 0
                    else:
                        print("potion => 숫자 아님")
                else:
                    potion_ready = text_check_get(730, 1004, 752, 1016, cla)
                    print("앞3자리 potion_?", potion_ready)
                    result_num_in = in_number_check(cla, potion_ready)
                    if result_num_in == True:
                        potion = change_number(potion_ready)
                        potion_bloon = potion.isdigit()
                        if potion_bloon == True:
                            potion = int(potion)
                            print("potion?", potion)
                            if cla == "one":
                                v_.mypotion_1 = potion
                            else:
                                v_.mypotion_2 = potion

                            if potion < 10:
                                v_.potion_count += 1
                                if v_.potion_count > 3:
                                    v_.potion_count = 0
                                    maul_potion(cla)
                            else:
                                v_.potion_count = 0
                        else:
                            print("potion => 숫자 아님")
                    else:
                        potion_ready = text_check_get(738, 1004, 759, 1016, cla)
                        print("뒷3자리 potion_??", potion_ready)
                        result_num_in = in_number_check(cla, potion_ready)
                        if result_num_in == True:
                            potion = change_number(potion_ready)
                            potion_bloon = potion.isdigit()
                            if potion_bloon == True:
                                potion = int(potion)
                                print("potion?", potion)
                                if cla == "one":
                                    v_.mypotion_1 = potion
                                else:
                                    v_.mypotion_2 = potion

                                if potion < 100:
                                    v_.potion_count += 1
                                    if v_.potion_count > 3:
                                        v_.potion_count = 0
                                        maul_potion(cla)
                                else:
                                    v_.potion_count = 0

                            else:
                                print("potion => 숫자 아님")
            # if potion_ is None:
            #     v_.potion_count += 1
            #     if v_.potion_count > 20:
            #         v_.potion_count = 0
            #         maul_potion(cla)
        else:
            full_path = "c:\\nightcrow\\imgs\\potion\\out_potion_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 950, 760, 1030, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("화면에 물약 존재한다", imgs_)
            else:
                full_path = "c:\\nightcrow\\imgs\\potion\\out_potion_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 950, 760, 1030, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("화면에 물약 존재한다", imgs_)
                else:
                    print("화면에 물약 존재하지 않는다", v_.potion_count)
                    v_.potion_count += 1
                    print("not have potoin?", v_.potion_count)
                    if v_.potion_count > 2:
                        v_.potion_count = 0

                        bag_open(cla)
                        time.sleep(0.2)

                        # 물약 찾기
                        potion_have = False
                        for i in range(10):
                            click_pos_2(935, 265, cla)
                            time.sleep(0.1)
                            full_path = "c:\\nightcrow\\imgs\\potion\\potion_in_bag.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(670, 110, 900, 900, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                potion_have = True
                                print("가방에 물약 존재한다", imgs_)
                                break
                            time.sleep(0.1)
                        if potion_have == False:
                            maul_potion(cla)
        dead_die_before(cla)



        return potion
    except Exception as e:
        print(e)


def maul_potion(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, imgs_set_, click_pos_reg, in_number_check
        from action import out_check, clean_screen, bag_open, maul_check, dead_die_before
        from realtime import soojib, moogi_, jaelyo_, boonhae_
        from schedule import myQuest_play_add
        from get_item import get_items

        get_items(cla)
        soojib(cla)
        moogi_(cla)
        boonhae_(cla)


        jab_ready = False
        jab_ready_count = 0
        while jab_ready is False:
            jab_ready_count += 1
            if jab_ready_count > 3:
                jab_ready = True
            full_path = "c:\\nightcrow\\imgs\\check\\maul_move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("maul_move_1", imgs_)
                jab_ready = True
                full_path = "c:\\nightcrow\\imgs\\potion\\janhwa_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("janhwa_1", imgs_)
                else:
                    result_maul = maul_check(cla)
                    if result_maul == True:
                        click_pos_2(230, 90, cla)
                    else:
                        full_path = "c:\\nightcrow\\imgs\\check\\maul_move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                bag_open(cla)
                time.sleep(1)
                full_path = "c:\\nightcrow\\imgs\\check\\maul_move_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 100, 920, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(710, 935, cla)
                    time.sleep(0.5)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(290, 1000, cla)
                    time.sleep(0.5)
                    clean_screen(cla)

                time.sleep(1)
                click_pos_2(290, 1000, cla)


        time.sleep(2)
        jab_1_count = 0
        jab_1 = False
        while jab_1 is False:
            time.sleep(1)
            full_path = "c:\\nightcrow\\imgs\\potion\\janhwa_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("janhwa_1^_^", imgs_)
                jab_1 = True
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:

                full_path = "c:\\nightcrow\\imgs\\potion\\dunjun_out_.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 510, 560, 560, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(555, 610, cla)
                    time.sleep(2)
                    click_pos_2(295, 1000, cla)
                    time.sleep(2)
                else:
                    jab_1_count += 1
                    clean_screen(cla)

                    if jab_1_count > 5:
                        jab_1_count = 0
                        full_path = "c:\\nightcrow\\imgs\\check\\maul_move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("maul_move__1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        # click_pos_2(230, 90, cla)
            time.sleep(1)

        jab_2 = False
        while jab_2 is False:
            full_path = "c:\\nightcrow\\imgs\\potion\\janhwa_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 900, 175, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("janhwa_2", imgs_)
                jab_1_count = 0
                time.sleep(0.2)
                # lv. 45 부터 사용 가능한 물약
                # full_path = "c:\\nightcrow\\imgs\\potion\\middle_potion.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.83)
                # if imgs_ is not None and imgs_ != False:
                #     print("middle_potion", imgs_)
                #     jab_2 = True
                #     click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                # else:
                full_path = "c:\\nightcrow\\imgs\\potion\\small_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("small_potion", imgs_)
                    jab_2 = True
                    click_pos_reg(imgs_.x + 70, imgs_.y, cla)
            else:
                jab_1_count += 1
                time.sleep(2)
                if jab_1_count > 5:
                    jab_1_count = 0
                    full_path = "c:\\nightcrow\\imgs\\potion\\janhwa_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("janhwa_11", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
        jab_3 = False
        while jab_3 is False:
            full_path = "c:\\nightcrow\\imgs\\potion\\potion_buy.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("potion_buy", imgs_)
                click_pos_2(560, 550, cla)
                jab_3 = True
                time.sleep(0.5)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)
                click_pos_2(410, 745, cla)
                time.sleep(1.2)
            else:
                jab_1_count += 1

                time.sleep(1)
                if jab_1_count > 5:
                    jab_1_count = 0
                    full_path = "c:\\nightcrow\\imgs\\potion\\small_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("small_potion", imgs_)
                        jab_3 = True
                        click_pos_reg(imgs_.x + 70, imgs_.y, cla)


        # 랜덤이동서
        full_path = "c:\\nightcrow\\imgs\\potion\\random_move.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("already_in___1", imgs_)

            if cla == "one":
                move_ = text_check_get(imgs_.x - 10, imgs_.y + 10, imgs_.x + 30, imgs_.y + 30, cla)
            if cla == "two":
                move_ = text_check_get(imgs_.x - 10 - 960, imgs_.y + 10, imgs_.x + 30 - 960, imgs_.y + 30, cla)
            print("how many 1?", move_)

            move_bool = in_number_check(cla, move_)
            if move_bool == True:
                print("int_put_(move_) 1?", int(int_put_(move_)))
                random_move = int(int_put_(move_))
                if random_move < 100:
                    jab_3 = False
                    click_count = 0
                    while jab_3 is False:
                        full_path = "c:\\nightcrow\\imgs\\potion\\potion_buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_buy", imgs_)
                            click_pos_2(450, 620, cla)
                            jab_3 = True
                            time.sleep(0.5)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_2(410, 745, cla)
                            time.sleep(1.2)
                        else:
                            full_path = "c:\\nightcrow\\imgs\\potion\\soongan.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_count += 1
                                if click_count > 4:
                                    print("돈 없다. 강제노역이다~!")
                                    v_.force_sub_quest = True
                                    jab_3 = True
                                print("soongan????", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                jab_3 = False
                click_count = 0
                while jab_3 is False:
                    full_path = "c:\\nightcrow\\imgs\\potion\\potion_buy.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_buy", imgs_)
                        click_pos_2(510, 580, cla)
                        jab_3 = True
                        time.sleep(0.5)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_2(410, 745, cla)
                        time.sleep(1.2)
                    else:
                        full_path = "c:\\nightcrow\\imgs\\potion\\soongan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            click_count += 1
                            if click_count > 4:
                                print("돈 없다. 강제노역이다~!")
                                v_.force_sub_quest = True
                                jab_3 = True
                            print("soongan????", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)


        # 마을이동서
        full_path = "c:\\nightcrow\\imgs\\potion\\maul_move_.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("already_in___2", imgs_)

            if cla == "one":
                move_ = text_check_get(imgs_.x - 10, imgs_.y + 10, imgs_.x + 30, imgs_.y + 30, cla)
            if cla == "two":
                move_ = text_check_get(imgs_.x - 10 - 960, imgs_.y + 10, imgs_.x + 30 - 960, imgs_.y + 30, cla)
            print("how many 2?", move_)
            move_bool = in_number_check(cla, move_)
            if move_bool == True:
                print("int_put_(move_) 2?", int(int_put_(move_)))
                maul_move_ = int(int_put_(move_))
                if maul_move_ < 100:
                    jab_3 = False
                    click_count = 0
                    while jab_3 is False:
                        full_path = "c:\\nightcrow\\imgs\\potion\\potion_buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_buy", imgs_)
                            click_pos_2(450, 620, cla)
                            jab_3 = True
                            time.sleep(0.5)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_2(410, 745, cla)
                            time.sleep(1.2)
                        else:
                            full_path = "c:\\nightcrow\\imgs\\potion\\gujum.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_count += 1
                                if click_count > 4:
                                    print("돈 없다. 강제노역이당 흑흑")
                                    v_.force_sub_quest = True
                                    jab_3 = True
                                print("soongan", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                jab_3 = False
                click_count = 0
                while jab_3 is False:
                    full_path = "c:\\nightcrow\\imgs\\potion\\potion_buy.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_buy", imgs_)
                        click_pos_2(510, 580, cla)
                        jab_3 = True
                        time.sleep(0.5)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_2(410, 745, cla)
                        time.sleep(1.2)
                    else:
                        full_path = "c:\\nightcrow\\imgs\\potion\\gujum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            click_count += 1
                            if click_count > 4:
                                print("돈 없다. 강제노역이당 흑흑")
                                v_.force_sub_quest = True
                                jab_3 = True
                            print("soongan", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)


        jab_3 = False
        print("potion_jab_3")
        while jab_3 is False:
            out_result = out_check(cla)
            if out_result == True:
                full_path = "c:\\nightcrow\\imgs\\check\\pvp_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 60, cla)
                jab_3 = True
            else:
                clean_screen(cla)

        jaelyo_(cla)
        dead_die_before(cla)

    except Exception as e:
        print(e)

