#!/usr/bin/env ruby

require_relative 'rpncalculator'

begin
    rpn = RPNCalculator.new
    puts rpn.calculate(ARGV[0])
rescue StandardError => ex
    puts ex
end
