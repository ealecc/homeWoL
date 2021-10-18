from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

# list of networked machines
# hostname, ip address, status, mac address 
machines = [
    ["edmund-nas", "192.168.0.15", "00:11:32:ee:26:c6"],
    ["orangepizero", "192.168.0.11", "02:42:52:e2:69:a0"],
    ["Edmund's Phone", "192.168.0.130", ""]
]

# default page
@app.route("/")
def index():
    return render_template("index.html", machines=machines)

@app.route("/ping", methods=["GET","POST"])
def ping():
    address = request.get_data().decode('utf-8')
    status = os.system('timeout 1 ping -c 1 ' + address)
    if status == 0:
        return "online"
    return "offline"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")
