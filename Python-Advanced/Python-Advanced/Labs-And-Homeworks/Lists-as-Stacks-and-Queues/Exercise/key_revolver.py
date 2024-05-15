price_per_bullet = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = list(map(int, input().split()))
intelligence_value = int(input())

bullets_count = len(bullets)
locks_count = len(locks)
bullets_cost = 0

while bullets_count > 0 and locks_count > 0:
    current_bullet = bullets.pop()
    bullets_count -= 1

    current_lock = locks[0]

    if current_bullet <= current_lock:
        print("Bang!")
        locks.pop(0)
        locks_count -= 1
    else:
        print("Ping!")

    bullets_cost += price_per_bullet

    if bullets_count > 0 and bullets_count % gun_barrel_size == 0:
        print("Reloading!")

money_earned = intelligence_value - bullets_cost

if locks_count == 0:
    print(f"{bullets_count} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {locks_count}")
