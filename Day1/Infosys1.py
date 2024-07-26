n = int(input())
lev = int(input())
p = []
b = []
a = []
ans = 0
for i in range(n):
   p.append(int(input()))
for j in range(n):
   b.append(int(input()))
for k in range(n):
   a.append([p[k], b[k]])
print(a)
a.sort()
print(a)
for z in a:
   if z[0] > lev:
       break
   lev += z[1]
   ans += 1
print(ans)