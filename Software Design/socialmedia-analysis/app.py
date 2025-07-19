from flask import Flask, render_template, request
from social_medias import SocialMediaFacade

app = Flask(__name__)
facade = SocialMediaFacade()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data', methods=['POST'])
def get_data():
    platform = request.form['platform']
    username = request.form['username']
    user = facade.get_user(platform, username)
    posts = facade.get_latest_posts(platform, username)
    data = {"user_info": user, "posts": posts}
    return render_template('dashboard.html', data=data, platform=platform.capitalize())


if __name__ == '__main__':
    app.run(debug=True, port=8080)
