from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'title':'test post',
            'slug':'test_post',
            'author':'SpaceCadet',
            'timestamp':'2020/09/06 00:00',
            'published':True,
            'body':'This is test content! This one should be visible!',
        },
        {
            'title':'test post 2',
            'slug':'test_post_2',
            'author':'SpaceCadet',
            'timestamp':'2020/09/06 01:00',
            'published':False,
            'body':'This is test content! This one should NOT be visible!',
        }
    ]

    return render_template('index.html', posts=posts)
