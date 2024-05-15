from collections import deque

def pie_pursuit():
    # Input lines for contestants and pies.
    contestants_input = input()
    pies_input = input()

    contestants = deque(int(x) for x in contestants_input.split())
    pies = deque(int(x) for x in pies_input.split())

    while contestants and pies:
        contestant = contestants.popleft()
        pie = pies.pop()

        if contestant >= pie:
            contestant -= pie
            if contestant > 0:
                contestants.append(contestant)
        else:
            pie -= contestant
            if pie == 1 and pies:
                pies[-1] += 1
            elif pie > 1 or not pies:
                pies.appendleft(pie)

    if not pies and not contestants:
        print('We have a champion!')
    elif not pies:  # No pies but we have some contestants left.
        print('We will have to wait for more pies to be baked!')
        print(f"Contestants left: {', '.join(map(str, contestants))}")
    else:  # Pies left but no contestants.
        print('Our contestants need to rest!')
        print(f"Pies left: {', '.join(map(str, pies))}")

pie_pursuit()