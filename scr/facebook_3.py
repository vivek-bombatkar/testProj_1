import facebook
import config


graph = facebook.GraphAPI(access_token=config.ACCESS_TOKEN_FB,version="2.1")
#post=graph.get_object(id='162856757783225', fields='message')
#print post["message"]
#event = graph.get_object(id='162856757783225',fields='attending_count,declined_count')
#print(event['attending_count'])
#print(event['declined_count'])

users = graph.search(type='user',q='Mark Zuckerberg')
for user in users['data']:
    print('%s %s' % (user['id'],user['name'].encode()))



