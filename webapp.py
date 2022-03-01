from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    word = request.args['word'] 
    number = request.args['number']
   
    if number > 100:
        print("&", number, word.upper(1:3), "##!")
    else:
        print(number, "##", word.upper(1:2), "()!")
        
    if __name__=="__main__":
    app.run(debug=False)
        
render_response()
        
        