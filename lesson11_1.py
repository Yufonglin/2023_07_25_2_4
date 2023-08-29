import random
def get_score() -> list:
    score = []
    for i in range(5):
        score.append(random.randint(50, 100))
    return score

nums_int = int(input("請輸入學生數:"))
#取得30個姓名
with open('names.txt',encoding='utf-8',newline='') as file:
    names_str = file.read()
    all_names_list = names_str.split(sep="\n")
    names_list = random.choices(all_names_list,k=nums_int) #取出一定數量的姓名
print(names_list)
students = []
for _ in range(nums_int):
    scores = get_score()
    students.append(scores)
students