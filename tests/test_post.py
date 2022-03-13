
import unittest
from app.models import Post, User

class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username = 'Sharon',password = 'potato', email = 'sharon@em.com')
        self.new_post = Post(content = 'random post content to test', title = 'random test post', user = self.new_user)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))
        self.assertTrue(isinstance(self.new_user,User))

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

    def test_get_posts_by_id(self):
        self.new_post.save_post()
        got_post = Post.get_posts(1)
        self.assertTrue(len(got_post) == 1)

    def test_delete_post(self):
        got_post = Post.get_posts(id = self.new_post.id)
        self.new_post.delete_posts(got_post)
        self.assertTrue(len(Post.query.all())==0)

    