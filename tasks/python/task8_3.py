n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
num_of_row = int(input())
summa = 0
res_lst = []

for i in range(n):
    for j in range(m):
        if i == num_of_row:
            continue
        summa += (nums[num_of_row][j]-nums[i][j])**2
    if i != num_of_row:
        res_lst.append(summa)
    summa = 0

print(min(res_lst))
