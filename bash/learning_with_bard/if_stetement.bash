

echo "Working on if statement."
echo "------------------------"
# check if the person is adult or minor

# age=18
# if [ $age -ge 18 ]; then
#     echo "You are an adult."
# else
#     echo "You are a minor."
# fi

# get user's favourite color

colors=("red" "gree" "blue" "white" "black")
read -rp "What is you favourite color: " color
if  $color in ({$colors}); then
    echo "You color is in the list"
else
    echo "You color is not in the list."
fi
