import operator

class RPNCalculator(object):
    
    def __init__(self):
        self.ops = {
            '+': operator.add,
            '*': operator.mul,
            '/': operator.div,
            '-': operator.sub
        }
        self.stack = []


    def set_rpn(self, rpn_val):
        self.values = rpn_val.split(' ')
        if len(self.values) < 3:
            raise Exception("invalid number of arguments: %s" % len(self.values))


    def calculate_rpn(self):
        for n in self.values:
            if n.isdigit():
                self.stack.insert(0, int(n))
            elif n in self.ops:
                y,x = self.stack.pop(0), self.stack.pop(0)
                z = self.ops[n](x,y)
                self.stack.insert(0, z)
            else:
                raise Exception("invalid argument: %s" % n)

        return self.stack.pop(0)


if __name__ == '__main__':

    inputs = [
        '1 2 +',         # 3
        '4 2 /',         # 2
        '2 3 4 + *',     # 14
        '3 4 + 5 6 + *', # 77
        '13 4 -',        # 9
        'a b +',
        '1 /'
    ]
    calculator = RPNCalculator()
    for value in inputs:
        try:
            calculator.set_rpn(value)
            total = calculator.calculate_rpn()
            print '%s = %s' % (value, total)
        except Exception as e:
            print '%s (%s)' % (e, value)
