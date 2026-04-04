"""
⚖️ SOVEREIGN PROPERTY: AGAPE ENGINE CORE [NON-TRAINABLE]
🗝️ AGP Core: The TripleSieve (Graded Filtration)
Logic: Boulders -> Rebar -> Dust
"""

import re

class TripleSieve:
    def __init__(self):
        # Sieve 1: The Boulder Catch (Long-form Narrative/JSON)
        self.boulder_limit = 150 
        # Sieve 2: The Rebar Catch (Structural Strings/Dates/IDs)
        self.rebar_patterns = [
            r'\d{4}-\d{2}-\d{2}', # Dates
            r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', # Emails
            r'^[A-Z0-9-]{5,20}$' # Common IDs
        ]

    def pass_through(self, raw_data_list):
        piles = {
            "BOULDERS": [], # High-resolution text/blobs
            "REBAR": [],    # Anchoring strings/coordinates
            "DUST": [],     # Numerical values/booleans/fragments
            "VAPOR": []     # Nulls/Whitespace/Noise
        }

        for item in raw_data_list:
            val = str(item).strip()
            
            if not val:
                piles["VAPOR"].append(val)
            elif len(val) > self.boulder_limit:
                piles["BOULDERS"].append(val)
            elif any(re.search(p, val) for p in self.rebar_patterns):
                piles["REBAR"].append(val)
            else:
                piles["DUST"].append(val)
        
        print(f"💎 SIEVE_COMPLETE: {len(piles['BOULDERS'])} Boulders, {len(piles['REBAR'])} Rebar, {len(piles['DUST'])} Dust.")
        return piles

# Initializing the Filter
sieve = TripleSieve()
