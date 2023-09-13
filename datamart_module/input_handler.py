import os

class InputHandler:
    def __init__(self):
        pass

    @staticmethod
    def InputValue():
        sanitize_results = {}
        input_dict = {
            "table_name": os.getenv('table_name'),
            "table_type": os.getenv('table_type')
        }
        for key, value in input_dict.items():
            if isinstance(value, str):
                sanitize_value = value.strip().lower()
            else:
                sanitize_value = value
            sanitize_results[key] = sanitize_value
        return sanitize_results