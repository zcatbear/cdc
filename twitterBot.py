import tweepy

auth = tweepy.OAuthHandler('sH7XlU8l61ZDwKCQ8RlTjp8n1', 'DiE7UIZsEiWAEgVbSSPlf5f3UD7CxrOtD4YevvsKEh8rEsBGLL')
auth.set_access_token('2507420954-YUrMIfkMzJ2U8bjubVBbpPxCRBYBaWpMk6Wo6e5', 'iWxjJ1orRZqUZ706W3geQPUeu3HzNEmSzYs9IM5ByRWww')

api = tweepy.API(auth)

persons = api.user_timeline('@enkrona_')
for tweet in persons:
        print tweet.text


        
