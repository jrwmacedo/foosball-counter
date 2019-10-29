# Foosbal Counter

 1. A foosball counter developed using mycropython, IR sensors and nodemmcu V3 CH340
 2. Angular 8 for the scoreboard
 3. Mosquitto MQTT server
 
# Materials
 4. Nodemmcu V3 Ch340
 ![[https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/](https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/)](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/05/ESP8266-NodeMCU-kit-12-E-pinout-gpio-pin.png?w=817&ssl=1)
 
 5. Two IR sensors KY032
 ![KY032](https://github.com/jrwmacedo/foosball-counter/blob/master/KY032.png?raw=true)

 6. 4  x push buttons ( 2 x Increase / 2 x Decrease / 1 x Reset)
![Buttons](https://github.com/jrwmacedo/foosball-counter/blob/master/buttons.png?raw=true)

 7. Wires to make the connection based on the pinout configured in the boot.py 
![Wires](https://github.com/jrwmacedo/foosball-counter/blob/master/wires.png?raw=true)
# Python Files

 1. boot.py - Boot configurations (Pinout, Wifi information, MQTT Serve configuration)
 2. button.py - Increase/Decrease/ Reset button configurations
 3. connection.py - Connection/ Subscribe/Publish management
 4. counter.py - Counter class object used by manager information for each team.
 5. main.py - Main file
 6. message.py - Check message status to send to MQTT Server
 7. sensor.py - IR Sensor management
 8. umqttsimple.py - MQTT library used to make easier the communication with the MQTT server  - [https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/MQTT/umqttsimple.py](https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/MQTT/umqttsimple.py)

## Docker files

 1. Dockerfile - Build the Angular application to show the game score.
 ![Angular App Screenshot](https://github.com/jrwmacedo/foosball-counter/blob/master/angular-app-screenshot.png?raw=true)
 3. docker-compose.yml - Setup two containers (Mosquitto MQTT Server and the Angular application)

## Mosquitto configuration file

 1. mosquitto.conf - Configuration file allowing websocket (because of the Angular application) and MQTT protocol.
