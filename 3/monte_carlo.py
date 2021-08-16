#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random

def main():
    #seed固定
    random.seed(0)
    # 現在の推定状態価値定義
    v = np.array([0., 0., 0., 0.])
    # 次の推定状態価値定義
    new_v = np.array([0., 0., 0., 0.])
    # 報酬を定義
    r = np.array([-1., -1., -1., 10.])
    # 学習率alpha定義
    alpha = 0.0005
    # 割引率gamma定義
    gamma = 1.0
    # 遷移確率p定義　このpは未知であることに注意
    p =1/4
    # T回探索させる
    T = 10000
    
    for t in range(T):
        
        # スタート位置を決める indexにした方が色々便利なので少しややこしいけど我慢
        now_s_index = 1
        #ゴールについたかの真理値定義
        done = False
        #経験したsを保存しておくリスト定義
        experienced_s_index = []
        experienced_s_index.append(now_s_index)
        
        while not done:
            
            #エージェントは必ず左に行くことに注意する
            #1にいるときは確率pでゴール 確率1-pで元に戻る
            if now_s_index == 0:
                
                if random.random() < p:
                    
                    now_s_index = 3
                    done = True
                    
                else:
                    
                    now_s_index = 0
                                    
            #2にいるときは確実に1に行く
            elif now_s_index == 1:
                
                now_s_index = 0
            
            experienced_s_index.append(now_s_index)
        
        experienced_s_index = np.array(experienced_s_index)
        #もらった報酬取得　gave_r[0]は実際にはもらってないので注意
        gave_r = r[experienced_s_index]
        #経験した全てのsに対して累積報酬和計算　ただしゴールは除く
        for i,s in enumerate(experienced_s_index[:-1]):
            
            #報酬にかける割引率計算
            gamma_mask = np.array([gamma**(j) for j in range(len(experienced_s_index) - (i+1))])
            #累積報酬和計算
            G = (gave_r[i+1:] * gamma_mask).sum()
            #状態価値更新
            if s == 0:
                new_v[0] = v[0] + alpha*(G - v[0])
                
            else:
                new_v[1] = v[1] + alpha*(G - v[1])
            
            v = new_v.copy()
            
    print('v(s1):{} v(s2):{}'.format(new_v[0], new_v[1]))