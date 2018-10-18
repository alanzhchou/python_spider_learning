#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan-11510 
# Date: 2018/10/13
# version: 1.0
# python_version: 3.62

import numpy as np
import random

COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0

random.seed(0)

shapes = [
    (1000, [0, 0, 0, 1, 0, 1]),  # 眠二
    (1000, [1, 0, 1, 0, 0, 0]),  # 眠二
    (1000, [0, 0, 0, 0, 1, 1]),  # 眠二
    (1000, [1, 1, 0, 0, 0, 0]),  # 眠二

    (1000, [0, 1, 0, 1, 0, 0]),  # 眠二
    (1000, [0, 0, 1, 0, 1, 0]),  # 眠二

    (10000, [0, 1, 1, 0, 0, -1]),  # 活二
    (10000, [0, 0, 1, 1, 0, -1]),  # 活二
    (10000, [-1, 0, 0, 1, 1, 0]),  # 活二
    (10000, [0, -1, 0, 1, 1, 0]),  # 活二
    (30000, [0, 1, 1, 0, 0, 0]),  # 活二
    (30000, [0, 0, 1, 1, 0, 0]),  # 活二
    (30000, [0, 0, 0, 1, 1, 0]),  # 活二

    (10000, [-1, 1, 0, 1, 0, 1]),  # 眠三
    (10000, [1, 0, 1, 0, 1, -1]),  # 眠三
    (50000, [0, 1, 0, 1, 0, 1]),  # 眠三
    (50000, [1, 0, 1, 0, 1, 0]),  # 眠三

    (10000, [-1, 0, 0, 1, 1, 1]),  # 眠三
    (10000, [1, 1, 1, 0, 0, -1]),  # 眠三
    (50000, [0, 0, 0, 1, 1, 1]),  # 眠三
    (50000, [1, 1, 1, 0, 0, 0]),  # 眠三

    (10000, [-1, 0, 1, 0, 1, 1]),  # 眠三
    (10000, [1, 1, 0, 1, 0, -1]),  # 眠三
    (50000, [0, 0, 1, 0, 1, 1]),  # 眠三
    (50000, [1, 1, 0, 1, 0, 0]),  # 眠三

    (50000, [-1, 1, 0, 1, 1, 0]),  # 跳连三
    (50000, [0, 1, 1, 0, 1, -1]),  # 跳连三
    (300000, [0, 1, 0, 1, 1, 0]),  # 跳连三
    (300000, [0, 1, 1, 0, 1, 0]),  # 跳连三

    (100000, [-1, 0, 1, 1, 1, 0]),  # 活连三
    (100000, [0, 1, 1, 1, 0, -1]),  # 活连三
    (500000, [0, 0, 1, 1, 1, 0]), # 活连三
    (500000, [0, 1, 1, 1, 0, 0]),  # 活连三

    (100000, [-1, 0, 1, 1, 1, 1]),  # 冲四
    (100000, [1, 1, 1, 1, 0, -1]),  # 冲四
    (1000000, [0, 0, 1, 1, 1, 1]),  # 冲四
    (1000000, [1, 1, 1, 1, 0, 0]), # 冲四

    (100000, [-1, 1, 1, 1, 0, 1]),  # 跳冲四
    (100000, [1, 1, 1, 0, 1, -1]),  # 跳冲四
    (1000000, [0, 1, 1, 1, 0, 1]),  # 跳冲四
    (1000000, [1, 1, 1, 0, 1, 0]),  # 跳冲四

    (100000, [-1, 1, 1, 0, 1, 1]),  # 跳冲四
    (100000, [1, 1, 0, 1, 1, -1]),  # 跳冲四
    (1000000, [0, 1, 1, 0, 1, 1]),  # 跳冲四
    (1000000, [1, 1, 0, 1, 1, 0]),  # 跳冲四

    (100000, [-1, 1, 0, 1, 1, 1]),  # 跳冲四
    (100000, [1, 0, 1, 1, 1, -1]),  # 跳冲四
    (1000000, [0, 1, 0, 1, 1, 1]),  # 跳冲四
    (1000000, [1, 0, 1, 1, 1, 0]),  # 跳冲四

    (100000, [-1, 1, 1, 1, 1, 0]),  # 跳冲四
    (100000, [0, 1, 1, 1, 1, -1]),  # 跳冲四
    (10000000, [0, 1, 1, 1, 1, 0]), # 活四

    (100000000, [-1, 1, 1, 1, 1, 1]),  # 成5
    (100000000, [1, 1, 1, 1, 1, -1]),  # 成5
    (100000000, [0,1, 1, 1, 1, 1]), # 成5
    (100000000, [1, 1, 1, 1, 1,0]) # 成5
]


