import sys
import os
from datamart_module.input_handler import InputHandler
from datamart_module.validator import Validator,ValidationResults

#retrieve input
input_value = InputHandler.InputValue()

rule = [
    Validator('table_name',input_value["table_name"]).set_required().set_min_length(3).set_max_length(127),
    Validator('table_type',input_value["table_type"]).set_required().set_dropdown_list(["presentations"])
]

validate_input = ValidationRule(rule)

if validate_input.run :
    sys.exit(validation_results)
else:
    print('validation pass')


