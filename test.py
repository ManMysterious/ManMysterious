import random
#-----------------The-global-function-can-be-used-like-a-better-return-statement--------------------
#--------------------------------------Player-Stats-------------------------------------------------
import tkinter

game = tkinter.Tk()
game.geometry('1000x100')
game.configure(bg="white")
game.title("To Be Determined")
game.mainloop()

playerChoice = ""
playerMagicChoice = ""
playerSkillChoice = ""
playerAttack = ""
player = []
playerManaCost = 0
playerDead = "Dead" in player
playerPriority = 0
playerSpellList = ["Frostbite", "Heal", "Light", "Blizzard", "Shine", "Permafrost"]
playerSkillList = ["Frigid Jab", "Wide Sweep", "Light Lance", "Triple Thrust", "Icicle Spear", "Sub-Zero Stab"]
playerDamage = 0
playerHealing = 0

playerHP = 100
playerMaxHP = 100

playerMP = 75
playerMaxMP = 75

playerSP = 80
playerMaxSP = 80

playerSTR = 20
playerBaseSTR = 20

playerDEF = 5
playerBaseDEF = 5

playerSKL = 15
playerBaseSKL = 15

playerMAG = 15
playerBaseMAG = 15

playerRES = 5
playerBaseRES = 5

playerSPD = 15
playerBaseSPD = 15

#----------------------------------------Computer-Stats---------------------------------------------
cpuChoice = random.randint(1,2)
cpuAttack = ""
cpu = []
cpuOneName = "Bandit"
cpuDead = "Dead" in cpu
cpuPriority = 0
cpuDamage = 0
cpuHealing = 0
cpuHP = 120
cpuMaxHP = 120

cpuMP = 0
cpuMaxMP = 0

cpuSP = 75
cpuMaxSP = 75

cpuSTR = 15
cpuBaseSTR = 15

cpuDEF = 10
cpuBaseDEF = 10

cpuSKL = 15
cpuBaseSKL = 15

cpuMAG = 5
cpuBaseMAG = 5

cpuRES = 5
cpuBaseRES = 5

cpuSPD = 20
cpuBaseSPD = 20
#-------------------------------------Misc-Stats----------------------------------------------------
speedOrder = [playerPriority, cpuPriority]
placeHolderInt = 0
placeHolderStr = ""
manaCost = 0
staminaCost = 0
userSTR = 0
userMAG = 0
userSKL = 0
userACC = 90
targetDEF = 0
targetRES = 0
targetSPD = 0
freezeCounter = 0
bleedCounterCPU = 0
bleedCounterPlayer = 0
blindCounter = 0
extraDamage = 0
#=========================================Functions=================================================
#-------------------------------------Menu----------------------------------------------------------
def menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice):
    if(playerMaxHP < playerHP):
        playerHP = 100
    print("")
    print(name, "HP:", playerHP, "MP:", playerMP, "SP:", playerSP)
    print(cpuOneName, "HP:", cpuHP, "MP:", cpuMP, "SP:", cpuSP)
    playerChoice = menuChoice(playerChoice, playerMP)
    return playerChoice
#-------------------------------------Menu-Choice---------------------------------------------------
def menuChoice(playerChoice, playerMP):
    print("")
    print("1. Attack")
    print("2. Magic")
    print("3. Skills")
    playerChoice = input("Choose your action: ")
    while(playerChoice != "1" and playerChoice != "2" and playerChoice != "3"):
        playerChoice = input("Choose your action: ")
    return playerChoice
#------------------------------------------Bash-----------------------------------------------------
def bash(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, targetDEF, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD)
    userCritRate = userSKL - targetDEF
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds > userCritRate):
            playerAttack = "hit"
            cpuAttack = "hit"
            playerDamage = int((userSTR * random.uniform(.8, 1.2)) - targetDEF)
            cpuDamage = int((userSTR * random.uniform(.8, 1.2)) - targetDEF)
        elif(odds < userCritRate):
            playerAttack = "crit"
            cpuAttack = "crit"
            playerDamage = int(((userSTR * random.uniform(.8, 1.2)) * 2) - targetDEF)
            cpuDamage = int(((userSTR * random.uniform(.8, 1.2)) * 2) - targetDEF)
    elif(odds > userAccuracy):
        playerAttack = "miss"
        cpuAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage
