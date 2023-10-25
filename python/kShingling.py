def kShingling(sentences, k=2):
    k_shingles = []
    for s in sentences:
        for i in range(0, len(s) - k + 1):

            k_shingles.append(s[i:i+k])
        
    return set(k_shingles)

testShingle = kShingling(["this is a test sentence"])
print(testShingle)
