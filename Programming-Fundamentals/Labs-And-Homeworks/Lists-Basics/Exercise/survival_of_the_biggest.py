#numbers_string = input().split()
#numbers = 0

#for number in numbers_string:
#    numbers.append(number)

#remover = int(input())

#for _ in range(remover):
#    numbers.remove(min(numbers))

#print(numbers)

a = input()
number = int(input())
ll = [int(i) for i in a.split(' ')]

for _ in range(number):
    x = min(ll)
    ll.remove(x)

result = ', '.join(map(str, ll))
print(result)