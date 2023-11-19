class TypeEffectiveness:
    
    def __init__(self):
        self.type_chart = {
            "Normal": {
                "offense": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 2},
                "defense": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1}
            },
            "Fire": {
                "offense": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 0.5, "Ice": 1, "Fighting": 1},
                "defense": {"Normal": 1, "Fire": 1, "Water": 0.5, "Electric": 1, "Grass": 2, "Ice": 2, "Fighting": 1}
            },
            "Water": {
                "offense": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 2, "Grass": 2, "Ice": 1, "Fighting": 1},
                "defense": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 1, "Fighting": 1}
            },
            "Electric": {
                "offense": {"Normal": 1, "Fire": 1, "Water": 0.5, "Electric": 0.5, "Grass": 1, "Ice": 1, "Fighting": 1},
                "defense": {"Normal": 1, "Fire": 1, "Water": 2, "Electric": 1, "Grass": 0.5, "Ice": 1, "Fighting": 1}
            },
            "Grass": {
                "offense": {"Normal": 1, "Fire": 2, "Water": 0.5, "Electric": 1, "Grass": 0.5, "Ice": 2, "Fighting": 1},
                "defense": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1}
            },
            "Ice": {
                "offense": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 1, "Grass": 2, "Ice": 0.5, "Fighting": 2},
                "defense": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 1, "Fighting": 1}
            },
            "Fighting": {
                "offense": {"Normal": 2, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 0.5, "Fighting": 1},
                "defense": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 2}
            },
        }

    def get_multiplier(self, attacking_type, defending_type, interaction_type):
        return self.type_chart.get(attacking_type, {}).get(interaction_type, {}).get(defending_type, 1)
