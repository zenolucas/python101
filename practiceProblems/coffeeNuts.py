def ingredients_needed(almonds, hazelnuts, almond_coffee, special_hazel_coffee, mixed_nut_coffee):
    # Code here
    totalNeededAlmonds = 0
    totalNeededHazelnuts = 0
    totalNeededNuts = 0

    # almond_coffee
    for x in range(almond_coffee):
        totalNeededAlmonds += 2

    # special_hazel_coffee
    for x in range(special_hazel_coffee):
        totalNeededHazelnuts += 3

    # mixed_nut_coffee
    for x in range(mixed_nut_coffee):
        totalNeededAlmonds += 1
        totalNeededHazelnuts += 1

    if totalNeededAlmonds > almonds:
        totalNeededNuts += totalNeededAlmonds - almonds

    if totalNeededHazelnuts > hazelnuts:
        totalNeededNuts += totalNeededHazelnuts - hazelnuts

    return totalNeededNuts


# sample input 1
answer = ingredients_needed(4, 2, 1, 1, 1)
print(answer)
