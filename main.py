from random import randint
heroName = input("What is your hero's name? ")
health = 200
defense = 0
if heroName == "mcdonalds":
    mcMurderHealth = 10000
else:
    mcMurderHealth = 600
while (mcMurderHealth > 0 and health > 0):
    weapon = 0
    action = int(input("Do you want to Fight(1), Heal(2), or Defend(3) \n"))
    
    if action == "":
        print("You didn't do anythibg to bad")
    elif action == 1 and (heroName == "Jodim" or heroName == "Aldric Eventide" or heroName == "Baiden"):
        weapon = int(input("Bow(1), Sword(2), Lightning attack(3) \n"))
    elif action == 1:
        weapon = int(input("Bow(1), Sword(2) \n"))
    elif action == 2:
        if health > 100:
            health = health+randint(10,20)
        else: 
            health = health+randint(20,30)
        print("You healed and are now at", health, "health")
    elif action == 3:
        "You defended yourself from McMurders next attack and will take 10% damage"

    if weapon == 1:
        print("You shot McMurder with your bow")
        mcMurderHealth = mcMurderHealth - randint(15,25)
        print("McMurder now has", mcMurderHealth, "health remaining")
    elif weapon == 2:
        print("You hit McMurder with your sword")
        mcMurderHealth = mcMurderHealth - randint(25,40)
        print("McMurder now has", mcMurderHealth, "health remaining")
        randomInfluence = randint(1,100)
        if randomInfluence < 21:
            health = health-randomInfluence
            print("McMurder got you with his McLettuce when you tried to hit him with your sword, you are now at", health, "health")
            
    elif weapon == 3 and (heroName == "Jodim" or heroName == "Aldric Eventide" or heroName == "Baiden"):
        print("You summoned the power of nature and called a lighning bolt to strike down McMurder")
        mcMurderHealth = mcMurderHealth - randint(75,125)
        print("McMurder now has", mcMurderHealth, "health remaining")
    mcRandom = randint(1,100)
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
    print("You won, good job!")

