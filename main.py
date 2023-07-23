import os
from hand import Hand
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    args = request.args

    text = args.get("text", default="Hello World!!!", type=str)
    style = args.get("style", default="1", type=str)

    hand = Hand()

    lines = [
        "Writer has written",
        "One writes in kind",
        "You see the mind",
        "Source begets source",
        "Begets source"
    ]
    
    biases = [.75 for i in lines]
    styles = [5 for i in lines]
    stroke_colors = ['black' for i in lines]
    stroke_widths = [1 for i in lines]
    
    svgText = hand.write(
        filename='img/source.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths,
        center_align=False,
        line_height=50,
        output_png=False
    )

    return "ver11 " + text + " - " + svgText

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
