import re
from sets import Set
import math
import ranking
import Stemmer
import json_collection

class query_engine(object):
    # construct a query processor
    def __init__(self, json_file):
        parse_json = json_collection.json_search(json_file)
        parse_json.record_wordsandPosition()
        getWeight = ranking.weight_cal(parse_json.word_dict)
        getWeight.getVocabulary()
        getWeight.add_contain_info()
        getWeight.cal_tf_idf()
        getWeight.normalize_tfidf()
        self.word_dict = getWeight.word_dict
        self.word_space = getWeight.word_space
        self.query_string = ""

    # simple query test. a test method.
    # query is the input query string.
    def query_parsing(self, string):
        # remove unnecessary chars
        self.query_string = string.lower()
        re.sub(r'[^0-9A-Za-z]+', r'', self.query_string)
        stemmer = Stemmer.Stemmer('english')
        words = self.query_string.split()
        for i in range(0, len(words)):
            words[i] = stemmer.stemWord(words[i])
        self.query_string = ' '.join(words)
    # comparison function of item ids
    # input: an item id
    def rank_cmp(self, id):
        words = self.query_string.split()
        score = 0
        for word in words:
            # counts = words.count(word)
            if word in self.word_dict[id]:
                score += self.word_dict[id][word][2]
            else: pass
        return score
    # query processing
    # rtype: list[item_id]
    def query_processing(self):
        self.item_ids = set()
        for word in self.query_string.split():
            if word in self.word_space:
                ids = self.word_space[word][1]
                for id in ids:
                    self.item_ids.add(id)
            else: pass
        return sorted(self.item_ids, key=self.rank_cmp)

# Test
def main():
    query_test = query_engine('test.json')
    query_test.query_parsing("earn momma")
    print query_test.query_processing()
    # print query_test.item_ids
    # print query_test.word_dict
    # print query_test.word_space
    # print query_test.query_string

if __name__ == '__main__':
    main()