#---------------------------------------Player-Magic------------------------------------------------
def playerMagic(playerMagicChoice, playerSpellList, playerMP, manaCost):
    for x in range(len(playerSpellList)):
        print(x + 1, ".", playerSpellList[x], end=" ( Mana Cost: ")
        if(playerSpellList[x] == "Frostbite"):
            manaCost = 5
        if(playerSpellList[x] == "Heal"):
            manaCost = 10
        if(playerSpellList[x] == "Light"):
            manaCost = 5
        if(playerSpellList[x] == "Blizzard"):
            manaCost = 15
        if(playerSpellList[x] == "Shine"):
            manaCost = 10
        if(playerSpellList[x] == "Permafrost"):
            manaCost = 20
        print(manaCost, ")")
    print("0. Back")
    playerMagicChoice = input("Choose your Magic: ")
    if(playerMagicChoice == "1"):
        manaCost = 5
        if(playerMP < manaCost):
            print()
            print("Not enough MP!")
            playerMagicChoice = playerMagic(playerMagicChoice, playerSpellList, playerMP, manaCost)
    if(playerMagicChoice == "2"):
        manaCost = 10
        if(playerMP < manaCost):
            print()
            print("Not enough MP!")
            playerMagicChoice = playerMagic(playerMagicChoice, playerSpellList, playerMP, manaCost)
    if(playerMagicChoice == "3"):
        manaCost = 5
        if(playerMP < manaCost):
            print()
            print("Not enough MP!")
            playerMagicChoice = playerMagic(playerMagicChoice, playerSpellList, playerMP, manaCost)
    if(playerMagicChoice == "4"):
        manaCost = 15
        if(playerMP < manaCost):
            print()
            print("Not enough MP!")
            playerMagicChoice = playerMagic(playerMagicChoice, playerSpellList, playerMP, manaCost)
    if(playerMagicChoice == "5"):
        manaCost = 10
        if(playerMP < manaCost):
            print()
            print("Not enough MP!")
            playerMagicChoice = playerMagic(playerMagicChoice, playerSpellList, playerMP, manaCost)
    if(playerMagicChoice == "6"):
        manaCost = 20
        if(playerMP < manaCost):
            print()
            print("Not enough MP!")
            playerMagicChoice = playerMagic(playerMagicChoice, playerSpellList, playerMP, manaCost)
    if(playerMagicChoice != "1" and playerMagicChoice != "2" and playerMagicChoice != "3" and playerMagicChoice != "4" and playerMagicChoice != "5" and playerMagicChoice != "6" and playerMagicChoice != "0"):
        playerMagicChoice = playerMagic(playerMagicChoice, playerSpellList, playerMP, manaCost)
    return playerMagicChoice
#---------------------------------------Player-Skills-----------------------------------------------
def playerSkills(playerSkillChoice, playerSkillList, playerSP, staminaCost):
    for x in range(len(playerSkillList)):
        print(x + 1, ".", playerSkillList[x], end=" ( Stamina Cost: ")
        if(playerSkillList[x] == "Frigid Jab"):
            staminaCost = 5
        if(playerSkillList[x] == "Wide Sweep"):
            staminaCost = 10
        if(playerSkillList[x] == "Light Lance"):
            staminaCost = 10
        if(playerSkillList[x] == "Triple Thrust"):
            staminaCost = 15
        if(playerSkillList[x] == "Icicle Spear"):
            staminaCost = 20
        if(playerSkillList[x] == "Sub-Zero Stab"):
            staminaCost = 50
        print(staminaCost, ")")
    print("0. Back")
    playerSkillChoice = input("Choose your Skill: ")
    if(playerSkillChoice == "1"):
        staminaCost = 5
        if(playerSP < staminaCost):
            print()
            print("Not enough SP!")
            playerSkillChoice = playerSkills(playerSkillChoice, playerSkillList, playerSP, staminaCost)
    if(playerSkillChoice == "2"):
        staminaCost = 10
        if(playerSP < staminaCost):
            print()
            print("Not enough SP!")
            playerSkillChoice = playerSkills(playerSkillChoice, playerSkillList, playerSP, staminaCost)
    if(playerSkillChoice == "3"):
        staminaCost = 5
        if(playerSP < staminaCost):
            print()
            print("Not enough SP!")
            playerSkillChoice = playerSkills(playerSkillChoice, playerSkillList, playerSP, staminaCost)
    if(playerSkillChoice == "4"):
        staminaCost = 15
        if(playerSP < staminaCost):
            print()
            print("Not enough SP!")
            playerSkillChoice = playerSkills(playerSkillChoice, playerSkillList, playerSP, staminaCost)
    if(playerSkillChoice == "5"):
        staminaCost = 10
        if(playerSP < staminaCost):
            print()
            print("Not enough SP!")
            playerSkillChoice = playerSkills(playerSkillChoice, playerSkillList, playerSP, staminaCost)
    if(playerSkillChoice == "6"):
        staminaCost = 20
        if(playerSP < staminaCost):
            print()
            print("Not enough SP!")
            playerSkillChoice = playerSkills(playerSkillChoice, playerSkillList, playerSP, staminaCost)
    if(playerSkillChoice != "1" and playerSkillChoice != "2" and playerSkillChoice != "3" and playerSkillChoice != "4" and playerSkillChoice != "5" and playerSkillChoice != "6" and playerSkillChoice != "0"):
        playerSkillChoice = playerSkills(playerSkillChoice, playerSkillList, playerSP, staminaCost)
    return playerSkillChoice
