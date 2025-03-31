class Command:
    # def __init__(self, name, number_of_parameters, parameter_list):
    #     self.name = name
    #     self.number_of_parameters = number_of_parameters
    #     self.parameter_list = parameter_list

    # def __init__(self, name, number_of_parameters, parameter_list, breakpoint_info):
    #     self.name = name
    #     self.number_of_parameters = number_of_parameters
    #     self.parameter_list = parameter_list
    #     self.breakpoint_info = breakpoint_info

    # def __init__(self, name, number_of_parameters, parameter_list, breakpoint_info=None):
    #     self.name = name
    #     self.number_of_parameters = number_of_parameters
    #     self.parameter_list = parameter_list
    #     if breakpoint_info is not None:
    #         self.breakpoint_info = breakpoint_info

    def __init__(self, *args):
        if len(args) == 3:
            self.name = args[0]
            self.number_of_parameters = args[1]
            self.parameter_list = args[2]
        if len(args) == 4:
            self.name = args[0]
            self.number_of_parameters = args[1]
            self.parameter_list = args[2]
            self.breakpoint_info = args[3]

    def __str__(self):
        parameters_string = ""
        for i in range(self.number_of_parameters):
            parameters_string = parameters_string + str(self.parameter_list[i]) + " "
        if hasattr(self, "breakpoint_info"):
            return f"{self.name}, {self.number_of_parameters} parameters: {parameters_string} \nbreakpoint info: upper bound {self.breakpoint_info.upper_bound} lower bound {self.breakpoint_info.lower_bound}"
        else:
            return f"{self.name}, {self.number_of_parameters} parameters: {parameters_string}"

class BreakpointInfo:
    def __init__(self, parameter_index, lower_bound, upper_bound):
        self.parameter_index = parameter_index
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound