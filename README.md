# stadtwinzerei.lab
Python Code for Cloud based Wine Cellar Monitoring

## Prerequisites
* raspberry pi 3
* python3 installed
* a bunch of sensors connected to the rasp
* google cloud service account with permissions to edit a google spreadsheet

## Installation as systemd service

In order to start the sensor reporter script each time the Raspberry Pi boots the following steps should be carried out

1. Copy .service file into systemd folder (adopt working-diretory variable if necessary)
    ```bash
    sudo cp sensor-reporter.service /etc/systemd/system/sensor-reporter.service
    ```
2. Enable service to be run at boot time
    ```bash
    sudo systemctl enable sensor-reporter.service
    ```

