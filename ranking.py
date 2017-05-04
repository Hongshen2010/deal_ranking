import math
import json_collection

# Define the calculation of tf*idf weights.
class weight_cal(object):
    # Constructor
    def __init__(self, word_dict):
        self.word_dict = word_dict
        self.word_space = {}
    
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
    def getVocabulary(self):
        for i in range(0, len(self.word_dict)):
            for item in self.word_dict[i].items():
                self.insertItem(item)
    # For every word in word_dict, attach the item id which contains this word.
    def add_contain_info(self):
        for item in self.word_space.items():
            contain_list = []
            for i in range(0, len(self.word_dict)):
                if item[0] in self.word_dict[i]:
                    contain_list.append(i)
            item[1].append(list(contain_list))

    # Calculate tf*idf
    def cal_tf_idf(self):
        # vocabular_size = 0
        # for item in self.word_space.items():
            # vocabular_size += item[1][0]
        N = float(len(self.word_dict))
        for i in range(0, len(self.word_dict)):
            for item in self.word_dict[i].items():
                nk = float(len(self.word_space[item[0]][1]))
                tf = float(item[1][0])
                idf = math.log10(N/nk)
                item[1].append(tf*idf)
    # Normalize the tf*idf weights
    def normalize_tfidf(self):
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
    
    # Parsing the collected json data file
    search_test = json_collection.json_search('test.json')
    # record words' information
    search_test.record_wordsandPosition()

    # Weight computations
    # construct an object for weight calculation
    tfidf_test = weight_cal(search_test.word_dict)
    # helpers
    tfidf_test.getVocabulary()
    tfidf_test.add_contain_info()
    # tf*idf weight calculation
    tfidf_test.cal_tf_idf()
    # normalize tf*idf weights
    tfidf_test.normalize_tfidf()

    # tests
    # print tfidf_test.word_dict
    print tfidf_test.word_dict
    # print tfidf_test.word_dict[0]
    # print tfidf_test.word_dict[1]
    # print tfidf_test.word_dict[2]
    # print tfidf_test.word_dict[3]


if __name__ == '__main__':
    main()