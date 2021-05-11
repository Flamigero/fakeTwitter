""" FakeTwitter tests """

# Test
import unittest

# Model
from fakeTwitter_main import FakeTwitterPage

class FakeTwitterTest(unittest.TestCase):

    def setUp(self):
        os = 'windows'
        self.fakeTwitter = FakeTwitterPage(os)

    def login_test(self):
        self.fakeTwitter.open()
        self.fakeTwitter.login()

    def tearDown(self):
        self.fakeTwitter.quit()

if __name__ == '__name__':
    unittest.main(verbosity=2)        