class Musician(object):
    def __init__(self, sounds, name):
        self.sounds = sounds
        self.name = name

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self, name):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"], name)
        self.type = 'bassist'

class Guitarist(Musician):
    def __init__(self, name):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"], name)
        self.type = 'guitarist'

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self, name):
        # Call the __init__ method of the parent class
        super().__init__(['solo', 'count to four', 'spontaneously combust'], name)
        self.type = 'drummer'
        self.counted_time = False
        
    def count_time(self):
        self.counted_time = True
         
class Band(object):
    def __init__(self):
        self.band = []
    
    def hire(self, musician):
        self.band.append(musician)
    
    def fire(self, musician):
        for member in self.band:
            if member.name == musician:
                self.band.remove(member)
    
    def count(self):
        print(len(self.band))
        
    def list(self):
        for member in self.band:
            print(member.name, '-', member.type)
            
    def solo(self, soloist):
        okay_to_solo = False
        for member in self.band:
            if (member.type == 'drummer') and (member.counted_time):
                okay_to_solo = True
        if okay_to_solo:
            for member in self.band:
                if member.name == soloist:
                   member.solo(6)
                
nigel = Guitarist('Nigel')
griffin = Drummer('Griffin')
basso = Bassist('Basso')

funky_bunch = Band()
funky_bunch.hire(nigel)
funky_bunch.hire(griffin)
funky_bunch.hire(basso)
funky_bunch.count()
funky_bunch.list()
griffin.count_time()
funky_bunch.solo('Nigel')
funky_bunch.fire('Nigel')
funky_bunch.list()