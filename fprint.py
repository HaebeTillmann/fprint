import sys

colors = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow" : "33",
    "blue" : "34",
    "purple" : "35",
    "cyan" : "36",
    "white" : "37"
}
styles = {
    "bold": "1",
    "underline" : "4",
    "italic": "3",
    "blink" : "5"
}
background_colors = {
    "black": "40",
    "red": "41",
    "green": "42",
    "yellow" : "43",
    "blue" : "44",
    "purple" : "45",
    "cyan" : "46",
    "white" : "47"
}

def fprint(text, text_color = None, text_style = None, background_color = None):
    color = ""
    style = ""
    back_color = ""

    if text_color is not None:
        color = colors[text_color]
        if text_style is not None or background_color is not None:
            color += ";"

    if text_style is not None:
        style = styles[text_style]
        if background_color is not None:
            style += ";"

    if background_color is not None:
        back_color = background_colors[background_color]

    prefix = f"\033[{color}{style}{back_color}m"

    print(f"{prefix}{text}\033[0m")

def fstr(text, text_color = None, text_style = None, background_color = None):
    color = ""
    style = ""
    back_color = ""

    if text_color is not None:
        color = colors[text_color]
        if text_style is not None or background_color is not None:
            color += ";"

    if text_style is not None:
        style = styles[text_style]
        if background_color is not None:
            style += ";"

    if background_color is not None:
        back_color = background_colors[background_color]

    prefix = f"\033[{color}{style}{back_color}m"

    return(f"{prefix}{text}\033[0m")


def prev():
    sys.stdout.write("\033[F")
