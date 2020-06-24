import os
import sys
import requests

client_id = "hjpUcrC21mwYUSLAsAVb"
client_secret = "3yxRtOWz32"

url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
#url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

#file_name = 'ex_01.jpg'
file_name = 'ex_02.jpg'

files = {'image': open(file_name, 'rb')}

headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code

if(rescode==200): # 웹 요청이 성공할 경우
    print(response.text)
else: # 웹 요청이 실패할 경우
    print("Error Code:", rescode)