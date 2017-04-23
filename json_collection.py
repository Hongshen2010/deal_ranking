import re
import sys
import json
import time
import Stemmer

class json_search():
    # constructor
    def __init__(self, json_file):
        self.word_dict = []
        with open(json_file, 'r') as f:
            self.data = json.load(f)
    
    def normalize_str(self, string):
        strip_chars = [
                       ',', '.', '%', '"', ':', '/', '(',
                       ')', ';', '&', '#', '@', '\'', 
                       '$', '[', ']', '+', '-'
                      ]
        dump_strings = [
                        'is', 'a', 'an','and','to','get',
                        'over','out','from', 'now', 'of', 
                        'the', 'with', 'by', 'up', 'us',
                        'per','each','all', 'via', 'are',
                        'was', 'were', 'in', 'any','not',
                        'or', 'been', 'on', 'for', 'offer'
                        'that', 'com', 'offer', 'your'
                       ]
        stemmer = Stemmer.Stemmer('english')
        # Replace all unnecessary dots.
        front_dots = re.findall(r'\.\D', string)
        back_dots = re.findall(r'\D\.', string)
        for dot in front_dots:
            tmp = ' ' + dot[1]
            string = string.replace(dot, tmp)
        for dot in back_dots:
            tmp = dot[0] + ' '
            string = string.replace(dot, tmp)
        string = string.lower()
        # Split string into list
        string = map(lambda substr: stemmer.stemWord(substr), re.split(r'[\s,;\(\)$]+', string))
        # Eliminate skip words
        string = filter(lambda str: str not in strip_chars and str not in dump_strings, string)
        # string = ' '.join(string)
        return string
    
    # Insert words into dict
    def insert_word(self, word, dict):
        tmp_list = []
        if word not in dict:
            tmp_list.append(1)
            dict[word] = (list(tmp_list))
            dict[word].append(list([])) # preserved list for positions
        else:
            dict[word][0] += 1
    # Doing statistical operation of each item in the json file.
    # Record how many times each word appears and its positions.
    def record_wordsandPosition(self):
        for i in range(0, len(self.data)):
            tmp_dict = {}
            # Description
            if len(self.data[i]['description']) != 0:
                des = self.normalize_str(self.data[i]['description'][0])
                des_str = ' '.join(des)
                for word in des:
                    self.insert_word(word, tmp_dict)
            else: pass
            # item name
            if len(self.data[i]['item']) != 0:
                ite = self.normalize_str(self.data[i]['item'][0])
                ite_str = ' '.join(ite)
                for word in ite: 
                    self.insert_word(word, tmp_dict)
            else: pass
            # feature
            if len(self.data[i]['feature']) != 0:
                fea = self.normalize_str(self.data[i]['feature'][0])
                fea_str = ' '.join(fea)
                for word in fea: 
                    self.insert_word(word, tmp_dict)

            else: pass
            tmp_dict.pop('', None)
            self.word_dict.append(dict(tmp_dict))
    # Helper for test.
    def print_item(self, id):
        return dict(self.data[id])


# Find all occurences of a sub_string(or word) in a string.
def find_all_sub(string, sub_string, indeces):
    start, end = 0, len(string)
    while start < end:
        idx = string.find(sub_string)
        if idx == -1:
            break
        else:
            indeces.append(start + idx)
            start = idx
            string = string[idx:]
                

# TEST
def main():
    
    search_test = json_search('dm_modified.json')
    # start = time.time()
    search_test.record_wordsandPosition()
    # end = time.time()
    # print end - start
    # print search_test.word_dict
    if len(sys.argv) > 1:
        print search_test.print_item(int(sys.argv[1]))
    else: pass


if __name__ == '__main__':
    main()