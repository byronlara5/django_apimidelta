import pandas as pd
import csv 
import json
import sys
import re

#for testing
import pdb

#import codecs
ENCODING = 'utf-8'

def ConvertToJson(filecsv):
 	df = pd.read_csv(filecsv, sep="|", encoding='utf-8', 
 		low_memory=False, dtype={"niv": str})
 	fname = re.sub(r'(.*?\/)(.*)(\_follow.*)(\.csv)',r"\2",filecsv)
 	#pdb.set_trace()

 	print(fname)

 	jsonfile = open(fname+".json", 'w')
 	jsonfile.write('[')

 	L = len(df.index)
 	print(L)

 	df=df.fillna('')
 	for i,row in df.iterrows():
 		json.dump(dict(row), jsonfile,ensure_ascii=True)
 		if i < L-1:
 			jsonfile.write(', \n')

 	jsonfile.write(']')
 	jsonfile.close()

filecsv=sys.argv[1]
ConvertToJson(filecsv) 