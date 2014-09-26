#!/usr/bin/env ruby

require_relative 'rpncalculator'
rpn = RPNCalculator.new
begin
    puts rpn.calculate(ARGV[0])
rescue StandardError => ex
    puts ex
end
