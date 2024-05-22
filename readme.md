# rpi_talktimer

LED display to indicate time elapsed during a presentation, with a push button to start and stop the sequence. Under the default settings:

- Green LED turns on for 10 minutes
- Yellow LED turns on after 10-12 minutes
- Red LED turns on after 12-14 minutes
- Red LED blinks after 14-15 minutes

To start, run the `talk_timer.py` Python script, e.g. on the command line
```python talk_timer.py```

## Hardware setup

LEDs are connected to GPIO pins and ground with an inline resistor

- Green LED is connected to pin 11 (GPIO 17) 
- Yellow LED is connected to pin 13 (GPIO 27) 
- Red LED is connected to pin 15 (GPIO 22)

 
A push button is connected to 3v3 power and pin 10 (GPIO 15) with an inline pull-down resistor.

## Optional setup

To run the script automatically at startup:

- Make sure the path to this this directory is correct in `launcher.sh`. By default it is located at `/home/pi/Desktop/rpi_talktimer`

- Make `launcher.sh` executable with the command 
```chmod 755 launcher.sh```

- Edit your crontab by typing
```sudo crontab -e```

- Enter the line (making sure to edit the path to `launcher.sh` if necessary
```@reboot sh /home/pi/Desktop/rpi_talktimer/launcher.sh```