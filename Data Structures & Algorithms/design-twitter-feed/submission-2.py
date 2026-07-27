import time
import heapq
class Twitter:
    user_follower_map = {
        # "2": [
        #     "1"
        # ]
    }
    user_tweets = {
        # "2" : [
        #     ( time.time(): 20 ),
        #     ( time.time(): 30 ),
        # ]
    }
    def __init__(self):
        self.user_follower_map = {}
        self.user_tweets = {}  

    def postTweet(self, userId: int, tweetId: int) -> None:
        curr_user_tweets = self.user_tweets[userId] if userId in self.user_tweets else None
        tweet = (time.time(), tweetId)        
        if not curr_user_tweets:
            # Replace the list in the dict with a new one containing the tweet
            self.user_tweets[userId] = [tweet]
        else:
            # Mutate the existing list
            curr_user_tweets.append(tweet)
                       

    def getNewsFeed(self, userId: int) -> List[int]:
        curr_followers = self.user_follower_map[userId] if userId in self.user_follower_map else []
        # iterate through the followers list of userId then club all of their tweets based on time sorted upto 10
        user_ids = [userId] + curr_followers
        tweets_of_userId = []
        heap = []
        for uid in user_ids:            
            tweets_of_userId += self.user_tweets.get(uid, [])
            
        for _tweet_of_userId in tweets_of_userId:
            heapq.heappush(heap, _tweet_of_userId)
            if len(heap) > 10:
                heapq.heappop(heap)
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        user_followers = self.user_follower_map[followerId] if followerId in self.user_follower_map else []
        curr_followers = list(set(user_followers))
        if followeeId is followerId:
            return
        if not curr_followers:
            self.user_follower_map[followerId] = [followeeId]
        else:
            curr_followers.append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        curr_followers = self.user_follower_map[followerId] if followerId in self.user_follower_map else []
        try:
            curr_followers.remove(followeeId)
        except ValueError:
            pass
        
