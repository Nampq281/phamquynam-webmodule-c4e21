import mlab
from post import Post

#1. Connect
mlab.connect()

def test_load_data():
    all_post= Post.objects()

post = all_post[0]

test_load_data()

