import Stemmer
import query_processor

class evaluation(object):
    
    def __init__(self, fileName):
        datas = query_processor.query_engine(fileName)
        self.vocabulary = datas.word_space
        self.all_items = datas.data
        self.evaluation_string = ""
    # avoid constructing object too many times when evaluate different words
    def init_evaluation(self, string):
        stemmer = Stemmer.Stemmer('english')
        self.evaluation_string = stemmer.stemWord(string)
    # record all items which contain the word to be evaluated
    def find_all_occurrence(self):        
        # rtype list of item ids
        ids = []
        for i in range(0, len(self.all_items)):
            if len(self.all_items[i]['description']) != 0:
                if self.evaluation_string in self.all_items[i]['description'][0].lower():
                    ids.append(i)
                    continue
            if len(self.all_items[i]['item']) != 0:
                if self.evaluation_string in self.all_items[i]['item'][0].lower():
                    ids.append(i)
                    continue
            if len(self.all_items[i]['feature']) != 0:
                if self.evaluation_string in self.all_items[i]['feature'][0].lower():
                    ids.append(i)
                    continue
        return ids
    def check_occurrence(self):
        tmp_ids = []
        evaluation_tuples = []
        for item in self.vocabulary.items():
            len_not_equal = 0
            self.init_evaluation(item[0])
            tmp_ids = self.find_all_occurrence()
            if len(tmp_ids) == 0:
                evaluation_tuples.append((item[0], len(item[1][1]), len(item[1][1])))
            else: evaluation_tuples.append((item[0], len(tmp_ids), len(item[1][1])))
        return evaluation_tuples

    
def main():
    # evaluation_test = evaluation("dm_modified.json") # dm_modified: 0.72260
    evaluation_test = evaluation("test.json")
    # evaluation_test.init_evaluation('dine')
    # print evaluation_test.find_all_occurrence()
    samples = evaluation_test.check_occurrence()
    equal = 0
    for sample in samples:
        if sample[1] == sample[2]: equal += 1
    print float(equal) / float(len(samples))

if __name__ == '__main__':
    main()
