# Learn about bash array.


colors=("Red" "Green" "Blue" "Cyan" "Black")

# Accessinng all elements in the array `colors`.
echo "Colors:" "${colors[@]}"




echo "------First Element--------------"
# What about accessing first or last or specific element.
first_color=${colors[0]}
echo "The first color is: $first_color"

echo "-------- Slice -----------"
# not working as expected
a=("${colors[@]:1:2}")
echo "Two colors: $a"

# update array element
colors[0]="Cyan"


echo "-------- Element of the Array -----------"
# iterate over array.
for color in "${colors[@]}"; do
    echo "The color is: " "$color"
done
