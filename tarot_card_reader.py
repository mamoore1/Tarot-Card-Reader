import random

from thoth_functions import thoth_pairer


#work in Crowley's actual Thoth thingy

tarot = {0:'The Fool', 1:'The Magus', 2:'The Priestess', 3:'The Empress', 4:'The Emperor', 5:'The Hierophant', 6:'The Lovers', 7:'The Chariot', 8:'Adjustment', 9:'The Hermit', 10:'Fortune', 11:'Lust', 12:'The Hanged Man', 13:'Death', 14:'Art', 15:'The Devil', 16:'The Tower', 17:'The Star', 18:'The Moon', 19:'The Sun', 20:'The Aeon', 21:'The Universe'}
descriptions = ['Know naught!\nAll ways are lawful to innocence.\nPure folly is the key to initiation.\nSilence breaks into rapture.\nBe neither man nor woman, but both in one.\n Be silent, babe in the egg of blue, that thou mayest grow to bear the mlance and graal!\n Wander alone, and sing! In the King\'s Palace his daughter awaits thee', 'The True Self is the meaning of the True Will: know Thyself through thy Way. Calculate well the formula of Thy Way. Create freely; absorb joyously; divide intently; consolidate completely.\nWork thou Omnipotent, Omniscient, Omnipresent, in and for Eternity.', 'Purity is to live only to the highest; and the Highest is All; be thou as Artemis to Pan.\nRead thou in the Book of the Law, and break through the veil of the Virgin.', 'This is the Harmony of the Universe, and Love unites the Will to create with the Understanding of that Creation: understand thou thine own Will.\nLove and let love. Rejoice in every shape of love, and get thy rapture and thy nourishment thereof.', 'Pour water on thyself: thus shalt thou be a Fountain of the Universe. Find thou thyself in every Star. Achieve thou every possibility.', 'Offer thyself Virgin to the Knowledge and Conversation of thine Holy Guardian Angel. All else is a snare.\nBe thou athlete with the eight limbs of Yoga: for without these thou are not disciplined for any fight.', 'The Oracle of the Gods is the Child-Voice of Love in Thine own Soul; hear thou it.\nHeed not the Siren-Voice of Sense, of the Phantom-Voice of Reason, rest in Simplicity, and listen to the Silence.', 'The Issue of the Vulture, Two in One, conveyed; this is the Chariot of Power. TRINC: the last oracle.', 'Balance against each thought its exact opposite. For the Marriage of thse is the Annihilation of Illusion.', 'Wander alone: bearing the Light and Thy Staff. And be the Light so bright that no one seeth thee. Be not moved by aught without or within: keep Silence in all ways.', 'Follow thy Fortune, careless where it lead thee. The axle moveth not: attain thou that.', 'Mitigate Energy with Love; but let Love devour all things.\nWorship the name ---, foursquare, mystic, wonderful, and the name of His House 418.', 'Let not the waters whereon thou journeyest wet thee. And, being come to shore, plant thou the Vine and rejoice without shame.', 'The Universe is Change; every Change is the effect of an Act of Love; all Acts of Love contain Pure Joy. Die daily.\nDeath is the apex of one curve of the snake Life: behold all opposites as necessary complements, and rejoice.', 'Pour thine all freely from the Vase in thy right hand, and lose no drop. Hath not thy left hand a vase?\n Transmute all wholly into the Image of thy Will, bringing each to its true token of Perfection.\nDissolve the Pearl in a Wine-cup; drink, and make manifest the Virtue of that Pearl.', 'With thy right Eye create all for thyself, and with the left accept all that created otherwise.', 'Break down the fortress of thine individual Self, that thy Truth may spring free from the ruins.', 'Use all thine energy to rule thy thought: burn up thy thought as the Phoenix.', 'Let the Illusion of the World pass over theee, unheeded, as thou goest from Midnight to the Morning.', 'Give forth thy light to all without doubt; the clouds and shadows are no matter for thee.\nMake Speech and Silence, Energy and Stillness, twin forms of thy play.', 'Be every Act an Act of Love and Worship. Be every Act the Fiat of a God. Be every Act a Source of Radiant Glory.', 'Treat time and all conditions of Event as Servants of Thy Will, appointed to present the Universe to thee in the form of thy Plan.\nAnd: blessing and worship to the prophet of the lovely Star.']
wand_court_descriptions = {'knight of wands': 'Representing the fiery part of Fire, the moral qualities appropriate to the knight are activity, generosity, fireceness, impetuosity, pride, impulsiveness, swiftness in unpredictable actions. If wrongly energised, he is evil-minded, cruel, bigoted and brutal. He is in either case ill-fitted to carry on his avtion; he has no means of modifying it according to circumstances. If he fails in his first effort, he has no recourse.', 'queen of wands' : 'Representing the watery part of Fire,its fluidity and colour, the Queen\'s characteristics are adaptability, persistent energy, calm authority. She is kindly and generous, but impatient of opposition. She has immense capacity for friendhsip and fo rlove, but always on her own initiative.\n\nHowever, the Queen also has a tendency to brood, come to a wrong decision, and react with great savagery. She may be easily deceived: the she is likely to shew herself stupid, obstinate, tyrannical. She may be quick to take offense, and harbour revenge without good cause. When she misses her bite, she breaks her jaw.', 'prince of wands' : 'Representing the airy part of Fire, with its faculty of expanding and volatising, the Prince\'s qualities are swiftness and strength. He is sometimes inclined to act on impulse, led by external influences, sometimes prey to indecision. He is often violent in the expression of an opinion, although he does not necessarily hold that opinion. He is slow to make up his mind on any subject, but always sees both sides.\n\nWhen this card is badly dignified, the character degenerates. There is great cruelty in him, partly sadistic and partly due to callousness arising from indifference - and, in a sense, laziness! So, too, he may be intolerant, prejudiced and idle - principally because it saves troubles.', 'princess of wands': 'Repesenting the earthy part of Fire, the Princess is extremely individual. She is brilliant and daring. She creates her own beauty by her essential vigour and energy/ In anger and love she is sudden, violent, and implacable. She consumes all that comes into her sphere. She is ambitious and aspiring, full of enthusiasm which is often irrational. She never forgets an injury, and the only quality of patience with which is lies in ambush is avenge. When ill-dignified, she is superficial and theatrical, completely shallow and false, yet without suspecting that she is anything of the sort, as she believes entirely in herself. She is cruel, unreliable, faithless and domineering.'}
cups_court_descriptions = {'knight of cups': 'Representing the fiery part of Water, the Knight is mostly passive. He is graceful, dilettante. He is amiable in a passive way. He is quick to respond to  attraction, and easily becomes enthusiastic under such stimulus: but he is not very enduring. He is exceedingly sensisitive to external influence, but with no material depth in his character.\n\nWhen the card is ill-dignified, he is sensual, idle and untruthful. Yet with all this he possesses an innocence and purity which are the essence of his nature. But he is, on the whole, so superificial that it is hard to reach this depth.', 'queen of cups': 'Representing the watery part of Water, the Queen has an image of extreme purity and beauty, with infinite subtlety; to see the Truth of her is hardly possible, for she reflects the nature of the observer in great perfection.\n\nHer characteristics are principally dreaminess, illusion and tranquility. She is the perfect agent and patient, able to receive and transmit everything without herself affected thereby. If ill-dignified, all these qualities are degraded. Everything that passes through her is refracted and distorted. But, speaking generally, her characteristics depend mostly upon the influences which affect her.', 'prince of cups': 'Representing the airy part of water, the Prince is associated with subtlety, secret violence, and craft. He is intensely secret, an artist in all his ways. On the surface he appears calm and imperturbable, but this is a mask of the most intense passion. He is on the surface susceptible to external influences, but he accepts them only to transmute them to the advantage of his secret designs. He is thus completely without conscience in the ordinary sense of the word, and is therefore usually distrusted by his neighbours. They feel they do not, and can never, understand him. Thus he inspires unreasonable fear. He is in fact perfectly ruthless. He cares intensely for power, wisdom, and his abilities are so immense, he cannot be relied upon to work in harness.', 'princess of cups': 'Representing the earthy part of Water, the Princess is infinitely gracious. All sweetness, all voluptuousness, gentleness, kindness and tenderness are in her character. She lives in the world of Romance, in the perpetual dream of rapture. On a superficial examination she might be thought selfish and indolent, but this is quite a false impression; silently and effortlessly she goes about her work.'}
swords_court_descriptions = {'knight of swords':'Representing the fiery part of Air, the Knight\'s characteristics are activity and skill, subtletly and cleverness. He is fierce, delicate and courageous, but altogether the prey of his idea, which comes to him as an inspiration without reflection.\n\nIf ill-dignified, the vigour in all these qualities being absent, he is incapable of decision or purpose. Any action that he takes is easily brushed aside by opposition. Inadequate violence spells futility.', 'queen of swords': 'Representing the watery part of Air, the Queen is intensely perceptive, a keep observer, a subtle interpreter, an intense individualist, swift and accurate at recording ideas; in action confident, in spirit gracious and just. her movements will be graceful, and her ability in dancing and balancing exceptional.\n\nIf ill-dignified, these qualities will all be turned to unworthy purposes. She will be cruel, sly, deceitful and unreliable; in this way, very dangerous, on account of the superficial beauty and attractiveness which distinguish her.', 'prince of swords': 'representing the airy part of Air, the Prince is purely intellectual. He is full of ideas and designs which tumble over each other. He is a mass of fine ideals unrelated to practical effort. he has all the apparatus of Thought in the highest degree, intensely clever, admirably rational, but unstable of purpose and in reality indifferent even to his own ideas, as knowing that any one of them is just as good as any other. He reduces everything to unreality by removing its substance and transmuting it to an ideal world of ratiocination which is purely formal and out of relation to any facts, even those upon which it is based.', 'princess of swords': 'Representing the earthy part of Air, the character of the Princess is stern and vengeful. Her logic is destructive. She is firm and aggressive, with great practical wisdom and subtlety in material things. She shews great cleverness and dexterity in the management of practical affairs, especially where they are of a controversial nature. She is very adroit in the settlement of controversies.\n\nIf ill-dignified, all these qualities are dispersed; she becomes incoherent, and all her gifts tend to combine to form a species of low cunning whose object is unworthy of the means.'}
discs_court_descriptions = {'knight of discs': 'Representing the fiery part of Earth, he is dull, heavy and preoccupied with material things. they are laborious and patient, but with little intellectual grasp even of matters which concern them most closely. Their success in these is due to instinct, to imitation of Nature. They lack initiative, their fire is the smouldering fire of the process of growth.\n\nIf ill-dignified, the Knight is hopelessly stupid, incapable of foresight even in his own affairs, or of taking an intelligent interest in anything outside them. He is churlish, surly and jealous of what they instinctively realise is the superior state of others; but they have not the courage or intelligence to better themselves.', 'queen of discs': 'Representing the watery part of Earth, the Queen represents passivity in its highest aspect. She is ambitious, but only in useful directions. She possesses immense funds of affection, kindness, and greatness of heart. She is not intellectual, and not particularly inteliigent, but instinct and intuition are more than adequate for her needs.\n\nIf ill-dignified, she is dull, servile, foolish. Life for her is purely mechanical, and she cannot rise, or even seek to rise, above her appointed lot.', 'prince of discs': 'Representing the airy part of Earth, the Prince\'s character is that of great energy brought to bear upon the most solid practical matters. He is energetic and enduring, a capable manager, a steadfast and perserving worker. He is competent, ingenious, thoughtful, cautious, trustworthy, imperturbable; he constantly seeks new uses for common things, and adapts his circumstances to his purposes in a slow, steady, well thought-out plan.\n\nThe Prince is lacking almost entirely in emotion. He is somewhat insensitive, and may appear dull, but only because he makes no effort ot understand ideas which are beyond his scope. If ill-dignified, both the quality and quantity of his characteristics are somewhat degraded.', 'princess of discs':'Representing the earthy part of Earth, the Princess has too many characteristics to ennumerate: she is Womanhood in its ultimate projection. She contains all the characterists of woman, and it would depend entirely upon the influences to which she is subjected whether one or another becomes manifest. In one sense, then, her general reputation will be of bewildering inconsistency. It is rather tlike a lottery wheel from which the extraction of any number does not predict or influence the result of any subsequent operation.'}
lower_tarot_descriptions = {'ace of wands': 'the primordial Energy of Fire: the beginning of action, activities, the "do" in its pure form.', 'ace of cups':'The primordial Energy of Water: the root of feeling, believing, inspiring confidence as it is evoked by a deep inclination from the very beginning.', 'ace of swords':'The primordial Energy of Air: the conscious thought as being the root of thinking, distinguishing, seperating and arranging, so to give a new order to the world around.', 'ace of discs': 'The primordial Energy of Earth: the root of matter as the manifested form of energy to be handled or dealt with; anyway, there is a physical aspect to it, as the quantity or even abundance of its existence represents a certain measurable kind of richness, condition or even status; thus its usual interpretation is that of wealth or the rudimentary state of possessions to be increased.', '2 of wands': 'The Lord of Dominions, representing the energy of Fire in its best and highest form: setting off for action by deliberately planning and scheming the way to go; or even checking the possibilities for ranging.', '2 of cups':'The Lord of Love, representing the energy of Water in its best and highest form: there is a feeling of love and a certain kind of mutual understanding, as well regarded as harmony.', '2 of swords': 'The Lord of Peace, the symbolising balance between ideas: a stalemate or standstill, as nothing is able to cut out each other for it equals to balance.', '2 of discs':'The Lord of Change, symbolising balance in growth: there is a constant flow and change in material or likewise matters, as nothing is to be kept aside, but always return to the flux of matter; so it is like living without having or even possessing anything on one\'s own.', '3 of wands':'The Lord of Virtue, symbolising stability in character: there is efficacy by cooperation and helpful teamwork, as action is based in common intentions or schemes.', '3 of cups':'The Lord of Abundance, representing the idea of love coming to fruition: the reception of the feeling "to be loved by somebody else" and thus returning a corresponding feeling; it is joy as well as healing from the inside.', '3 of swords':'The Lord of Sorrow, representing the idea of division and mutability: distress and grief, as emotions try to overwhelm the conscious thought, and so, embarrassing any reasonable consideration.', '3 of discs':'The Lord of Work, symbolising the crystalisation of forces: the effect and outcome of things done; so there is recognition and appreciation rewarded.','4 of wands':'Completion, symbolising Fire becoming manifest: the accomplishment of forces of energy as a solid foundation for further growth; forces are gathered or bound to form a stable comunity.', '4 of cups':'Luxury, representing the manifestation of water. However, water\'s weakness means that this card is a little unstable: if there is no further satisfaction possible, boredom and vexation will arise, and be taken as a "comforting thrill"; actually this is as well a depressive state of mind, at times unfolding strange and eccentric pre-occupations.', '4 of swords':'Truce, on the lines of "the strong man armed, keeping his house in peace": at first, moved by the restrictions of thought and reason, second pondering about one\'s own possibilities to advance.', '4 of discs':'Power, which dominates and stablises everything through negotiation rather than force: the power of fortune and property accumulated, thus to maintain the means for further stable conditions.', '5 of wands':'Strife, symbolising disturbance in the element of Fire: a struggle to set forth one\'s intentions; maybe even an interruption in activities or doings, which is quite annoying.', '5 of cups':'Disappointment, symbolising a disturbance of ease: usually this is a sad feeling, like one having been betrayed or mistreated, and, what even makes it worse, one cannot see a given reason for.', '5 of swords': 'Defeat, symbolising a quarrel which ends an armed peace: during a faintness or weakening a trouble or quarrel cannot be withstood, as there is nothing spare to fall back on. This disadvantage is only to be equalled by a certain retreat.', '5 of discs':'Worry, symbolising an overthrow of social stability: the loss of goods, things or money, even by an inflation, is a contemporary serious event, as it is hardly possible to preserve some values; but there is no use in looking back, sticking to former conditions, as this only increaases anxiety and trouble.', '6 of wands':'Victory, symbolising the outburst of the energy of Fire: this success is a certain "breakthrough" in pursuing one\'s intentions, but solely depending on how it will be made us of; so, for the moment it is useful to secure the achieved.', '6 of cups': 'Pleasure, symbolising a fertile harmony, one of the best cards in the pack: it is like pleasure in leisure on a festivity or fete, where new acquaintances are made, where loving couples find a way to one another and have fun.', '6 of swords':'Science, symbolising intelligence which has turned away from quarrel and achieved its goal: difficulties are overcome by the development of new and uncommon ideas; in a certain way this can be compared to a kind of "brainstorming", where solutions are found by creative and even spontaneous thinking, leading to new shores.', '6 of discs':'Success, symbolising settling down with the implication of future change: on the one hand it is indicated an exceptional participation from "the flux of money, goods or things" obtainable; on the other hand, this is mainly a single grant or grain.', '7 of wands': 'Valour, symbolising the energy of Fire at its last gasp: although there is a certain will to enforce one\'s intentions, obstacles ahead increase and draw off too much energy, so it is even hard and strenuous to withstand.','7 of cups':'Debauch, representing the sinking into the mire of false pleasure: because of delusions or illusions, one tends to overestimate a moment of fugitive joy.', '7 of swords':'Futility, symbolising an incapability for sustained mental labour: although there is an attempt to rise again or set forth, it lacks a substantial and even attainable aim.', '7 of discs':'Failure, representing the extreme of passivity, no effort, not even a dream: on the one hand, there is waiting for the fruits to be harvested, but on the other hand the time has not come yet for any kind of proceeds.', '8 of wands':'Swiftnes, representing energy in its most exalted and tenuous sense: a swift motion heading towards the aim, intentions carried out at least; also a meeting offering new possibilities.', '8 of cups': 'Indolence, the very apex of unpleasantness. Comparable to a party for which all preparations have been made, but the host has to forgotten to invite the guests - however, this was in some way or other the host\'s own fault: on the one hand turning away from an obvious aim; on the other hand there is no compatible aim recognised yet.', '8 of swords':'Interference, representing the error of being good-natured when good-nature is disastrous, also an element of sheer bad luck: at the moment there is not way to escape from a very restricting and unfortunate situation.', '8 of discs':'Prudence, representing the strength of doing nothing at all in financial matters: negotiations about money are held; these offer a good opportunity for a betterment of the financial situation.', '9 of wands':'Strength, illustrating the idea that "Change is Stability" and that a good defence must be mobile: continuous activity with hardly a moment for a rest; a steady transformation of energy, maybe even exhausting.', '9 of cups':'Happiness, representing good fortune in the sense of complete satiety as a result of luck: indicates deep contentment and satisfaction; justn ear to the attainment of one\'s deepest desire.', '9 of swords':'Cruelty, representing the disruption inherent to Swords raised to the highest power. It is agony of mind. Thought has gone through every possible stage and the conclusion is despair: there is a mood like "no hope left" and a certain temptation to burst out for a violent clash establishing new and concrete facts.', '9 of discs':'Gain, representing a reckoning up of one\'s winnings combined with dull self-satisfaction: contentment and safety based on the solid state of one\'s own possessions; values and valuations are set to a high level - too high?', '10 of wands':'Oppression, representing the use of force overreaching its limits and not knowing when to stop: there is no more development possible in this direction; it is an enforced half, and anyway a premonition to change direction.', '10 of cups':'Satiety, representing the successful pursuit of pleasure leading to the realisation that, having got what one wanted, one did not want it at all: the longing for an ultimate quest is fulfilled - and now leads emptiness behind.', '10 of swords':'Ruin, teaching the lesson that if one goes on fighting long enough, all ends in destruction. However, there is always space for rebuilding: there is definitive disillusionment; but as there is nothing more to lose, another attempt for a new beginning might do as well.', '10 of discs':'Wealth, representing the way in which, once wealth reaches a certain point, it either becomes inert and ceases to be wealth or demands intelligence to be used correctly: reaching one\'s utmost point of wealth leads to a change in attitude and manner; wealth is being transformed into another condition of living.'}
elements_suits = {'fire':'Wands', 'water':'Cups','air':'Swords','earth':'Discs'}
elements_cards = {'fiery':'Knight', 'watery':'Queen', 'airy':'Prince', 'earthy':'Princess'}

