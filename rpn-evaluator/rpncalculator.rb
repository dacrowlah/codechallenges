class RPNCalculator

    def calculate(rpn_value)
        rpn = rpn_value.split

        if rpn.length < 3
            raise "invalid number of arguments"        
        end
        stack = []

        rpn.each do | value |
            case value
            when /\d/
                stack.insert(0, value.to_i)
            when "*","/","+","-"
               ops = stack.take(2)
               total = ops[1].send(value, ops[0])
               stack.delete_at(1)
               stack.delete_at(0)
               stack.insert(0, total)
            else
               raise "invalid argument"
            end
        end
        return stack[0]
    end
end

