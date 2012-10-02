import unittest
import hello

class FlaskIntegration(unittest.TestCase):

  def setUp(self):
    self.myapp = hello.app.test_client()

  def testRequestingExistingURLReturnsCorrectResponse(self):
    response = self.myapp.get('/')
    self.assertEqual('Hello World!', response.data)
  
  def testRequestingNonExistentURLReturns404(self):
    response = self.myapp.get("/madeupurl")
    self.assertEqual(404, response.status_code)

if __name__ == '__main__':
  unittest.main()
