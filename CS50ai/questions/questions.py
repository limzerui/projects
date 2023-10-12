import nltk
import sys
import os
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """

    file_dict = dict()

    # Iterate through .txt files in the given directory:
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                file_string = file.read()
                file_dict[filename] = file_string

    return file_dict


    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """


def tokenize(document):
    list = []
    tokenized = nltk.word_tokenize(document)
    for words in tokenized:
        if words.isalpha():
            list.append(words.lower())
    return list


    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """


def compute_idfs(documents):
    num_docs = len(documents)
    dict_of_words = {}
    for document in documents:
        doc_words = set(documents[document])
        for word in doc_words:
            if word not in dict_of_words:
                dict_of_words[word] = 1
            else:
                dict_of_words[word] += 1
    word_idfs = {}
    for word in dict_of_words:
        word_idfs[word] = math.log((num_docs/dict_of_words[word]))

    return word_idfs
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """


def top_files(query, files, idfs, n):
    file_scores = {filename:0 for filename in files}

    for word in query:
        if word in idfs:
            for filename in files:
                tf=files[filename].count(word)
                tf_idf = tf * idfs[word]
                file_scores[filename] += tf_idf
    sorted_files = sorted(file_scores, key=file_scores.get, reverse=True)
    #sorted_files = sorted([filenames for filenames in files], key = lambda x: file_scores[x], reverse=True)
    print(sorted_files)
    return sorted_files[:n]

    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """


def top_sentences(query, sentences, idfs, n):
    sentence_score = {sentence:{'idf_score':0, 'length':0, 'query_words':0, 'qtd_score':0} for sentence in sentences}

    for sentence in sentences:
        s=sentence_score[sentence]
        s['length']=len(nltk.word_tokenize(sentence))
        for word in query:
            if word in sentences[sentence]:
                s['idf_score']+=idfs[word]
                s['query_words']+=sentences[sentence].count(word)
        s['qtd_score'] = s['query_words']/s['length']

    sorted_sentences = sorted([sentence for sentence in sentences], key = lambda x: (sentence_score[x]['idf_score'], sentence_score[x]['qtd_score']), reverse=True)
    return sorted_sentences[:n]
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """


if __name__ == "__main__":
    main()
