from collections import Counter

# English letter frequency (from highest to lowest)
ENGLISH_FREQ = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def frequency_analysis(ciphertext):
    # Remove non-alphabetic characters and convert to uppercase
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
    
    # Count the frequency of each letter
    freq = Counter(ciphertext)
    
    # Sort letters by frequency (most frequent first)
    sorted_freq = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    
    return sorted_freq

def decrypt(ciphertext, mapping):
    decrypted_text = []
    for char in ciphertext:
        if char.upper() in mapping:
            # Preserve the original case
            if char.isupper():
                decrypted_text.append(mapping[char])
            else:
                decrypted_text.append(mapping[char.upper()].lower())
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def main():
    # Input encrypted text
    ciphertext = input("Enter the encrypted text: ")
    
    # Perform frequency analysis
    sorted_freq = frequency_analysis(ciphertext)
    
    # Create a mapping based on frequency analysis
    mapping = {}
    for i in range(min(len(sorted_freq), len(ENGLISH_FREQ))):
        mapping[sorted_freq[i]] = ENGLISH_FREQ[i]
    
    # Decrypt the text using the mapping
    decrypted_text = decrypt(ciphertext, mapping)
    
    # Output the most likely decrypted text
    print("\nMost likely decrypted text:")
    print(decrypted_text)

if __name__ == "__main__":
    main()