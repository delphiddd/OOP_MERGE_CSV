import csv

class merg_csv():
    def __init__(self , file):
        self.list_csv = []
        self.infile = open(file , 'r')
        self.head = next(self.infile)
        self.csv_obf = csv.reader(self.infile)
        self.keys = []
        self.point = []
        self.keys_and_point = None
        self.last_list = []
    def csv_to_list(self):
        for i in self.csv_obf:
            self.list_csv.append(i)
        print("THIS IS YOUR DATA => ",self.list_csv)
        self.head = self.head.strip().split(',')
        self.infile.close()
    def clean(self):
        for i in range(len(self.list_csv)):
            for y in range(len(self.head)):
                if self.list_csv[i][0] == self.list_csv[i][y]:
                    self.keys.append(self.list_csv[i][y])
                elif self.list_csv[i][3] == self.list_csv[i][y]:
                    float_point = float(self.list_csv[i][y])
                    self.point.append(float_point)
        self.keys_and_point = list(zip(self.keys, self.point))
        print("Combined key and point:", self.keys_and_point)
    def merge(self ,a):
        if len(a) > 1:
            mid = len(a) // 2
            left = a[:mid]
            right = a[mid:]
            self.merge(left)
            self.merge(right)
            i = 0
            j = 0
            k = 0
            while len(left) > i and len(right) > j:
                if left[i] > right[j]:
                    a[k] = left[i]
                    i = i + 1
                else:
                    a[k] = right[j]
                    j = j +1
                k = k + 1
            if len(left) > i:
                a[k:] = left[i:]
            else:
                a[k:] = right[j:]
    def merge_sort(self):
        self.merge(self.point)
        print("SORT: " , self.point)
        self.merge_data()
    def merge_data(self):
       count = 0
       while len(self.point) > count:
            for i in range(len(self.keys_and_point)):
                for y in range(2):
                    if self.keys_and_point[i][y] == self.point[count]:
                        self.last_list.append(self.keys_and_point[i])
                        count +=1
                        break
                if count == len(self.point):
                    break
       print(self.last_list)
                         
merge_ = merg_csv("/Users/delphi/Desktop/works/python/SU/data.csv")
merge_.csv_to_list()
merge_.clean()
merge_.merge_sort()