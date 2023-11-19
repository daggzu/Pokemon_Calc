class WaterType:
    
    def __init__(self):
        
        self.immune_offense = {}
        
        self.super_effective_offense = {"default": 2, "Fire": 2, "Ground": 2}
        self.not_very_effective_offense = {"default": 0.5, "Grass": 0.5, "water": 0.5}
        # The rest are neutral (1x)

        self.super_effective_defense = {"default": 2, "Electric": 2}
        self.not_very_effective_defense = {"default": 0.5, "Fire": 0.5, "Water": 0.5}
        # The rest are neutral (1x)

    def get_offense_multiplier(self, opponent_types):
        
        if any(opponent_type in self.immune_offense for opponent_type in opponent_types):
            return 0

        dual_type_se = tuple(sorted(opponent_types))
        if dual_type_se in self.super_effective_offense:
            return 4

        dual_type_nve = tuple(sorted(opponent_types))
        if dual_type_nve in self.not_very_effective_offense:
            return 0.25

        for opponent_type in opponent_types:
            if opponent_type in self.super_effective_offense:
                return 2
            elif opponent_type in self.not_very_effective_offense:
                return 0.5

        return 1  # Default to neutral if none of the conditions are met

    def get_defense_multiplier(self, opponent_types):
        
        max_super_effective = max(self.super_effective_defense.get(opponent_type, 1) for opponent_type in opponent_types)
        min_not_very_effective = min(self.not_very_effective_defense.get(opponent_type, 1) for opponent_type in opponent_types)
        
        if max_super_effective > 1:
            return max_super_effective
        elif min_not_very_effective < 1:
            return min_not_very_effective
        else:
            return 1  # Neutral effectiveness
