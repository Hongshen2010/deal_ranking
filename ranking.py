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
        if item[0] not in self.word_space:
            self.word_space[item[0]] = []
            self.word_space[item[0]].append(item[1][0])
        else:
            self.word_space[item[0]][0] += item[1][0]

    # Get the vocabulary pool.
    # Every string appears in the word_dict and their overall times.
    # Informations are stored in a list.
    def getVocabulary(self, word_dict):
        for i in range(0, len(self.word_dict)):
            for item in self.word_dict[i].items():
                self.insertItem(item)
    # For every word in word_dict, attach the item id which contains this word.
    def add_contain_info(self, word_space, word_dict):
        for item in self.word_space.items():
            contain_list = []
            for i in range(0, len(self.word_dict)):
                if item[0] in self.word_dict[i]:
                    contain_list.append(i)
            item[1].append(list(contain_list))

    # Calculate tf*idf
    def cal_tf_idf(self, word_space, word_dict):
        # vocabular_size = 0
        # for item in self.word_space.items():
            # vocabular_size += item[1][0]
        N = float(len(self.word_dict))
        for i in range(0, len(self.word_dict)):
            for item in self.word_dict[i].items():
                nk = float(len(word_space[item[0]][1]))
                tf = float(item[1][0])
                idf = math.log10(N/nk)
                item[1].append(tf*idf)
    # Normalize the tf*idf weights
    def normalize_tfidf(self, word_space, word_dict):
        for item in self.word_space.items():
            square_sum = 0
            for id in item[1][1]:
                square_sum += math.pow(self.word_dict[id][item[0]][2], 2)
            # print square_sum
            for id in item[1][1]:
                if square_sum == 0: pass
                else: self.word_dict[id][item[0]][2] /= math.sqrt(square_sum)
    # Helper for test.
    def print_item(self, id):
        return dict(self.word_dict[id])


# Test
def main():
    data = []
    word_dict = []
    word_space = {}
    search_test = json_collection.json_search(data, word_dict, 'dm_modified.json')
    search_test.record_wordsandPosition()
    tfidf_test = tf_idf(word_dict, word_space)
    tfidf_test.getVocabulary(word_dict)
    tfidf_test.add_contain_info(word_space, word_space)
    tfidf_test.cal_tf_idf(word_space, word_dict)
    tfidf_test.normalize_tfidf(word_space, word_dict)
    print tfidf_test.word_dict
    # print tfidf_test.word_space
    # print tfidf_test.word_dict[0]
    # print tfidf_test.word_dict[1]
    # print tfidf_test.word_dict[2]
    # print tfidf_test.word_dict[3]


if __name__ == '__main__':
    main()