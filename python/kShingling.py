def kShingling(sentences, k=2):
    vocab = []
    all_shingles = []
    for s in sentences:
        shingles = []

        for i in range(0, len(s) - k + 1):

            shingles.append(s[i:i+k])
        vocab += shingles
        all_shingles = (s, set(shingles))

    return all_shingles, set(vocab)

def createSparseVectors(shingles, vocab):
    zeroVector = [0] * len(vocab)
    sparseVectors = []
    for shingle in shingles:
        oneHot = zeroVector.copy()
        for i, v in enumerate(vocab):
            if v in shingle:
                oneHot[i] = 1
        sparseVectors.append(oneHot)

    return sparseVectors

test_sentences = ["this is a test sentence", "this is another test sentence", "sentence number three!"]
testShingles, vocab = kShingling(test_sentences)
sparceVectors = createSparseVectors(testShingles, vocab)



