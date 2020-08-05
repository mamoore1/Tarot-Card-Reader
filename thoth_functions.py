major_arcana_upper = {0:'The Fool', 1:'The Magus', 2:'The Priestess', 3:'The Empress', 4:'The Emperor', 5:'The Hierophant', 6:'The Lovers', 7:'The Chariot', 8:'Adjustment', 9:'The Hermit', 10:'Fortune', 11:'Lust', 12:'The Hanged Man', 13:'Death', 14:'Art', 15:'The Devil', 16:'The Tower', 17:'The Star', 18:'The Moon', 19:'The Sun', 20:'The Aeon', 21:'The Universe'}

major_arcana = []

for i in range(0,22):
    major_arcana.append(major_arcana_upper[i].lower())

#   major_arcana = {key:value for key, value in zip(i, major_arcana[i].lower())}

minor_arcana = ['ace of wands', '2 of wands', '3 of wands', '4 of wands', '5 of wands', '6 of wands', '7 of wands', '8 of wands', '9 of wands', '10 of wands', 'princess of wands', 'prince of wands', 'queen of wands', 'knight of wands', 'ace of cups', '2 of cups', '3 of cups', '4 of cups', '5 of cups', '6 of cups', '7 of cups', '8 of cups', '9 of cups', '10 of cups', 'princess of cups', 'prince of cups', 'queen of cups', 'knight of cups', 'ace of swords', '2 of swords', '3 of swords', '4 of swords', '5 of swords', '6 of swords', '7 of swords', '8 of swords', '9 of swords', '10 of swords', 'princess of swords', 'prince of swords', 'queen of swords', 'knight of swords', 'ace of discs', '2 of discs', '3 of discs', '4 of discs', '5 of discs', '6 of discs', '7 of discs', '8 of discs', '9 of discs', '10 of discs', 'princess of discs', 'prince of discs', 'queen of discs', 'knight of discs']
elemental_trumps = [major_arcana[0], major_arcana[12], major_arcana[20]]
#print(elemental_trumps)

planetary_trumps = [major_arcana[1], major_arcana[2], major_arcana[3], major_arcana[10], major_arcana[16], major_arcana[19], major_arcana[21]]
#print(planetary_trumps)

zodiacal_trumps = []
for i in range(4, 10):
    zodiacal_trumps.append(major_arcana[i])
zodiacal_trumps.append(major_arcana[11])
for i in range(13, 16):
    zodiacal_trumps.append(major_arcana[i])
for i in range(17, 19):
    zodiacal_trumps.append(major_arcana[i])
#print(zodiacal_trumps)

ordered_minor_numbers = []

for i in range (11, 1, -1):
    for item in minor_arcana:
        if str(i) in item:
            ordered_minor_numbers.append(item)
            num = minor_arcana.index(item)
            minor_arcana.pop(num)

ordered_minor_numbers.reverse()


aces = []
twos = ordered_minor_numbers[0:4]
threes = ordered_minor_numbers[4:8]
fours = ordered_minor_numbers[8:12]
fives = ordered_minor_numbers[12:16]
sixes = ordered_minor_numbers[16:20]
sevens = ordered_minor_numbers[20:24]
eights = ordered_minor_numbers[24:28]
nines = ordered_minor_numbers[28:32]
tens = ordered_minor_numbers[32:36]
princesses = []
pqk = []

for card in minor_arcana:
    if 'princess' in card:
        princesses.append(card)
    elif 'ace' in card:
        aces.append(card)
    else:
        pqk.append(card)


tarot_values = {}
tarot_values[2] = twos
tarot_values[3] = threes, elemental_trumps
tarot_values[4] = fours, pqk
tarot_values[5] = fives
tarot_values[6] = sixes
tarot_values[7] = sevens, princesses
tarot_values[8] = eights
tarot_values[9] = nines, planetary_trumps
tarot_values[10] = tens
tarot_values[11] = aces
tarot_values[12] = zodiacal_trumps

#print(tarot_values)

def thoth_value_addition(card_list):
    total = 0
    for item in card_list:
        total += thoth_pairer(item)
    return total

def thoth_pairer(card):
    list_cards = tarot_values.items()
    card = card.lower()
    value = 0
    for item in list_cards:
        for entry in item[1]:
            if entry == card:
                value = item[0]
            else:
                for subentry in entry:
                    if subentry == card:
                        value = item[0]
    return value

#print(thoth_pairer('The Sun'))