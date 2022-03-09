"""이코테 구현 예제4-2 왕실의 나이트
"""

input_data=input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a')) +1

result = 0 
steps = [(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,2)]

for step in steps :
    next_column = column +step[1]
    next_row = row + step[0]

    if next_row >=1 and next_row <=8 and next_column>=1 and next_column <=8 :
        result +=1

print(result)