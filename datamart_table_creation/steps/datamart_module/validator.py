import json

class Validator:
    def __init__(self, field_name,value):
        self.field_name = field_name
        self.value = value
        self._max_length = None
        self._min_length = None
        self._required = False
        self._valid_list = False
        self._dropdown_list = None

    @property
    def max_length(self):
        return self._max_length

    @property
    def min_length(self):
        return self._min_length

    @property
    def required(self):
        return self._required

    @property
    def valid_list(self):
        return self._valid_list

    @property
    def dropdown_list(self):
        return self._dropdown_list

    def set_max_length(self, length):
        self._max_length = length
        return self

    def set_min_length(self, length):
        self._min_length = length
        return self

    def set_required(self, default=True):
        self._required = default
        return self

    def set_valid_list(self, default=True):
        self._valid_list = default
        return self

    def set_dropdown_list(self, dropdown_list):
        self._dropdown_list = dropdown_list
        return self

    def validate(self):
        errors = []

        if self.required and (self.value is None or not str(self.value).strip()):
            errors.append(f"ErrorValidator - {self.field_name} is required.")

        if self.max_length is not None and len(str(self.value)) >= self.max_length:
            errors.append(f"ErrorValidator - {self.field_name} should be less than {self.max_length} characters.")

        if self.min_length is not None and len(str(self.value)) < self.min_length:
            errors.append(f"ErrorValidator - {self.field_name} must be at least {self.min_length} characters long.")

        if self.valid_list:
            try:
                json.loads(self.value.strip())
            except ValueError as e:
                errors.append(f"ErrorValidator - {self.field_name} is not a valid list")

        if self.dropdown_list is not None and self.value not in self.dropdown_list:
            errors.append(f"ErrorValidator - Field {self.field_name} is out of range")

        return errors

class ValidationRule:
    def __init__(self, rules):
        self.rules = rules
        self.validation_results = []

        for rule in self.rules:
            errors = rule.validate()
            self.validation_results.extend(errors)

    def run(self):
        return '\n'.join(self.validation_results)