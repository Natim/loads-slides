from loads.case import TestCase


class TestWebSite(TestCase):

    def test_something(self):
        self.assertTrue('island' in self.app.get('/'))
        self.incr_counter('island-was-there')
