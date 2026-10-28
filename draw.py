# Jamiya draw (D-113). Numbers only, no family data.
# Usage: python3 draw.py <block_hash> <number_of_names>
# Each name number i (1..N) gets key = SHA-256 of the text "<hash>:<i>".
# Sort by key, smallest first. First = month 1 (11/2026), second = month 2, and so on.
import hashlib, sys
h, n = sys.argv[1].strip().lower(), int(sys.argv[2])
assert len(h) == 64 and all(c in "0123456789abcdef" for c in h), "hash must be 64 hex characters"
keys = sorted((hashlib.sha256(f"{h}:{i}".encode()).hexdigest(), i) for i in range(1, n + 1))
assert sorted(i for _, i in keys) == list(range(1, n + 1)), "every number exactly once"
for month, (k, i) in enumerate(keys, 1):
    print(f"month {month}: name {i}   key {k[:12]}")
