from collections import Counter
import json
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plot


with open('usagov_bitly_data2012-03-16-1331923249.txt') as f:
    recoders = [json.loads(line) for line in f]
tzs = [rec['tz'] for rec in recoders if 'tz' in rec]
#python
counts = Counter(tzs)
# print(counts.most_common(10))
#pandas
frame = DataFrame(recoders)
tzs2 = frame['tz']
clean_tz = tzs2.fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknow'
tz_counts = clean_tz.value_counts()
print(tz_counts)

results = Series([x.split()[0] for x in frame.a.dropna()])
print(results)