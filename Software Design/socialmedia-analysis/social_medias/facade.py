from social_medias import TwitterAPI, InstagramAPI


class SocialMediaFacade:
    def __init__(self):
        self.twitter = TwitterAPI()
        self.instagram = InstagramAPI()
    
    def get_user(self, platform, username):
        if platform == 'twitter':
            return self.twitter.get_user(username)
        elif platform == 'instagram':
            return self.instagram.get_user(username)
        else:
            raise ValueError("Unsupported platform")

    def get_latest_posts(self, platform, username):
        if platform == 'twitter':
            return self.twitter.get_latest_tweets(username)
        elif platform == 'instagram':
            return self.instagram.get_latest_posts(username)
        else:
            raise ValueError("Unsupported platform")
