# import unittest
# from social_media import SocialMedia
#
# class TestSocialMedia(unittest.TestCase):
#     def setUp(self):
#         self.social_media = SocialMedia('Stefan', 'Instagram', 100, 'Test')
#
#     def test_constructor(self):
#         self.assertEqual(self.social_media._username, 'Stefan')
#         self.assertEqual(self.social_media._platform, 'Instagram')
#         self.assertEqual(self.social_media._followers, 100)
#         self.assertEqual(self.social_media._content_type, 'Test')
#         self.assertEqual(self.social_media._posts, [])
#
#     def test_platform_property(self):
#         self.assertEqual(self.social_media.platform, 'Instagram')
#
#     def test_followers_property(self):
#         self.assertEqual(self.social_media.followers, 100)
#
#     def test_platform_property_setter(self):
#         self.social_media.platform = 'Twitter'
#         self.assertEqual(self.social_media.platform, 'Twitter')
#
#     def test_followers_property_setter(self):
#         self.social_media.followers = 200
#         self.assertEqual(self.social_media.followers, 200)
#
#     def test_invalid_followers_property_setter(self):
#         with self.assertRaises(ValueError):
#             self.social_media.followers = -50
#
#     def test_invalid_platform_property_setter(self):
#         with self.assertRaises(ValueError):
#             self.social_media.platform = 'Facebook'
#
#     def test_create_post(self):
#         post_message = self.social_media.create_post('This is a test post.')
#         self.assertEqual(post_message, 'New Test post created by Stefan on Instagram.')
#         self.assertEqual(len(self.social_media._posts), 1)
#
#     def test_like_post(self):
#         self.social_media.create_post('This is a test post.')
#         like_message = self.social_media.like_post(0)
#         self.assertEqual(like_message, 'Post liked by Stefan.')
#         self.assertEqual(self.social_media._posts[0]['likes'], 1)
#
#     def test_invalid_post_index_like_post(self):
#         like_message = self.social_media.like_post(1)
#         self.assertEqual(like_message, 'Invalid post index.')
#
#     def test_comment_on_post(self):
#         self.social_media.create_post('This is a test post.')
#         comment_message = self.social_media.comment_on_post(0, 'Nice post! This is a great content')
#         self.assertEqual(comment_message, 'Comment added by Stefan on the post.')
#         self.assertEqual(len(self.social_media._posts[0]['comments']), 1)
#
#     def test_invalid_comment_length_comment_on_post(self):
#         self.social_media.create_post('This is a test post.')
#         comment_message = self.social_media.comment_on_post(0, 'Short!')
#         self.assertEqual(comment_message, 'Comment should be more than 10 characters.')
#         self.assertEqual(len(self.social_media._posts[0]['comments']), 0)
#
# if __name__ == "__main__":
#     unittest.main()
import unittest
from social_media import SocialMedia

class TestSocialMedia(unittest.TestCase):
    def setUp(self):
        self.social_media = SocialMedia("Stefan", "Instagram", 10000, "photo")

    def test_platform(self):
        self.assertEqual(self.social_media.platform, "Instagram")
        self.social_media.platform = "YouTube"
        self.assertEqual(self.social_media.platform, "YouTube")
        with self.assertRaises(ValueError):
            self.social_media.platform = "Facebook"

    def test_followers(self):
        self.assertEqual(self.social_media.followers, 10000)
        self.social_media.followers = 15000
        self.assertEqual(self.social_media.followers, 15000)
        with self.assertRaises(ValueError):
            self.social_media.followers = -100

    def test_create_post(self):
        post_message = self.social_media.create_post("New photo post")
        self.assertEqual(post_message, "New photo post created by Stefan on Instagram.")
        self.assertEqual(len(self.social_media._posts), 1)

    def test_like_post(self):
        self.social_media.create_post("New photo post")
        for i in range(10):
            like_message = self.social_media.like_post(0)
            self.assertEqual(like_message, "Post liked by Stefan.")
        like_message = self.social_media.like_post(0)
        self.assertEqual(like_message, "Post has reached the maximum number of likes.")

    def test_comment_on_post(self):
        self.social_media.create_post("New photo post")
        comment_message = self.social_media.comment_on_post(0, "Great photo!")
        self.assertEqual(comment_message, "Comment added by Stefan on the post.")
        with self.assertRaises(IndexError):
            self.social_media.comment_on_post(1, "Another comment")

if __name__ == '__main__':
    unittest.main()
