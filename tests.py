from PkmnTypes.py import type 

def run_tests():
    # Create an instance of the Type class
    test_type = Type()

    # Test offense multipliers
    assert test_type.get_offense_multiplier(["Fire"]) == 2  # Neutral (default)
    assert test_type.get_offense_multiplier(["Water"]) == 1  # Neutral (default)
    assert test_type.get_offense_multiplier(["Electric"]) == 2  # Super effective
    assert test_type.get_offense_multiplier(["Grass"]) == 0.5  # Not very effective
    assert test_type.get_offense_multiplier(["Ice"]) == 1  # Neutral (default)
    assert test_type.get_offense_multiplier(["Ground", "Fire"]) == 4  # Super effective (dual typing)
    assert test_type.get_offense_multiplier(["Grass", "Electric"]) == 0.25  # Not very effective (dual typing)
    assert test_type.get_offense_multiplier(["Water", "Electric"]) == 0  # Immune (Electric type)
    
    # Test defense multipliers
    assert test_type.get_defense_multiplier(["Fire"]) == 2  # Super effective
    assert test_type.get_defense_multiplier(["Water"]) == 0.5  # Not very effective
    assert test_type.get_defense_multiplier(["Electric"]) == 1  # Neutral (default)
    assert test_type.get_defense_multiplier(["Grass"]) == 2  # Super effective
    assert test_type.get_defense_multiplier(["Ice"]) == 1  # Neutral (default)
    assert test_type.get_defense_multiplier(["Ground", "Fire"]) == 0.25  # Not very effective (dual typing)
    assert test_type.get_defense_multiplier(["Grass", "Electric"]) == 4  # Super effective (dual typing)
    assert test_type.get_defense_multiplier(["Water", "Electric"]) == 0  # Immune (Electric type)

    print("All tests passed!")

# Run the tests
run_tests()
