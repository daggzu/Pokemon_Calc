class Type:
    """A base class representing a generic Pokemon type"""
    
    def __init__(self, name):
        self.name = name
        self.super_effective = {"default": 2}
        self.not_very_effective = {"default": 0.5}
        # Rest are neutral (1x)
        
    def get_multiplier(self, other_type):
        for multiplier_dict in [self.super_effective, self.not_very_effective]:
            multiplier = multiplier_dict.get(other_type)
            if multiplier is not None:
                return multiplier
        # If no match is found, default to neutral (1x)
        return 1
    
    def get_offense_multiplier(self, other_types):
        # Checking if one type is super effective and the other is not very effective
        super_effective_count = sum(1 for other_type in other_types if self.get_multiplier(other_type) == 2)
        not_very_effective_count = sum(1 for other_type in other_types if self.get_multiplier(other_type) == 0.5)
        
        if super_effective_count > 0 and not_very_effective_count > 0:
            return 1  # Neutral effectiveness
        
        # Checking if the dual typing is found twice in the super effective dict
        dual_type_key = tuple(sorted(other_types))
        if dual_type_key in self.super_effective:
            return 4  # 4x effectiveness
        
        # Checking if the dual typing is found twice in the not very effective dict
        if dual_type_key in self.not_very_effective:
            return 0.25  # 1/4 effectiveness (4x resistance)
        
        # For other cases, calculate the overall multiplier by considering each type individually
        multipliers = [self.get_multiplier(other_type) for other_type in other_types]
        return max(multipliers) if max(multipliers) != 0 else 1