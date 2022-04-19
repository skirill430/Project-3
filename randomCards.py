from mmap import PAGESIZE
import random
from random import randint
from tracemalloc import start
from mtgsdk import Card
import string 

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
        #get random page to choose existing mana cost 
        cardsMana = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        manaRandNum = randint(1, 25)
        manaNum = cardsMana[manaRandNum].mana_cost
        return manaNum

    def cost():
        #get random page to choose existing mana cost 
        cardsMana = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        manaRandNum = randint(1, 15)
        #get numerical mana value
        cost = cardsMana[manaRandNum].cmc
        return cost

    def colors():
        cardsColor = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        colorsRandNum = randint(1, 20)
        colors = cardsColor[colorsRandNum].colors  
        return colors

    def colorIdentity(): 
        cardsColor = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        colorsRandNum = randint(1, 20)
        colorIdentity = cardsColor[colorsRandNum].color_identity
        return colorIdentity

    def type():
        cardsType = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        typeRandNum = randint(1, 25)
        type = cardsType[typeRandNum].type
        return type

    def subtype():
        cardsType = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        subtypeRandNum = randint(1, 30)
        subtype = cardsType[subtypeRandNum].subtypes
        return subtype

    def supertype():
        cardsType = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        subtypeRandNum = randint(1, 30)
        supertypes = cardsType[subtypeRandNum].supertypes
        return supertypes

    def rarity():
        #get rarity of the card
        rarity_list = ["Common", "Uncommon", "Rare", "Mythic Rare", "Special", "Basic Land"]
        rarity = random.choice(rarity_list)
        return rarity

    def text():
        #get oracle text of the card and information
        cardsText = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        textRandNum = randint(1, 20)
        text = cardsText[textRandNum].text
        return text
    
    def flavor():
        cardsText = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        flvrRandNum = randint(1, 20)
        flavorTxt = cardsText[flvrRandNum].flavor
        return flavorTxt

    def artist():
        #get the artist
        artist = (''.join(random.choices(string.ascii_lowercase, k=8))) + ' ' + (''.join(random.choices(string.ascii_lowercase, k=5)))
        return artist

    def number():
        #get the card's number
        cardsNumber = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        numRandNum = randint(1, 25)
        number = cardsNumber[numRandNum].number
        return number

    def power():
        cardsNumber = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        #get the power
        powRandNum = randint(1, 25)
        power = cardsNumber[powRandNum].power
        return power

    def tough():
        cardsNumber = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        powRandNum = randint(1, 25)
        tough = cardsNumber[powRandNum].toughness
        return tough

    def loyalty():
        cardsNumber = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        powRandNum = randint(1, 25)
        loyalty = cardsNumber[powRandNum].loyalty
        return loyalty

    def multiverseID():
        #get the multiverse ID of the card
        cardsMulti = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        multRandNum = randint(1, 25)
        multiverseID = cardsMulti[multRandNum].multiverse_id
        return multiverseID
    
    def variations():
        cardsMulti = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        multRandNum = randint(1, 25)
        #get the variations if there exists in the multiverse
        variations = cardsMulti[multRandNum].variations
        return variations

    def watermark():
        cardsDesign = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        designRandNum = randint(1, 25)
        watermark = cardsDesign[designRandNum].watermark
        return watermark
    
    def border():
        cardsDesign = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        designRandNum = randint(1, 25)
        #get the border if it's different than normal
        border = cardsDesign[designRandNum].border

    def timeShifted():
        #return if the card was timeshifted
        cardsVan = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        vanRandNum = randint(1, 25)
        timeShifted = cardsVan[vanRandNum].timeshifted

    def hand():
        cardsVan = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        vanRandNum = randint(1, 25)
        #get max hand size only for Vanguard types
        hand = cardsVan[vanRandNum].hand

    def life():
        cardsVan = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        vanRandNum = randint(1, 25)
        #get life total only for Vanguard types
        life = cardsVan[vanRandNum].life

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
        cardsSet = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        setRandNum = randint(1, 20)
        printings = cardsSet[setRandNum].printings
        return printings

    def OGtext():
        #get the original text
        OGtext = (''.join(random.choices(string.ascii_lowercase, k=8))) + ' ' + (''.join(random.choices(string.ascii_lowercase, k=5)))
        return OGtext

    def OGtype():
        #get the original type
        OGtype = (''.join(random.choices(string.ascii_lowercase, k=8))) 
        return OGtype
    
    def source():
        #get the source only for promo cards 
        cardsSrc = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        srcRandNum = randint(1, 20)
        source = cardsSrc[srcRandNum].source
        return source

    def imageURL():
        cardsMulti = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        multRandNum = randint(1, 25)
        #image for URL only if has multiverse ID
        imageURL = cardsMulti[multRandNum].image_url
        return imageURL

    def set():
        cardsSet = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        setRandNum = randint(1, 20)
        #get the set the card belongs to
        set = cardsSet[setRandNum].set

    def setName():
        cardsSet = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        setRandNum = randint(1, 20)
        setName = cardsSet[setRandNum].set_name

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

    def rulings():
        cardsSet = Card.where(page = randint(1, 1200)).where(pageSize=50).all()
        setRandNum = randint(1, 20)
        #get the ruling information about the card
        rulings = cardsSet[setRandNum].rulings
        return rulings
