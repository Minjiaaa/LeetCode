class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i=len(self.tweets)-1
        while i>=0 and len(res)<10:
            if self.tweets[i][0] in self.users[userId] or self.tweets[i][0]==userId:
                res.append(self.tweets[i][1])
            i-=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]: self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
