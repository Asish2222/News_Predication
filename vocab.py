from collections import Counter

class Vocabulary:
    def __init__(self, max_size=10000):
        self.word2idx = {'<PAD>': 0, '<UNK>': 1}
        self.idx2word = {0: '<PAD>', 1: '<UNK>'}
        self.max_size = max_size

    def build_vocab(self, texts):
        word_counts = Counter()
        for text in texts:
            word_counts.update(text.split())

        most_common = word_counts.most_common(self.max_size - 2)
        for idx, (word, _) in enumerate(most_common, start=2):
            self.word2idx[word] = idx
            self.idx2word[idx] = word

    def encode(self, text, max_len=300):
        tokens = text.split()
        encoded = [self.word2idx.get(word, 1) for word in tokens]

        if len(encoded) < max_len:
            encoded += [0] * (max_len - len(encoded))
        else:
            encoded = encoded[:max_len]

        return encoded

    def __len__(self):
        return len(self.word2idx)
