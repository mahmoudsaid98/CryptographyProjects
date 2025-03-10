from collections import Counter

 ENGLISH_FREQ = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def frequency_analysis(ciphertext):
     ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
    
     freq = Counter(ciphertext)
    
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
     ciphertext = input("Enter the encrypted text: ")
    
     sorted_freq = frequency_analysis(ciphertext)
    
     mapping = {}
    for i in range(min(len(sorted_freq), len(ENGLISH_FREQ))):
        mapping[sorted_freq[i]] = ENGLISH_FREQ[i]
    
     decrypted_text = decrypt(ciphertext, mapping)
    
     print("\nMost likely decrypted text:")
    print(decrypted_text)

if __name__ == "__main__":
    main()
