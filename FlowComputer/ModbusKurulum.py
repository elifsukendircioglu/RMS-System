import asyncio
import threading
import logging
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext, ModbusSlaveContext

class ModbusKurulum:

    def __init__(self, host="0.0.0.0", port=5020):
        self.host = host
        self.port = port
        
        store = ModbusSlaveContext(
            hr=ModbusSequentialDataBlock(0, [0] * 5000)
        )
        self.context = ModbusServerContext(slaves=store, single=True)

    def server_start(self):
        def run_server():
            asyncio.run(StartAsyncTcpServer(context=self.context, address=(self.host, self.port)))
        
        thread = threading.Thread(target=run_server, daemon=True)
        thread.start()
        logging.info(f"Modbus TCP Server {self.host}:{self.port} portunda çalışıyor.")