#-----------------------------------------FrostBite-------------------------------------------------
def frostbite(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) + 5
    userCritRate = userSKL - targetRES + 4
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds > userCritRate):
            playerAttack = "hit"
            playerDamage = playerDamage = int(((userMAG + 2) * random.uniform(.8, 1.2)) - targetRES)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userMAG + 2) * random.uniform(.8, 1.2)) * 2) - targetRES) 
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage
#-----------------------------------------Blizzard--------------------------------------------------
def blizzard(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD)
    userCritRate = userSKL - targetRES + 7
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds > userCritRate):
            playerAttack = "hit"
            playerDamage = playerDamage = int(((userMAG + 4) * random.uniform(.8, 1.2)) - targetRES)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userMAG + 4) * random.uniform(.8, 1.2)) * 2) - targetRES) 
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage
#-----------------------------------------Permafrost------------------------------------------------
def permafrost(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) - 5
    userCritRate = userSKL - targetRES + 10
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds > userCritRate):
            playerAttack = "hit"
            playerDamage = playerDamage = int(((userMAG + 8) * random.uniform(.8, 1.2)) - targetRES)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userMAG + 8) * random.uniform(.8, 1.2)) * 2) - targetRES) 
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage
#-------------------------------------------Light---------------------------------------------------
def light(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) + 20
    userCritRate = userSKL - targetRES
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds > userCritRate):
            playerAttack = "hit"
            playerDamage = playerDamage = int(((userMAG + 1) * random.uniform(.8, 1.2)) - targetRES)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userMAG + 1) * random.uniform(.8, 1.2)) * 2) - targetRES) 
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage
#-------------------------------------------Shine---------------------------------------------------
def shine(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) + 15
    userCritRate = userSKL - targetRES + 5
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds > userCritRate):
            playerAttack = "hit"
            playerDamage = playerDamage = int(((userMAG + 3) * random.uniform(.8, 1.2)) - targetRES)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userMAG + 3) * random.uniform(.8, 1.2)) * 2) - targetRES) 
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage
#--------------------------------------------Heal---------------------------------------------------
def heal(playerAttack, playerHealing, cpuAttack, cpuHealing, cpuDamage, userMAG):
    odds = random.randint(1, 100)
    userBlessRate = userMAG
    if(odds >= userBlessRate):
        playerAttack = "Heal"
        playerHealing = int((playerMAG + 10) * random.uniform(.8, 1.2))
    elif(odds < userBlessRate):
        playerAttack = "Recover"
        playerHealing = int((playerMAG + 10) * random.uniform(.8, 1.2) * 2)
    return playerAttack, playerHealing, cpuAttack, cpuDamage
#-----------------------------------------Poison-Blade----------------------------------------------
def poisonBlade(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, targetDEF, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) - 5
    userCritRate = userSKL - targetDEF
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds >= userCritRate):
            cpuAttack = "hit"
            cpuDamage = playerDamage = int(((userSTR + 3) * random.uniform(.8, 1.2)) - targetDEF)
        elif(odds < userCritRate):
            cpuAttack = "crit"
            cpuDamage = int((((userSTR + 3) * random.uniform(.8, 1.2)) * 2) - targetDEF)
    elif(odds > userAccuracy):
        cpuAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage
#-----------------------------------------Frigid-Jab------------------------------------------------
def frigidJab(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, userMAG, targetDEF, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD)
    userCritRate = userSKL - targetDEF
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds >= userCritRate):
            playerAttack = "hit"
            playerDamage = int(((userSTR + 3 + (userMAG/5)) * random.uniform(.8, 1.2)) - targetDEF)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userSTR + 3 + (userMAG/5)) * random.uniform(.8, 1.2)) * 2) - targetDEF)
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage
#-----------------------------------------Wide-Sweep------------------------------------------------
def wideSweep(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, targetDEF, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) - 20
    userCritRate = userSKL - targetDEF
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds >= userCritRate):
            playerAttack = "hit"
            playerDamage = playerDamage = int(((userSTR + 5) * random.uniform(.8, 1.2)) - targetDEF)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userSTR + 5) * random.uniform(.8, 1.2)) * 2) - targetDEF)
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage

#-----------------------------------------Light-Lance-----------------------------------------------
def lightLance(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, userMAG, targetDEF, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) + 10
    userCritRate = userSKL - targetDEF
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds >= userCritRate):
            playerAttack = "hit"
            playerDamage = int(((userSTR + 5 + (userMAG/5)) * random.uniform(.8, 1.2)) - targetDEF)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userSTR + 5 + (userMAG/5)) * random.uniform(.8, 1.2)) * 2) - targetDEF)
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage, cpuAttack, cpuDamage
#-----------------------------------------Triple-Thrust---------------------------------------------
def tripleThrust(playerAttack, playerDamage, userSTR, userSKL, targetDEF, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) - 5
    userCritRate = userSKL - targetDEF
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds >= userCritRate):
            playerAttack = "hit"
            playerDamage = int(((userSTR - 1) * random.uniform(.8, 1.2)) - targetDEF)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userSTR - 1) * random.uniform(.8, 1.2)) * 2) - targetDEF)
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage
#-----------------------------------------Icicle-Spear----------------------------------------------
def icicleSpear(playerAttack, playerDamage, userSTR, userSKL, targetDEF, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) - 10
    userCritRate = userSKL - targetDEF
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds >= userCritRate):
            playerAttack = "hit"
            playerDamage = int(((userSTR - 2) * random.uniform(.8, 1.2)) - targetDEF)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userSTR - 2) * random.uniform(.8, 1.2)) * 2) - targetDEF)
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage
#-----------------------------------------SubZero-Stab----------------------------------------------
def subzeroStab(playerAttack, playerDamage, userSTR, userSKL,userMAG, targetDEF, targetSPD, userACC):
    odds = random.randint(1, 100)
    userAccuracy = userACC + (userSKL - targetSPD) - 5
    userCritRate = userSKL - targetDEF + 30
    if(odds <= userAccuracy):
        odds = random.randint(1, 100)
        if(odds >= userCritRate):
            playerAttack = "hit"
            playerDamage = int(((userSTR + 15 + (userMAG/3)) * random.uniform(.8, 1.2)) - targetDEF)
        elif(odds < userCritRate):
            playerAttack = "crit"
            playerDamage = int((((userSTR + 15 + (userMAG/3)) * random.uniform(.8, 1.2)) * 2) - targetDEF)
    elif(odds > userAccuracy):
        playerAttack = "miss"
    return playerAttack, playerDamage
