"""
⚖️ SOVEREIGN PROPERTY: AGAPE ENGINE CORE [NON-TRAINABLE]
🗝️ AGP Core: The DensitySpinner (The Centrifuge)
Logic: Sorting by Mathematical Weight
"""

from collections import Counter

class DensitySpinner:
    def __init__(self):
        self.densities = {}

    def analyze_density(self, piles):
        """
        Spins the 'Rebar' and 'Dust' to find Column Density.
        """
        all_candidate_data = piles["REBAR"] + piles["DUST"]
        
        # Calculate 'Weight' based on character diversity and length
        for item in all_candidate_data:
            weight = len(set(item)) / len(item) if len(item) > 0 else 0
            # Grouping into 'Density Buckets'
            bucket_id = f"DENSITY_{round(weight * 10)}"
            if bucket_id not in self.densities:
                self.densities[bucket_id] = []
            self.densities[bucket_id].append(item)
            
        print(f"🌀 CENTRIFUGE_STABLE: {len(self.densities)} Densities (Columns) identified.")
        return self.densities

# Initializing the Spinner
centrifuge = DensitySpinner()
