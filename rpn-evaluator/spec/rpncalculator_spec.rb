require_relative '../rpncalculator'

describe RPNCalculator, "#calculate" do
    it "returns 3 for '1 2 +'" do
        rpn = RPNCalculator.new
        total = rpn.calculate("1 2 +")
        expect(total).to eq (3)
    end
    it "returns 2 for '4 2 /'" do
        rpn = RPNCalculator.new
        total = rpn.calculate("4 2 /")
        expect(total).to eq (2)
    end
    it "returns 14 for '2 3 4 + *'" do
        rpn = RPNCalculator.new
        total = rpn.calculate("2 3 4 + *")
        expect(total).to eq (14)
    end
    it "returns 77 for '3 4 + 5 6 + *'" do
        rpn = RPNCalculator.new
        total = rpn.calculate("3 4 + 5 6 + *")
        expect(total).to eq (77)
    end
    it "returns 9 for '13 4 -'" do
        rpn = RPNCalculator.new
        total = rpn.calculate("13 4 -")
        expect(total).to eq (9)
    end
    it "raises not enough arguments error for '3 /'" do
        rpn = RPNCalculator.new
        expect { rpn.calculate("3 /") }.to raise_error
    end
    it "raises invalid arguments error for 'a b /'" do
        rpn = RPNCalculator.new
        expect { rpn.calculate("a b /") }.to raise_error
    end
end