#A list of ordinals for use in readings:
ordinals = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']


tarot_suits = ['Wands', 'Cups', 'Swords', 'Discs']
tarot_numbers = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Princess', 'Prince', 'Queen', 'Knight']
tarot_numbers_and_suits = []

#This produces a list consisting of all the possible non-major arcana tarot cards:
for suit in tarot_suits:
    for number in tarot_numbers:
        tarot_numbers_and_suits.append(str(number) + ' of ' + suit)
#print(tarot_numbers_and_suits)


#Produces a list of all the face cards:
major_tarot_cards = []
for suit in tarot_suits:
    for number in tarot_numbers[-4:]:
        major_tarot_cards.append(str(number) + ' of ' + suit)
#print(major_tarot_cards)
    
#Takes all the card names in the tarot list and convert them to lower case, allowing later functions to be case-insensitive
tarot_cards = list(tarot.values())
lower_tarot_cards = []
for card in tarot_cards:
    lower_tarot_cards.append(card.lower())
    
#Makes all the minor arcana cards and produces a list where they are all lower-case
lower_tarot_numbers_and_suits = []
for card in tarot_numbers_and_suits:
    lower_tarot_numbers_and_suits.append(card.lower())

#this adds the major arcana tarot cards to the list of face cards
for card in tarot_cards:
    major_tarot_cards.append(card)

    
