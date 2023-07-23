import os
from hand import Hand
from flask import Flask, request
import random
import string

app = Flask(__name__)

@app.route("/")
def hello_world():

    text1 = request.args.get('text1')
    style1 = request.args.get('style1')
    bias1 = request.args.get('bias1')

    hand = Hand()

    lines = text1.split('|')
    
    biases = [.75 for i in lines]
    styles = [int(style1) for i in lines]
    stroke_colors = ['black' for i in lines]
    stroke_widths = [1 for i in lines]

    tmpFilename = ''.join(random.choice(string.ascii_lowercase) for i in range(40))

    svgText = hand.write(
        filename='img/'+tmpFilename+'.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths,
        center_align=False,
        line_height=50,
        output_png=False
    )

    del hand

    return "ver13 " + svgText

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
