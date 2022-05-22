from pyModbusTCP.client import ModbusClient

ADDR = "192.168.0.188"
PORT = 5502

def main():
    client = ModbusClient(ADDR, PORT)
    client.open()
    input = client.read_holding_registers(0)
    print(f"Register value {input}")

if __name__ == "__main__":
    main()
