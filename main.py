import ubluetooth
import display


class BluetoothHandler:
    def __init__(self):
        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self.ble.irq(self.bt_irq)
        self.ble.config(gap_name='Monocle')

        self.service_uuid = ubluetooth.UUID("0000180F-0000-1000-8000-00805F9B34FB")
        self.characteristic_uuid = ubluetooth.UUID("00002A19-0000-1000-8000-00805F9B34FB")

        self.characteristic = (
            self.characteristic_uuid,
            ubluetooth.FLAG_READ | ubluetooth.FLAG_WRITE,
        )

        self.service = (
            self.service_uuid,
            (self.characteristic,)
        )

        self.ble.config(gatt=(self.service,))
        self.ble.gatts_write(self.ble.gatts_register_services((self.service,))[0][1], b'\x00')

        self.ble.advertise(100, b'\x02\x01\x06' + b'\x03\x03\x0F\x18' + b'\x05\x09Monocle')

    def bt_irq(self, event, data):
        if event == ubluetooth._IRQ_CENTRAL_CONNECT:
            self.central_connected(data[0])
        elif event == ubluetooth._IRQ_CENTRAL_DISCONNECT:
            self.central_disconnected()
        elif event == ubluetooth._IRQ_GATTS_WRITE:
            self.message_received(data[1])

    def central_connected(self, conn_handle):
        print("Central connected:", conn_handle)

    def central_disconnected(self):
        print("Central disconnected")
        self.ble.advertise(100, b'\x02\x01\x06' + b'\x03\x03\x0F\x18' + b'\x05\x09Monocle')

    def message_received(self, attr_handle):
        message = self.ble.gatts_read(attr_handle).decode('utf-8')
        self.display_message(message)

    def display_message(self, message):
        display.CLEAR
        text = display.Text(message, 0, 0, display.WHITE, justify=display.TOP_LEFT)
        display.show(text)


def main():
    bt_handler = BluetoothHandler()


if __name__ == "__main__":
    main()
