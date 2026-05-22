import numpy as np
import pandas as pd

df = pd.read_csv('Countries.csv')
df1 = pd.read_csv('Countries.csv')  # for change in data

#                              -:preprocessing data :-

print( "shape : " ,df.shape , "\n")
print( df.info() , "\n")
#print( df.describe(), "\n" )
print( df.columns, "\n", "\n")



# Question 1. which country has the highest population
print("1. which country has the highest population")

population = ( df['population'] == df['population'].max())
print( df[population][['country','population']] ,"\n")



# Question 2. what is the capital of the country with highest population
print("2. what is the capital of the country with highest population")

max_capital = ( df['population'] == df['population'].max())
print( df[max_capital]['capital_city'] ,"\n")



# Question 3. which country has the least population
print("3. which country has the least population")

least_popu = ( df['population'] == df['population'].min())
print(df[least_popu][['country','population']] ,"\n")



# Question 4. what is the capital of the country with least population
print("4. what is the capital of the country with least population")

least_capital = ( df['population'] == df['population'].min())
print(df[least_capital][['country','capital_city']] ,"\n")



# Question 5. give me top 5 countries with highest democratic score
print("5. give me top 5 countries with highest democratic score")

df1 = df1.sort_values( by='democracy_score' , ascending=False).head(5)
print( df1[['country', 'democracy_score']], "\n")



# Question 6. how many total regions are there
print("6. how many total regions are there")

region = df['region'].value_counts().count()
print(region, "\n")



# Question 7. how many countries lie in Eastern Europe region
print("7. how many countries lie in Eastern Europe region")

east_europe = ( df['region'] == "Eastern Europe" )
print( df[east_europe]['country'], "\n")



# Question 8. who is the political leader of the 2nd highest populated country
print("8. who is the political leader of the 2nd highest populated country")

second = ( df['population'] == df['population'].nlargest(2).iloc[1] )
print( df[second]['political_leader'] ,"\n")



# Question 9. how many countries are there whoes political leaders are unknown
print("9. how many countries are there whoes political leaders are unknown")

unknown = ( df['political_leader'].isna() )
print(df[unknown]['country'].count() , "\n")



# Question 10. how many country have Republic in their full name
print("10. how many country have Republic in their full name")

count = 0
def count_country (txt) :
    global count
    if "republic" in txt.lower() :
        count += 1
    return txt

df['country_long'] = df['country_long'].apply(count_country)
print( count, "\n")



# Question 11. which country in african region has highest population
print("11. which country in african region has highest population")

african_df = df[ df['continent'] == "Africa" ]
pop = ( african_df['population'] == african_df['population'].max() )

print( african_df[pop]['country'])
