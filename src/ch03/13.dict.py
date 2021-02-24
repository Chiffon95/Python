dict1 = {'번호' : 1, '성명' : '장동건', '나이' : 21, '사는곳' : '서울'}
print (dict1)
print(type(dict1))
print(dict1['나이'])
dict1['나이'] = 24
print(dict1['나이'])
dict1['직업'] = '배우'
print(dict1)
print(dict1.keys())
print(dict1.values())
print('사는곳' in dict1)
del dict1['사는곳']
print('사는곳' in dict1)
print(dict1)
