import random
import cromotographSim

class Veri:

    def __init__(self, params):
        self.params = params
        self.data_store = {
            item["name"]: item.get("value", 0.0) for item in params
        }
        self.gc_config = cromotographSim.generate_config_json()

    def calculate_gcv(self) -> float:
        """cromotographSim_2.py dosyasından anlık GCV değerini hesaplar."""
        gcv_info = self.gc_config["gcv"]
        components = self.gc_config["components"]

        eval_vars = {comp["name"]: comp["value"] for comp in components}
        eval_vars["base_gcv"] = gcv_info["base_gcv"]

        try:
            return float(eval(gcv_info["formula"], {}, eval_vars))
        except Exception as e:
            print(f"GCV Hesaplama Hatası: {e}")
            return gcv_info["base_gcv"]

    def update(self):
        
        self.data_store["gcv"] = round(self.calculate_gcv(), 4)
        for item in self.params:
            name = item["name"]
            if name == "gcv":
                continue

            mode = item.get("mode")
            decimals = item.get("decimals", 2)
            current = self.data_store.get(name, 0.0)

            if mode == "random_range":
                min_val = item.get("min", 0.0)
                max_val = item.get("max", 1.0)
                self.data_store[name] = round(random.uniform(min_val, max_val), decimals)

            elif mode == "step_bounded":
                min_val = item.get("min", 0.0)
                max_val = item.get("max", float("inf"))
                step = item.get("step", 1.0)
                next_val = current + random.uniform(-step, step)
                self.data_store[name] = round(max(min_val, min(max_val, next_val)), decimals)

            elif mode == "step_unbounded":
                step = item.get("step", 1.0)
                self.data_store[name] = round(current + random.uniform(-step, step), decimals)

        for item in self.params:
            if item.get("mode") == "calculated":
                name = item["name"]
                expression = item.get("expression")
                decimals = item.get("decimals", 2)

                if expression:
                    try:
                        new_val = eval(expression, {}, self.data_store)
                        self.data_store[name] = round(new_val, decimals)
                    except Exception as e:
                        print(f"Hata ({name}): Hesaplama yapılamadı -> {e}")

    def get_all_data(self):
        """Modbus register'larına aktarabileceğiniz tüm verileri döner."""
        return self.data_store