#first file
#Find posts like "retweet to win"
#If the text includes "follow" then follow them
#Then retweet with their hashtags

#Step one ~ Log into twitter
import tweepy

auth = tweepy.OAuthHandler('CMZftIIuswgVd1ZWqw7ZX2YvW', 'KLkfQqca5vhGTrrIvUkbSqFspfNrL8R8ozTiOqffFvwDxknJTc')
auth.set_access_token('4543331312-bZft183dtSnoYPiI2oue7DJhqY83rg6e66fEpuu', 'bvwqnccHWEcbYbp9Nv74NoyK5MlBAa5zE4RnWZztGNBHX')

api = tweepy.API(auth)

#api.update_status('Testing babe #art')
lastTweet = None
secondLast = None
searchQs = ["retweet to win", "RT to win", "Follow us and retweet", "chance to win"]
for searchQ in searchQs:
    searched_tweets = api.search(q=searchQ, count=100)
    for tweet in searched_tweets:
        lastTweet = tweet.id
        if tweet.retweeted:
            print(0)
            pass
        else:
            #parse text for 'follow', 'favorite'
            textLower = tweet.text.lower()
            text = textLower.encode('ascii','ignore')
            if text.count('rt ') > 0:
                print(1)
                pass
            else:
                if 'follow' in text or 'flw':
                    if tweet.author.following == False and tweet.author.screen_name != 'fajfkg':
                        print('Followed '+tweet.author.screen_name)
                        api.create_friendship(tweet.author.screen_name)
                if 'fav' in text:
                    if not tweet.favorited:
                        print('Favorited ' + text)
                        api.create_favorite(tweet.id)
                #and retweet if I haven't yet
                try:
                    if tweet.retweeted == False:
                        print("Retweeted "+text)
                        api.retweet(tweet.id)
                except:
                    print(4)
                    pass

    print(lastTweet)
    count = 0
while True:
    print(lastTweet)
    secondLast = lastTweet
    count += 1
    print(count)
    for searchQ in searchQs:
        searched_tweets = api.search(q=searchQ, count=100, max_id = lastTweet)
        for tweet in searched_tweets:
            lastTweet = tweet.id
            if tweet.retweeted:
                print(0)
                pass
            else:
                #parse text for 'follow', 'favorite'
                textLower = tweet.text.lower()
                text = textLower.encode('ascii','ignore')
                if text.count('rt ') > 0:
                    print(1)
                    pass
                else:
                    if 'follow' in text or 'flw':
                        if tweet.author.following == False and tweet.author.screen_name != 'fajfkg':
                            print('Followed '+tweet.author.screen_name)
                            api.create_friendship(tweet.author.screen_name)
                    if 'fav' in text:
                        if not tweet.favorited:
                            print('Favorited ' + text)
                            api.create_favorite(tweet.id)
                    #and retweet if I haven't yet
                    try:
                        if tweet.retweeted == False:
                            print("Retweeted "+text)
                            api.retweet(tweet.id)
                    except:
                        print(4)
                        pass