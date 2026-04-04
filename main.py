"""
💎 AGAPE ENGINE: AETHEL-SIEVE [CORE IGNITION]
"""

from core.sieves import TripleSieve
from core.centrifuge import DensitySpinner
from core.weaver import KineticWeaver

def run_refinery(mud_data, profession="PSYCHOLOGY"):
    # 1. The Sieve (Filter)
    sieve = TripleSieve()
    piles = sieve.pass_through(mud_data)

    # 2. The Centrifuge (Categorize)
    spinner = DensitySpinner()
    buckets = spinner.analyze_density(piles)

    # 3. The Weaver (Harmonize)
    weaver = KineticWeaver(template_type=profession)
    bedrock = weaver.vibrate_and_align(buckets)

    print("✅ REFINERY_COMPLETE: Data is now Bedrock.")
    return bedrock

if __name__ == "__main__":
    # Example: Your friend's Psychology Study Data (The Mud)
    test_mud = ["Participant_01", "2026-04-05", "5", "4", "3", "NULL", "Strongly Agree"]
    run_refinery(test_mud)
