import re
from collections import defaultdict
from math import gcd
from functools import reduce

def find_repeating_sequences(ciphertext, min_len=3):
    sequences = defaultdict(list)

    for length in range(min_len, len(ciphertext) // 2 + 1):
        for i in range(len(ciphertext) - length + 1):
            seq = ciphertext[i:i + length]
            sequences[seq].append(i)

    repeating_sequences = {seq: positions for seq, positions in sequences.items() if len(positions) > 1}
    return repeating_sequences


def calculate_distances(positions):
    distances = []
    for i in range(len(positions) - 1):
        distances.append(positions[i + 1] - positions[i])
    return distances


def find_gcd(numbers):
    return reduce(gcd, numbers)


def kasiski_analysis(ciphertext, min_pattern_length=3):
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())
    print(f"Ciphertext after cleaning: {ciphertext}\n")

    repeating_patterns = find_repeating_sequences(ciphertext, min_len=min_pattern_length)

    kasiski_results = {}

    for seq, positions in repeating_patterns.items():
        distances = calculate_distances(positions)
        if distances:
            gcd_value = find_gcd(distances)
            kasiski_results[seq] = (positions, distances, gcd_value)

    return kasiski_results


def main():
    ciphertext = input("Enter the ciphertext: ")

    results = kasiski_analysis(ciphertext, min_pattern_length=3)

    print("\nKasiski Analysis Results:")
    if not results:
        print("No repeating patterns found.")
    else:
        for seq, (positions, distances, gcd_value) in results.items():
            print(f"Pattern: {seq}")
            print(f"Positions: {positions}")
            print(f"Distances: {distances}")
            print(f"GCD of distances (possible keyword length): {gcd_value}")
            print()


if __name__ == "__main__":
    main()
