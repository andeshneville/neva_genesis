

from random import*


class Blackjack:
    def __init__(self):
        cardsfilename=open("names_of_cards.txt",'r')
        self.cardnames=[]
        for line in cardsfilename:
            self.cardnames.append(line)
    
    def getcards(self,pos):
        names=[]
        for i in pos:
            names.append(self.cardnames[i])
        return names
    def getcard(self,pos):
        return self.cardnames[pos]
    
    def getCardPoints(self,cards):
        points=0
        reset=0
        for i in cards:
            if i[0]=="A":
                points=points+1
            elif i[0] in ["J","K","Q","B"]:
                points=points+10
            else:
                a=i[:2]
                points=points+ int(a)
        return points

    def ret(self):
        nums=[]
        for i in self.cardnames:
            if i[0]=="0":
                nums.append(i)
        return nums

class Player:
    def __init__(self):
        self.points=0
        self.wins=0

    def getPoints(self):
        return self.points

    def addPoints(self,p):
        self.points=self.points+p
        
    def addWins(self):
        self.wins=self.wins+1
    def getWins(self):
        return self.wins
    def resetPoints(self):
        self.points=0
    
def main():
    card=Blackjack()
    dealer=Player()
    player=Player()
    for i in range(2000):
        play(card,dealer,player)
        a,b=dealer.getPoints(),player.getPoints()
        if a==21 or a<b:
            dealer.addWins()
        else:
            player.addWins()
        dealer.resetPoints()
        player.resetPoints()
    printstats(dealer,player)

def play(cards,dealer,player):
    shufled=shuf()
    drawer="A"
 #   while not isbusted(dealer,player):
    i=0
    while i <= 53 and not isbusted(dealer,player):
        if drawer=="A":
            card=cards.getcard(shufled[i])
            points= CardPoints(card,dealer)
            dealer.addPoints(points)
            drawer="B"
        else:
            card=cards.getcard(shufled[i])
            points= CardPoints(card,player)
            player.addPoints(points)
            drawer="A"
        i=i+1
def CardPoints(i,b):
        if i[0]=="A":
            if 6<= b.getPoints()<=10:
                return 11
            else:
                return 1
        elif i[0] in ["J","K","Q","B"]:
            return 10
        else:
            a=i[:2]
            return int(a)
        
def isbusted(dealer,player):
    return dealer.getPoints()>=21 or player.getPoints()>=21

def shuf():
    b=[]
    while len(b)<53:
        c=randrange(0,53)
        if c not in b:
            b.append(c)
    return b

def printstats(dealer,player):
    a,b=dealer.getWins(),player.getWins()
    n=a+b
    print("Dealer Winnings: {0} games".format(a))
    print("Player Winnings: {0} games".format(b))
    print ("Total Games Played: {0} games".format(n))
    print ("Probability that Dealer will Win {0:.2%}".format(a/n))
    print ("Probability that Player will Win {0:.2%}".format(b/n))



if __name__=='__main__':
    main()   
    #a=Blackjack()
    #print(a.getCardPoints(a.ret()))
