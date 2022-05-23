from pyModbusTCP.client import ModbusClient

ADDR = "192.168.0.188"
PORT = 5502

def main(addr, port):
    client = ModbusClient(addr, port)
    client.open()
    input = client.read_discrete_inputs(0, 100)
    print(f"Register value {input}")

if __name__ == "__main__":
    addr = input("Enter address of modbus master:\n")
    port = input("Enter port:\n")
    main(addr, port)
