
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 0001: Generate 200 unique activation codes (for app or coupons)

Author: Your Name
Date: YYYY-MM-DD
"""

import random
import string

def generate_activation_code(length=12):
    """
    Generate a single random activation code.
    Characters used: uppercase letters (A-Z) and digits (0-9)
    """
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

def generate_activation_codes(count=200, length=12):
    """
    Generate 'count' unique activation codes of given length.
    Returns a list of unique codes.
    """
    codes = set()
    while len(codes) < count:
        codes.add(generate_activation_code(length))
    return list(codes)

def save_codes_to_file(codes, filename="activation_codes.txt"):
    """Save all codes to a text file, one per line"""
    with open(filename, "w") as f:
        for code in codes:
            f.write(code + "\n")
    print(f"{len(codes)} activation codes saved to '{filename}'")

if __name__ == "__main__":
    # Generate 200 unique activation codes
    codes = generate_activation_codes(count=200, length=12)

    # Print codes to console with numbering
    print("=== Activation Codes ===")
    for i, code in enumerate(codes, start=1):
        print(f"{i:03d}: {code}")

    # Save codes to file
    save_codes_to_file(codes)
