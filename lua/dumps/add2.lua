local function convert_to_number(value)
	if value.match(value,"^%d+$") then
		return tonumber(value)
	else
		return nil
	end
end

print("Enter first number: ")
local num1 = io.read()
num1 = convert_to_number(num1)
print("Enter second number: ")
local num2 = io.read()
num2 = convert_to_number(num2)

if num1 ~= nil and num2 ~= nil then
	print(tostring(num1) .. " + " .. tostring(num2) .. " = " .. tostring(num1 + num2))
else
	print("Error: wrong value.")
end
