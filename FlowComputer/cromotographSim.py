def generate_config_json() -> dict:
    return {
        "gcv": {
            "name": "Gross Calorific Value",
            "type": "float",
            "unit": "MJ/m3",
            "base_gcv": 9.10,
            "formula": "(base_gcv+(Methane -91) + (Ethane - 3)*0.04 + (Propane - 0.5)*0.01)"
        },
        "components": [
            {
                "name": "Methane",
                "type": "float",
                "unit": "%",
                "value": 92.5,
                "min": 92.0,
                "max": 92.9,
                "step": 0.1
            },
            {
                "name": "Ethane",
                "type": "float",
                "unit": "%",
                "value": 4.2,
                "min": 4.0,
                "max": 4.9,
                "step": 0.05
            },
            {
                "name": "Propane",
                "type": "float",
                "unit": "%",
                "value": 1.1,
                "min": 0.1,
                "max": 1.9,
                "step": 0.05
            }
        ]
    }