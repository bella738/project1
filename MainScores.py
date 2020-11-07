from flask import Flask

import Utils

app = Flask(__name__)

# show the score
@app.route('/')
def score_server():
    try:
        score = open("./Score.txt", "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.BAD_RETURN_CODE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8777)
