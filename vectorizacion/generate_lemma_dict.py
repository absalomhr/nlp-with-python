def save(dict):
    import numpy as np
    # Save dict to disk
    np.save('lemmas.npy', dict) 

def get_lemmas_dict (filename):
    f = open(filename, encoding='latin-1')
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    lemmas = {}

    for l in lines:
        if l != '':
            words = l.split()
            words = [w.strip() for w in words]
            wordform = words[0]
            wordform = wordform.replace('#', '')
            lemmas[wordform] = words[-1]

    return lemmas

lemmas = get_lemmas_dict("generate.txt")
print("Size of lemma dict:", len(lemmas))
save(lemmas)