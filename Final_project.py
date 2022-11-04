import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')



st.title('Top Spotify songs from 2010-2019 - BY YEAR')
df = pd.read_csv('top10s.csv')



#滑块
popularity_filter = st.slider('pop', 0, 99, 40)


#top插件
top_genre_filter = st.sidebar.multiselect(
     'Music type',
     df.top_genre.unique(),  
     df.top_genre.unique())  


#pop插件
pop_filter = st.sidebar.radio(
    'Choose the pop level',
    ('All','Low', 'Medium', 'High'))
if pop_filter == 'Low':
    df = df[df['pop'] <= 50]
elif pop_filter == 'Medium':
    df = df[(df['pop'] < 75) & (df['pop'] > 50)]
else:
    df = df[df['pop'] > 75]


# create a input form
form = st.sidebar.form('title_form')
title_filter = form.text_input('Song Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

df = df[df['pop'] >= popularity_filter]

df = df[df.top_genre.isin(top_genre_filter)]

if title_filter!='ALL':
    df = df[df.title == title_filter]


#表1;哪一种音乐类型的流行度更广？
st.subheader('Which music genre has the most popular songs, based on spotify data?')
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_title('The relationship between genre and popularity of popular songs') 
pop = df.groupby('top_genre')['pop'].mean().sort_values().plot.bar(ax=ax)
ax.set_ylabel('pop') 

plt.xticks(size=10)
plt.yticks(size=10)
st.pyplot(fig)
fig, ax = plt.subplots(figsize=(12,12))

df.groupby('top_genre')['pop'].mean().sort_values().plot.pie(ax=ax,autopct='%1.1f%%')

st.pyplot(fig)



#Evaluate the popularity of popular music every year
st.subheader('Based on spotify data, in which year did songs written have the highest popularity?')

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_title('Evaluate the popularity of popular music every year')
pop = df.groupby('year')['pop'].mean().sort_values().plot.bar(ax=ax)
ax.set_ylabel('pop') 

plt.xticks(size=10)
plt.yticks(size=10)
st.pyplot(fig)
fig, ax = plt.subplots(figsize=(10, 5))

df.groupby('year')['pop'].mean().sort_values().plot.pie(ax=ax,autopct='%1.1f%%')

st.pyplot(fig)


#type of pop music is most favored by singers
st.subheader('The amount of different kinds of popular music being created')
fig, ax = plt.subplots(figsize=(10,10))

df.top_genre.hist(bins=30)
plt.xticks(rotation=60)
st.pyplot(fig)


#图表
st.subheader('Music Details:')
st.write(df[['title', 'artist', 'top_genre','pop']])


#总结

st.header('Summary:For the first question,pop has the most popular songs based on spotify data.For the second question,2019 was the most popular year ever for pop songsbased on spotify data')