prompt = """
1. add
2. del
3. List
5. Quit
"""

# 문자열을 줄 단위로 나누기
lines = prompt.strip().splitlines()

# 각 줄을 따로 저장
option1 = lines[0]
option2 = lines[1]
option3 = lines[2]
option4 = lines[3]

print(option1)  # "1. add"
print(option2)  # "2. del"
print(option3)  # "3. List"
print(option4)  # "5. Quit"


#//////////////////////////////


prompt = """
1. add 2. del
3. List 4. Quit
"""

# 줄 단위로 나누기
lines = prompt.strip().splitlines()

# 각 줄의 내용을 공백을 기준으로 나누기
options = []
for line in lines:
    options.extend(line.split())

# 결과 출력
for option in options:
    print(option)
