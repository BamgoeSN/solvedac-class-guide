import requests
import json

class_no = 2

url = "https://solved.ac/api/v3/search/problem"
headers = {"Accept": "application/json"}
params = {"query": f"e/{class_no}"}

ans = requests.get(url, headers=headers, params=params).json()
# print(json.dumps(ans, ensure_ascii=False))
problems = ans["items"]

for prob in problems:
    problem_id = prob["problemId"]
    title_ko = prob["titleKo"]
    tag = list(map(lambda x: x["key"], prob["tags"]))
    print(f"- E{problem_id}\t{title_ko}\t\t\t\t\t{tag}")

print()

url = "https://solved.ac/api/v3/search/problem"
headers = {"Accept": "application/json"}
params = {"query": f"c/{class_no} ~e/{class_no}"}

ans = requests.get(url, headers=headers, params=params).json()
# print(json.dumps(ans, ensure_ascii=False))
problems = ans["items"]

for prob in problems:
    problem_id = prob["problemId"]
    title_ko = prob["titleKo"]
    tag = list(map(lambda x: x["key"], prob["tags"]))
    print(f"- {problem_id}\t{title_ko}\t\t\t\t\t{tag}")
