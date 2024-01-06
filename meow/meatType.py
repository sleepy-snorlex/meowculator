class MeatType:

    # meat:bone:offal should be percentages taken from a pre-filled database
    def __init__(self, w, m, b, o):
        # total weight of meat type
        self.weight = w

        # ratios
        self.meat = m
        self.bone = b
        self.offal = o

    def calc_meat_wt(self):
        return self.weight * self.meat

    def calc_bone_wt(self):
        return self.weight * self.bone

    def calc_offal_wt(self):
        return self.weight * self.offal