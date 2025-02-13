//ПЕРВОЕ ЗАДАНИЕ
/*
#include <iostream>
#include <string>
#include <sstream>
#include <cctype>


bool isValidNumber(const std::string& input) {
    if (input.empty()) return false;

    size_t start = 0;
    bool hasDot = false;

    if (input[0] == '-') {
        if (input.length() == 1) return false; 
        start = 1;
    }

    for (size_t i = start; i < input.length(); ++i) {
        if (input[i] == '.') {
            if (hasDot) return false;
            hasDot = true;
        }
        else if (!std::isdigit(input[i])) {
            return false;
        }
    }

    return true;
}

int main() {

    setlocale(LC_ALL, "RU");
    double x, s1, s2, S;
    std::string input;

    while (true) {
        std::cout << "Введите положительное число, отличное от нуля: ";
        std::getline(std::cin, input);

 
        if (input.empty()) {
            std::cout << "Ошибка: строка не должна быть пустой. Попробуйте снова." << std::endl;
            continue;
        }

        if (!isValidNumber(input)) {
            std::cout << "Ошибка: введите только положительные числа (целые или с плавающей точкой)." << std::endl;
            continue;
        }

        std::stringstream ss(input);
        ss >> x;

        if (x<= 0) {
            std::cout << "Ошибка: введите положительное число больше нуля." << std::endl;
        }
        else {
            std::cout << "Вы ввели число: " << x << std::endl;
            break;
        }
    }
    s1 = x * x * 0.5;
    s2 = x * x;
    S = s2 - s1;
    std::cout << "S: " << S << std::endl;
    return 0;
}
*/
//ВТОРОЕ ЗАДАНИЕ
/*
#include <iostream>
#include <sstream>
#include <limits>
#include <cmath>

using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    double number, y;

    while (true) {
        cout << "Введите число: ";

        string input;
        getline(cin, input);  // Считываем ввод как строку

        if (input.empty()) {
            cout << "Ошибка! Ввод не должен быть пустым." << endl;
            continue;
        }

        stringstream ss(input);
        if (ss >> number && ss.eof()) {  // Проверяем, что всё было правильно преобразовано
            cout << "Вы ввели число: " << number << endl;
            break;  // Если ввод успешен, выходим из цикла
        }
        else {
            cout << "Ошибка! Введите правильное число." << endl;
        }
    }
    if (number < 1) {
        y = cbrt(5 * number + 9);
        std::cout << "y:" << y << std::endl;
    }
    else if (number >= 1 && number < 4) {
        y = (pow(number, 2)) / (6 + pow(2.71828, -1 * number));
        std::cout << "y:" << y << std::endl;
    }
    else {
        y = cos(3 * pow(number,3)+8);
        std::cout << "y:" << y << std::endl;
    }
    return 0;
}
*/