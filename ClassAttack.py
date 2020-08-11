class Hero:

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def attackHero(self,who):
        global damage
        damage = self.attack * who.armor/100
        who.health = who.health - damage
        print("{self} attacked {who} with {damage} damage! {who} has {hp} left.".format(self=self.name,who = who.name, damage = damage, hp = who.health))
        who.attackedHero(self)

    def attackedHero(self,who):
        print("{self} has been attacked by {who} with {damage} points! \n".format(self = self.name, who = who.name, damage = damage))

hero1 = Hero("Sniper", 100,50,30)
hero2 = Hero("Tank", 200,10,50)
hero3 = Hero("Mage",50,30,40)
print("COMMENCING\n")

hero1.attackHero(hero2)
hero1.attackHer(hero3)
