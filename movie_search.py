import pymysql
import csv
import pandas as pd
import numpy as np
import time

# connect
con = pymysql.connect(host='localhost',
                      user='root',
                      password='your passward',
                      db='your db_name',
                      charset='utf8')

print("connect successful!!")
cursorObject = con.cursor()


# (1) 사용자 인터페이스
# start
def user_interface():
    print('\n\n\n\n\n\n')
    print("#############################################")
    print("(0) 종료")
    print("(1) 릴레이션 생성 및 데이터 추가")
    print("(2) 제목을 이용한 검색")
    print("(3) 관객수를 이용한 검색")
    print("(4) 개봉일을 이용한 검색")
    print("#############################################")
    print("원하는 번호를 입력해주세요 : ", end='')
    user_pick = int(input())
    print('\n\n\n\n\n\n')
    return user_pick
# end


# (1) - 1 함수 이동
# start
def go_func(user_pick, db_obj):
    if user_pick == 0:
        pass
    elif user_pick == 1:
        create_DB(db_obj)
    elif user_pick == 2:
        search_title(db_obj)
    elif user_pick == 3:
        search_view(db_obj)
    elif user_pick == 4:
        search_date(db_obj)
    else:
        print("다시 입력해주세요")
    time.sleep(1)
# end


# (2) 릴레이션 생성 및 데이터 추가
# start
def create_DB(db):  # Table Create
    sqlQuery = "create table movie (id char(3), title varchar (100), company varchar (50), releasedate  date, country varchar (10),  totalscreen int, profit numeric (15,2), totalnum int, grade varchar (50), primary key (id));"
    db.execute(sqlQuery)
    insert_data(db)
    print("Table Create Complete.")


def insert_data(db):  # Insert Data
    data_list = np.array(pd.read_csv("Enter the folder path", sep='|'))
    for i in range(299):
        sqlQuery = "insert into movie values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        db.execute(sqlQuery, (data_list[i][1], data_list[i][2], data_list[i][3], data_list[i][4],
                   data_list[i][5], data_list[i][6], data_list[i][7], data_list[i][8], data_list[i][9]))
    print("Tuple Insert Complete.")
# end


# (3) 제목을 이용한 검색
# start
def search_title(db):  # Table Create
    print('======================= 제목 검색 =======================\n')
    print('입력한 제목을 포함하는 모든 영화가 검색됩니다.')
    print('검색을 원하시는 영화의 제목을 입력해주세요 : ', end='')
    want_title = input()
    print('\n\n')

    sqlQuery = "select * from movie where title like '%" + want_title + "%';"
    db.execute(sqlQuery)
    rows = db.fetchall()

    print("--------------검색 결과--------------\n")
    for row in rows:
        print(row)
        print()
    print("-------------------------------------")
    print()
    print('=========================================================')
    time.sleep(1)
# end


# (4) 관객수를 이용한 검색
# start
def search_view(db):  # Table Create
    print('======================= 제목 검색 =======================\n')
    print('입력한 관객수보다 더 많은 모든 영화가 검색됩니다.')
    print('관객수를 입력해주세요 : ', end='')
    want_viewer = input()
    print('\n\n')

    sqlQuery = "select * from movie where totalnum > " + want_viewer + ";"
    db.execute(sqlQuery)
    rows = db.fetchall()

    print("--------------검색 결과--------------\n")
    for row in rows:
        print(row)
        print()
    print("-------------------------------------")
    print()
    print('=========================================================')
    time.sleep(1)
# end


# (5) 개봉 일을 이용한 검색
# start
def search_date(db):  # Table Create
    print('======================= 제목 검색 =======================\n')
    print('시작 일과 종료 일 사이의 모든 영화가 검색됩니다.')
    print('시작 일을 입력해주세요 : ', end='')
    start_date = input()
    print('종료 일을 입력해주세요 : ', end='')
    end_date = input()

    print('\n\n')

    sqlQuery = "select * from movie where releasedate between '" + \
        start_date + "' and '" + end_date + "';"
    db.execute(sqlQuery)
    rows = db.fetchall()

    print("--------------검색 결과--------------\n")
    for row in rows:
        print(row)
        print()
    print("-------------------------------------")
    print()
    print('=========================================================')
    time.sleep(1)
# end


while (True):
    user_pick = user_interface()
    if (user_pick == 0):
        print("\n프로그램을 종료합니다.\n")
        break
    else:
        go_func(user_pick, cursorObject)


# Close connection
con.commit()
con.close()