class AI(object):
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        self.color = color
        self.time_out = time_out
        self.candidate_list = []

    def go(self, chessboard):
        self.candidate_list.clear()

        #Here is the simplest sample:Random decision
        new_pos = self.find_max_score_place(chessboard)
        # print(new_pos)

        assert chessboard[new_pos[0],new_pos[1]] == COLOR_NONE
        self.candidate_list.append(new_pos)

    def find_max_score_place(self,chessboard):
        COLOR = self.color
        indexs = self.get_less_emptys(chessboard)
        if len(indexs) == 0:
            return (0,0)

        best_index = indexs[0]
        if len(indexs) >= 2:
            max_scores = -100000000
            for index in indexs:
                chessboard[index[0]][index[1]] = COLOR
                score_i_my = self.calScore(chessboard,COLOR)
                score_i_you = self.calScore(chessboard, -COLOR)

                score_i_uni = score_i_my - score_i_you

                # indexs_you = self.get_less_emptys(chessboard)
                #
                # you_best_index = indexs_you[0]
                # you_max_score = -100000000
                # for index_you in indexs_you:
                #     chessboard[index_you[0]][index_you[1]] = -COLOR
                #     score_you_my = self.calScore(chessboard,COLOR)
                #     score_you_you = self.calScore(chessboard, -COLOR)
                #
                #     score_you_uni = score_you_you - score_you_my
                #     if score_you_uni > you_max_score:
                #         you_max_score = score_you_uni
                #         you_best_index = index_you
                #     chessboard[index_you[0]][index_you[1]] = 0
                # score_uni = score_i_uni - score_you_uni
                # # print(index,you_best_index,score_i_uni,score_you_uni,score_uni)

                if score_i_uni > max_scores:
                    max_scores = score_i_uni
                    best_index = index
                chessboard[index[0]][index[1]] = 0
        return best_index

    # def find_max_score_place_with_color(self,chessboard,COLOR):
    #     indexs = self.get_less_emptys(chessboard)
    #     if len(indexs) == 0:
    #         return None
    #
    #     best_index = indexs[0]
    #     max_scores = -100000000
    #     for index in indexs:
    #         chessboard[index[0]][index[1]] = COLOR
    #         score_i_my = self.calScore(chessboard,COLOR)
    #         score_i_you = self.calScore(chessboard, -COLOR)
    #
    #         score_i_uni = score_i_my - score_i_you
    #
    #         if score_i_uni > max_scores:
    #             max_scores = score_i_uni
    #             best_index = index
    #         chessboard[index[0]][index[1]] = 0
    #     return (best_index)


    # 计算盘面上的 COLOR 色的 得分
    def calScore(self,chessboard,COLOR):
        steps = 5
        all_scores = 0

        for row in range(0,self.chessboard_size - steps):
            for col in range(0,self.chessboard_size - steps):
                # cal down, right ,right-down
                down_list = []
                right_list = []
                right_down_list = []
                for step in range(0,steps+1):
                    if chessboard[row + step][col] == COLOR:
                        down_list.append(1)
                    elif chessboard[row + step][col] == -COLOR:
                        down_list.append(-1)
                    else:
                        down_list.append(0)

                    if chessboard[row][col + step] == COLOR:
                        right_list.append(1)
                    elif chessboard[row][col + step] == -COLOR:
                        right_list.append(-1)
                    else:
                        right_list.append(0)

                    if chessboard[row + step][col + step] == COLOR:
                        right_down_list.append(1)
                    elif chessboard[row + step][col + step] == -COLOR:
                        right_down_list.append(-1)
                    else:
                        right_down_list.append(0)

                all_scores += self.get_shape_score(down_list)
                all_scores += self.get_shape_score(right_list)
                all_scores += self.get_shape_score(right_down_list)
        return all_scores

    # 减少运算数， 只计算敌我双方棋子 周围 两格内的空位 计算得分
    def get_less_emptys(self,chessboard):
        emptys = np.where(chessboard == COLOR_NONE)
        emptys = list(zip(emptys[0], emptys[1]))

        whites = np.where(chessboard == COLOR_WHITE)
        whites = list(zip(whites[0], whites[1]))

        blacks = np.where(chessboard == COLOR_BLACK)
        blacks = list(zip(blacks[0], blacks[1]))

        have_gos = whites + blacks

        less_new_position = []
        step = 2

        # item is [x,y] 代表 空处坐标
        for empty in emptys:
            flag = True
            for i in range(1,step + 1):
                index_top = (empty[0] - i, empty[1])
                index_down = (empty[0] + i ,empty[1])
                index_left = (empty[0], empty[1] - i)
                index_right = (empty[0], empty[1] + i)

                index_top_left = (empty[0] - i, empty[1] -i)
                index_top_right = (empty[0] - i ,empty[1] + i)
                index_down_left = (empty[0] + i, empty[1] - i)
                index_down_right = (empty[0] + i, empty[1] + i)
                for gos in have_gos:
                    if gos == index_top or gos == index_down or gos == index_left or gos == index_right:
                        less_new_position.append(empty)
                        flag = False
                        break
                    if gos == index_top_left or gos == index_top_right or gos == index_down_left or gos == index_down_right:
                        less_new_position.append(empty)
                        flag = False
                        break
                if not flag:
                    break

        return less_new_position

    def get_shape_score(self,shape_list):
        score = 0
        for shape in shapes:
            if shape[1] == shape_list:
                score = shape[0]
        return score


if __name__ == "__main__":
    ai = AI(15,COLOR_WHITE,1)

    chessboard = np.zeros((15, 15))
    chessboard[4][6] = -1
    chessboard[5][8] = -1
    chessboard[7][4] = -1
    chessboard[7][6] = -1
    chessboard[7][7] = -1
    chessboard[8][5] = -1
    chessboard[10][7] = -1

    chessboard[5][7] = 1
    chessboard[6][8] = 1
    chessboard[7][8] = 1
    chessboard[7][9] = 1
    chessboard[8][8] = 1
    chessboard[9][4] = 1
    chessboard[9][6] = 1
    print(chessboard)
    # emptys = ai.get_less_emptys(chessboard)
    # print(emptys)

    print(ai.find_max_score_place(chessboard))



    # ai2 = AI(15, COLOR_BLACK, 1)

    # print(ai.find_max_score_place(chessboard))

    # print(chessboard)

    # print(ai.calScore(chessboard,1))
    # print(ai.find_max_score_place(chessboard))




