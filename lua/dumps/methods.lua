Calculator = {}

function Calculator.add(a, b) 
    return a + b
end

-- make instance of the Calculator table
local calc = Calculator

print(Calculator.add(2, 3))
print(calc.add(2, 3))

Text = {}

function upper(s) 
    return string.upper(s)
end

name = Text
print(name.upper("hello"))