#this joins the list of lowercase major arcana cards to the list of lowercase minor arcana cards    
all_lower_tarot = lower_tarot_cards + lower_tarot_numbers_and_suits
#print(all_lower_tarot)

#this combines the lowercase major arcana tarot cards with their descriptions in a dictionary
tarot_descriptions = {key:value for key, value in zip(lower_tarot_cards, descriptions)}

#Combines the Major Arcana dictionary with the dictionaries for the Minor Arcana Suits
complete_lower_tarot_descriptions = {**tarot_descriptions, **wand_court_descriptions, **cups_court_descriptions, **swords_court_descriptions, **discs_court_descriptions, **lower_tarot_descriptions}
#print(complete_lower_tarot_descriptions)

#The first thing displayed to the user, allows them to choose a type of reading
def reading_intro():
    option = input('\n\nWelcome to Mike\'s Tarot Card Reader v1.0! This reader uses Aleister Crowley\'s Thoth Deck, so some cards might be different from what you\'re used to!\n\nWould you like to do a a (3)-card spread, a (10)-card Celtic Cross reading, or a (C)rowley-style reading?\n> ')
    if option.lower() == 'three':
        start_three_reading()
    elif option.lower() == '3':
        start_three_reading()
    elif option.lower() == 'c':
        crowley_reading_intro()
    elif option.lower() == 'ten':
        start_cc()
    elif option.lower() == '10':
        start_cc()
    else:
        print('\n\nPlease type in one of the given options\n')
        return reading_intro()

