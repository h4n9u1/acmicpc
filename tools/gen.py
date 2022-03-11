import sys
import os
import requests
from bs4 import BeautifulSoup
from base64 import b64decode
import json

if len(sys.argv) != 3:
    print("Usage: gen.py INDEX DIST")
    sys.exit()

index = sys.argv[1]
dist = sys.argv[2]

# 프로그래밍 언어 리스트
with open("languages.json") as f:
    langs = json.load(f)

# 저작권 및 라이선스 고지
with open("license") as f:
    _license = f.readlines()

# 해당 문제에 대한 정보 크롤링
url = f"https://www.acmicpc.net/problem/{index}"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15"
headers = {'User-Agent': user_agent}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find("span", id="problem_title")
    problem_info = soup.find("table", id="problem-info")
    
    timeout = int(problem_info.find_all("td")[0].get_text().split(" ")[0])
    memory = int(problem_info.find_all("td")[1].get_text().split(" ")[0])
else : 
    print(response.status_code)
    sys.exit()

os.makedirs(dist, exist_ok=True)

for lang in langs:
    ext = lang["ext"]
    comment = lang["comment"]
    N = timeout
    _timeout = eval(lang["advantage"]["time"])
    N = memory
    _memory = eval(lang["advantage"]["memory"])

    

    # 문제 정보
    problem_info = f"""
    {comment} Baekjoon Online Judge
    {comment} {index} - {title}
    {comment} {url}
    {comment}
    {comment} Timeout: {_timeout} sec
    {comment} Memory: {_memory} MB
    {comment}
    """.replace("    ", "")

    commented_license = ""

    for i in _license:
        commented_license += f"{comment} {i}"

    problem_info += commented_license

    # 템플릿 파일 읽기
    with open(f"./template/template.{ext}", "r") as f:
        template = f.read().replace("{{ PROBLEM_INFO }}",problem_info)

    print(template)

    # N = 0
    with open(os.path.join(dist, f"{index}.{ext}"), "w") as f:
        f.write(template)

