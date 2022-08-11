import pygame
import os
import random

class newSprite(pygame.sprite.Sprite):
    """
    The newSprite class is a abstract base class from which other sprites are made from
    Adapted from pygame_functions
    """
    def __init__(self, filename, framesX=1, framesY=1):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename)
        self.originalWidth = img.get_width() / framesX
        self.originalHeight = img.get_height() / framesY
        frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
        x = 0
        y=0
        for Column in range(framesY):
            for frameNo in range(framesX):
                frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
                frameSurf.blit(img, (x, y))
                self.images.append(frameSurf.copy())
                x -= self.originalWidth
            y -=self.originalHeight
            x=0

        self.currentImage = 0
        self.image = pygame.Surface.copy(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1
        self.orientation = 0

class Deck(newSprite):
    def __init__(self):
        newSprite.__init__(self,"CardImages.png", 13, 4)
        self.cards = []
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        i = 0
        for suit in suits:
            for value in range(13):
                a_card = Card(self.images[i], suit, value+1)
                i += 1
                self.cards.append(a_card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def drawCard(self):
        if len(self.cards) > 0:
            a_card = self.cards.pop()
            return a_card
        else:
            print("No Cards Left In Deck")
            return None

class Card():
    def __init__(self, image, suit, value):
        self.image = image
        self.suit = suit
        self.value = value
        self.name = str(value) + " of " + str(suit)
        if self.suit == "Clubs" or self.suit == "Spades":
            self.color = "Black"
        else:
            self.color = "Red"
        if self.value == 1:
            self.name = "Ace of " + str(suit)
        if self.value == 13:
            self.name = "King of " + str(suit)
        if self.value == 12:
            self.name = "Queen of " + str(suit)
        if self.value == 11:
            self.name = "Jack of " + str(suit)

def loadImage(fileName, useColorKey=False):
    """
    This function handles file names needed to load images
    Also adapted from pygame_functions
    """
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + fileName + " - Check filename and path?")


"""
#Testing Program
screen = pygame.display.set_mode((800, 800))

a_deck = Deck()
a_deck.shuffle()
x = 0
for card in a_deck.cards:
    screen.blit(card.image, (50+x, 50))
    x += 20
    print(card.color, card.name)
    
drawn_card = a_deck.drawCard()
screen.blit(drawn_card.image, (50, 200))
        
pygame.display.flip()
"""