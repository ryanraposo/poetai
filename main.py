import os
from hand import Hand
from flask import Flask

app = Flask(__name__)

if __name__ == '__maxxxxxxxin__':

    hand = Hand()

    lines = [
        "Writer has written",
        "One writes in kind",
        "You see the hand",
        "You see the mind",
        "Source begets source",
        "Begets source",
        "Begets source"
    ]
    
    biases = [.75 for i in lines]
    styles = [5 for i in lines]
    stroke_colors = ['black' for i in lines]
    stroke_widths = [1 for i in lines]
    
    hand.write(
        filename='img/source.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths,
        center_align=False,
        line_height=50,
        output_png=True
    )

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
