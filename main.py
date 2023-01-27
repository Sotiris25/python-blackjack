# Βάλε ΟΛΗ την βιβλιοθήκη random
import random

# =================================================
# Λεξικό το οποίο χρησιμοποιείται για την σύγκριση
# και την μετάφραση των καρτών (π.χ. King > Two)
# =================================================
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11,
}
# =================================================

# Σύμβολα καρτών (Tuple)
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# Αξία καρτών (Tuple) (π.χ. King, Jack)
ranks = (
    'Two', 
    'Three', 
    'Four', 
    'Five', 
    'Six', 
    'Seven', 
    'Eight', 
    'Nine', 
    'Ten', 
    'Jack', 
    'Queen', 
    'King', 
    'Ace'
)

# Δημιουργία κάρτας
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

# Δημιουργία τράπουλας
class Deck:

    def __init__(self):
        
        self.cards = []
        
        for suit in suits:
            for rank in ranks:
                # Βάλε την κάρτα στην λίστα που περιέχει την τράπουλα
                newCard = Card(suit, rank)
                self.cards.append(newCard)
     
    # Εκτύπωση της τράπουλας και όλων των καρτών
    def __str__(self):
        string = ''
        for card in self.cards:
            string += f'{card.__str__()}\n'
        
        return string

    # Εκτύπωση του μήκους της τράπουλας (το πόσα χαρτι΄ά έχει)
    def __len__(self):
        return len(self.cards)

    # Ανακάτεμα της τράπουλας (λίστας) με χρήση της βιβλιοθήκης "random"
    def shuffle(self):
        random.shuffle(self.cards)
        print('The Deck has been successfully shuffled.')
        
    # Πάρε το 1ο χαρτί της τράπουλας
    def deal(self):
        return self.cards.pop()

# Δημιουργία του χεριού του παίχτη
class Hand:
    
    def __init__(self):
        self.currentCards = [] # Η λίστα με τις κάρτες του παίχτη
        self.totalValue = 0 # Το σύνολο της αξίας των καρτών του παίχτη
        self.totalAces = 0 # Πόσους άσους έχει ο παίχτης;
        
    # Μέθοδος που επιτρέπει το χέρι να μαζέβει χαρτιά
    def addCard(self, card):
        # -----------------------------------------
        # Προθέτω την κάρτα στ λίστα με τις κάρτες
        # που κρατάει ο παίχτης
        # -----------------------------------------
        self.currentCards.append(card)
        # Προσθέτω την αξία (value) της κάρτας στο σύνολο
        self.totalValue += values[card.rank] # Το value της κάρτας
        
        # ----------------------------------------------------
        # Η ανομαλία με τους Άσους: (1 ή 11 έχουν τιμή αξίας)
        # ελέγχω πόσους άσους έχει ο παίχτης διότι έχουν είτε
        # 11 είτε 1 ως τιμή αξίας
        # ----------------------------------------------------
        if card.rank == 'Ace':
            self.totalAces += 1
            
    # Μέθοδος που ελέγχει τις τιμές των άσων του παίχτη
    def checkForAces(self):
        
        # ---------------------------------------------------------------
        # Εάν ο παίχτης έχει μεγαλύτερο από 21 και έχει έστω εναν άσο
        # τότε κάνε την αξία του άσου 1 αφαιρόντας 10 από την συνολική
        # αξία του παίχτη.
        # ---------------------------------------------------------------
        if (self.totalValue > 21) and (self.totalAces > 0):
            self.totalValue -= 10
            self.totalAces -= 1

# Κλάσση που περιέχει τα λεφτά του παίχτη
class Chips:

    def __init__(self, total = 1000):
        self.total = total
        self.bet = 0
        
    # Έχασε λεφτά
    def loseBet(self):
        self.total -= self.bet    
    
    # Κέρδισε λεφτά
    def winBet(self):
        self.total += self.bet

