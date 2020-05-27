# Inventory Manager
A manager for inventory.

## Deps
You're gonna need apache2, pip3, flask

(make sure you have internet connection before proceeding)

### Apache
```$ sudo apt install apache2```
Once that's done check if it's working by going to a browser (on the same network as the Pi/computer) and typing in its ip address (you can get this by typing in ```$ ip addr show|grep 192``` and take the one before .255)

If it worked you should now see a cool little page saying hey apache worked.

### Pip3
```$ sudo apt install python3-pip```

### Flask
```$ sudo apt install flask```
```$ pip3 install flask```

## Setup
( all of this is in a terminal just so you know )
1. Direct yourself to wherever you cloned
2. Execute ```$ echo FLASK_APP=main.py```
3. Execute ```$ flask run```
  3a. Ensure that ran properly (no errors, says something along the lines of ```Serving Flask app "main.py" blah blah blah```
  3b. Hit Ctrl+C to kill it, that was a test run
    3ba. If something went wrong call me
4. Navigate to ```/etc/apache2/sites-available```
5. Execute ```$ sudo mv 000-default.conf 000-default-old.conf```
6. Execute ```$ sudo cp <WHEREVER YOU CLONED>/000-default.conf ./```
  6a. If you execute ```$ ls``` it should have 3 entries: ```000-default.conf 000-default-old.conf default-ssl.conf```
  6b. If not, call me
7. Execute ```$ sudo systemctl restart apache2.service```
8. Navigate back to where you cloned
9. Restart the flask server (step 3)
10. If all went well you should be able to go to any browser on the same network and type in the address to the raspberry pi and see the inventory manager

Good luch & have fun
