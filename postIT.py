from flask import Flask,render_template,url_for
app= Flask(__name__)


# creating dummy data, which contains an array called 'posts' that holds  dictionary with key and value
Jan_posts=[
    # Creating the 1st dictionary
    {
        'author':"Osama A",
        'title': "Blog TITLE 1",
        "content": "First post content",
        "date_posted":"Jan 1, 2019"
    },
    # Creating the 2nd dictionary
    {
        'author':"Sam X",
        'title': "Blog TITLE 2",
        "content": "second post content",
        "date_posted":"Jan 2, 2019"
    },
    
]



@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html",Jan_posts=Jan_posts)

@app.route("/about")
def about():
    return render_template("about.html",titleName="About")



if __name__=="__main__": 
    app.run(debug=True)