def generate_config_json() -> list[dict]:
    return [
        {
            "name": "flow_rate",
            "type": "float",
            "unit": "m3/h",
            "address": 3998,
            "value": 50.0,
            "mode": "step_bounded",
            "min": 10.0,
            "max": 100.0,
            "step": 2.0
        },
        {
            "name": "pressure",
            "type": "float",
            "unit": "BarA",
            "address": 4000,
            "value": 25.0,
            "mode": "random_range",
            "min": 18.0,
            "max": 40.0
        },
        {
            "name": "temperature",
            "type": "float",
            "unit": "degC",
            "address": 4002,
            "value": 25.0,
            "mode": "step_unbounded",
            "step": 0.2
        }, 
        {
            "name": "gcv",
            "type": "float",
            "unit": "MJ/m3",
            "address": 4004,
            "value": 9.10,
            "mode": "external"
        },
        {
            "name": "energy",
            "type": "float",
            "unit": "kWh",
            "address": 4006,
            "value": 0.0,
            "mode": "calculated",
            "expression": "flow_rate * gcv"
        },
    ]