#------------------------------------------Player-Outcome-------------------------------------------
def playerOutcome(playerHP, cpuHP, playerAttack, playerMagicChoice, playerSkillChoice, playerChoice, playerHealing, cpu, playerDamage, freezeCounter, bleedCounterCPU, blindCounter):
    print("")
    if(playerChoice == "1"):
        if(playerAttack == "hit" and playerDead == False):
            print(name, "attacks and did", playerDamage, "damage!")
            cpuHP = cpuHP - playerDamage
        elif(playerAttack == "miss" and playerDead == False):
            print(name, "attack missed!")
        elif(playerAttack == "crit" and playerDead == False):
            print(name, "attacks and did", playerDamage, "damage! Critical Hit!")
            cpuHP = cpuHP - playerDamage
        odds = random.randint(1, 10)
        bleed = ("Bleed" in cpu)
        if(odds >= 9 and (bleed == False) and (playerAttack == "crit" or playerAttack == "hit")):
            print(cpuOneName, "is bleeding! They will lose life for 3 to 5 turns!")
            cpu.append("Bleed")
            bleedCounterCPU = random.randint(3,5)
    #---------------------------------------------
    elif(playerChoice == "2"):
        if(playerMagicChoice == "1"):
            if(playerAttack == "hit" and playerDead == False):
                print(name, "casted a frostbite spell and did", playerDamage, "damage!")
                cpuHP = cpuHP - playerDamage
            elif(playerAttack == "miss" and playerDead == False):
                print(name, "casted a frostbite spell and it missed!")
            elif(playerAttack == "crit" and playerDead == False):
                print(name, "casted a frostbite spell and did", playerDamage, "damage! Critical Hit!")
                cpuHP = cpuHP - playerDamage
            odds = random.randint(1, 10)
            frozen = ("Frozen" in cpu)
            if(odds >= 10 and (frozen == False) and (playerAttack == "crit" or playerAttack == "hit") and playerDead == False):
                print(cpuOneName, "has been Frozen! They can not move on their next 2 turns!")
                cpu.append("Frozen")
                freezeCounter = 2
        #----------------
        elif(playerMagicChoice == "2"):
            if(playerAttack == "Heal" and playerDead == False):
                print("You casted a spell to heal yourself", playerHealing, "damage!")
                playerHP = playerHP + playerHealing
            elif(playerAttack == "Recover" and playerDead == False):
                print("You casted a spell to heal yourself", playerHealing, "damage! Massive Heal!")
                playerHP = playerHP + playerHealing
        #----------------
        elif(playerMagicChoice == "3"):
            if(playerAttack == "hit" and playerDead == False):
                print(name, "casted a light spell and did", playerDamage, "damage!")
                cpuHP = cpuHP - playerDamage
            elif(playerAttack == "miss" and playerDead == False):
                print(name, "casted a light spell and it missed!")
            elif(playerAttack == "crit" and playerDead == False):
                print(name, "casted a light spell and did", playerDamage, "damage! Critical Hit!")
                cpuHP = cpuHP - playerDamage
            odds = random.randint(1, 10)
            blind = ("Blind" in cpu)
            if(odds >= 8 and (blind == False) and (playerAttack == "crit" or playerAttack == "hit") and playerDead == False):
                print(cpuOneName, "has been blinded! Their accuracy has dropped for 2 to 4 turns!")
                cpu.append("Blind")
                blindCounter = random.randint(2,4)
        #----------------
        elif(playerMagicChoice == "4"):
            if(playerAttack == "hit" and playerDead == False):
                print(name, "casted a blizzard spell and did", playerDamage, "damage!")
                cpuHP = cpuHP - playerDamage
            elif(playerAttack == "miss" and playerDead == False):
                print(name, "casted a blizzard spell and it missed!")
            elif(playerAttack == "crit" and playerDead == False):
                print(name, "casted a blizzard spell and did", playerDamage, "damage! Critical Hit!")
                cpuHP = cpuHP - playerDamage
            odds = random.randint(1, 10)
            frozen = ("Frozen" in cpu)
            if(odds >= 9 and (frozen == False) and (playerAttack == "crit" or playerAttack == "hit") and playerDead == False):
                print(cpuOneName, "has been Frozen! They can not move on their next 3 turns!")
                cpu.append("Frozen")
                freezeCounter = 3
        #----------------
        elif(playerMagicChoice == "5"):
            if(playerAttack == "hit" and playerDead == False):
                print(name, "casted a shine spell and did", playerDamage, "damage!")
                cpuHP = cpuHP - playerDamage
            elif(playerAttack == "miss" and playerDead == False):
                print(name, "casted a shine spell and it missed!")
            elif(playerAttack == "crit" and playerDead == False):
                print(name, "casted a shine spell and did", playerDamage, "damage! Critical Hit!")
                cpuHP = cpuHP - playerDamage
            odds = random.randint(1, 10)
            blind = ("Blind" in cpu)
            if(odds >= 7 and (blind == False) and (playerAttack == "crit" or playerAttack == "hit") and playerDead == False):
                print(cpuOneName, "has been blinded! Their accuracy has dropped for 3 to 5 turns!")
                cpu.append("Blind")
                blindCounter = random.randint(3,5)
        #----------------
        elif(playerMagicChoice == "6"):
            if(playerAttack == "hit" and playerDead == False):
                print(name, "casted a permafrost spell and did", playerDamage, "damage!")
                cpuHP = cpuHP - playerDamage
            elif(playerAttack == "miss" and playerDead == False):
                print(name, "casted a permafrost spell and it missed!")
            elif(playerAttack == "crit" and playerDead == False):
                print(name, "casted a permafrost spell and did", playerDamage, "damage! Critical Hit!")
                cpuHP = cpuHP - playerDamage
            odds = random.randint(1, 10)
            frozen = ("Frozen" in cpu)
            if(odds >= 8 and (frozen == False) and (playerAttack == "crit" or playerAttack == "hit") and playerDead == False):
                print(cpuOneName, "has been Frozen! They can not move on their next 4 turns!")
                cpu.append("Frozen")
                freezeCounter = 4
    #---------------------------------------------
    elif(playerChoice == "3"):
        if(playerSkillChoice == "1"):
            if(playerAttack == "hit" and playerDead == False):
                print(name, "used the Jab Stab skill and did", playerDamage, "damage!")
                cpuHP = cpuHP - playerDamage
            elif(playerAttack == "miss" and playerDead == False):
                print(name, "used the Frigid Jab skill and it missed!")
            elif(playerAttack == "crit" and playerDead == False):
                print(name, "used the Frigid Jab skill and did", playerDamage, "damage! Critical Hit!")
                cpuHP = cpuHP - playerDamage
            odds = random.randint(1, 10)
            chilled = ("Chilled" in cpu)
            if(odds >= 8 and (chilled == False) and (playerAttack == "crit" or playerAttack == "hit") and playerDead == False):
                print(cpuOneName, "has been Chilled! Their speed has been reduced!")
                cpu.append("Chilled")
            odds = random.randint(1, 10)
            bleed = ("Bleed" in cpu)
            if(odds >= 8 and (bleed == False) and (playerAttack == "crit" or playerAttack == "hit")):
                print(cpuOneName, "is bleeding! They will lose life for 3 to 5 turns!")
                cpu.append("Bleed")
                bleedCounterCPU = random.randint(3,5)
            #----------------
        elif(playerSkillChoice == "2"):
            if(playerAttack == "hit" and playerDead == False):
                print(name, "used the WideSweep skill to hit everyone in range! It did", playerDamage, "damage!")
                cpuHP = cpuHP - playerDamage
            elif(playerAttack == "miss" and playerDead == False):
                print(name, "used the WideSweep skill to hit everyone in range and it missed!")
            elif(playerAttack == "crit" and playerDead == False):
                print(name, "used the WideSweep skill to hit everyone in range! It did", playerDamage, "damage! Critical Hit!")
                cpuHP = cpuHP - playerDamage
            odds = random.randint(1, 10)
            bleed = ("Bleed" in cpu)
            if(odds >= 8 and (bleed == False) and (playerAttack == "crit" or playerAttack == "hit")):
                print(cpuOneName, "is bleeding! They will lose life for 3 to 5 turns!")
                cpu.append("Bleed")
                bleedCounterCPU = random.randint(3,5)
            #----------------
        elif(playerSkillChoice == "3"):
            if(playerAttack == "hit" and playerDead == False):
                print(name, "used the Light Lance skill and did", playerDamage, "damage!")
                cpuHP = cpuHP - playerDamage
            elif(playerAttack == "miss" and playerDead == False):
                print(name, "used the Light Lance skill and it missed!")
            elif(playerAttack == "crit" and playerDead == False):
                print(name, "used the Light Lance skill and did", playerDamage, "damage! Critical Hit!")
                cpuHP = cpuHP - playerDamage
            odds = random.randint(1, 10)
            explosed = ("Exposed" in cpu)
            if(odds >= 8 and (explosed == False) and (playerAttack == "crit" or playerAttack == "hit") and playerDead == False):
                print(cpuOneName, "has been Exposed! They are more vulnerable to magical attacks now!")
                cpu.append("Exposed")
            odds = random.randint(1, 10)
            bleed = ("Bleed" in cpu)
            if(odds >= 8 and (bleed == False) and (playerAttack == "crit" or playerAttack == "hit")):
                print(cpuOneName, "is bleeding! They will lose life for 3 to 5 turns!")
                cpu.append("Bleed")
                bleedCounterCPU = random.randint(3,5)
            #----------------
        elif(playerSkillChoice == "4"):
            print(name, "started to use the Triple Thrust attack!")
            print("")
            for x in range(3):
                playerAttack, playerDamage = tripleThrust(playerAttack, playerDamage, userSTR, userSKL, targetDEF, targetSPD, userACC)
                if(playerAttack == "hit" and playerDead == False):
                    cpuHP = cpuHP - playerDamage
                    print(name, "did ", playerDamage, "damage!")
                elif(playerAttack == "miss" and playerDead == False):
                    print(name, "missed!")
                elif(playerAttack == "crit" and playerDead == False):
                    print(name, "did", playerDamage, "damage! Critical Hit!")
                    cpuHP = cpuHP - playerDamage
                odds = random.randint(1, 10)
                bleed = ("Bleed" in cpu)
                if(odds >= 8 and (bleed == False) and (playerAttack == "crit" or playerAttack == "hit")):
                    print(cpuOneName, "is bleeding! They will lose life for 3 to 5 turns!")
                    cpu.append("Bleed")
                    bleedCounterCPU = random.randint(3,5)
            print("It was used", x + 1, "consecutive times!")
            #----------------
        elif(playerSkillChoice == "5"):
            print(name, "started to use the Icicle Spear attack!")
            print("")
            for x in range(random.randint(2, 5)):
                playerAttack, playerDamage = icicleSpear(playerAttack, playerDamage, userSTR, userSKL, targetDEF, targetSPD, userACC)
                if(playerAttack == "hit" and playerDead == False):
                    cpuHP = cpuHP - playerDamage
                    print(name, "did ", playerDamage, "damage!")
                elif(playerAttack == "miss" and playerDead == False):
                    print(name, "missed!")
                elif(playerAttack == "crit" and playerDead == False):
                    print(name, "did", playerDamage, "damage! Critical Hit!")
                    cpuHP = cpuHP - playerDamage
                odds = random.randint(1, 10)
                chilled = ("Chilled" in cpu)
                if(odds >= 9 and (chilled == False) and (playerAttack == "crit" or playerAttack == "hit") and playerDead == False):
                    print(cpuOneName, "has been Chilled! Their speed has been reduced!")
                    cpu.append("Chilled")
                odds = random.randint(1, 10)
                bleed = ("Bleed" in cpu)
                if(odds >= 8 and (bleed == False) and (playerAttack == "crit" or playerAttack == "hit")):
                    print(cpuOneName, "is bleeding! They will lose life for 3 to 5 turns!")
                    cpu.append("Bleed")
                    bleedCounterCPU = random.randint(3,5)
            print("It was used", x + 1, "consecutive times!")
        #----------------
        elif(playerSkillChoice == "6"):
            if(playerAttack == "hit" and playerDead == False):
                print(name, "used the Sub-Zero Stab skill and did", playerDamage, "damage!")
                cpuHP = cpuHP - playerDamage
            elif(playerAttack == "miss" and playerDead == False):
                print(name, "used the Sub-Zero Stab skill and it missed!")
            elif(playerAttack == "crit" and playerDead == False):
                print(name, "used the Sub-Zero Stab skill and did", playerDamage, "damage! Critical Hit!")
                cpuHP = cpuHP - playerDamage
            odds = random.randint(1, 10)
            chilled = ("Chilled" in cpu)
            if(odds >= 6 and (chilled == False) and (playerAttack == "crit" or playerAttack == "hit") and playerDead == False):
                print(cpuOneName, "has been Chilled! Their speed has been reduced!")
                cpu.append("Chilled")
            odds = random.randint(1, 10)
            bleed = ("Bleed" in cpu)
            if(odds >= 6 and (bleed == False) and (playerAttack == "crit" or playerAttack == "hit")):
                print(cpuOneName, "is bleeding! They will lose life for 3 to 5 turns!")
                cpu.append("Bleed")
                bleedCounterCPU = random.randint(3,5)
    #---------------------------------------------
    return cpuHP, playerHP, cpu, freezeCounter, bleedCounterCPU, blindCounter
