import eel

eel.init("web")

# to send data from python to javascript


@eel.expose
def get_data():
    return "get data from python"

# get data from javascript


@eel.expose
def send_data(data):
    print("in python", data)


eel.start("main.html")
