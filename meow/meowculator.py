from meatType import MeatType

class Meowculator:
    def __init__(self):
        self.list_of_meats = []     # list of meatType objects
        self.weight = 0             # total weight

        self.meat_wt = 0            # meat weight
        self.bone_wt = 0            # bone weight
        self.offal_wt = 0           # offal weight

        self.meat_percent = 0       # meat %
        self.bone_percent = 0       # bone %
        self.offal_percent = 0      # offal %

    # Take list of meats and calculate:
    #   total weight
    #   meat:bone:offal ratio
    def meowculate(self):
        print("Meowculate")

        # iterate over list of meats and calculate various weights
        if self.list_of_meats:
            for m in self.list_of_meats:
                self.weight += m.weight
                self.meat_wt += m.calc_meat_wt()
                self.bone_wt += m.calc_bone_wt()
                self.offal_wt += m.calc_offal_wt()

            self.check_ratios()
        else:
            print("No meats added! Please add some meats.")

    # check meat:bone:offal ratios
    def check_ratios(self):
        self.meat_percent = self.meat_wt / self.weight
        self.bone_percent = self.bone_wt / self.weight
        self.offal_percent = self.offal_wt / self.weight
