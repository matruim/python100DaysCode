import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
df.head()
print(df.shape)
print(df.columns)
print(df.isna())
clean_df = df.dropna()
print(clean_df.tail())
print(clean_df['Starting Median Salary'].max())
print(clean_df['Starting Median Salary'].idxmax())
print(clean_df['Undergraduate Major'].loc[43])
print(clean_df.loc[43])
# Highest Mid-career Salary
print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmax()])
# LOWEST Mid-career Salary
print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()])
# Lowest Starting Salary
print(clean_df.loc[clean_df['Starting Median Salary'].idxmin()])
# lowest Risk Majors
print(clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary'])
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())
# lowest risk jobs
low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())
# highest potential
high_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(high_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())
# Greatest Spread
high_spread = clean_df.sort_values('Spread', ascending=False)
print(high_spread[['Undergraduate Major', 'Spread']].head())
# Mid-Career
high_mid = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
print(high_mid[['Undergraduate Major', 'Mid-Career Median Salary']].head())
# grouping
print(clean_df.groupby('Group').count())
# print(clean_df.groupby('Group').mean())
pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group')[['Spread', 'Starting Median Salary', 'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary', 'Mid-Career 90th Percentile Salary']].mean())

# Extra Credit get today's figures with Webscrapping
table_from_html = pd.read_html("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
df = table_from_html[0].copy()
df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]
for page_no in range(2, 35):
    table_from_html = pd.read_html(f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page_no}")
    page_df = table_from_html[0].copy()
    page_df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]
    df.add(page_df)
df = df[["Major", "EarlyCareerPay", "MidCareerPay"]]
df.replace({"^Major:": "", "^Early Career Pay:\$": "", "^Mid-Career Pay:\$": "", ",": ""}, regex=True, inplace=True)
df[["EarlyCareerPay", "MidCareerPay"]] = df[["EarlyCareerPay", "MidCareerPay"]].apply(pd.to_numeric)
print(df.nlargest(5, 'EarlyCareerPay'))
print(df.nlargest(5, 'MidCareerPay'))