import csv
import pandas
import numpy as np


data_matrix = []
lennn=[]
with open('D:\dev\webscrap_nhthu\m1.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        lennn.append(row)
        for e in row:
            data_matrix.append(float(e))

data_matrix = np.array(data_matrix).reshape(len(lennn), len(lennn[0])

#rint(data_matrix)


#print(data_matrix[1][1])
distinct_value = []
for e in range(len(data_matrix)):
    distinct_value.append(data_matrix[e][5])

unique_value = np.unique(distinct_value)
#print(unique_value)

filter_matr = []
result = []

for i in unique_value:
    for j in data_matrix:
        if(j[len(j)-1]==i):
            filter_matr.append(j)

#print(type(filter_matr[0][1]))

def matrix_computing(matrix):
    m = np.transpose(matrix)
    summary = []
    for i in m:
        a = sum(i)/len(matrix)
        summary.append(a)
    summary = np.transpose(summary)
    return summary

def filter_data(matrix, compare_val, column_val):
    buff = []
    for i in matrix:
        if(i[column_val]== compare_val):
            buff.append(i)
    return buff


b = [[1, 2, 3, 4],[5,6,7,8],[9,10,11,12]]
print(matrix_computing(b))
print(filter_data(b,4,3))

kml=[]
result = []
for k in unique_value:
    g=filter_data(data_matrix,k, len(data_matrix[0])-1)
    kml.append(g)
for mls in kml:
    gh = matrix_computing(mls)
    result.append(gh)
print(result)


#a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
np.savetxt("m2.csv", result, delimiter=",")
#print(len(result))




