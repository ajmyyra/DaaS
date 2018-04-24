import socket, os, random, datetime
from flask import Flask

application = Flask(__name__)
dogdir = "doggos.d"

@application.route("/")
def hello():
    log_visit("/")
    return "Greetings from Doggo as a Service (DaaS) endpoint "+socket.gethostname()+"\nVisit /doggo to get actual content.\n"

@application.route("/doggo")
def show_doggo():
    log_visit("/doggo")
    return get_dog()

def log_visit(uri):
    currenttime=datetime.datetime.today().strftime('%Y-%m-%d %H:%m:%S')
    print(currenttime + " Access to " + uri + " in " + socket.gethostname() + ".\n")
    
def get_dog():
    dogs = []
    for filename in os.listdir(dogdir):
        if filename.endswith(".dog"):
            with open(dogdir + "/" + filename) as f:
                dogs.append(f.readlines())
    
    dognumber = random.randint(0, len(dogs)-1)
    combined_dog = ""
    for line in dogs[dognumber]:
        combined_dog += line

    return combined_dog

if __name__ == "__main__":
    application.run(host="0.0.0.0")
