from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform, randint 
import traceback

ADDR = "192.168.0.188"
PORT = 5502

def main():
    server = ModbusServer(ADDR, PORT, no_block=True)
    discrete_inputs = []
    holding_registers = []
    for x in range(0, 100): discrete_inputs.append(randint(0, 10))
    for x in range(0, 100): holding_registers.append(randint(0, 65535))
    
    try:
        print(f"Starting server on address {ADDR} on port {PORT}")
        server.start()
        print("server online...")
        state = [0]
        while True:
            DataBank.set_bits(0, discrete_inputs)
            DataBank.set_words(101, holding_registers)
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
        traceback.print_exc()
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
