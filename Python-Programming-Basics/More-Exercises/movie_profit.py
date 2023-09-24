name_film = str(input())
num_days = int(input())
num_tickets = int(input())
price_ticket = float(input())
percent_cinema = int(input())

price_ticket_per_day = num_tickets * price_ticket
profit_period = num_days * price_ticket_per_day
percent_profit = profit_period * percent_cinema / 100
profit_film = profit_period - percent_profit

print(f"The profit from the movie {name_film} is {profit_film:.2f} lv.")
