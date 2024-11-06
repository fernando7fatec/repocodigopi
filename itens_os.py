import csv
import statistics
import datetime

PATH = '/Users/fernandoramos/Desktop/FATEC/repos/estatisticaPi'
FILE_NAME = 'ITENOSDATA.csv'

# opens a csv file to read dataI/dataF
def openCSVFile(path,file_name):
    with open(f'{PATH}/{FILE_NAME}') as csvfile:
     dataIF = csv.reader(csvfile,delimiter=',')
    return dataIF

def getAvarageTime(csvReader):
   timeList = []
   csvfile = openCSVFile(PATH,FILE_NAME)
   for l in csvReader(csvfile):
    print(' ** '.join(l))

# convert a timestamp to datetime
# and returns in total seconds
# btw two timestamps
def deltaDataIeDataF(dataI,dataF):
   # timestamp format to be converted sample:
   # 2024-07-15 17:50:58.590 
   # d6 = datetime.fromisoformat('2024-07-15 17:50:58.590')
   # find the delta btw 2 timestamps
   deltaDataIDataF = (datetime.fromisoformat(dataI) - datetime.fromisoformat(dataF))

   # return the delta in seconds
   return round((deltaDataIDataF.seconds)/60)

getAvarageTime(openCSVFile(PATH,FILE_NAME))