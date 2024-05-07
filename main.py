from random import randint
heroName = input("What is your hero's name? ")
health = 200
if heroName == "mcdonalds":
    mcMurderHealth = 10000
    
else:
    mcMurderHealth = 1000
while (mcMurderHealth > 0 and health > 0):
    weapon = 0
    action = int(input("Do you want to Fight(1), Heal(2), or Defend(3) \n"))
    
    if not(action == (1) or action == (2) or action == (3)):
        print("You didn't do anything, too bad")
    elif action == 1 and (heroName == "Jodim" or heroName == "Aldric Eventide" or heroName == "Baiden"):
        weapon = int(input("Daedalus Stormbow(1), Falcon Blade(2), Lunar Flare(3) \n"))
    elif action == 1:
        weapon = int(input("Daedalus Stormbow(1), Falcon Blade(2) \n"))
    elif action == 2:
        if health > 100:
            randomInfluence = randint(1,100)
            if randint > 85:
                health = health + randint(10,20)
                print("You drank a greater healing potion")
            else:
                print("You drank a lesser healing potion")
            health = health+randint(10,20)
        else: 
            health = health+randint(20,30)
        print("You healed and are now at", health, "health")
    elif action == 3:
        "You prepare to defend yourself from McMurders next attack"

    if weapon == 1:
        print("You shot McMurder with your Daedalus Stormbow")
        mcMurderHealth = mcMurderHealth - randint(15,25)
        print("McMurder now has", mcMurderHealth, "health remaining")
    elif weapon == 2:
        print("You hit McMurder with your Falcon Blade")
        mcMurderHealth = mcMurderHealth - randint(25,40)
        print("McMurder now has", mcMurderHealth, "health remaining")
        randomInfluence = randint(1,100)
        if randomInfluence < 21:
            health = health-randomInfluence
            print("McMurder got you with his McLettuce when you tried to hit him with your Falcon Blade, you are now at", health, "health")
            
    elif weapon == 3 and (heroName == "Jodim" or heroName == "Aldric Eventide" or heroName == "Baiden"):
        print("You summoned the power of the moon and called Lunar Flares to strike down McMurder from the sky")
        mcMurderHealth = mcMurderHealth - randint(75,125)
        print("McMurder now has", mcMurderHealth, "health remaining")
    mcRandom = randint(1,100)
    if action == 3:
        randomInfluence = randint(1,100)
        if randomInfluence > 85:
            print("While defending you bashed McMurder with your shield")
            mcMurderHealth = mcMurderHealth - randint(10,20)
            print("McMurder is now at", mcMurderHealth, "health")
        elif randomInfluence > 15:
            print("You defended yourself against McMurder and took no damage!")
        else:
            print("McMurder used a gooey cheese trap to get past your defense")
            health = health - randint(25,30)
            print("You are now at", health, "health")
    else:
        if mcMurderHealth > 150:
            if mcRandom < 51:
                health = health - randint(10,20)
                print("McMurder threw some McNuggets at you")
                print("You are now at", health, "health")
            elif mcRandom < 61:
                health = health - randint(30,40)
                print("McMurder threw you onto the frying pan")
                print("You are now at", health, "health")
            elif mcRandom < 71:
                health = health + randint(10,20)
                print("McMurder gave you some apples")
                print("The apples healed you and you are now at", health, "health")
            else:
                health = health - randint(15,25)
                print("McMurder jousted with you with some fries")
                print("You are now at", health, "health")
        elif mcMurderHealth > 50: 
            if mcRandom < 26:
                mcMurderHealth = mcMurderHealth + randint(45,55)
                print("McMurder drank some McMilk and is now at ", mcMurderHealth, "health")
            else:
                health = health - randint(10,20)
                print("McMurder threw some McNuggets at you")
                print("You are now at", health, "health")
        elif mcMurderHealth <= 50:
            health = health - randint(40,50)
            mcMurderHealth = -100
            print("McMurder did his final attack, the big mac smash!")
            print("You are now at", health, "health")



if health <= 0:
    print("You died, try again")
elif mcMurderHealth <= 0:
    print("You won, good job", heroName, "!     ")

