class AircraftStrategy:
    def execute(self):
        print "travel by Aircraft"

class TrainStrategy:
    def execute(self):
        print "travel by Train"
  
class BicycleStrategy:
    def execute(self):
        print "travel by Bicycle"

class Human:
    def __init__(self, strategy):
        self.strategy = strategy

    def travel(self):
        self.strategy.execute()
       
rich_man = Human(AircraftStrategy())
norm_man = Human(TrainStrategy())
poor_man = Human(BicycleStrategy())
for man in (rich_man, norm_man, poor_man):
    man.travel()
