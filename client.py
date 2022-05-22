from pyModbusTCP.client import ModbusClient

ADDR = "192.168.0.188"
PORT = 5502

def main():
    client = ModbusClient(ADDR, PORT)
    client.open()
    input = client.read_discrete_inputs(0, 100)
    print(f"Register value {input}")

if __name__ == "__main__":
    main()
