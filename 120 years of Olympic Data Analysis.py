#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


events=pd.read_csv(r"C:\Users\Gopal\Downloads\athlete_events.csv\athlete_events.csv")
noc=pd.read_csv(r"C:\Users\Gopal\Downloads\noc_regions.csv")


# In[3]:


events.head()


# In[4]:


noc.head()


# In[5]:


df=events.merge(noc, on='NOC', how='left')


# In[6]:


df.head()


# In[7]:


print('The shape of the dataset : ', df.shape)


# ### Columns name 

# In[8]:


df.columns


# ### Data types present in the columns 

# In[9]:


df.dtypes


# ### Summary of dataset 

# In[10]:


df.info()


# In[11]:


df.nunique()


# ### Statistical properties of dataset
# 

# In[12]:


df.describe().T


# In[13]:


df.describe(include=['object']).T


# In[14]:


df.isnull().sum()


# In[15]:


events=df.groupby(['Year', 'Season', 'City'], as_index=False).first()


# In[16]:


events.head()


# ## Summer Olympics 

# In[17]:


event_summer = events.loc[(events['Season']=='Summer'),['Year','Season','City']]


# In[18]:


event_summer


# ## Winter Olympics

# In[19]:


event_winter=events.loc[(events['Season']=='Winter'),['Year','Season','City']]


# In[20]:


event_winter


# ### Number of unique sports in olympic

# In[21]:


print(df['Sport'].unique())


# In[22]:


print(df['Sport'].nunique())


# In[23]:


plt.scatter(df.Height, df.Weight)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()


# In[24]:


sns.scatterplot(x='Height', y='Weight', hue='Sex', data=df)
plt.show()


# In[25]:


#  using discrete color scheme
sns.scatterplot(x='Height', y='Weight', hue='Sex', data = df, palette='Set2')
plt.show()


# In[26]:


## using this graph we can find out most of the people are of which age
sns.displot(df['Age'])
plt.show()


# In[27]:


## Histogram
plt.hist(df.Age)
plt.ylabel("Frequency")
plt.xlabel("Age")
plt.show()


# In[28]:


sns.countplot(x="Sex", data=df, palette = 'Set3')
plt.show()


# ### Top Countries in Olympic Medals

# In[29]:


topc = df.groupby('region')['Medal'].count().reset_index()
topc


# In[30]:


topc = df.groupby('region')['Medal'].count().nlargest(20).reset_index()


# In[31]:


topc.head(20)


# In[32]:


plt.figure(figsize=(12, 10))
sns.barplot(x='region', y='Medal', data=topc)
plt.xlabel('regions')
plt.ylabel('Number of medals')
plt.title('Top Countries in Olympic Medals')
plt.xticks(rotation=45)
plt.show()


# In[33]:


df.head()


# ### Number of medals of countries in summer olympics

# In[34]:


df[df['Season'] == 'Summer'].groupby(['region', 'Medal']).size().reset_index()


# In[35]:


summer_medals = df[df['Season']=='Summer'].groupby(['region', 'Medal']).size().reset_index()
summer_medals.columns =['region','Medal', 'count']


# In[36]:


##summer_medals = df.groupby(['region', 'Medal']).size().reset_index()
#summer_medals.columns =['region','Medal', 'count']


# In[37]:


summer_medals.pivot('region','Medal', 'count')


# In[38]:


summer_medals.pivot('region','Medal', 'count').fillna(0)


# In[39]:


summer_medals_20 = summer_medals.pivot('region', 'Medal', 'count').fillna(0).sort_values(['Gold'],ascending=False).head(20)


# In[40]:


summer_medals_20.plot(kind='bar')
plt.xlabel('Country')
plt.title('Medals by Country- Summer olympics')
fig = plt.gcf()
fig.set_size_inches(18.5,10.5)
plt.show()


# ### Number of medals in winter olympics 

# In[41]:


winter_medals = df[df['Season']=='Winter'].groupby(['region', 'Medal']).size().reset_index()
winter_medals.columns =['region','Medal', 'count']


# In[42]:


winter_medals.pivot('region','Medal', 'count')


# In[43]:


winter_medals_20 = winter_medals.pivot('region', 'Medal', 'count').fillna(0).sort_values(['Gold'],ascending=False).head(20)


# In[44]:


winter_medals_20.plot(kind='bar')
plt.xlabel('Country')
plt.title('Medals by Country- Winter olympics')
fig = plt.gcf()
fig.set_size_inches(18.5,10.5)
plt.show()


# ### Number of participants by year 

# In[45]:


