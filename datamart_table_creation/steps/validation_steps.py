import sys
import os
# sys.path.append('./')
# from datamart_module.input_handler import InputHandler
# from datamart_module.validator import Validator,ValidationRule

#retrieve input
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

x = os.getenv('redshift_ddl')
print(x)
def test(x):
        try:
        x.get('schema')
        return True
    except:
        return "ErrorValidator - is not a valid dictionary"
print(test(x))