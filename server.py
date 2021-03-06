"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULT = [
    'smelly', 'strange', 'goofy', 'weird']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
    Hi! This is the home page.
    <a href="/hello">Click!</a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    

    # which_page = choice(["/greet", "/diss"])

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action= "/greet">
          <h3>Get a greeting</h3>
          What's your name? <input type="text" name="person"><br>
          <input type="radio" name="tone" value="compliment">Compliment
          <input type="radio" name="tone" value="insult">Insult<br>
          Level: 
            <select name="level">
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
            </select><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

# <form action="/diss">
#   <h3>Now get dissed!</h3>
#   What's your name? <input type="text" name="person"><br>
#   Diss:
#     <select name="diss">
#       <option value='smelly'>Smelly</option>
#       <option value='strange'>Strange</option>
#       <option value='goofy'>Goofy</option>
#     </select><br>
#   <input type="submit" value="Submit">
# </form>

# Compliment:
#             <select name="compliment">
#               <option value='brilliant'>Brilliant</option>
#               <option value='coolio'>Coolio</option>
#               <option value='wowza'>Wowza</option>
#             </select><br>


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    level = request.args.get("level")

    tone = request.args.get("tone")

    # compliment = choice(AWESOMENESS)
    if tone == "compliment":
      if level == "1":
        compliment = "comp1"
      if level == "2":
        compliment = "comp2"
      if level == "3":
        compliment = "comp3"
    elif tone == "insult":
      if level == "1":
        compliment = "ins1"
      if level == "2":
        compliment = "ins2"
      if level == "3":
        compliment = "ins3"



    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = choice(INSULT)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
