rndtable = [0,8,109,220,222,241,149,107,75,248,254,140,16,66,74,21,211,47,80,242,154,27,205,128,161,89,77,36,95,110,85,48,212,140,211,249,22,79,200,50,28,188,52,140,202,120,68,145,62,70,184,190,91,197,152,224,149,104,25,178,252,182,202,182,141,197,4,81,181,242,145,42,39,227,156,198,225,193,219,93,122,175,249,0,175,143,70,239,46,246,163,53,163,109,168,135,2,235,25,92,20,145,138,77,69,166,78,176,173,212,166,113,94,161,41,50,239,49,111,164,70,60,2,37,171,75,136,156,11,56,42,146,138,229,73,146,77,61,98,196,135,106,63,197,195,86,96,203,113,101,170,247,181,113,80,250,108,7,255,237,129,226,79,107,112,166,103,241,24,223,239,120,198,58,60,82,128,3,184,66,143,224,145,224,81,206,163,45,63,90,168,114,59,33,159,95,28,139,123,98,125,196,15,70,194,253,54,14,109,226,71,17,161,93,186,87,244,138,20,52,123,251,26,36,17,46,52,231,232,76,31,221,84,37,216,165,212,106,197,242,98,43,39,175,254,145,190,84,118,222,187,136,120,163,236,249]
rndInx = 0

def roundUp(ammo):
    return 0 if ammo < 0 else ammo
        
def isHit(myHand, opHand):
    if myHand == opHand:
        return 0
    elif myHand == '5' and opHand == '1':
        return -1
    elif myHand == '1' and opHand == '5':
        return 1
    elif myHand == '!':
        if opHand == '!':
            return 0
        elif int(opHand) % 2 == 0:
            return 1
        else:
            return -1
    elif opHand == '!':
        if int(myHand) % 2 == 0:
            return -1
        else:
            return 1
    else:
        return 1 if int(myHand) > int(opHand) else 0 

def canWinOrDraw(hand, opponentsHands):
    for d in opponentsHands:
        if isHit(hand, d) > -1:
            return True
    return False

def getOponentsHands(history):
    fullhands = ['1', '2', '3', '4', '5', '!']
    
    for d in history:
        del fullhands[fullhands.index(d[1])]

    return fullhands 

def sort(hands):
    return hands
    after = copy.deepcopy(hands)

    for i in len(after):
        swapidx = rndtable[rndInx]%len(after)-1
        temp = after[swapidx]
        after[swapidx] = after[i]
        after[i] = temp
        rndInx = rndInx + 1 if rndInx < 255 else 0

    return after

def think(hands, history, old_games):
    rndInx = len(old_games) % 255

    if len(history) > 0: # after first step for this round
        for d in sort(hands):
            if canWinOrDraw(d, getOponentsHands(history)):
                return d

    return hands[roundUp(rndtable[rndInx]%len(hands)-1)]
        


