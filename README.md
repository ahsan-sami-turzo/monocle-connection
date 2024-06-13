# monocle-connection
This repository contains MicroPython code for the Monocle device to connect and display data from the Android application



### BluetoothHandler Class: This class handles the Bluetooth Low Energy (BLE) functionality.
'''
Initializes the BLE and sets it up to advertise with a custom name "Monocle".
Sets up a custom service and characteristic UUID for communication.
Handles Bluetooth events such as connection, disconnection, and data writes.
'''

### bt_irq Method: This method handles the Bluetooth events:
'''
- ubluetooth._IRQ_CENTRAL_CONNECT: Called when a central device (e.g., an Android phone) connects.
- ubluetooth._IRQ_CENTRAL_DISCONNECT: Called when the central device disconnects.
- ubluetooth._IRQ_GATTS_WRITE: Called when the central device writes data to the characteristic.
'''

### central_connected and central_disconnected Methods: Manage the state of the connection and re-advertise the device when disconnected.

### message_received Method: Reads the message sent from the Android application and displays it on the Monocle screen.

### display_message Method: Displays the received message on the Monocle screen using the display module.

### main Function: Instantiates the BluetoothHandler to start the process.

### Android application UUID 00002A19-0000-1000-8000-00805F9B34FB.