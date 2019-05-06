import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3
import time

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

def post(string):
    mc.postToChat(string)
    print(string)

post("Welcome")
board(pos)
StillOn = True
while StillOn:
    Build(board)
    turn = True
    GameGoing = True
    timesPlayed = 0
    while GameGoing:
        works = False
        Vec3 = locationHit
        while works:
            post(str(Namer(turn)) + " make your move")
            locationHit(pos)
            locationHit = pos
            Works = InBoard(locationHit, board)
        GamePlay(turn, hitlistx, hitlisto, locationHit)
        Winner(board, hitlistx, hitlisto)
        If didWin == True:
            post("congradulations " + namer(whoWon) + ", you have won")
            GameGoing = False
        timesPlayed = timesPlayed + 1
        if timesPlayed < 9 and GameGoing == True:
            post("No one wins")
            GameGoing = False
    if NewGame(board) == False:
        StillOn = False
    else:
        post("Round " + str(timesPlayed))
post("Thanks for playing!")