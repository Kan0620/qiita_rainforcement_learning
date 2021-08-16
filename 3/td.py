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
    alpha = 0.0003
    # 割引率gamma定義
    gamma = 1.0
    # 遷移確率p定義　このpは未知であることに注意
    p =1/2
    # T回探索させる
    T = 100000
    
    for t in range(T):
        
        # スタート位置をランダムに決める indexにした方が色々便利なので少しややこしいけど我慢
        now_s_index = random.choice([0,1])
        next_s_index = 0
        #ゴールについたかの真理値定義
        done = False
        
        while not done:
            
            action = random.choice([-1, 1])
            
            if now_s_index == 0 and action == -1:
                
                if random.random() < p:
                    
                    next_s_index = 3
                    done = True
                    
                else:
                    
                    next_s_index = 0
            else:
                
                next_s_index = now_s_index + action
                
                if next_s_index == 3:
                    
                    done = True
            
            gave_r = r[next_s_index]
            new_v[now_s_index] = v[now_s_index] + alpha*(gave_r + gamma*v[next_s_index] - v[now_s_index])
            
            v = new_v.copy()
            now_s_index = next_s_index
    print(v)
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        