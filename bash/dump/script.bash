#!/usr/bin/env bash

name="John"
age=54
country=""

echo "Hello my name is $name and I am $age years old."
echo "My name contains ${#name} characters."
# default value just for country in this area.
echo "Currently I am living in ${country:-'Anonymous'}!" 
# to give name value inside string referencing use = insted of -
echo "Currently I am living in ${country:='Anonymous'}!" 
echo "$country"

echo "-------------------"
# sub shell
# Changes in sub shell doesn't effect main shell.
# for example if you cd in sub shell it's only happend
# in the sub shell. main shell still point where it was.
# sub shell will return the result of the execuation.
var=$(pwd)
echo "The path is $var"

echo "-------------------"
# process subsitution, sub proc: output of command like file
# <() <- proc subsitution.
diff <(ls /home/saeed)  <(ls /home/saeed/dox/codes)

# $(()) arthimatic expansion
# 
echo "-------------------"
plus=$((3 + 7))
echo "Reault of 3 + 7 is $plus"

echo "-------------------"
# command line args
# $0 : command name
# $1 : arg 1
# $2 : arg 2
# ...
# 

# if [[ cond ]]; then
# elif  [[ cond ]]; then 
# else
# fi

# check if the person is adult
# for string comprison : == !=
# for numerical comprison : -eq -ne -lt ...
# 
if [[ $age -ge 18 ]]; then
  echo "Adult"
else
  echo "Minor"
fi

# 0: means success 
# anything rather than 0 is failure.

# -z : variable existence (empty)
# -n : if something is not null
# [[ -n $val ]]
#

# -f : file exists
# -d : dir exists
# -e : file/dir exists
#
# -r, -w, -x : permission checks

# internal
# -a : and
# -o : or

# external 
# && : and
# || : or

# sleep 10
#
# read -r name  # read and store `name`
#
#
#
# Array
#
a=(1 2 3 4 5)
echo "${a[0]}"
echo "${a[@]}" # all elms
echo "${#a[@]}" # len
