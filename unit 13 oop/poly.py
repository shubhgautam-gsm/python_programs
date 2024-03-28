class player_weapon:
    def enfield(self):
        print("pistol")

class p1(player_weapon):
    def enfield(self):
        print("bazuka")
 

class p2(player_weapon):
 pass

# Polymorphic behavior


players = [p1(), p2()]
for player in players:
    player.enfield()


