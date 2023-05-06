import time

import requests
import json
# import os
import sys
sys.path.append('C:/nightcrow/mymodule')

import variable as v_

def jadong_play(cla, result_schedule_):
    try:
        import cv2
        import os
        import numpy as np
        from function import text_check_get, int_put_, imgs_set_, click_pos_reg
        from action import out_check, clean_screen
        from massenger import line_to_me

        dungeon_ = result_schedule_.split("_")

        print("자동사냥냥터 : ", dungeon_[2])

        complete_ = False

        result_out = out_check(cla)
        if result_out == False:
            clean_screen(cla)

        if "_" in result_schedule_:
            dungeon_ = result_schedule_.split("_")

        dir_path = "C:\\nightcrow"

        if dungeon_[1] == "아빌리우스":
            file_path = dir_path + "\\jadong\\abilius.txt"
        if dungeon_[1] == "바스티움":
            file_path = dir_path + "\\jadong\\bastium.txt"
        if dungeon_[1] == "첼라노":
            file_path = dir_path + "\\jadong\\chalano.txt"
        file_path2 = dir_path + "\\jadong\\jadong.txt"

        if os.path.isfile(file_path) == True:
            with open(file_path, "r", encoding='UTF8') as file:
                read_ready = file.read()
                read_ready = read_ready.split(":")
                read_ = read_ready[1].split("/")
                print("read_", read_)

                # for i in range(len(read_)):
                #     if read_[i] == dungeon_[2]:
                #         hunter_spot =
        else:
            print("자료가 없다")
            line_to_me(cla, "나크 자동사냥 자료 없다.")


        if os.path.isfile(file_path2) == True:
            with open(file_path2, "r", encoding='UTF8') as file:
                read_line = file.read().splitlines()
                for i in range(len(read_line)):
                    result_ = read_line[i].split("/")
                    if result_[0] == dungeon_[2]:
                        hunter_spot = result_[2]


        else:
            print("자료가 없다")
            line_to_me(cla, "나크 자동사냥 자료 없다.2")


        full_path = "c:\\nightcrow\\imgs\\jadong\\" + read_ready[0] + "\\" + hunter_spot + ".PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(40, 80, 160, 110, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("도착한 상태")
            now_playing(cla)
        else:
            print("사냥터 진입하러 가자")
            # 자동사냥 진입
            in_world(cla)
            in_spot(cla, result_schedule_)
            go_to_spot(cla)

        return complete_
    except Exception as e:
        print(e)

