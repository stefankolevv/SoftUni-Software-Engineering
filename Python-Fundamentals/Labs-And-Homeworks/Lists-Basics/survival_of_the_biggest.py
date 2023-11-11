a = input()
number = int(input())
ll = [int(i) for i in a.split(' ')]

for _ in range(number):
    x = min(ll)
    ll.remove(x)

result = ', '.join(map(str, ll))
print(result)
