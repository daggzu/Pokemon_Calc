class Type:
    
    def __init__(self):
        self.immune_offense = {"default": 0}
        self.super_effective_offense = {"default": 2}
        self.not_very_effective_offense = {"default": 0.5}
        # The rest are neutral (1x)

        self.super_effective_defense = {"default": 2}
        self.not_very_effective_defense = {"default": 0.5}
        self.immune_defense = {"default": 0}
        # The rest are neutral (1x)

    def get_offense_multiplier(self, opponent_types):
        if any(opponent_type in self.immune_offense for opponent_type in opponent_types):
            return 0

        dual_type_super = tuple(opponent_types)
        if dual_type_super in self.super_effective_offense:
            return 4

        dual_type_not_very = tuple(opponent_types)
        if dual_type_not_very in self.not_very_effective_offense:
            return 0.25

        multiplier = 1
        for opponent_type in opponent_types:
            if opponent_type in self.super_effective_offense:
                multiplier *= 2
            elif opponent_type in self.not_very_effective_offense:
                multiplier *= 0.5
        return multiplier

    def get_defense_multiplier(self, move_type_opponent):
        if move_type_opponent in self.immune_defense:
            return 0

        if move_type_opponent in self.super_effective_defense:
            return 2

        if move_type_opponent in self.not_very_effective_defense:
            return 0.25

        return 1  # Default to neutral if none of the conditions are met
    
class WaterType(Type):
    def __init__(self):
        super().__init__()
        self.super_effective_offense.update({"Fire": 2, "Ground": 2})
        self.not_very_effective_offense.update({"Grass": 0.5, "Water": 0.5})
        self.super_effective_defense.update({"Electric": 2,"Grass":2})
        self.not_very_effective_defense.update({"Fire": 0.5, "Water": 0.5})

# Example usage:
water_type = WaterType()
opponent_types = ["Fire", "Ground"]

# Test offense multiplier
print(water_type.get_offense_multiplier(opponent_types))  # Output: 4 (super effective)

# Test defense multiplier
move_type_opponent = "Water"
print(water_type.get_defense_multiplier(move_type_opponent))  # Output: 2 (super effective)
