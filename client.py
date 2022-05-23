from pyModbusTCP.client import ModbusClient

ADDR = "192.168.0.188"
PORT = 5502

def main(addr, port, op_code, mod_addr):
    client = ModbusClient(addr, port)
    client.open()
    if op_code == 1:
        coils = client.read_discrete_inputs(mod_addr)
        print(coils)
    elif op_code == 4:
        holding = client.read_holding_registers(mod_addr)
        print(holding)
    else:
        print("Invalide opcode")

if __name__ == "__main__":
    addr = input("Enter address of modbus master:\n->")
    port = input("Enter port:\n->")
    op_code = input("Enter op code:\n\t1. Read Coils\n\t4.Read Holding Register\n->")
    mod_addr = input("Enter modbus address:\n->")
    main(addr, port, int(op_code), int(mod_addr))
