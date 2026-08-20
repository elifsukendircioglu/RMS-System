import asyncio
import logging
from generate_config import generate_config_json
from ModbusKurulum import ModbusKurulum
from RegisterManager import RegisterManager
from Veri import Veri

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


async def simulation_loop(veri, rm, params, interval=5):

    while True:
        veri.update()

        for item in params:
            param_name = item["name"]
            address = item["address"]
            val = veri.data_store.get(param_name, 0.0)
            
            rm.write_float(address, val)

        log_messages = []
        for item in params:
            p_name = item["name"]
            p_unit = item.get("unit", "")
            p_val = veri.data_store.get(p_name, 0.0)
            log_messages.append(f"{p_name.capitalize()}: {p_val:.2f} {p_unit}")

        logging.info(" | ".join(log_messages))

        await asyncio.sleep(interval)


if __name__ == "__main__":
    params = generate_config_json()

    mk = ModbusKurulum(port=5020)
    mk.server_start()

    veri = Veri(params)
    rm = RegisterManager(mk.context)

    try:
        asyncio.run(simulation_loop(veri, rm, params, interval=10))

    except (KeyboardInterrupt, SystemExit):
        print("\nSimülasyon durduruldu.")