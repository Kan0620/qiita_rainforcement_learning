#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def main():
    # 漸化式の右辺のv定義　マスに対応していて左から1,2,3,ゴール
    v = np.array([0., 0., 0., 0.])
    # 漸化式の左辺のv定義
    new_v = np.array([0., 0., 0., 0.])
    # 報酬を定義 
    r = np.array([-1., -1., -1., 10.])
    # マス1から左に行った時にゴールに行く確率　今回は1/2にした
    p = 1/2
    # 割引率γ定義　今回は1にした
    gamma = 1.0
    
    while True:
        # 漸化式からnew_vを計算    
        new_v[0] = 1/2*(p*(r[3]+gamma*v[3])+(1-p)*(r[0]+gamma*v[0])) + 1/2*(r[1]+gamma*v[1])
        new_v[1] = 1/2*(r[0]+gamma*v[0]) + 1/2*(r[2]+gamma*v[2])
        new_v[2] = 1/2*(r[1]+gamma*v[1]) + 1/2*(r[3]+gamma*v[3])
        # 元のvとの誤差の合計が0.01より小さければ計算終了
        if np.abs(new_v-v).sum() < 0.01:
            
            break
        print(v)
        #vを更新
        v=new_v.copy()
        
    return 0