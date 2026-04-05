"""
💎 AGAPE ENGINE: AETHEL-SIEVE [CORE IGNITION]
Logic: Intake -> Sieve -> Centrifuge -> Weaver -> Monitor
"""

from core.sieves import TripleSieve
from core.centrifuge import DensitySpinner
from core.weaver import KineticWeaver
from output.bedrock_monitor import BedrockMonitor

def run_refinery(mud_data, profession="PSYCHOLOGY"):
    # 1. The Sieve (Filter: Boulders/Rebar/Dust)
    sieve = TripleSieve()
    piles = sieve.pass_through(mud_data)

    # 2. The Centrifuge (Categorize by Density)
    spinner = DensitySpinner()
    buckets = spinner.analyze_density(piles)

    # 3. The Weaver (Harmonize & Triangulate)
    # Note: Returns a list of 'Bedrock' pixels with IDs
    weaver = KineticWeaver(template_type=profession)
    bedrock_data = weaver.vibrate_and_align(buckets)

    # 4. The Bedrock Monitor (Visualizing the 80/20 Piscine)
    monitor = BedrockMonitor()
    analysis = monitor.analyze_piscine(bedrock_data)
    monitor.generate_visual_map(analysis)

    print(f"✅ REFINERY_COMPLETE: {profession} data is now Bedrock.")
    return bedrock_data

if __name__ == "__main__":
    # Example: Your friend's Psychology Study Data (The Mud)
    test_mud = ["Participant_01", "2026-04-05", "5", "4", "3", "NULL", "Strongly Agree"]
    run_refinery(test_mud)