# Συνάρτηση που διαβάζει το πόσα λεφτά θα παίξει ο παίχτης
def takeBet(chips):
    bet = int(input('Πόσα λεφτά θες να παίξεις; '))

    # --------------------------------------------------------------------
    # Φίλτρο ελέγχου: 
    # Μην επιτρέψεις τον παίχτη να παίξει περισσότερα λεφτά από όσα έχει
    # ή να παίξει καθόλου λεφτά
    # --------------------------------------------------------------------
    while (bet > chips.total) or (bet <= 0):
        if bet <= 0:
            print('Δεν μπορείς να μην παίξεις καν.')
            
        else:
            print(f'Δεν μπορείς να παίξεις παραπάνω λεφτά από όσα έχεις. Έχεις {chips.total}.')

        bet = int(input('Πόσα λεφτά θες να παίξεις; '))

    # Όρισε το bet (τα λεφτά που θα παίξει)
    chips.bet = bet

# Συνάρτηση που μοιράζει/δίνει χαρτιά στους παίχτες
def giveFirstTwoCards(deck, player, dealer):
    player.addCard(deck.deal())
    dealer.addCard(deck.deal())
    player.addCard(deck.deal())
    dealer.addCard(deck.deal())

# ---------------------------------------------------------------
# Συνάρτηση που εμφανίζει το ένα χαρτί του dealer στον παίχτη 
# αλλά και τα χαρτιά που έχει ο ίδιος ο παίχτης
# ---------------------------------------------------------------
def showCards(player, dealer):
    
   # print('\nDEALER\'S HAND:\nFRST CARD IS HIDDEN')
   # print(dealer.currentCards[-1])
   # 
   # print('\nYOUR HAND')
   # for card in player.currentCards:
   #     print(card)
    
    playerTotalValue = 0
    for card in player.currentCards:
        playerTotalValue += values[card.rank]
    
    print(f'\nPLAYER (YOU): [{playerTotalValue}]')
    
    # Εμφανίζω τις κάρτες του παίχτη 
    #playerStr = ''
    for card in player.currentCards:
        #playerStr += f'{values[card.rank]} + '
        print(f'{card} ({values[card.rank]})')
        
    #playerStr[-1] = '' # βγάλε το '+' από το τέλος
    #print(f'[{playerStr}]') # Εκτύπωσε το σύνολο του παίχτη (την πρόσθεση)
        
    # Εμφανίζω τις κάρτες του dealer
    print(f'\nDEALER: [{values[dealer.currentCards[-1].rank]} + ?]')
    print(f'{dealer.currentCards[-1]} ({values[dealer.currentCards[-1].rank]})')
    print('Other card is hidden')

# Συνάρτηση που ρωτάει και διαβάζει την απάντηση του παίχτη
def hitOrStay(deck, player):
    answer = input('\nHit or Stay? (H / S): ').lower()

    # Φίλτρο για την απάντηση
    while answer not in 'hs':
        print('Please respond with hit or stay.')
        answer = input('Hit or Stay? (H / S): ').lower()
    
    # ---------------------------------------------------------
    # Πάρε το πρώτο στοιχείο της απάντησης πχ αν είναι hskgfg
    # δηλαδή κάτι τυχαίο που ξεκινάει με αυτό
    # ---------------------------------------------------------
    if answer == 'h': # Hit
        player.addCard(deck.deal())
        player.checkForAces()
        return True
        
    else: # Stay
        return False

# Συνάρτηση που ρωτάει για συνέχιση του παιχνιδιού (New game? (Y \ N))
def newGame():
    answer = input('\nDo you want to play again? (Y / N): ').lower()
    
    while answer not in 'yn': # Όσο το answer δεν είναι 'y' ή 'n'
        answer = input('Do you want to play again? (Y / N): ').lower()

    return answer == 'y' # Στείλε στο main program True ή False

# Συνάρτηση που δείχνει όλα τα χαρτιά και των δύο παιχτών
def showAllCards(player, dealer):
    # Εκτύπωσε τα χαρτιά του παίχτη και την αξία τους
    print(f'\nPLAYER HAS: {player.totalValue}')
    print(*player.currentCards, sep = "\n")

    # Εκτύπωσε τα χαρτιά του dealer και την αξία τους
    print(f'\nDEALER HAS: {dealer.totalValue}')
    print(*dealer.currentCards, sep = "\n")