#----------------------------------------Computer-Outcome-------------------------------------------
def enemyOutcome(playerHP, cpuAttack, cpuDamage, player, cpuChoice, bleedCounterPlayer):
    print("")
    if(cpuChoice == 1):
        if(cpuAttack == "hit" and cpuDead == False):
            print(cpuOneName, "attacked! It did", cpuDamage , "damage!")
            playerHP = playerHP - cpuDamage
        elif(cpuAttack == "miss" and cpuDead == False):
            print(cpuOneName, "attacked and missed!")
        elif(cpuAttack == "crit" and cpuDead == False):
            print(cpuOneName, "attacked! It did", cpuDamage , "damage! Critical Hit!")
            playerHP = playerHP - cpuDamage
        odds = random.randint(1, 10)
        bleed = ("Bleed" in player)
        if(odds >= 9 and (bleed == False) and (cpuAttack == "crit" or cpuAttack == "hit")):
            print(name, "is bleeding! They will lose life for 3 to 5 turns!")
            player.append("Bleed")
            bleedCounterPlayer = random.randint(3,5)
    elif(cpuChoice == 2):
        if(cpuAttack == "hit" and cpuDead == False):
            print(cpuOneName, "attacked with a poisoned blade! It did", cpuDamage , "damage!")
            playerHP = playerHP - cpuDamage
        elif(cpuAttack == "miss" and cpuDead == False):
            print(cpuOneName, "attacked with a poisoned blade and missed!")
        elif(cpuAttack == "crit" and cpuDead == False):
            print(cpuOneName, "attacked with a poisoned blade! It did", cpuDamage , "damage! Critical Hit!")
            playerHP = playerHP - cpuDamage
        odds = random.randint(1, 10)
        poison = ("Poisoned" in player)
        if(odds >= 8 and (poison == False) and (cpuAttack == "crit" or cpuAttack == "hit") and cpuDead == False):
            print(name, "has been Poisoned! They will lose life every turn!")
            player.append("Poisoned")
        odds = random.randint(1, 10)
        bleed = ("Bleed" in player)
        if(odds >= 8 and (bleed == False) and (cpuAttack == "crit" or cpuAttack == "hit") and cpuDead == False):
            print(name, "his bleeding! They will lose life for 3 to 5 turns!")
            player.append("Bleed")
            bleedCounterPlayer = random.randint(3,5)
    return playerHP, player, bleedCounterPlayer
