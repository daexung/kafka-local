'''
- 로그 생성 -> 파일 기록
- json 형태, 텍스트(한줄에 로그 작성) 형태
- 연습을 위해 json 형태와 텍스트 형태를 둘다 시도중
'''

# 1. 모듈 가져오기

import json
import time
import datetime
import os
import random

# 2. 로그가 저장되는 디렉토리 생성/지정 

log_dir = './sensor_logs'
if not os.path.exists(log_dir):   # 로그 디렉토리 없으면 생성
    os.mkdir(log_dir)

# 3. 로그 발생 및 저장

def generate_logs():
    # 로그 샘플
    data = {
        'timestamp' : datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
        'sensor_id' : "AI-FACTORY-001",
        'temperature' : round(random.uniform(50,100),2),
        'humidity' : round(random.uniform(0,30),2),
        'status' : "RUNNING"
    }
    # json 형태로 파일 기록(한줄에 로그 1개씩) -> dict 객체의 직렬화 처리가 필요하다
    # 파일명 ./sensor_logs/sensor_json.log
    with open(f"{log_dir}/sensor_json.log", "+a" , encoding= 'utf-8') as f:  # 계속해서 추가해야되니까 append
        f.write(json.dumps(data)+"\n")



    # 텍스트 형태로 파일 기록(한줄에 로그 1개씩) -> f-string 사용해서 구성
    # 파일명 ./sensor_logs/sensor_text.log
    pass


# 4. 로그 발생기 가동

def main():
    try :
        while True:
            generate_logs()
            time.sleep(2) # 2초 대기
    except Exception:   # 강제 종료 예외처리  
        print('종료') 
    pass

# 5. 프로그램 시작

if __name__ == '__main__':
    print('로그 발생 시작. 종료 방법: ctrl + c')
    main()