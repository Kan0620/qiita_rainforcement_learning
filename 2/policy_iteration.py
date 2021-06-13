#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def main():
    # 漸化式の右辺のv定義　マスに対応していて左から1,2,3,ゴール
    v = np.array([0.,0.,0.,0.])
    # 漸化式の左辺のv定義
    new_v = np.array([0.,0.,0.,0.])
    # 報酬を定義 
    r = np.array([-1.,-1.,-1.,10.])
    # マス1から左に行った時にゴールに行く確率
    p = 3/4
    # 割引率γ定義　今回は1にした
    gamma = 1.0
    # 方策を定義　最初はランダムに動くよう初期化　pi[マスのindex,行動のindex]の値がπ(s,α)
    #行動のindexは左が0で右が1　例えばpi[0,0]はマス1で左を選ぶ確率
    pi = np.ones(6).reshape(3,2) * 1/2
    # 更新した後の方策
    new_pi = np.ones(6).reshape(3,2) * 1/2
    #行動価値関数定義
    q=np.zeros(6).reshape(3,2)
    
    
    while True:
        # 動的計画法で今のπでのvを計算
        while True:
            # 漸化式からnew_v計算
            new_v[0] = pi[0,0]*(p*(r[3]+gamma*v[3])+(1-p)*(r[0]+gamma*v[0])) + pi[0,1]*(r[1]+gamma*v[1])
            new_v[1] = pi[1,0]*(r[0]+gamma*v[0]) + pi[1,1]*(r[2]+gamma*v[2])
            new_v[2] = pi[2,0]*(r[1]+gamma*v[1]) + pi[2,1]*(r[3]+gamma*v[3])
            # 元のvとの誤差の合計が0.01より小さければ計算終了
            if np.abs(new_v-v).sum() < 0.01:
                break
            # v更新
            v = new_v.copy()
        
        print('v=',v)
        # 行動価値関数計算
        q[0,0] = p*(r[3]+gamma*v[3]) + (1-p)*(r[0]+gamma*v[0])
        q[0,1] = r[1] + gamma*v[1]
        q[1,0] = r[0] + gamma*v[0]
        q[1,1] = r[2] + gamma*v[2]
        q[2,0] = r[1] + gamma*v[1]
        q[2,1] = r[3] + gamma*v[3]
        
        # 新しい方策計算 0で初期化
        new_pi=np.zeros(6).reshape(3,2)
        for state_index in range(3):
            # 行動価値関数が高い行動のindex求める
            a_index = np.argmax(q[state_index])
            # 行動価値関数が大きかった行動をするように方策を変える
            new_pi[state_index,a_index] = 1
        # 元のpiとの誤差の合計が0.01より小さければ計算終了
        if np.abs(new_pi-pi).sum() < 0.01:
            print('best policy')
            print(new_pi)
            break
            # pi更新
        pi = new_pi.copy()
    
    
    
    
    
    
    
    
    
    
    
    
    