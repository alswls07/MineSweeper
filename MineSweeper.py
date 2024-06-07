import random

mine_map=[[0 for i in range(100)] for j in range(100)]
player_map=[[0 for i in range(100)] for j in range(100)]

def set_Game(r, c):
    make_Map(r, c)
    add_Count_Mines(r, c)
    
def make_Map(r, c):
    global mine_map
    for i in range(r):
        for j in range(c):
            if random.randint(1, 11)<=3:
                mine_map[i][j]=-1
            else:
                mine_map[i][j]=0

def add_Count_Mines(r, c):
    global mine_map
    for i in range(r):
        for j in range(c):
            if mine_map[i][j]!=-1:
                mine_map[i][j]=count_Mines(i, j)
            
def count_Mines(m, n):
    global mine_map
    count=0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i==0 and j==0:
                continue
            else:
                if mine_map[m+i][n+j]==-1:
                    count+=1
    return count

def start_Game():
    pass
            
col, row=map(int, input('가로와 세로를 입력하시오: ').split())

set_Game(row, col)
start_Game()