#Asks whether the user wants to do their three card reading with all cards or only Major Arcana
def start_three_reading():
    type = (input('\n\nWould you like to use (a)ll the cards or (M)ajor Arcana only?\n> ')).lower()
    if type == 'm':
        tarot_reading()
    elif type == 'a':
        all_cards_tarot_reading()
    else:
        print('\n\nPlease choose one of the two types.')
        start_three_reading()
    more_information()
        

#Carries out a three card reading with only Major Arcana
def tarot_reading():
    print('\n\nIn this reading, we will draw three cards which symbolise your past, present and future. Please make sure you have your question firmly in mind.\n')
    input('Press enter to continue.')
    random.shuffle(lower_tarot_cards)
    results = lower_tarot_cards
    #print(results)
    spread = {}
    spread['past'] = results[0].title()
    spread['present'] = results[1].title()
    spread['future'] = results[2].title()
    #print(spread)
    for key, value in spread.items():
        print('\n\nYour ' + key + ' is ' + value + '\n')
        print(tarot_descriptions[spread[key].lower()])
        input('\nPress enter to continue\n')
    print('Your reading is complete!\n')
    
def all_cards_tarot_reading():
    print('\n\nIn this reading, we will draw three cards which symbolise your past, present and future. Please make sure you have your question firmly in mind.\n')
    input('Press enter to continue.')
    random.shuffle(all_lower_tarot)
    results = all_lower_tarot
    #print(results)
    spread = {}
    spread['past'] = results[0].title()
    spread['present'] = results[1].title()
    spread['future'] = results[2].title()
    #print(spread)
    for key, value in spread.items():
        print('\n\nYour ' + key + ' is ' + value + '\n')
        print(complete_lower_tarot_descriptions[spread[key].lower()])
        input('\nPress enter to continue\n')
    print('\nYour reading is complete!\n')

