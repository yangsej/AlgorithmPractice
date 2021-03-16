info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

info_s = []
for i in info:
    temp = i.split(' ')
    temp[4] = int(temp[4])
    info_s.append(temp)

import collections
print(collections.Counter(info))

info_dict = {'java':0, 'python':0, 'cpp':0, 'frontend':0, 'backend':0, 'junior':0, 'senior':0, 'pizza':0, 'chicken':0}
for lang, part, work, food, score in info_s:
    info_dict[lang] += 1
    info_dict[part] += 1
    info_dict[work] += 1
    info_dict[food] += 1

query_s = []
for i in query:
    temp = list(i.split(' '))
    temp = list(filter(lambda x: x!='and', temp))
    temp[4] = int(temp[4])
    query_s.append(temp)

answer = []
for lang, part, work, food, score in query_s:
    answer.append(len(list(filter(lambda i: (i[0] == lang or lang == '-') and (i[1] == part or part == '-') and (i[2] == work or work == '-') and (i[3] == food or food == '-') and i[4] >= score, info_s))))
print(answer)
