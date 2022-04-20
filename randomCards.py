from mmap import PAGESIZE
import random
from random import randint
from tracemalloc import start
from mtgsdk import Card
import string 

#get random page to choose existing mana cost 
cardsMana = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
manaRandNum = randint(1, 25)

class randomCards:

    def name():
        name = (''.join(random.choices(string.ascii_lowercase, k=8)))
        return name

    def layout():
        #get random layout type
        layout_list = ["normal", "split", "flip", "double-faced", "token", "plane", "scheme", "phenomenon", "leveler", "vanguard", "aftermath"]
        layout = random.choice(layout_list)
        return layout

    def manaCost():
        manaNum = cardsMana[manaRandNum].mana_cost
        return manaNum

    def cost():
        #get numerical mana value
        cost = random.randint(100, 500)/100
        return cost

    def colors():
        color_list = ["white", "blue", "black", "red", "green"]
        color = random.choice(color_list)
        return color

    def type():
        type_list = ["creature", "land", "instant", "sorcery", "artifact", "enchantment", "planeswalker", "tribal"]
        type = random.choice(type_list)
        return type

    def subtype():
        subtype_list = ["Blood", "Clue", "Contraption", "Equipment", "Food", "Fortification", "Gold", "Treasure", "Vehicle", "Aura", "Cartouche", "Class", "Curse", "Rune", "Saga", "Shrine", "Shard", "Plains", "Island", "Swamp", "Mountain","Forest","Desert", "Gate", "Lair", "Locus", "Urzas", "Mine", "Power-Plant", "Tower"]
        subtype = random.choice(subtype_list)
        return subtype

    def supertype():
        supertypes_list = ["basic", "legendary", "ongoing", "snow", "world"]
        supertype = random.choice(supertypes_list)
        return supertype

    def rarity():
        #get rarity of the card
        rarity_list = ["Common", "Uncommon", "Rare", "Mythic Rare", "Special", "Basic Land"]
        rarity = random.choice(rarity_list)
        return rarity

    def text():
        text_list = ["This is for a Data Structures project!", "This card has unlimited powers!", "This card is the end of your game!"]
        text = random.choice(text_list)
        return text

    def artist():
        #get the artist
        artist = (''.join(random.choices(string.ascii_lowercase, k=8))) + ' ' + (''.join(random.choices(string.ascii_lowercase, k=5)))
        return artist

    def number():
        #get the card's number
        cardsNumber = Card.where(page = randint(1, 3)).where(pageSize=50).all()
        numRandNum = randint(1, 15)
        number = cardsNumber[numRandNum].number
        return number

    def power():
        power = (''.join(random.choices(string.digits, k=2)))
        return power

    def tough():
        tough = (''.join(random.choices(string.digits, k=3)))
        return tough

    def loyalty():
        loyalty = (''.join(random.choices(string.digits, k=2)))
        return loyalty
    
    def border():
        border_list = ["Borderless", "Gold", "Silver", "Holofoil Stamp"]
        border = random.choice(border_list)
        return border

    def hand():
        hand = (''.join(random.choices(string.digits, k=2)))
        return hand

    def life():
        life = (''.join(random.choices(string.digits, k=2)))
        return life

    def date():
        #get the year the card released
        releaseYear = randint(1993, 2022)
        return releaseYear

    def starter():
        #get true or false if released in core box set
        starterBool = ["True", "False"]
        starter = random.choice(starterBool)
        return starter

    def printings():
        #get the set that the card is printed in
        setPrint_list = ["Alpha (Limited Edition)", "Beta (Limited Edition)", "Arabian Nights", "Antiquities", "Legends", "The Dark", "Fallen Empires", "Ice Age", "Chronicles", "Renaissance", "Homelands", "Alliances", "Mirage", "Visions", "Weatherlight", "Tempest", "Stronghold", "Exodus", "Portal Second Age", "Urza's Saga", "Urza's Legacy"]
        print = random.choice(setPrint_list)
        return print

    def OGtext():
        #get the original text
        OGtext = (''.join(random.choices(string.ascii_lowercase, k=8))) + ' ' + (''.join(random.choices(string.ascii_lowercase, k=5)))
        return OGtext

    def OGtype():
        #get the original type
        OGtype = (''.join(random.choices(string.ascii_lowercase, k=8))) 
        return OGtype

    def set():
        set_list = ["Alpha (Limited Edition)", "Beta (Limited Edition)", "Arabian Nights", "Antiquities", "Legends", "The Dark", "Fallen Empires", "Ice Age", "Chronicles", "Renaissance", "Homelands", "Alliances", "Mirage", "Visions", "Weatherlight", "Tempest", "Stronghold", "Exodus", "Portal Second Age", "Urza's Saga", "Urza's Legacy"]
        set = random.choice(set_list)
        return set

    def setName():
        setName_list = ["Alpha (Limited Edition)", "Beta (Limited Edition)", "Arabian Nights", "Antiquities", "Legends", "The Dark", "Fallen Empires", "Ice Age", "Chronicles", "Renaissance", "Homelands", "Alliances", "Mirage", "Visions", "Weatherlight", "Tempest", "Stronghold", "Exodus", "Portal Second Age", "Urza's Saga", "Urza's Legacy"]
        setName = random.choice(setName_list)
        return setName

    def id():
        #get a random card ID 
        id = (''.join(random.choices(string.ascii_lowercase + string.digits, k=8))) + '-' + (''.join(random.choices(string.ascii_lowercase + string.digits, k=4)))
        id = id + '-' + (''.join(random.choices(string.ascii_lowercase + string.digits, k=4))) + '-' +(''.join(random.choices(string.digits, k=4)))
        id = id + '-' + (''.join(random.choices(string.ascii_lowercase + string.digits, k=12))) 
        return id

    def legality():
        #get the legality
        legality_list = ["Legal", "Banned", "Restricted"]
        legality = random.choice(legality_list)
        return legality