#-------------------------------------Dead-Check-Player---------------------------------------------
def checkingPlayerDead(playerHP, player):
    if(playerHP <= 0 and playerDead == False):
        print("You have fallen!")
        player.append("Dead")
    return player
#-----------------------------------------------Dead-Check-Computer---------------------------------
def checkingCPUDead(cpuHP, cpu):
    if(cpuHP <= 0 and cpuDead == False):
        print("The", cpuOneName, "has fallen!")
        cpu.append("Dead")
    return cpu
#--------------------------------------------Outcome------------------------------------------------
def outcome(player, cpu):
    if(playerDead == True):
        print("Uh oh, looks like you lost. The bandit stole all your goods...and your life...")
    if(cpuDead == True):
        print("You won! That outta teach em a lesson...")
#============================================Game===================================================
name = input("Enter your name here: ")
print("You come face to face with a bandit...")
while(playerDead == False and cpuDead == False):
    playerChoice = ""
    playerMagicChoice = ""
    
    playerSkillChoice = ""
    cpuChoice = 0
    print("")
    playerChoice = menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
#---------------------------------------------------------------------------------------------------
    if(playerChoice == "1" and (playerMagicChoice != "0" and playerSkillChoice != "0")):
        userSTR = playerSTR
        userSKL = playerSKL
        targetDEF = cpuDEF
        targetSPD = cpuSPD
        userACC = 90
        playerAttack, playerDamage, placeHolderStr, placeHolderInt = bash(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, targetDEF, targetSPD, userACC)
    elif(playerChoice == "2" and (playerMagicChoice != "0" and playerSkillChoice != "0")):
        userMAG = playerMAG
        userSKL = playerSKL
        targetRES = cpuRES
        targetSPD = cpuSPD
        userACC = 90
        playerMagicChoice = playerMagic(playerMagicChoice,playerSpellList, playerMP, manaCost)
        if(playerMagicChoice == "1"):
            playerAttack, playerDamage, placeHolderStr, placeHolderInt = frostbite(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC)
            playerMP = playerMP - 5
        elif(playerMagicChoice == "2"):
            playerAttack, playerHealing, placeHolderStr, placeHolderInt = heal(playerAttack, playerHealing, cpuAttack, cpuHealing, cpuDamage, userMAG)
            playerMP = playerMP - 10
        elif(playerMagicChoice == "3"):
            playerAttack, playerDamage, placeHolderStr, placeHolderInt = light(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC)
            playerMP = playerMP - 5
        elif(playerMagicChoice == "4"):
            playerAttack, playerDamage, placeHolderStr, placeHolderInt = blizzard(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC)
            playerMP = playerMP - 15
        elif(playerMagicChoice == "5"):
            playerAttack, playerDamage, placeHolderStr, placeHolderInt = shine(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC)
            playerMP = playerMP - 5
        elif(playerMagicChoice == "6"):
            playerAttack, playerDamage, placeHolderStr, placeHolderInt = permafrost(playerAttack, playerDamage, cpuAttack, cpuDamage, userMAG, userSKL, targetRES, targetSPD, userACC)
            playerMP = playerMP - 15
    elif(playerChoice == "3" and (playerMagicChoice != "0" and playerSkillChoice != "0")):
        userSTR = playerSTR
        userSKL = playerSKL
        userMAG = playerMAG
        targetDEF = cpuDEF
        targetSPD = cpuSPD
        userACC = 90
        playerSkillChoice = playerSkills(playerSkillChoice, playerSkillList, playerSP, staminaCost)
        if(playerSkillChoice == "1"):
            playerAttack, playerDamage, placeHolderStr, placeHolderInt = frigidJab(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, userMAG, targetDEF, targetSPD, userACC)
            playerSP = playerSP - 5
        elif(playerSkillChoice == "2"):
            playerAttack, playerDamage, placeHolderStr, placeHolderInt = wideSweep(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, targetDEF, targetSPD, userACC)
            playerSP = playerSP - 10
        elif(playerSkillChoice == "3"):
            playerAttack, playerDamage, placeHolderStr, placeHolderInt = lightLance(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, userMAG, targetDEF, targetSPD, userACC)
            playerSP = playerSP - 10
        elif(playerSkillChoice == "4"):
            playerSP = playerSP - 15
        elif(playerSkillChoice == "5"):
            playerSP = playerSP - 20
        elif(playerSkillChoice == "6"):
            playerAttack, playerDamage = subzeroStab(playerAttack, playerDamage, userSTR, userSKL,userMAG, targetDEF, targetSPD, userACC)
            playerSP = playerSP - 50
    elif(playerMagicChoice == "0"):
        menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
