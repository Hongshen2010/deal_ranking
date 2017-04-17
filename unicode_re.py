import re
import unicodedata
import json

# string = u"dealmoon \n dealmoon dealmoon\n \u00a0 \u00ae"
string = u"Sephora.com offers the Guerlain My Beauty Essentials Set for $32.Plus, receive a free Bare Minerals foundation mini via coupon code \"BARECLASSIC\".Free Shipping on orders over $50."

# match = re.search(ur'\\\u\d\d\w\d', string, re.UNICODE)
# # print match.group()
# if match is not None:
#     print match.group()
# string = string.replace(match.group(), "DM!!")
# with open('dm.json', 'r') as f:
#     data = json.load(f)
#     print len(data)
    # for item in data:
    #     print len(item['feature']) != 0, item['feature'] is not None
    #     print item['feature'] is not None
# print string
print string
for word in string.split():
    for w in word.split():
        print w