import sys
import itertools
import time

def build_allowed():
    """
    Build an allowed ASCII table.
    Allowed characters are:
      - Lowercase letters (a-z)
      - Uppercase letters (A-Z)
      - Digits (0-9)
      - Space
      - Brackets: ( )
      - Common symbols: ;  :  ,  .  '  ?  -  !
    """
    allowed = [False] * 128
    # Lowercase letters a-z (97-122)
    for i in range(97, 123):
        allowed[i] = True
    # Uppercase letters A-Z (65-90)
    for i in range(65, 91):
        allowed[i] = True
    # Digits 0-9 (48-57)
    for i in range(48, 58):
        allowed[i] = True
    # Space (32)
    allowed[32] = True
    # Brackets ( ( and ) )
    allowed[40] = True  # (
    allowed[41] = True  # )
    # Common symbols: ; (59), : (58), , (44), . (46), ' (39), ? (63), - (45), ! (33)
    for code in [59, 58, 44, 46, 39, 63, 45, 33]:
        allowed[code] = True
    return allowed

# Global allowed table
ALLOWED = build_allowed()

def decrypt_message(ciphertext):
    """
    Given a list of integers representing the encrypted ASCII codes,
    iterate over all 3-letter lower-case keys and return the key and
    the decrypted text if a candidate produces only allowed characters.
    
    If no valid key is found, returns (None, None).
    """
    n = len(ciphertext)
    if n == 0:
        return None, None

    # Try each possible key candidate (three lowercase letters)
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                key = (a, b, c)
                valid = True
                # Early check: verify the first few characters (e.g., first 100)
                check_limit = min(100, n)
                for i in range(check_limit):
                    k = key[i % 3]
                    decrypted_val = ciphertext[i] ^ k
                    if decrypted_val < 0 or decrypted_val >= 128 or not ALLOWED[decrypted_val]:
                        valid = False
                        break
                if not valid:
                    continue

                # If the candidate passes the early check, verify the entire text.
                full_valid = True
                for i in range(n):
                    k = key[i % 3]
                    decrypted_val = ciphertext[i] ^ k
                    if decrypted_val < 0 or decrypted_val >= 128 or not ALLOWED[decrypted_val]:
                        full_valid = False
                        break
                if full_valid:
                    # Construct decrypted text from the key.
                    decrypted_text = ''.join(chr(ciphertext[i] ^ key[i % 3]) for i in range(n))
                    key_str = ''.join(chr(x) for x in key)
                    return key_str, decrypted_text
    return None, None

def main():
    # Read from standard input.
    data = sys.stdin.read().strip().split()
    if not data:
        return
    try:
        # First token is the number of encrypted integers.
        n = int(data[0])
    except:
        sys.exit("Invalid input format")
    ciphertext = list(map(int, data[1:]))
    if len(ciphertext) != n:
        sys.exit("Number of integers does not match the count specified.")
    key, decrypted_text = decrypt_message(ciphertext)
    if key is not None:
        # Output the found key.
        print(key)
    else:
        print("No valid key found")

# ---------------------- Testing ----------------------
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        import unittest

        class TestXORDecryption(unittest.TestCase):
            def test_sample(self):
                # Sample test from the problem statement.
                sample_ciphertext = [
                    32, 66, 50, 20, 11, 0, 42, 66, 33, 19, 13, 20, 47, 66, 37, 14, 58, 67, 43, 23, 14, 17, 
                    49, 67, 46, 20, 6, 51, 66, 55, 9, 39, 67, 45, 3, 25, 56, 66, 39, 14, 37, 34, 65, 51, 
                    22, 8, 1, 40, 65, 32, 17, 14, 21, 45, 65, 36, 12, 57, 66, 41, 20, 15, 19, 50, 66, 44, 
                    23, 7, 49, 65, 54, 11, 36, 66, 47, 0, 24, 58, 65, 38, 12, 38
                ]
                key, decrypted = decrypt_message(sample_ciphertext)
                self.assertEqual(key, "abc")

            def test_invalid_ciphertext(self):
                # Test with a ciphertext that cannot be validly decrypted.
                # Example: using a number that, when XORed with any lower-case letter, gives an out-of-range ASCII.
                ciphertext = [200]
                key, decrypted = decrypt_message(ciphertext)
                self.assertIsNone(key)
                self.assertIsNone(decrypted)

            def test_performance(self):
                # Performance test: encrypt a long plaintext and ensure decryption recovers the key.
                import random
                random.seed(0)
                # Build a list of allowed ASCII codes.
                allowed_chars = [i for i in range(128) if ALLOWED[i]]
                # Create a plaintext of 100,000 characters.
                plaintext = [random.choice(allowed_chars) for _ in range(100000)]
                # Choose a random key of 3 lowercase letters.
                key = [random.randint(97, 122) for _ in range(3)]
                # Encrypt the plaintext with the key (cyclically).
                ciphertext = [plaintext[i] ^ key[i % 3] for i in range(100000)]
                start = time.time()
                found_key, decrypted_text = decrypt_message(ciphertext)
                end = time.time()
                self.assertEqual(found_key, ''.join(chr(x) for x in key))
                # Verify the decrypted text matches the original plaintext.
                decrypted_list = [ord(c) for c in decrypted_text]
                self.assertEqual(decrypted_list, plaintext)
                print("Performance test completed in {:.3f} seconds.".format(end - start))

        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        main()
