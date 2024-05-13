# 딕셔너리 생성
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# 딕셔너리 값 조회
print("이름:", my_dict["name"])
print("나이:", my_dict["age"])

# 딕셔너리 값 변경
my_dict["age"] = 31
print("변경된 나이:", my_dict["age"])

# 새로운 키-값 쌍 추가
my_dict["gender"] = "Female"
print("새로운 딕셔너리:", my_dict)

# 키-값 쌍 제거
removed_value = my_dict.pop("city")
print("제거된 값:", removed_value)
