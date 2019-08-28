import nltk

def delete_html_tags(text_string):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(text_string, 'lxml')
    return soup.get_text()

def lower_case(text_string):
    return text_string.lower()
    
def tokenize_text(text_string):
    from nltk.tokenize import word_tokenize
    return word_tokenize(text_string)
    
def only_words(text_list):
    import re
    new_tokens = []
    for token in text_list:
        clean_token = ""
        for c in token:
            if re.match(r'[a-záéíóúñü]', c):
                clean_token += c
        if clean_token != '':
            new_tokens.append(clean_token)
    return new_tokens

def delete_stopwords(text_list):
    from nltk.corpus import stopwords

    stopWords = set(stopwords.words('spanish'))

    return [w for w in text_list if w not in stopWords]

def load_dict(filename):
    import numpy as np
    dict = np.load(filename+'.npy', allow_pickle=True).item()
    return dict

def save_dict(dict, filename):
    import numpy as np
    # Save dict to disk
    np.save(filename+'.npy', dict)

def save_list_pickle(l, filename):
    import pickle    
    with open(filename+'.txt', "wb") as fp:
        pickle.dump(l, fp)

def load_list_pickle(filename):
    import pickle
    with open(filename+'.txt', "rb") as fp:
        l = pickle.load(fp)
    return l

def lemmatize(words):
    lemmas = load_dict("lemmas")

    lemmatized = []
    for w in words:
        if w in lemmas: 
            lemmatized.append(lemmas[w])
        else:
            lemmatized.append(w)

    return lemmatized


def get_word_context(text_string, window_size=8):
    '''
    Receives a text as a string and returns a
    dictionary of contexts where the keys are
    each word of the vocabulary of the text and
    the values the context of each word as a list
    '''

    # Normalizing the text

    # Getting rid of html tags



    clean_text = delete_html_tags(text_string)

    # Make the text lowercase
    clean_text = lower_case(clean_text)

    # Tokenizing the text
    text_list = tokenize_text(clean_text)

    # Getting rid of urls
    #$text_list = delete_urls(text_list)

    # Getting rid of punctuation
    text_list = only_words(text_list)

    # Getting rid of stopwords
    text_list = delete_stopwords(text_list)

    text_list = lemmatize(text_list)
    
    print("The lenght of the text is:", len(text_list))

    # Getting the vocabulary

    vocab = list(set (text_list))
    vocab.sort()
    
    
    print("The lenght of the vocabulary is:", len(vocab))

    # Extract context of each word

    # Getting the contexts

    contexts = {}

    for w in vocab:
     single_context = []
     contexts[w]=[]
     for i, t in enumerate(text_list):
         if t == w:
             if (i - window_size / 2) < 0:
                 single_context += text_list[:i]
             elif (i + (window_size / 2)) > (len(text_list) - 1):
                 single_context += text_list[i + 1:]
             else:
                 # left
                 single_context += text_list[i-(window_size // 2):i]
                 # right
                 single_context += text_list[i+1:i+(window_size // 2)+1]
             contexts[w] += single_context
             single_context = []
    return (contexts, vocab)

corpus_root = './texts'
filename = 'e960401_mod.htm'

# Get text as a string
# f = open(corpus_root +"/"+ filename, encoding='utf-8')
# raw_text = f.read()

# contexts, vocab = get_word_context(raw_text)
# save_dict(contexts, "contexts")
# save_list_pickle(vocab, "vocabulary")


# vocab = load_list_pickle('vocabulary')
# contexts = load_dict('contexts')

# print("The context of 'presidente' has", len(contexts['presidente']), " words")
# print("The context of 'discutir' has", len(contexts['discutir']), " words")
# print("The context of 'méxico' has", len(contexts['méxico']), " words")

# vectors = {}
# for i in range(len(contexts)):
#     current_v = []
#     for j in range(len(contexts)):
#         current_v.append(contexts[vocab[i]].count(vocab[j]))
#     vectors[vocab[i]] = current_v[:]

# save_dict(vectors, "vectors")

vocab = load_list_pickle('vocabulary')
contexts = load_dict('contexts')
vectors = load_dict("vectors")