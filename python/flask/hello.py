from flask import Flask
app = Flask(__name__)

def article_big_list():
  return 'all articles!'

@app.route("/")
def hello():	
  return "Hello World!"

@app.route("/articles")
def article_list():
  return article_big_list()

@app.route("/articles/<nid>")
def articles(nid):
  return "returning article with nid %s" % nid

if __name__ == "__main__":
  app.run()
