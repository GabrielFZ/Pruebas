import pandas as pd
import os

dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dir, 'dataset.csv')
df = pd.read_csv(file)
df['summary_date'] = pd.to_datetime(df['summary_date']).dt.date
to_fill = ['impressions', 'clicks', 'installs', 'spend']
df[to_fill] = df[to_fill].fillna(0)

grouped_df = df.groupby('campaign_id').agg({
    'impressions': 'sum',
    'clicks': 'sum',
    'installs': 'sum',
    'spend': 'sum'
}).reset_index()

grouped_df['CTR'] = grouped_df['clicks'] / grouped_df['impressions']
grouped_df['CPI'] = grouped_df['spend'] / grouped_df['installs']

grouped_df.columns = ['Campaign ID', 'Total Impressions', 'Total Clicks', 'Total Installs', 'Total Spend', 'CTR', 'CPI']
print(grouped_df)