def more_information():
    response = input('\nWould you like another (r)eading? Or would you like to e(x)it?:\n> ')
    if response == 'r':
        reading_intro()
    elif response == 'x':
        print('\n\nFarewell!\n\n')
        exit()
    else:
        print('\n\n' + response.upper() + '\n\n' + complete_lower_tarot_descriptions.get(response.lower(), 'Sorry, that isn\'t a card! Remember to type the article if present!') + '\n')
        more_information()

def crowley_reading_intro():
    response = (input('\n\nIn this style of reading, you first must choose a card to represent yourself as questioner, also known as the querant. In this program, the querant must be either one of the Major Arcana, or a face card from the suits of Wands, Cups, Swords or Disks.\n\nPlease enter the name of your chosen querant. If you aren\'t sure, you can either see a (list) of the querants or take our querant (quiz):\n> ')).lower()
    if response == 'list':
        print('\nThe possible querants are:\n')
        for card in major_tarot_cards:
            print(card)
        querant = str(querant_picker())
        print(querant)
    elif response == 'quiz':
        querant = querant_quiz()
    elif response in all_lower_tarot:
        querant = str(response)
    else:        
        print('\n\nYou must choose either a card from the Major Arcana or a Knight, Queen, Prince or Princess.')
        crowley_reading_intro()
    print('\n\nYou have chosen ' + querant.title() + ' to represent you.')
    response = input('\n\nIs this correct? Make sure you have your question firmly in mind before continuing. (y/n):\n> ')
    if response == 'y':
        crowley_reading(querant)
    elif response == 'n':
        crowley_reading_intro()
    else:
        print('That wasn\'t a \'y\' or an \'n\' was it?\n> ')
        crowley_reading_intro()
    more_information()
    
