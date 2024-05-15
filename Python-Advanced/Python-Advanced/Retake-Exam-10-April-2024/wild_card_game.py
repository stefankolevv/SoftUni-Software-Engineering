def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []

    # Separate cards into lists.
    for card_info in args:
        if card_info[1] == 'monster':
            monster_cards.append(card_info[0])
        elif card_info[1] == 'spell':
            spell_cards.append(card_info[0])

    for card_name, card_type in kwargs.items():
        if card_type == 'monster':
            monster_cards.append(card_name)
        elif card_type == 'spell':
            spell_cards.append(card_name)

    # Sorting monster cards in descending order, spell cards in an ascending.
    monster_cards.sort(reverse=True)
    spell_cards.sort()

    result = ''
    if monster_cards:
        result += 'Monster cards:\n'
        for card in monster_cards:
            result += f"  ***{card}\n"

    if spell_cards:
        result += 'Spell cards:\n'
        for card in spell_cards:
            result += f"  $$${card}\n"

    return result

# Test codes
print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))