from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route('/')
#def home():
 #  return app.send_static_file('index.html')

@app.route('/echo/<thing>/<place>')
def echo(thing, place):
    #thing = request.args.get('thing')
    #place = request.args.get('place')
    return render_template('flask2.html', thing=thing, place=place)

app.run(port=9999, debug=True)