def querant_picker():
    response = (input('\n\nIf you have chosen a card, type the name of the card. For more information on a card, type (more). To exit, type (x).\n> ')).lower()
    if response == 'more':
        card_information = (input('\n\nPlease type the name of the card you would like information about, or type (x) to return to the card selection menu.\n> ')).lower()
        if card_information == 'x':
            crowley_reading_intro()
        elif card_information in complete_lower_tarot_descriptions.keys():
            print('\n\n' + card_information.upper() + '\n\n' + complete_lower_tarot_descriptions[card_information])
            return querant_picker()
        else:
            print('\n\nSorry, I didn\'t understand your command.')
            return querant_picker()
    elif response == 'x':
        more_information()
    elif response in complete_lower_tarot_descriptions.keys():
        return response
    else:
        print('\n\nSorry, I didn\'t understand your command.')
        return querant_picker()
    
def querant_quiz():
    response1 = (input('\n\nWhich of the four elements do you most identify with?\n> ').lower())
    if response1 in elements_suits.keys():
        response2 = (input('\n\nEach element can be divided into four further aspects, namely Fiery, Watery, Airy and Earthy. Which aspect of ' + response1.title() + ' do you identify with the most?\n> ').lower())
        if response2 in elements_cards.keys():
            print('\n\nYour querant is the ' + elements_cards[response2] + ' of ' + elements_suits[response1] + '.')
            response3 = (input('\n\nDo you want to (use) this querant, would you like to (return) to the querant selection screen, or would you like to (retake) the quiz?\n> ').lower())
            if response3 == 'use':
                return str(elements_cards[response2] + ' of ' + elements_suits[response1]).lower()
            elif response3 == 'retake':
                return querant_quiz()
            elif response3 == 'return':
                crowley_reading_intro()
            else:
                print('Sorry, I didn\'t understand your command')
                querant_quiz()
        else:
            print('Sorry, ' + response2 + ' is not one of the four elements.')
            return querant_quiz()
    else:
        print('Sorry, ' + response1 + ' is not one of the four elements.')
        return querant_quiz()
    
