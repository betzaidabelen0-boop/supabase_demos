import web

render = web.template.render('mvc/views', base='template')

class Index:

    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()
    