import hello
import unittest
import sys

class TestFlaskArticle(unittest.TestCase):

  def test_get_articles_returns_specific_article(self):
    function_output = hello.article_big_list()
    expected_output = 'all articles!'
    self.assertEqual(function_output, expected_output)

if __name__ == '__main__':
  unittest.main()
