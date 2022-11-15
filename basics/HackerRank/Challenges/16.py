score_list = []
names = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.append([name, score])

second_lowest_grade = sorted(set(score_list))[1]

for score in score_list:
    if score[1] == second_lowest_grade:
        names.append(score[0])

names.sort()
for name in names:
    print(name)


