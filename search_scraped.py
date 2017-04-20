import re
import json
import unicodedata

# Define characters to ignore
dump_chars = ['&', '']

# Define rgex to parse the scraped data

def remove_unicode_reserved_word(string):
    string = string.encode('ascii', 'ignore')
    return string
    
def remove_newline(string):
    match = re.search(r'\n *', string)
    if match is None: 
        return string
    else:
        string = string.replace(match.group(), "")
        return remove_newline(string)
        
with open('dm_test.json', 'r') as f:
    data = json.load(f)
    for item in data:
        
        # parse description attribute
        if len(item['description']) != 0:
            des = []
            for string_part in item['description']:
                des.append(remove_unicode_reserved_word(string_part))
            item['description'] = des
        else: pass

        # parse item attribute
        if len(item['item']) != 0:
            item['item'][0] = remove_unicode_reserved_word(item['item'][0])
        else: pass

        # parse feature attribute
        if len(item['feature']) != 0:
            item['feature'][0] = remove_unicode_reserved_word(item['feature'][0])
        else: pass
        
        # parse discount attribute
        if len(item['discount']) !=0:
            des = ""
            for element in item['discount']:
                des += element
            item['discount'] = remove_newline(des)
            item['discount'] = remove_unicode_reserved_word(item['discount'])
            item['discount'] = re.sub(ur'\(,\s', ur' (', item['discount'], re.UNICODE)
            remove_spaces = re.search(r'\)(\s)+', item['discount'])
            if remove_spaces is not None:
                item['discount'] = item['discount'].replace(remove_spaces.group(1), '')
        else: pass

with open('dm_modified.json', 'w+') as fm:
    json.dump(data, fm)
    