def crowley_reading(querant):
    deck_number = random.sample(range(1, 5), 1)
    #print(deck_number)
    abandon = '\n\nUnfortunately, the reading must be abandoned.'
    question = 'Is your question about {}? (y/n):\n> '
    lower_querant = querant.lower()
    print('\nWe now shuffle the querant back into the deck and divide it into four packs, symbolising the Hebrew letters Y H V H. We then determine which pack the querant is located in. If the querant is in the deck that matches the topic of your question, we can proceed. Otherwise, the reading must be abandoned.')
    if lower_querant in all_lower_tarot:
        if deck_number == [1]:
            print('\nYour Significator, ' + querant.title() + ', is in the Yod pack.\n')
            result = input(question.format('your career'))
            if result == 'y':
                crowley_second_step(querant)
            else:
                print(abandon)
        elif deck_number == [2]:
            print('\nYour Significator, ' + querant.title() + ', is in the He pack.\n')
            result = input(question.format('love, marriage, or pleasure'))
            if result == 'y':
                crowley_second_step(querant)
            else:
                print(abandon)
        elif deck_number == [3]:
            print('\nYour Significator, ' + querant.title() + ', is in the Vau pack.\n')
            result = input(question.format('trouble, scandal, or loss'))
            if result == 'y':
                crowley_second_step(querant)
            else:
                print(abandon)
        elif deck_number == [4]:
            print('\nYour Significator, ' + querant.title() + ', is in the He final pack.\n')
            result = input(question.format('money, goods, or material matters'))
            if result == 'y':
                crowley_second_step(querant)
            else:
                print(abandon)
    else:
        print('That is not a Thoth Tarot Card.')
        crowley_reading_intro()
  
