from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform 

ADDR = "192.168.0.188"
PORT = 502

def main():
    server = ModbusServer(ADDR, PORT, no_block=True)

    try:
        print(f"Starting server on address {ADDR} on port {PORT}")
        server.start()
        print("server online...")
        state = [0]
        while True:
            DataBank.set_words(0, [666])
            if state != DataBank.get_words(1):
                state = DataBank.get_words(1)
                print(f"Value of register 1 {state}")
                sleep(0.5)
    except KeyboardInterrupt:
        print("\nkeyboard interrupt")
        server.stop()
        print("server stopped...")
    except:
        print("server shutdown...")
        server.stop()
        print("server is offline")
if __name__ == "__main__":
    main()

"""
Modbus Function Codes
    Read Coils               = 0x01
    Read Discrete Inputs     = 0x02
    Read Holding Registers   = 0x03
    Read Input Registers     = 0x04
    Write Single Coil        = 0x05
    Write Single Register    = 0x06
    Write Multiple Coils     = 0x0F
    Write Multiple Registers = 0x10
"""
