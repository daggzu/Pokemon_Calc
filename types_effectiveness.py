class TypeEffectiveness:
    
    def __init__(self):
        
        self.type_chart = {
            "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1},
            "Fire": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 0.5},
            "Water": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 2, "Grass": 2},
            "Electric": {"Normal": 1, "Fire": 1, "Water": 0.5, "Electric": 0.5, "Grass": 1},
            "Grass": {"Normal": 1, "Fire": 2, "Water": 0.5, "Electric": 1, "Grass": 0.5},
            "Ice": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 1, "Grass": 2},
            "Fighting": {"Normal": 2, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 0.5},
        }

    def get_multiplier(self, attacking_type, defending_type):
        return self.type_chart.get(attacking_type, {}).get(defending_type, 1)