def crowley_second_step(querant):
    random.shuffle(all_lower_tarot)
    lower_querant = querant.lower()
    #print(lower_querant)
    pack = all_lower_tarot[0:19]
    if lower_querant not in pack:
        pack.append(lower_querant)
        random.shuffle(pack)
    else:
        pack.append(all_lower_tarot[19])
    #print(pack)
    crowley_third_step(pack)
    
def crowley_third_step(card_list):
    i = 0
    cards = ''
    while i < len(card_list):
        cards += (card_list[i].title() + ', ')
        i += (thoth_pairer(card_list[i]))
    cards_complete = cards[0:-2]
    print('\n\nYour cards are ' + cards_complete + '. Use these cards to create a story, providing the outline for the answer to your question.')
    lst = cards.lower().split(',')
    #print(lst)
    for card in lst:
        card = card.lower().strip()
        if card in complete_lower_tarot_descriptions.keys():
            print('\n\n' + card.upper() + '\n\n' + complete_lower_tarot_descriptions[card])
            input('\n\nPress enter to continue.\n')
    print('\nYour reading is complete!')
    more_information()

def start_cc():
    print('\n\nIn this reading, we will draw ten cards which each symbolise a different aspect of your answer. Please make sure you have your question firmly in mind.')
    response = input('\nAre you ready? (y/n)?\n> ')
    if response.lower() == 'y':
        celtic_cross()
    elif response.lower() == 'n':
        more_information()
    else:
        print('\n\nPlease enter either \'y\' or \'n\'.')
        start_cc()
        

def celtic_cross():
    random.shuffle(all_lower_tarot)
    results = all_lower_tarot
    #print(results)
    spread = {}
    spread['the present'] = results[0].title()
    spread['the challenge'] = results[1].title()
    spread['the past'] = results[3].title()
    spread['the future'] = results[4].title()
    spread['conscious aim'] = results[5].title()
    spread['unconscious'] = results[6].title()
    spread['advice'] = results[7].title()
    spread['external influence'] = results[8].title()
    spread['hopes and fears'] = results[9].title()
    spread['outcome'] = results[10].title()
    ordinal_spread = {key:value for key, value in zip(spread, ordinals)}
    #print(spread)
    for key, value in spread.items():
        print('\nYour ' + ordinal_spread[key] + ' card, ' + key.title() + ', is the ' + value.lstrip(' The') + ':\n')
        print(complete_lower_tarot_descriptions[spread[key].lower()])
        input('\nPress enter to continue\n')
    print('Your reading is complete!\n')
    more_information()
 
#crowley_second_step('The Universe') 
 
#crowley_reading('7 of swords')


reading_intro()
