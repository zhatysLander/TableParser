# int  -целые числа  1,2,3,
# float - числа с запятой 1.3 , 5.2
# str - строки ' '  " "
# list -списки []

# list1-имя переменной
# [] -создания списка
# list1=[]
# print(list1)
#
# list2=[2,3,4]
# print(list2)
#Задание
#создать список list3
# заполните его числами
# list3=[2,3,4,5]
# print(list3)

#Пример
# list=[-1,9,4,2]
# print(len(list))
# #Задание
# list=[9,2,8,-2]
# Нужно вывести длину списка (list)




#Пример
#      0 1 2 3
# list=[-1,9,4,2]
# #Нужно вывести цифру -1
# #Нужно вывести цифру 4
# print(list[0]) # -1
# print(list[2]) # 4
# #Задание
# #     0 1  2 3
# list=[6,9,-2,5]
#Нужно вывести цифру 9


#Пример
# list=[1,2,'winter',6.7,'red',9]
# print(list)

#Пример
# метод append добавляет элемент в список list
#добавьте значение 4 в list
list=[1,2,3]
list.append(4)
print(list)
#Задание
list1=[8,0,3]
#добавьте значение 9 в list1
# ________________________________________________
# int
# float
#str
# list список
# list1=[3,7,9,1]
# list2=[0,1,2]
# list1=list1+list2
# print(list1)
# [3,7,9,1,0,1,2]
#Задание1
#у вас есть список list1=[2,9]
# list2=[7,1]
# добавить значение списка list2 к list1
# при выводе list1 [2,9,7,1]

#.Добавление элемента в список. Метод append() добавляет элемент в конец списка.
# a=[1,2,3]
# a.append(5) # имя листа.append(элемент)
# print(a)
# list=[5,2,9]
# добавить туда нужно цифру 3
#  в конце чтобы вышло [5,2,9,3]

#
# a=['winter','summer']
# a.append(5)
# print(a)
# #Задание
# list=['red','code']
#добавить строку 'good'
# ['red','code','good']



# Добавление нескольких элементов в список. Метод extend() добавляет
# все элементы указанного объекта (список) в конец списка
# first_list=[7,8]
# second_list=[5,6]
# first_list.extend(second_list) #все значения second_list в first_list
# # имя списка.extend([])
# print(first_list)
# #Задание
# a=[2,4]
# b=[6,7]
#все значения списка b добавить в список a
#при выводе списка a, [2,4,6,7]




# Удаление элемента из списка.
# Метод remove() удаляет первый соответствующий элемент (который передается
# в качестве аргумента) из списка.
# list1=[2,6,1]
# # имя списка.remove(элемент)
# list1.remove(1)
# print(list1)
#Задание
# list1=[7,9,0]
# нужно удалить цифру 9
# [7,0]

# _____________________________________

# list=[2,5,6]
# #добавить цифру 9 в список
# list.append(9)
# # удалить цифру 5 в списке
# list.remove(5)
# #  и добавить список [0,1]
# list.extend([0,1])
# # [2,6,9,0,1]
# print(list)

#Задание
#list=[9,1,3]
#добавить цифру 7 в список
# удалить цифру 3 в списке
#  и добавить список [5,2]

# __________________________________
# Метод count() возвращает количество раз, когда указанный элемент
# появляется в списке.
# имя списка.count(элемент)
first_list=[7,8,6,5,6,2]
value=first_list.count(6)
print('количество шестерок в списке: ',value)
#Задание
# list=[7,9,7,8,7]
# посчитать сколько семерок есть в списке

# __________________________________________
#Добавление элемента в список
# Метод insert() вставляет элемент в список по указанному индексу.
#
# insert(индекс, элемент)
#  0 1 2
a=[1,2,3]
a.insert(0,9) # [9,1,2,3]
print(a)
#  012345
# a='winter'
# print(a[1])
#Задание
#list=[3,9,1,7]
#добавить этот список цифру 2
#чтобы в конце вышло [3,2,9,1,7]

