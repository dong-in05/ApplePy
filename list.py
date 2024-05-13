# 빈 리스트를 생성합니다
my_list = []

# 리스트에 요소를 추가합니다
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

# 리스트의 길이를 출력합니다
print("리스트의 길이:", len(my_list))

# 리스트의 요소를 인덱스를 통해 접근합니다
print("첫 번째 요소:", my_list[0])
print("두 번째 요소:", my_list[1])
print("마지막 요소:", my_list[-1])

# 리스트 슬라이싱을 통해 부분 리스트를 추출합니다
subset = my_list[2:4]
print("부분 리스트:", subset)

# 리스트에서 요소를 제거합니다
removed_element = my_list.pop(0)
print("제거된 요소:", removed_element)
print("제거 후 리스트:", my_list)

# 리스트에 특정 요소를 삽입합니다
my_list.insert(2, 6)
print("삽입 후 리스트:", my_list)

# 리스트 내부의 요소를 정렬합니다 (오름차순)
my_list.sort()
print("정렬 후 리스트:", my_list)

# 리스트 내부의 요소를 역순으로 정렬합니다 (내림차순)
my_list.reverse()
print("역순 정렬 후 리스트:", my_list)

# 리스트를 반복하여 요소를 출력합니다
print("리스트의 요소:")
for element in my_list:
    print(element)

# 리스트를 복사합니다
copied_list = my_list.copy()
print("복사된 리스트:", copied_list)

# 리스트를 모두 제거합니다
my_list.clear()
print("모든 요소가 제거된 리스트:", my_list)
