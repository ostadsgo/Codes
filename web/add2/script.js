
function calculate() {
    var num1_element = document.getElementById("num1");
    var num2_element = document.getElementById("num2");

    var num1_value = num1_element.value;
    var num2_value = num2_element.value;

    var num1 = parseInt(num1_value);
    var num2 = parseInt(num2_value);
    var sum = num1 + num2;

    var result_element = document.getElementById("result");
    result_element.textContent = sum;

    num1_element.value = "";
    num2_element.value = "";
}


