import csv
from collections import defaultdict

class count_school(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.csv_f = csv.reader(open(self.file_name))

        self.state_filter = defaultdict(int)
        self.mlocal_filter = defaultdict(int)
        self.city_filter = defaultdict(int)

        self.total = 0
        self.city_with_school_cnt = 0

        self.highest_schools_in_city = ""

        for counter, row in enumerate(self.csv_f):
            if counter == 0:
                # print row #to skip the header row
                continue
            self.city_filter[row[4]] += 1
            self.state_filter[row[5]] += 1
            self.mlocal_filter[row[8]] += 1
        self.__update_stats()

    def __update_stats(self):
        curr = float("-inf")
        for i, v in enumerate(self.city_filter):
            if self.city_filter[v] > curr:
                curr = self.city_filter[v]
                self.highest_schools_in_city = v
            if self.city_filter[v] > 1:
                self.city_with_school_cnt += 1

        for i, v in enumerate(self.state_filter):
            self.total += self.state_filter[v]

    def total_schools_by_states(self):
        print "Schools by State "
        for i, v in enumerate(self.state_filter):
            print v + ":" + str(self.state_filter[v])

    def total_schools(self):
        print "Total Schools are " + str(self.total)
        return self.total

    def total_schools_by_mlocal(self):
        print "Schools by Metro-centric locale"
        for i, v in enumerate(self.mlocal_filter):
            print v + ":" + str(self.mlocal_filter[v])

    def city_with_most_schools(self):
        print "City with Most Schools is " + self.highest_schools_in_city + " with a total of " + str(self.city_filter[self.highest_schools_in_city]) + " schools"

    def unique_cities_with_schools(self):
        print "Cities with at least one school are a total of " + str(self.city_with_school_cnt)

obj = count_school("school_data.csv")
obj.total_schools()
obj.total_schools_by_states()
obj.total_schools_by_mlocal()
obj.city_with_most_schools()
obj.unique_cities_with_schools()

