import os

class InputHandler:
    def __init__(self):
        pass

    @staticmethod
    def InputValue():
        sanitize_results = {}
        input_dict = {
            "table_name": os.getenv('table_name'),
            "table_type": os.getenv('table_type'),
            "business_key": os.getenv('business_key'),
            "incremental_key": os.getenv('incremental_key'),
            "parent_dag": os.getenv('parent_dag'),
            "redshift_ddl": os.getenv('redshift_ddl')
        }
        for key, value in input_dict.items():
            if isinstance(value, str):
                sanitize_value = value.strip().lower()
            else:
                sanitize_value = value
            sanitize_results[key] = sanitize_value
        return sanitize_results