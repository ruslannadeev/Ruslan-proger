f = open('info.txt', 'r')
w = open('release.txt', 'w')
input_array = [i.split() for i in f.read().split("\n")]
output_str = ''
grades = ''
for line in input_array:
    avg_grade = (int(line[4]) + int(line[5]) + int(line[6]))/3
    output_str += f'{line[0]} | {line[1]} | {line[2]} | {line[3]} \
| {line[4]} {line[5]} {line[6]}  -> {avg_grade}\n'
    grades += f'{avg_grade} '
grades = grades.split()
output_str = output_str.split("\n")
final = []
while len(grades) > 0:
    a = max(grades)
    for j in output_str:
        if j.endswith(a):
            
            final.append(j)
    grades.remove(a)
   
def listmerge(lstlst):
    all=''
    for lst in lstlst:
      all += lst + '\n'
    return all
listmerge(final)          
w.write(listmerge(final))
f.close()
w.close()




'''
создаем массив из всех avg_grade
берем максимальный из элементов
проверяем в какой строке находится этот элемент
ставим эту строку первой
удаляем нахуй данный элемент из массива с avg_grade
продолжаем дальше
теперь из трех ищем максимальный
ищем его в строке
ставим строку на второе место
'''