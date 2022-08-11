import PlayingCards
import pygame

def DrawEvent():
    global theDeck, AScore, BScore
    #Make a new deck if we run out of cards
    if len(theDeck.cards) == 0:
        theDeck = PlayingCards.Deck()
        theDeck.shuffle()
    #draws one card from the deck
    card = theDeck.drawCard()
    #Displays it on the screen
    screen.blit(card.image, (200, 300))
    #Displays the card name
    print(card.name)
    
    """
    PROGRAM under the comments
    Program it to award points to the correct player
    Remember Player A Score is called AScore and Player B is called BScore
    """
    
    
    
    """
    STOP do not program past this point
    """
    
    DrawScore()
    
def DrawScore():
    font = pygame.font.SysFont(None, 48)
    img = font.render("Player A: " + str(AScore), True, BLUE)
    screen.blit(img, (15, 30))
    img = font.render("Player B: " + str(BScore), True, YELLOW)
    screen.blit(img, (600, 30))
    font = pygame.font.SysFont(None, 24)
    img = font.render("Press Space Bar to Play New Card", True, GRAY)
    screen.blit(img, (200, 600))
    
#Makes the screen 800x800, Set up colors    
screen = pygame.display.set_mode((800, 800))
pygame.font.init()
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
#Make Variables for Player A Score and Player B Score
AScore = 0
BScore = 0


#Puts the orange card back in the right center of screen to give illusion that it is the deck
cardBack = pygame.image.load("orangeBack.jpg")
screen.blit(cardBack, (500, 300))
DrawScore()

#Make an Card Deck
theDeck = PlayingCards.Deck()

#Shuffle the Deck
theDeck.shuffle()

#Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(BLACK)
                DrawEvent()
                screen.blit(cardBack, (500, 300))
                
    pygame.display.flip()

pygame.quit()
