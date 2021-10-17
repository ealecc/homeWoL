from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

# list of networked machines
# hostname, ip address, status, mac address 
machines = [
  ["edmund-nas", "192.168.0.15", "", "00:11:32:ee:26:c6"],
  ["orangepizero", "192.168.0.11", "", "02:42:52:e2:69:a0	"],
]

# default page
@app.route("/", methods=["GET","POST"])
def index():
  # get machine data from hardcoded lists
  for machine in machines:
    if ping(machine[1]):
      machine[2] = "online"
    else:
      machine[2] = "offline"
  # if a button is pressed, send WoL
  mac = "test"
  if request.method == "POST":
    mac = request.form['mac']
    wake(mac)
  return render_template("index.html", machines=machines, mac=mac)

# run when wake button pressed
@app.route("/wake", methods=["GET","POST"])
def wake(mac):
  os.system("wakeonlan " + mac)
  return

# Ping to see if host is awake
def ping(address):
  response = os.system("ping -c 1 " + address)
  if response == 0:
    return True
  else:
    return False

if __name__ == "__main__":
  app.run(host="0.0.0.0")