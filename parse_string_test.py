import re

# s = "BookingBuddy offers the  Roundtrip Ticket from Denver to Dallas for $57.Frontier Airline.Example date: 4/6-4/11.Book now.i3-6100T 3.2GHz, 4GBDDR4(supports up to 32GB), 128GB SSD;Gigabit Ethernet,802.11ac; 6 x USB3.0, 2 x DP; Windows 10 Professional (64-bit)."
# front_dot = re.findall(r'\.\D', s)
# print front_dot
# back_dot = re.findall(r'\D\.', s)
# print back_dot
# for fd in front_dot:
#     tmp_char = ' ' + fd[1]
#     s = s.replace(fd, tmp_char)
# for bd in back_dot:
#     tmp = s.find(bd)
    
# print s

def find_all_sub(string, sub_string, indeces):
    find_all_helper(string, sub_string, 0, len(string), indeces)
    return indeces
# Recursive helper of find_all_sub.
def find_all_helper(string, sub_string, start, end, indeces):
    if start+len(sub_string) > end:
        return indeces
    string = string[start:]
    idx = string.find(sub_string)
    if idx == -1:
        return indeces
    else:
        indeces.append(idx)
        find_all_helper(string, sub_string, idx+len(sub_string), end, indeces)

def main():
    s = "BookingBuddy offers the  Roundtrip Ticket from Denver to Dallas for $57.Frontier Airline.Example date: 4/6-4/11.Book now."
    s = s.lower()
    words = s.split()
    pos = []
    for word in words:
        tmp_list = []
        pos.append(list(find_all_sub(s, word, tmp_list)))
    print pos

if __name__ == '__main__':
    main()