year=df['Year'].value_counts()


# In[46]:


plt.figure(figsize=(15,10))
sns.barplot(x=year.index, y=year.values)
plt.xticks(rotation=90)
plt.xlabel("Year")
plt.ylabel("Number of athletes")
plt.title("Number of participants by year")
plt.show()


# ### Number of participants by year and gender
# 

# In[47]:


year_sex_medal=df.groupby(['Year', 'Sex'])['Medal'].count().reset_index()


# In[48]:


year_sex_medal.head()


# In[49]:


year_sex_medal_pivot=year_sex_medal.pivot(index='Year', columns='Sex', values='Medal').fillna(0)


# In[50]:


year_sex_medal_pivot.head()


# In[51]:


plt.figure(figsize=(20,10))
fig=plt.gcf()
year_sex_medal_pivot.plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Number of participants')
plt.title('Number of participants by year and gender')
plt.show()


# ### Number of events in each sports in the summer olympics 

# In[52]:


sport_summer=df[df['Season']=='Summer']['Sport'].value_counts().sort_values(ascending=False).head(20)


# In[53]:


sport_summer.head()


# In[54]:


plt.figure(figsize=(15,10))
sns.barplot(y=sport_summer.index, x=sport_summer.values, palette='magma')
plt.xlabel('Number of events')
plt.ylabel('Sport')
plt.xticks(rotation=90)
plt.title("Number of events in each sport in the summer olympics")
plt.show()


# ### Number of events in each sport in the winter olympics 

# In[55]:


sport_winter=df[df['Season']=='Winter']['Sport'].value_counts().sort_values(ascending=False)


# In[56]:


sport_winter.head()


# In[57]:


plt.figure(figsize=(15,10))
sns.barplot(y=sport_winter.head(20).index, x=sport_winter.head(20).values, palette='magma')
plt.xlabel('Number of events')
plt.ylabel('Sport')
plt.xticks(rotation=90)
plt.title("Number of events in each sport in the winter Olympics")
plt.show()


# ### How many different countries compete in the Summer Olympics each year? 

# In[58]:


summer_year_region=df[df['Season']=='Summer'].groupby('Year')['region'].nunique()


# In[59]:


plt.figure(figsize=(12, 8))
sns.pointplot(x=summer_year_region.index, y=summer_year_region.values)
plt.xticks(rotation=90)
plt.xlabel("Year")
plt.ylabel('Different country number')
plt.show()


# ### Male-Female Ratio in olympics 

# In[60]:


sex_count=df.groupby(['Year', 'Sex'])['ID'].nunique().reset_index()


# In[61]:


sex_count.head()


# In[62]:


sex_count.columns=['Year','Sex','count']


# In[63]:


sex_count_pivot=sex_count.pivot(index='Year', columns='Sex', values='count').fillna(0)


# In[64]:


plt.figure(figsize=(20,10))
sex_count_pivot.plot(kind='bar')
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.xlabel("Year")
plt.ylabel("number of athletes")
plt.title("Male-Female Ratio in olympics")
plt.show()


# ### Medals by age 

# In[65]:


age_medal=events.groupby('Age')['Medal'].count().reset_index()


# In[66]:


age_medal.head()


# In[67]:


plt.figure(figsize=(20,10))
sns.barplot(x='Age',y='Medal', data=age_medal)
plt.title('Medals by age')
plt.xlabel('Age')
plt.ylabel('Number of medals')
plt.show()


# ### Age- Distribution of Gold Medals 

# In[68]:


goldMedal=df[df['Medal']=='Gold']
goldMedal.head()


# In[69]:


import warnings
warnings.filterwarnings('ignore')
plt.figure(figsize=(20, 10))
plt.tight_layout()
sns.countplot(goldMedal['Age'])
plt.xticks(rotation=90)
plt.title('Distribution of Gold Medals')
plt.show()


# In[ ]:





# In[70]:


country=df[df['region']=='India']
country.head()


# In[71]:


India=df[df['region']=='India'].groupby(['Name', 'Medal']).size().reset_index()
India.columns=['Name','Medal','count']
India


# In[72]:


India.pivot('Name','Medal', 'count').fillna(0)


# In[73]:


India_medals_20 = India.pivot('Name', 'Medal', 'count').fillna(0).sort_values(['Gold'],ascending=False).head(20)


# In[74]:


India_medals_20.plot(kind='bar')
plt.xlabel('Name')
plt.title('Medals won by Indians olympics')
fig = plt.gcf()
fig.set_size_inches(18.5,10.5)
plt.show()

