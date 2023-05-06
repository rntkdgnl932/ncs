import time

import requests
import json
# import os
import sys
sys.path.append('C:/nightcrow/mymodule')

import variable as v_

def dungeon_play(cla, result_schedule_):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, imgs_set_, click_pos_2, click_pos_reg
        from action import menu_open, clean_screen

        print("dungeon")

        complete_ = False

        dungeon_ = result_schedule_.split("_")

        print("던전 시작")

        if dungeon_[1] == "번영":
            dungeon_name = "bunyuong_1"
        elif dungeon_[1] == "수련":
            dungeon_name = "soolyun_1"
        elif dungeon_[1] == "신전":
            dungeon_name = "sinjun_1"
        elif dungeon_[1] == "유적":
            dungeon_name = "youjuk_1"
        elif dungeon_[1] == "동굴":
            dungeon_name = "dongool_1"

        dungeon_clear = False

        in_dungeon__ = False

        in_dungeon__count = 0
        while in_dungeon__ is False:
            in_dungeon__count += 1
            if in_dungeon__count > 3:
                in_dungeon__count = 0

            print("던전체크")
            time.sleep(1)

            full_path = "c:\\nightcrow\\imgs\\dungeon\\" + dungeon_name + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 75, 150, 110, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print(dungeon_[1], imgs_)

                in_dungeon__ = True

                now_playing(cla, dungeon_[1])
            else:

                # 던전 진입하기
                in_dungeon_title = False
                while in_dungeon_title is False:
                    full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 40, 100, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        in_dungeon_title = True

                        if dungeon_[1] == "번영":
                            full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_clear.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 160, 120, 200, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dungeon_clear = True

                            if dungeon_clear == False:
                                click_pos_2(80, 110, cla)
                                time.sleep(0.2)
                                click_pos_2(200, 200, cla)
                        elif dungeon_[1] == "수련":
                            full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_clear.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 260, 120, 300, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dungeon_clear = True

                            if dungeon_clear == False:
                                click_pos_2(80, 110, cla)
                                time.sleep(0.2)
                                click_pos_2(200, 300, cla)
                        elif dungeon_[1] == "신전":
                            full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_clear.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 360, 120, 400, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dungeon_clear = True

                            if dungeon_clear == False:
                                click_pos_2(80, 110, cla)
                                time.sleep(0.2)
                                click_pos_2(200, 400, cla)
                        elif dungeon_[1] == "유적":
                            full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_clear.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 460, 120, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dungeon_clear = True

                            if dungeon_clear == False:
                                click_pos_2(80, 110, cla)
                                time.sleep(0.2)
                                click_pos_2(200, 500, cla)
                        elif dungeon_[1] == "동굴":
                            click_pos_2(210, 110, cla)
                            time.sleep(0.7)

                            full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_clear.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 160, 120, 200, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dungeon_clear = True

                            if dungeon_clear == False:
                                click_pos_2(200, 200, cla)
                    else:
                        menu_open(cla)
                        click_pos_2(840, 200, cla)
                        print("진입중")
                    time.sleep(0.2)
                    full_path = "c:\\nightcrow\\imgs\\dungeon\\y_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 400, 800, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(2)
                if dungeon_clear == False:
                    step_ready = int(dungeon_[2])
                    if dungeon_[1] == "신전":
                        if step_ready == 6:
                            step_ready = 5
                    print("step_ready", step_ready)
                    step = 95 + (step_ready * 50)
                    click_pos_2(800, step, cla)
                    time.sleep(1)

                    full_path = "c:\\nightcrow\\imgs\\dungeon\\already_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 80, 500, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("already_in!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", imgs_)
                        click_pos_2(930, 60, cla)

                    # click_pos_2(550, 620, cla)
                    # time.sleep(0.3)
                    # click_pos_2(880, 1010, cla)
                    # time.sleep(0.3)

                    full_path = "c:\\nightcrow\\imgs\\clean_screen\\confirm_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 600, 620, 640, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        click_pos_2(880, 1010, cla)
                        time.sleep(0.5)
                        full_path = "c:\\nightcrow\\imgs\\clean_screen\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 600, 620, 640, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                    loop_y = False
                    loop_y_count = 0
                    while loop_y is False:
                        loop_y_count += 1
                        if loop_y_count > 10:
                            loop_y = True
                        full_path = "c:\\nightcrow\\imgs\\dungeon\\y_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 400, 700, 800, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("y_1", imgs_)
                            loop_y = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\nightcrow\\imgs\\clean_screen\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 400, 700, 800, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm_1", imgs_)
                            loop_y = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                    full_path = "c:\\nightcrow\\imgs\\dungeon\\already_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 80, 500, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("already_in!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", imgs_)
                        click_pos_2(930, 60, cla)


                    time.sleep(1)
                else:
                    in_dungeon__ = True
                    complete_ = True
                    print("던전클리어", result_schedule_)
                    time.sleep(0.2)

        return complete_
    except Exception as e:
        print(e)

