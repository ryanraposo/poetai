from hand import Hand


if __name__ == '__main__':

    hand = Hand()

    lines = [
        "Pour euphoric still in Neverland",
        "Torrents mourn the wind's intelligence",
        "Hot blown cold as winter's peace"
    ]
    
    biases = [.75 for i in lines]
    styles = [5 for i in lines]
    stroke_colors = ['black' for i in lines]
    stroke_widths = [1.2 for i in lines]
    background_color = None
    
    hand.write(
        filename='img/pour.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths,
        center_align=False,
        line_height=40,
        background_color=background_color,
        output_png=True
    )
