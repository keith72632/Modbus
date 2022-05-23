from pyModbusTCP.client import ModbusClient

ADDR = "192.168.0.188"
PORT = 5502

def main(addr, port, op_code):
    client = ModbusClient(addr, port)
    client.open()
    if op_code == 1:
        coils = client.read_discrete_inputs(0, 100)
        print(coils)
    elif op_code == 4:
        holding = client.read_holding_registers(101, 100)
        print(holding)
    else:
        print("Invalide opcode")

if __name__ == "__main__":
    addr = input("Enter address of modbus master:\n")
    port = input("Enter port:\n")
    op_code = input("Enter op code:\n\t1. Read Coils\n\t4.Read Holding Register\n\t->")
    main(addr, port, int(op_code))
