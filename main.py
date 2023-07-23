import os
from hand import Hand
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():

    text1 = request.args.get('text1')
    style1 = request.args.get('style1')
    bias1 = request.args.get('bias1')
    biasFloat = float(int(bias1)) / float(100) 
    styleInt = int(style1) 
    hand = Hand()

    lines = text1.split('|')
    
    biases = [biasFloat for i in lines]
    styles = [styleInt for i in lines]
    stroke_colors = ['black' for i in lines]
    stroke_widths = [1 for i in lines]

    svgText = hand.write(
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths,
        center_align=False,
        line_height=50
    )

    del hand

    return "ver16<br/>style: " + str(styleInt) + "<br/>bias: " + str(biasFloat) + "<br/>"  + svgText

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