# Win Or Lose Functions (Συναρτήσεις που ελέγχουν ποιός κέρδισε και ποιός έχασε)
def playerBust(chips, player, dealer):
    print('\nPLAYER BUSTED! DEALER WINS!')
    showAllCards(player, dealer)
    chips.loseBet()

def dealerBust(chips, player, dealer):
    print('\nDEALER BUSTED! PLAYER WINS!')
    showAllCards(player, dealer)
    chips.winBet()

def playerWin(chips, player, dealer):
    print(f'\nPlayer wins with a total value of {player.totalValue}!')
    showAllCards(player, dealer)
    chips.winBet()

def dealerWin(chips, player, dealer):
    print(f'\nDealer wins with a total value of {player.totalValue}!')
    showAllCards(player, dealer)
    chips.loseBet()

def push(player, dealer):
    print(f'\nPUSH! Both dealer and player have a total value of {player.totalValue}')
    showAllCards(player, dealer)

# ================================================================
# MAIN PROGRAM
# ================================================================

# Δημιούργησε την τράπουλα και ανακάτεψέ την
newDeck = Deck()
newDeck.shuffle()


# -------------------------------------------------------------
# Δημιούργησε τα λεφτά του παίχτη (Chips)
# Ταυτόχρονα ρώτα τον παίχτη πόσα λεφτά θέλει να παίξει
# Με πόσα λεφτά θα αρχίσει ο παίχτης
# ---------------------------------------------------------------
totalChips = int(input('Πόσα συνολικά λεφτά θέλεις να παίξεις; '))

# Φίλτρο, μην επτρέπεις αρνητικές τιμές
while totalChips <= 0:
    print('Invalid chips!')
    totalChips = int(input('Πόσα λεφτά θέλεις να παίξεις; '))
    
playerChips = Chips(totalChips)

playing = True

while playing:
    
    # Δημιούργησε τον παίχτη και τον dealer
    player = Hand()
    dealer = Hand()

    # GANE BEGINS.

    # Διάβασε τα λεφτά που θα παίξει ο παίχτης
    takeBet(playerChips)

    # Δώσε (μοίρασε) χαρτιά στους παίχτες
    giveFirstTwoCards(newDeck, player, dealer)
    
    # Ξεκίνα το παιχνίδι και περίμενε την απάντηση του παίχτη
    
    # PLAYER PLAYS
    while True:
        showCards(player, dealer)
        playerPlays = hitOrStay(newDeck, player)

        if player.totalValue > 21: # Έχασε ο παίχτης
            playerBust(playerChips, player, dealer)
            break

        if not playerPlays:
            # DEALER PLAYS
            while dealer.totalValue < 17: # Ο dealer φτάνει μέχρι 17 αλλιώς χάνει
                dealer.addCard(newDeck.deal())
                dealer.checkForAces()
    
            # Check For Winner (Βρες ποιός νίκησε και ποιός έχασε)
            if dealer.totalValue > 21: # Έχασε ο dealer (Dealer Busted)
                dealerBust(playerChips, player, dealer)
    
            # Νίκησε ο παίχτης με μεγαλύτερη αξία (value) από τον dealer
            elif dealer.totalValue < player.totalValue:
                playerWin(playerChips, player, dealer)
    
            # Νίκησε ο dealer με μεγαλύτερη αξία (value) από τον παίχτη
            elif dealer.totalValue > player.totalValue:
                dealerWin(playerChips, player, dealer)
    
            # Ισοπαλία (και ο dealer και ο πα΄ίχτης έχουν την ίδια αξία (value))
            else:
                push(player, dealer)

            break

    # Ρώτησε τον παίχτη αν θέλει να ξαναπαίξει
    playing = newGame()

print(f'Thank you for playing! Your total money is {playerChips.total}')
# ================================================================
