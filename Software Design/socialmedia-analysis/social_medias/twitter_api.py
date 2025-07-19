import requests
import tweepy

class TwitterAPI:
    def __init__(self):
        self.rapid_api_key = "2fb86e469dmsh88fe43922238e96p1fdc27jsn719ba5770ad1"
        self.rapid_api_host = "twitter154.p.rapidapi.com"
        
        self.api_headers = {
            	"X-RapidAPI-Key": self.rapid_api_key,
	            "X-RapidAPI-Host": self.rapid_api_host
        }

    def get_user(self, username):
        response = requests.get(
            "https://twitter154.p.rapidapi.com/user/details",
            headers=self.api_headers,
            params={"username": username}
        )
        user = response.json()
        
        return {
            "name": user["name"],
            "bio": user["description"],
            "user_id": user["user_id"],
            "username": user["username"],
            "follower_count": user["follower_count"],
            "following_count": user["following_count"],
            "profile_pic_url": user["profile_pic_url"],
        }

    def get_latest_tweets(self, username):
        querystring = {"username":username,"limit":"5","include_replies":"false","include_pinned":"false"}
        
        response = requests.get(
            "https://twitter154.p.rapidapi.com/user/tweets",
            headers=self.api_headers,
            params=querystring
        )
        tweets = response.json()["results"]

        return [
            {
                'text': tweet["text"],
                'created_at': tweet["creation_date"],
                "images": tweet["media_url"],
                "likes": tweet["favorite_count"],
            }
            for tweet in tweets
        ]
