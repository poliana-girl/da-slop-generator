class Command:
    def __init__(self, name, number_of_parameters, parameter_list):
        self.name = name
        self.number_of_parameters = number_of_parameters
        self.parameter_list = parameter_list

    def __str__(self):
        parameters_string = ""
        for i in range(self.number_of_parameters):
            parameters_string = parameters_string + str(self.parameter_list[i]) + " "

        return f"{self.name}, {self.number_of_parameters} parameters: {parameters_string}"