def in_world(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, click_pos_2, imgs_set_

        in_worldmap = False
        while in_worldmap is False:
            full_path = "c:\\nightcrow\\imgs\\jadong\\world_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("worldmap", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                in_worldmap = True

                last_in = False
                while last_in is False:
                    full_path = "c:\\nightcrow\\imgs\\jadong\\world_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("진입 대기중")
                    else:
                        last_in = True

            else:
                maul_ = False
                full_path = "c:\\nightcrow\\imgs\\jadong\\world_ready_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("world_ready_3", imgs_)
                    maul_ = True

                full_path = "c:\\nightcrow\\imgs\\jadong\\world_ready_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("world_ready_4", imgs_)
                    maul_ = True

                if maul_ == True:
                    click_pos_2(230, 90, cla)

                else:
                    world_check = False
                    full_path = "c:\\nightcrow\\imgs\\jadong\\world_ready_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 70, 40, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("world_ready_1", imgs_)
                        world_check = True
                    full_path = "c:\\nightcrow\\imgs\\jadong\\world_ready_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 70, 40, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("world_ready_2", imgs_)
                        world_check = True
                    if world_check == True:
                        click_pos_2(110, 160, cla)

    except Exception as e:
        print(e)


def in_spot(cla, result_schedule_):
    try:
        import cv2
        import numpy as np
        import os.path
        from function import text_check_get, int_put_, click_pos_reg, click_pos_2, imgs_set_, drag_pos
        from massenger import line_to_me

        in_map = False
        while in_map is False:
            full_path = "c:\\nightcrow\\imgs\\jadong\\sin_triesde.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sin_triesde", imgs_)
                click_pos_reg(imgs_.x, imgs_.y - 50, cla)
                in_map = True
                time.sleep(1)
            full_path = "c:\\nightcrow\\imgs\\jadong\\bastium.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bastium", imgs_)
                in_map = True
            full_path = "c:\\nightcrow\\imgs\\jadong\\abilius.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                in_map = True
                print("abilius", imgs_)
            full_path = "c:\\nightcrow\\imgs\\jadong\\chalano.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                in_map = True
                print("chalano", imgs_)
            if in_map == True:
                # 사냥터에 따라 지도 클릭 달라짐

                if "_" in result_schedule_:

                    dungeon_ = result_schedule_.split("_")


                dir_path = "C:\\nightcrow"

                if dungeon_[1] == "아빌리우스":
                    file_path = dir_path + "\\jadong\\abilius.txt"
                if dungeon_[1] == "바스티움":
                    file_path = dir_path + "\\jadong\\bastium.txt"
                if dungeon_[1] == "첼라노":
                    file_path = dir_path + "\\jadong\\chalano.txt"
                file_path2 = dir_path + "\\jadong\\jadong.txt"



                if os.path.isfile(file_path) == True:
                    with open(file_path, "r", encoding='UTF8') as file:
                        read_ready = file.read()
                        read_ready = read_ready.split(":")
                        read_ = read_ready[1].split("/")
                        print("read_", read_)

                        # for i in range(len(read_)):
                        #     if read_[i] == dungeon_[2]:
                        #         hunter_spot
                else:
                    print("자료가 없다")
                    line_to_me(cla, "나크 자동사냥 자료 없다.")
                full_path = "c:\\nightcrow\\imgs\\jadong\\" + read_ready[0] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y - 50, cla)
                    in_worldmap = False
                    while in_worldmap is False:
                        full_path = "c:\\nightcrow\\imgs\\jadong\\world_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("worldmap", imgs_)
                            if os.path.isfile(file_path2) == True:
                                with open(file_path2, "r", encoding='UTF8') as file:
                                    read_line = file.read().splitlines()
                                    for i in range(len(read_line)):
                                        result_ = read_line[i].split("/")
                                        if result_[0] == dungeon_[2]:
                                            in_worldmap = True
                                            print("완벽", result_[1])
                                            in_spot_start = False
                                            while in_spot_start is False:
                                                full_path = "c:\\nightcrow\\imgs\\jadong\\confirm_1.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    in_spot_start = True
                                                else:
                                                    if result_[1] == "like":
                                                        click_pos_2(880, 130, cla)
                                                        time.sleep(0.5)
                                                        click_pos_2(800, int(result_[2]), cla)
                                                    elif result_[1] == "drag":
                                                        drag_pos(800, 900, 800, 200, cla)
                                                        time.sleep(0.5)
                                                        click_pos_2(800, int(result_[2]), cla)
                                                    else:
                                                        drag_pos(800, 200, 800, 900, cla)
                                                        time.sleep(0.5)
                                                        click_pos_2(800, int(result_[1]), cla)
                                                time.sleep(0.2)
                            else:
                                print("자료가 없다..")
                                line_to_me(cla, "나크 자동사냥 자료 없다.")

                        else:
                            print("다시 월드맵 진입중")
                        time.sleep(0.3)



    except Exception as e:
        print(e)

def go_to_spot(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, click_pos_2, imgs_set_

        print("사냥터 이동중")

        bihangjang = False
        while bihangjang is False:
            full_path = "c:\\nightcrow\\imgs\\jadong\\bihangjang.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 80, 160, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                bihangjang = True
            else:
                print("비행장 이동중")
            time.sleep(0.2)

        flying = False
        while flying is False:
            full_path = "c:\\nightcrow\\imgs\\jadong\\flying_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(820, 880, 910, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                flying = True
                fly_to_the_sky = False
                while fly_to_the_sky is False:
                    full_path = "c:\\nightcrow\\imgs\\jadong\\flying_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(820, 880, 910, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\nightcrow\\imgs\\jadong\\fly_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 970, 960, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        fly_to_the_sky = True
                        time.sleep(15)
                    time.sleep(3.5)
            else:
                print("날려고 달리는 중")
            time.sleep(0.2)

    except Exception as e:
        print(e)

def now_playing(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos
        from potion import potion_check
        from action import clean_screen, out_check, bag_open

        if cla == "one":
            potion = v_.mypotion_1
        else:
            potion = v_.mypotion_2

        print("now_jadong_playing")

        play_ = False

        in_ = False
        while in_ is False:

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

            full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\quest_soolock_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 300, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_soolock_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\quest_complete_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 300, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_complete_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            if in_ == False:
                clean_screen(cla)
                # 공격하기
                click_pos_2(930, 850, cla)


            else:
                print("정상적으로 사냥중...5초 딜레이중")
                potion_check(cla)
                time.sleep(5)
                play_ = True

        return play_
    except Exception as e:
        print(e)
