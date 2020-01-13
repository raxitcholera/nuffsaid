import csv, linecache, time
from collections import defaultdict

class count_school(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.csv_f = csv.reader(open(self.file_name))
        self.dic = defaultdict(list)

        for i, v in enumerate(self.csv_f):
            if i==0:
                # print v
                continue
            self.addSearchTerms(v[3], i)
            self.addSearchTerms(v[4], i)
            self.addSearchTerms(v[5], i)

    def addSearchTerms(self, words, index):
        for w in words.split(" "):
            self.dic[w.lower()].append(index)

    def get_school_info(self, line_numbers):
        res = []
        for row_number in line_numbers[:3]:
            line = linecache.getline(self.file_name, row_number+1).split(",")
            print line[3] + str("\n") + line[4] + str(",") + line[5]
            res.append(line)
        return res

    def search_school(self, search_str):
        start = time.time()
        res = []
        for w in search_str.split(" "):
            if w.lower() in self.dic:
                new = list(set(self.dic[w.lower()]) & set(res))
                if len(res) == 0:
                    res = self.dic[w.lower()]
                elif len(new) != 0 and len(new) < len(res):
                    res = new
        print "Result for \""+search_str+"\" took "+str(round(time.time() - start, 4)) +"s"
        self.get_school_info(res)


obj = count_school("school_data.csv")
obj.search_school("elementary school highland park")
obj.search_school("jefferson belleville")
obj.search_school("riverside school 44")
obj.search_school("granada charter school")
obj.search_school("foley high alabama")
obj.search_school("KUSKOKWIM")
