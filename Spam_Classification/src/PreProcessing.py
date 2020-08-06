import re
import string
from unicodedata import normalize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer


class TextPreProcessing:

    # This function removes stopwords from text.
    def remove_stopwords(str_):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(str_)

        newStr = []
        for w in word_tokens:
            if w not in stop_words:
                newStr.append(w)

        return " ".join(newStr)

    # This function removes the punctuation from the sentences.
    def remove_punctuation(str_):
        new_str = ''
        for letter in str_:
            if letter not in string.punctuation:
                new_str += letter

        return new_str

    # This function removes URL's from text.
    def remove_url(str_):
        return re.sub(r"http\S+", " ", str_)

    # This function removes html tags from text.
    def remove_html_tags(str_):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', str_)

    # This function converts accented characters to ascii character.
    def convert_to_ascii(str_):
        str_ = normalize('NFKD', str_).encode('ASCII', 'ignore')
        return str_.decode('utf8')

    # This function removes whitespaces
    def remove_whitespaces(self):
        return self.strip()

    # This function stems the tokenized words
    def stem_words(self):
        words = word_tokenize(self)
        stemmer = LancasterStemmer()
        words = [stemmer.stem(word) for word in words]
        return words


class NormalizeNumbers:
    # Rescale dataset columns to the range 0-1
    def normalize_dataset(self):
        min_value = min(self)
        max_value = max(self)
        for row in range(len(self)):
            normalized = (row - min_value) / (max_value - min_value)
            self[row] = normalized
        return self
