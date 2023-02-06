# more checks than needed, especially for exceptions, messages in list, can be called by index (0-12)
class HonestCalculator:
    operand_1: None
    operand_2: None
    operator: None
    operators: list[str]
    result: None
    store_result: str
    memory: float
    msg_equitation: str
    msg_laziness: str
    dont_continue: bool
    calculation_ok: bool
    message_index: int
    msg = []
    msg = msg[:len(msg)] + ["Enter an equation"]
    msg = msg[:len(msg)] + ["Do you even know what numbers are? Stay focused!"]
    msg = msg[:len(msg)] + ["Yes ... an interesting math operation. You've slept through all classes, haven't you?"]
    msg = msg[:len(msg)] + ["Yeah... division by zero. Smart move..."]
    msg = msg[:len(msg)] + ["Do you want to store the result? (y / n):"]
    msg = msg[:len(msg)] + ["Do you want to continue calculations? (y / n):"]
    msg = msg[:len(msg)] + [" ... lazy"]
    msg = msg[:len(msg)] + [" ... very lazy"]
    msg = msg[:len(msg)] + [" ... very, very lazy"]
    msg = msg[:len(msg)] + ["You are"]
    msg = msg[:len(msg)] + ["Are you sure? It is only one digit! (y / n)\n"]
    msg = msg[:len(msg)] + ["Don't be silly! It's just one number! Add to the memory? (y / n) \n"]
    msg = msg[:len(msg)] + ["Last chance! Do you really want to embarrass yourself? (y / n) \n"]


    def __init__(self):
        self.operand_1 = None
        self.operand_2 = None
        self.operator = None
        self.operators = ['+', '-', '*', '/']
        self.result = None
        self.memory = 0.0
        self.dont_continue = False
        self.calculation_ok = False
        self.store_result = 'n'
        self.msg_equitation = ""
        self.msg_laziness = ""

    def print_msg(self, msg):
        if msg != "": print(msg)
        print(self.msg[0])


    def check_M(self, x):
        if x == 'M':
            x = self.memory
        return x


    def string_check(self, calc):
        try:
            x, self.operator, y = calc.split(' ')
        except ValueError:
            return False
        try:
            operands_ok = self.check_numbers(self.check_M(x), self.check_M(y))
        except TypeError:
            # print("TypeError {} type: {}, {} type: {}".format(x, type(x), y, type(y)))
            return False
        self.check_laziness(self.operand_1, self.operand_2, self.operator)
        if self.operator not in self.operators:
            self.msg_equitation = self.msg[2]
            return False
        elif self.operand_2 == 0 and self.operator == '/':
            self.msg_equitation = self.msg[3]
            return False
        elif operands_ok:
            self.calculation_ok = True
            self.result = float(self.evaluate(self.operand_1, self.operator, self.operand_2))
            print(self.result)
            return True


    def number_value_error(self):
        self.msg_equitation = self.msg[1]
        return False


    def check_numbers(self, a, b) -> object:
        try:
            float_a = float(a)
            float_b = float(b)
        except ValueError:
            self.msg_equitation = self.msg[1]
            return False
        self.operand_1 = float_a
        self.operand_2 = float_b
        return True

    @staticmethod
    def is_one_digit(v1):  # new in Stage 4/5: The laziness test
        v1 = float(v1)
        return True if v1 > -10 and v1 < 10 and v1.is_integer() else False


    def check_laziness(self, n1, n2, operator) -> object:  # new in Stage 4/5: The laziness test
        self.msg_laziness = ""
        if self.is_one_digit(n1) and self.is_one_digit(n2):
            self.msg_laziness = self.msg_laziness + self.msg[6]
        if (n1 == 1 or n2 == 1) and operator == '*':
            self.msg_laziness = self.msg_laziness + self.msg[7]
        if (n1 == 0 or n2 == 0) and operator in ('*', '+', '-'):
            self.msg_laziness = self.msg_laziness + self.msg[8]
        if self.msg_laziness != "":
            self.msg_laziness = self.msg[9] + self.msg_laziness
            print(self.msg_laziness)


    @staticmethod
    def evaluate(no_a, operator, no_b):
        if operator == '+':
            return no_a + no_b
        elif operator == '-':
            return no_a - no_b
        elif operator == '*':
            return no_a * no_b
        elif operator == '/':
            return no_a / no_b


    def ask_store_result(self) -> object:
        print(self.msg[4])
        self.store_result = input()
        if self.store_result != 'n' and self.store_result != 'y':
            self.ask_store_result()
        elif self.store_result == 'y':
            if self.is_one_digit(self.result):
                self.message_index = 10
                self.one_digit_messages() # new algorithm for version 5/5
            else:
                self.memory = self.result


    def one_digit_messages(self):
        answer = input(self.msg[self.message_index])
        if answer == 'y':
            if self.message_index < 12:
                self.message_index += 1
                self.one_digit_messages()
            else:
                self.memory = self.result

    def ask_continue(self) -> object:
        print(self.msg[5])
        self.do_continue = input()
        if self.do_continue != 'n' and self.do_continue != 'y':
            self.ask_continue()
        elif self.do_continue != 'y':
            self.dont_continue = True
        else:
            self.calculation_ok = False
            self.dont_continue = False
            self.operator = None
            self.operand_1 = None
            self.operand_2 = None
            self.msg_equitation = ""
            self.msg_laziness = ""

    def main(self):
        while not self.dont_continue:
            while not self.calculation_ok:
                self.print_msg(self.msg_equitation)
                if self.string_check(input()):
                    break
                else:
                    pass
            self.ask_store_result()
            self.ask_continue()


    def __del__(self):
        pass # print('Destructor called, HonestCalculator deleted.')

calculator = HonestCalculator()
calculator.main()
