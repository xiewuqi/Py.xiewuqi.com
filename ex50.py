import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())
  
class index:
    def GET(slef):
        greetion = "Hello world"
        return greeting
        
if __name__ == "__main__":
     app.run()