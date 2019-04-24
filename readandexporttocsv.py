import pandas as pd

dateparse = lambda x: pd.to_datetime(x,  format='%Y%m%d', errors='coerce')
df = pd.read_csv('sample_input.csv', sep='\t', parse_dates=['valid_start_date','valid_end_date'], date_parser=dateparse, dtype={"invalid_reason": object})
df.to_csv('outputfile.csv',index=False, sep='\t')