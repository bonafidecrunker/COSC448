# Day One
def pattern_count(pattern, text):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            count = count + 1
    return count


def frequency_map(text, k):
    freq = {}
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        if pattern in freq:
            freq[pattern] += 1
        else:
            freq[pattern] = 1
    return freq


def frequent_words(text, k):
    words = []
    freq = frequency_map(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words


def reverse(pattern):
    return ''.join(reversed(pattern))


def complement(pattern):
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(pairs[n] for n in pattern)


def reverse_complement(pattern):
    return complement(reverse(pattern))


def pattern_matching(pattern, genome):
    gen_length = len(genome)
    pat_length = len(pattern)
    return [i for i in range(gen_length - pat_length + 1) if genome[i: i + pat_length] == pattern]


# Day Two
def symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    ext_gen = genome + genome[0: n // 2]

    array[0] = pattern_count(symbol, genome[0: n // 2])

    for i in range(1, n):
        array[i] = array[i - 1]
        if ext_gen[i - 1] == symbol:
            array[i] -= 1
        if ext_gen[i + (n // 2) - 1] == symbol:
            array[i] += 1

    return array


def skew_array(genome):
    skew = [0]
    n = len(genome)
    pairs = {'A': 0, 'T': 0, 'G': 1, 'C': -1}
    for i in range(1, n + 1):
        skew.append(pairs[genome[i - 1]] + skew[i - 1])
    return skew


def minimum_skew(genome):
    positions = []
    skew = skew_array(genome)
    # return [skew.index(i) for i in skew if i = min(skew)]
    minimum = min(skew)
    for i in range(len(skew)):
        positions.append(i) if minimum == skew[i] else None
    return positions


def hamming_distance(p, q):
    # Python way to do this operation
    return sum(1 for i, j in zip(p, q) if i != j)

    # Java like way to do this operation
    # hamming = 0
    # for i in range(len(p)):
    #     if p[i] != q[i]:
    #         hamming += 1
    # return hamming


# Just adapts pattern_matching method to account for the Hamming distance as an approximation
def approximate_pattern_matching(text, pattern, distance):
    gl = len(text)
    pl = len(pattern)
    return [i for i in range(gl - pl + 1) if hamming_distance(text[i: i + pl], pattern) <= distance]


def approximate_pattern_count(pattern, text, distance):
    return len(approximate_pattern_matching(pattern, text, distance))


# Day Three
def count(motifs):
    count = {}
    k = len(motifs[0])
    for c in "ACGT":
        count[c] = []
        for i in range(k):
            count[c].append(0)
    l = len(motifs)
    for i in range(l):
        for j in range(k):
            c = motifs[i][j]
            count[c][j] += 1
    return count


def profile(motifs):
    count = {}
    k = len(motifs[0])
    for c in "ACGT":
        count[c] = []
        for i in range(k):
            count[c].append(0)
    l = len(motifs)
    for i in range(l):
        for j in range(k):
            c = motifs[i][j]
            count[c][j] += 1 / l
    return count


def consensus(motifs):
    k = len(motifs[0])
    counts = count(motifs)
    output = ''
    for j in range(k):
        m = 0
        ch = ''
        for c in "ACGT":
            if counts[c][j] > m:
                m = counts[c][j]
                ch = c
        output += ch
    return output


def score(motifs):
    sum = 0
    for i in range(len(motifs)):
        sum += hamming_distance(motifs[i], consensus(motifs))
    return sum


def pr(text, profile):
    p = 1
    for i in range(len(text)):
        p *= profile[text[i]][i]
    return p


def profile_most_probable_kmer(text, k, profile):
    l = len(text)
    probabilities = {}
    out = []
    for i in range(l - k + 1):
        pattern = text[i: i + k]
        p = pr(pattern, profile)
        probabilities[pattern] = p
    m = max(probabilities.values())
    for key, value in probabilities.items():
        if probabilities[key] == m:
            out.append(key)
    return out[0]


def greedy_motif_search(dna, k, t):
    best_motifs = []
    for i in range(t):
        best_motifs.append(dna[i][0: k])
    n = len(dna[0])
    for i in range(n - k + 1):
        motifs = []
        motifs.append(dna[0][i: i + k])
        for j in range(1, t):
            p = profile(motifs[0: j])
            motifs.append(profile_most_probable_kmer(dna[j], k, p))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs

