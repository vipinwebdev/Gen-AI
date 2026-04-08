import pandas as pd

filedata = pd.read_csv('../../INvideos.csv')

likes = filedata['likes']
views = filedata['views']
dislikes = filedata['dislikes']
comment_count = filedata['comment_count']
channel_name = filedata['channel_title']
