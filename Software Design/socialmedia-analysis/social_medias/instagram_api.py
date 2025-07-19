import instaloader

class InstagramAPI:
    def __init__(self):
        self.loader = instaloader.Instaloader()

    def get_user(self, username):
        profile = instaloader.Profile.from_username(self.loader.context, username)
        return {
            "name": profile.full_name,
            "bio": profile.biography,
            "user_id": profile.userid,
            "username": profile.username,
            "follower_count": profile.followers,
            "following_count": profile.followees,
            "profile_pic_url": profile.profile_pic_url,
        }

    def get_latest_posts(self, username):
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)
            latest_posts = []
            for post in profile.get_posts():
                if len(latest_posts) >= 5:
                    break
                latest_posts.append({
                    'created_at': post.date,
                    'text': post.caption,
                    'images': [post.url],
                    "likes": post.likes,
                })
            return latest_posts
        except instaloader.exceptions.ProfileNotExistsException:
            print(f"Error: The profile {username} does not exist.")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []

