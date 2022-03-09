"""이코테 구현 예제4-2 시각
직접셀수있음
"""
h = int(input())

cnt = 0
for i in range(h+1) :
    for k in range (60):
        for j in range (60):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1
print (cnt)