def dungeon_1(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_
        from potion import potion_check

        print("hi")


    except Exception as e:
        print(e)

def now_playing(cla, dun_):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos
        from potion import potion_check, maul_potion
        from action import clean_screen, out_check, bag_open, skill_check_


        print("now_dungeon_playing")

        play_ = False

        in_ = False
        while in_ is False:

            # 서브퀘스트
            full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\quest_soolock_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 300, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("던전 서브 수락", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\quest_complete_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 300, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("던전 서브 완료", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\nightcrow\\imgs\\check\\hunting_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hunting_1", imgs_)
                in_ = True
            full_path = "c:\\nightcrow\\imgs\\check\\hunting_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hunting_2", imgs_)
                in_ = True
            full_path = "c:\\nightcrow\\imgs\\check\\hunting_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hunting_3", imgs_)
                in_ = True


            if in_ == False:
                clean_screen(cla)


                if v_.skill_checked_ == False:
                    skill_check_(cla)

                # drag_pos(480, 250, 480, 600, cla)
                # time.sleep(1)
                # click_pos_2(480, 280, cla)
                # time.sleep(3)
                if dun_ == "동굴":
                    go_ice_1 = False
                    go_ice_count = 0
                    while go_ice_1 is False:
                        print("go_ice_count_1", go_ice_count)
                        go_ice_count += 1
                        if go_ice_count > 10:
                            go_ice_1 = True
                        full_path = "c:\\nightcrow\\imgs\\dungeon\\dongool_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 75, 150, 110, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("dongool_1", imgs_)
                            go_ice_1 = True
                            go_ice_2 = False
                            go_ice_count = 0
                            while go_ice_2 is False:
                                print("go_ice_count_2", go_ice_count)
                                go_ice_count += 1
                                if go_ice_count > 10:
                                    go_ice_2 = True
                                full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_map_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 100, 80, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_move_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(260, 260, 670, 870, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("자동이동")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)
                                        go_ice_2 = True
                                        go_ice_3 = False
                                        go_ice_count = 0
                                        while go_ice_3 is False:
                                            print("go_ice_count_3", go_ice_count)
                                            go_ice_count += 1
                                            if go_ice_count > 10:
                                                go_ice_3 = True
                                            full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_move_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(260, 260, 670, 870, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(1)
                                            else:
                                                full_path = "c:\\nightcrow\\imgs\\dungeon\\dungeon_map_1.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(30, 30, 100, 80, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_2(930, 60, cla)
                                                else:
                                                    go_ice_3 = True
                                    else:
                                        click_pos_2(535, 470, cla)
                                    time.sleep(0.2)
                                else:
                                    click_pos_2(110, 160, cla)
                                time.sleep(0.2)
                        time.sleep(0.3)

                full_path = "c:\\nightcrow\\imgs\\check\\random_move_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 960, 400, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("random_move_1", imgs_)
                    in_ = True
                    click_pos_2(345, 995, cla)
                    time.sleep(2)
                    click_pos_2(930, 850, cla)
                else:
                    bag_open(cla)
                    time.sleep(1)
                    full_path = "c:\\nightcrow\\imgs\\check\\random_move_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 100, 920, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(710, 935, cla)
                        time.sleep(0.5)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        click_pos_2(345, 1000, cla)
                        time.sleep(0.5)
                        clean_screen(cla)
                        time.sleep(2)
                        click_pos_2(930, 850, cla)
                    else:
                        print("랜덤이동서가 없다. 마을 포션 구매하러 가자")
                        maul_potion(cla)

            else:
                v_.skill_checked_ = True
                print("정상적으로 사냥중...총 10초 딜레이중")
                potion_check(cla)
                time.sleep(10)
                play_ = True

        return play_
    except Exception as e:
        print(e)



