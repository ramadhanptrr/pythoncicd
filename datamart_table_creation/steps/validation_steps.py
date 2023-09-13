import sys
import os
import json
# from datamart_module.input_handler import InputHandler
# from datamart_module.validator import Validator,ValidationRule

# #retrieve input
# input_value = InputHandler.InputValue()

# rules = [
#     Validator('table_name',input_value["table_name"]).set_required().set_min_length(3).set_max_length(127),
#     Validator('table_type',input_value["table_type"]).set_required().set_dropdown_list(["presentations"]),
#     Validator('business_key',input_value["business_key"]).set_required().set_min_length(2).set_max_length(127),
#     Validator('incremental_key',input_value["incremental_key"]).set_required().set_valid_list(),
#     Validator('parent_dag',input_value["parent_dag"]).set_required(),
#     Validator('redshift_ddl',input_value["redshift_ddl"]).set_required()
# ]

# validation_results = ValidationRule(rules)

# if validation_results.run() :
#     sys.exit(validation_results.run())
# else:
#     print('validation pass')

# print(os.getenv('incremental_key'))
# print(type(os.getenv('incremental_key')))
incr_key = os.getenv('incremental_key')

if incr_key is not None :
    try:
        json.loads(incr_key)
    except ValueError as e:
        # errors.append(f"ErrorValidator - {self.field_name} is not a valid list")
        print(e)
