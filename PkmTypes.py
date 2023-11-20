class Type:
    def __init__(self):
        self.immune_offense = {"default": 0}
        self.super_effective_offense = {"default": 2}
        self.not_very_effective_offense = {"default": 0.5}
        # The rest are neutral (1x)

        self.super_effective_defense = {"default": 2}
        self.not_very_effective_defense = {"default": 0.5}
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

    def get_defense_multiplier(self, opponent_types):
        dual_type_super = tuple(opponent_types)
        if dual_type_super in self.super_effective_defense:
            return 4

        dual_type_not_very = tuple(opponent_types)
        if dual_type_not_very in self.not_very_effective_defense:
            return 0.25

        multiplier = 1
        for opponent_type in opponent_types:
            if opponent_type in self.super_effective_defense:
                multiplier *= 2
            elif opponent_type in self.not_very_effective_defense:
                multiplier *= 0.5
        return multiplier


class WaterType(Type):
    def __init__(self):
        super().__init__()
        # Customize specific values for WaterType
        self.super_effective_offense.update({"Fire": 2, "Ground": 2})
        self.not_very_effective_offense.update({"Grass": 0.5})
        self.super_effective_defense.update({"Electric": 2})
        self.not_very_effective_defense.update({"Fire": 0.5, "Water": 0.5})


# Example usage:
water_type = WaterType()
print(water_type.get_offense_multiplier(["Fire", "Ground"]))  # Output: 4 (super effective)
print(water_type.get_defense_multiplier(["Fire"]))  # Output: 0.5 (not very effective)
