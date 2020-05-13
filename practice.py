import pandas as pd 




database = pd.read_csv('movies.csv')
intended_list = database['title_id']
titles = database['title'].unique() 


#line = ['titl33e_id','tit33le','release_33date','poster33_path','youtube33_key','overvi33ew']
#series = pd.Series(line, index = database.columns)
#database = database.append(series, ignore_index=True)


#database.to_csv('movies.csv', mode='a', header=False, index = False) #saves to movies csv

print(database[database['title_id']== 671].index.values)