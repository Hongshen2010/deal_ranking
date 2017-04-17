import math
import json_collection

# Define the calculation of tf*idf weights.
class tf_idf(object):
    # Constructor
    def __init__(self, word_dict, word_space):
        self.word_dict = word_dict
        self.word_space = word_space
    
    # Insert 
    def insertItem(self, item):
        if item[0] in self.word_space:
            self.word_space[item[0]] += item[1]
        else:
            self.word_space[item[0]] = item[1]

    # Get the vocabulary pool.
    def getVocabulary(self, word_dict):
        for i in range(0, len(word_dict)):
            for item in word_dict[i].items():
                self.insertItem(item)
    
    # Calculate tf*idf
    # def cal(self, word_space):
        
    
# Test
def main():
    data = []
    word_dict = []
    word_space = {}
    search_test = json_collection.json_search(data, word_dict, 'dm_modified.json')
    search_test.record_wordsandPosition()
    tfidf_test = tf_idf(word_dict, word_space)
    tfidf_test.getVocabulary(word_dict)
    print tfidf_test.word_space

if __name__ == '__main__':
    main()