#---------------------------------------------------------------------------------------------------
    if(playerMagicChoice != "0" and playerSkillChoice != "0"):
        if("Blind" in cpu and (playerDead == False and cpuDead == False)):
            userACC = 60
        else:
            userACC = 90
        userSTR = cpuSTR
        userSKL = cpuSKL
        targetDEF = playerDEF
        targetSPD = playerSPD
        cpuChoice = random.randint(1,2)
        if(cpuChoice == 1):
            placeHolderStr, placeHolderInt, cpuAttack, cpuDamage = bash(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, targetDEF, targetSPD, userACC)
        elif(cpuChoice == 2):
            if(cpuSP >= 10):
                placeHolderStr, placeHolderInt, cpuAttack, cpuDamage = poisonBlade(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, targetDEF, targetSPD, userACC)
                cpuSP = cpuSP - 10
            elif(cpuSP < 10):
                placeHolderStr, placeHolderInt, cpuAttack, cpuDamage = bash(playerAttack, playerDamage, cpuAttack, cpuDamage, userSTR, userSKL, targetDEF, targetSPD, userACC)
#---------------------------------------------------------------------------------------------------
    if("Chilled" in cpu):
        cpuSPD = int(cpuBaseSPD * .75)
    if("Exposed" in cpu):
        cpuRES = int(cpuBaseRES * .75)
    playerPriority = int(playerSPD * random.uniform(.8, 1.2))
    cpuPriority = int(cpuSPD * random.uniform(.8, 1.2))
    while(playerPriority == cpuPriority):
        playerPriority = int(playerSPD * random.uniform(.8, 1.2))
        cpuPriority = int(cpuSPD * random.uniform(.8, 1.2))
    speedOrder = [playerPriority, cpuPriority]
    speedOrder.sort()
    speedOrder.reverse()
    for x in speedOrder:
        if(x == playerPriority):
            cpuHP, playerHP, cpu, freezeCounter, bleedCounterCPU, blindCounter = playerOutcome(playerHP, cpuHP, playerAttack, playerMagicChoice, playerSkillChoice, playerChoice, playerHealing, cpu, playerDamage, freezeCounter, bleedCounterCPU, blindCounter)
            player = checkingPlayerDead(playerHP, player)
            cpu = checkingCPUDead(cpuHP, cpu)
            playerDead = "Dead" in player
            cpuDead = "Dead" in cpu
        if(x == cpuPriority):
            if("Frozen" in cpu):
                print("")
                print(cpuOneName, "is frozen and cannot move!")
                freezeCounter = freezeCounter - 1
                if(freezeCounter == 0):
                    cpu.remove("Frozen")
                    print(cpuOneName, "has been thawed!")
            else:
                playerHP, player, bleedCounterPlayer = enemyOutcome(playerHP, cpuAttack, cpuDamage, player, cpuChoice, bleedCounterPlayer)
                player = checkingPlayerDead(playerHP, player)
                cpu = checkingCPUDead(cpuHP, cpu)
                playerDead = "Dead" in player
                cpuDead = "Dead" in cpu
    if("Poisoned" in player and (playerDead == False and cpuDead == False) and (playerMagicChoice != "0" and playerSkillChoice != "0")):
        print("")
        extraDamage = random.randint(5,10)
        print(name, "took", extraDamage, "poison damage!")
        playerHP = playerHP - extraDamage
        playerSP = playerSP - extraDamage
        player = checkingPlayerDead(playerHP, player)
        playerDead = "Dead" in player
    if("Bleed" in player and (playerDead == False and cpuDead == False) and (playerMagicChoice != "0" and playerSkillChoice != "0")):
        print("")
        extraDamage = random.randint(1,3)
        print(name, "took", extraDamage, "bleeding damage!")
        playerHP = playerHP - extraDamage
        player = checkingPlayerDead(playerHP, player)
        playerDead = "Dead" in player
        bleedCounterPlayer = bleedCounterPlayer - 1
        if(bleedCounterPlayer == 0):
            player.remove("Bleed")
            print(name, "has stopped bleeding!")
    if("Bleed" in cpu and (playerDead == False and cpuDead == False) and (playerMagicChoice != "0" and playerSkillChoice != "0")):
        print("")
        extraDamage = random.randint(1,2)
        print(cpuOneName, "took", extraDamage, "bleeding damage!")
        playerHP = playerHP - extraDamage
        cpu = checkingCPUDead(cpuHP, cpu)
        cpuDead = "Dead" in cpu
        bleedCounterCPU = bleedCounterCPU - 1
        if(bleedCounterCPU == 0):
            cpu.remove("Bleed")
            print(cpuOneName, "has stopped bleeding!")
    if("Blind" in cpu and (playerDead == False and cpuDead == False) and (playerMagicChoice != "0" and playerSkillChoice != "0")):
        blindCounter = blindCounter - 1
        if(blindCounter == 0):
            print(cpuOneName, "can see clearly again!")
    if(playerMP < 0):
        playerMP = 0
    if(playerSP < 0):
        playerSP = 0
#---------------------------------------------------------------------------------------------------
outcome(player, cpu)


