# check this video about VSCode's Python Interactive mode: 
#   https://www.youtube.com/watch?v=lwN4-W1WR84

# # EDA Test with Netflix data

# ## Import data

# %%
import pandas as pd
import plotly.express as px
import datetime


# %%
# source: https://www.kaggle.com/datasets/shivamb/netflix-shows
df = pd.read_csv('./data/netflix_titles.csv.zip', compression='zip', header=0, sep=',', quotechar='"') #parse_dates=['date_added'], date_parser=lambda x: pd.datetime.strptime(str(x), "%B %d, %Y"))
df.date_added = pd.to_datetime(df.date_added.str.strip(), format='%B %d, %Y')
df.head()


# ## Column check

# %%
df.dtypes


# code to convert column types...not necessary in this case
#df = df.astype({"show_id": int}, errors='raise')
#df.dtypes


# ## Value (NaN) check

# %%
df.isna().sum()

# %%
df.date_added = df.date_added.fillna(pd.Timestamp('19900101')) # set NaN to 01/01/1990


# ## Column release_year
# %%
df.describe() # release year is the only numerical column


# %%
df.release_year.hist() # with Matplotlib

# %%
px.histogram(df, 'release_year') # with plotly ... it allows zooming


# ## What about the oldest movie in the dataset?
# %%
# showing the oldest film in the dataset
df[df.release_year < 1930]

# %%
# printing the full description
row_idx = df[df.release_year < 1930].index[0]
col_idx = df.columns.get_loc("description")
df.iloc[row_idx, col_idx]

# ## Column added_date
# %%
px.histogram(df[df.date_added > datetime.datetime(year=1990,month=1,day=1)], 'date_added', nbins=10, title='10 bins histogram of added_date')

# %%
df['date_added_month'] = pd.DatetimeIndex(df['date_added']).month
px.histogram(df[df.date_added > datetime.datetime(year=1990,month=1,day=1)], 'date_added_month', title='histogram of added_date months')

# %%
df['date_added_day'] = pd.DatetimeIndex(df['date_added']).day
px.histogram(df[df.date_added > datetime.datetime(year=1990,month=1,day=1)], 'date_added_day', title='histogram of added_date days')


# ## Column type
# %%
df.type.unique()

# %%
px.histogram(df[df.date_added > datetime.datetime(year=1990,month=1,day=1)], 'date_added_month', title='histogram of added_date months colored by type', color='type')

# %%
# px.histogram(df_types, 'type')
# Histogram built manually with groupby (just to try...):
df_types = df[df.date_added > datetime.datetime(year=1990,month=1,day=1)]
#df_types['type'].count() # 8797
bar_data = df_types.groupby(['type']).size()
px.bar(bar_data, title='Histogram (obtained with a bar plot) of Movie / TV Show')

# ## Column country
# %%
df.country.unique()

# %%
# drop non defined countries
countries = df.country.dropna()
# split cell with multiple countries movie 
countries_all = countries.str.split(',', expand=True)
countries_all = countries_all.apply(lambda x: x.str.strip())
countries_all = countries_all.fillna('')
countries_all

# %%
countries_unique = pd.concat([countries_all[0], countries_all[1], countries_all[2], countries_all[3], countries_all[4], countries_all[5],   countries_all[6], countries_all[7], countries_all[8], countries_all[9], countries_all[10], countries_all[11]]).unique()
countries_unique

# %%
df_for_countries = df[df.date_added > datetime.datetime(year=1990,month=1,day=1)]
# ... fare istogramma con tutte le nazioni...
# https://www.youtube.com/watch?v=E-q24gS8cqg&list=PLkilSo1vpRstuKw4Iu_Qh6Usz6Gy6c0bi&index=1&t=1871s

