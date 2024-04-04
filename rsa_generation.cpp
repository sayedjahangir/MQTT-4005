#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <vector>
#include <stdexcept> // for std::invalid_argument

// custom GCD function
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

bool isPrime(int number) {
    if (number < 2) return false;
    for (int i = 2; i <= number / 2; ++i) {
        if (number % i == 0) return false;
    }
    return true;
}

int generatePrime(int min_value, int max_value) {
    srand(static_cast<unsigned int>(time(0))); // seed for random number generation
    int prime = min_value + rand() % (max_value - min_value);
    while (!isPrime(prime)) {
        prime = min_value + rand() % (max_value - min_value);
    }
    return prime;
}

int modInverse(int e, int phi) {
    for (int d = 3; d < phi; ++d) {
        if ((d * e) % phi == 1) return d;
    }
    throw std::invalid_argument("Modular inverse does not exist.");
}

std::vector<int> encryptMessage(std::string message, int e, int n) {
    std::vector<int> ciphertext;
    for (char ch : message) {
        int encoded_ch = static_cast<int>(ch);
        int encrypted_ch = static_cast<int>(pow(encoded_ch, e)) % n; // simplified modular exponentiation
        ciphertext.push_back(encrypted_ch);
    }
    return ciphertext;
}

std::string decryptMessage(const std::vector<int>& ciphertext, int d, int n) {
    std::string message = "";
    for (int ch : ciphertext) {
        int decrypted_ch = static_cast<int>(pow(ch, d)) % n; // simplified modular exponentiation
        message += static_cast<char>(decrypted_ch);
    }
    return message;
}

int main() {
    int lowest_value, highest_value;
    std::cout << "Enter the minimum value for generating primes: ";
    std::cin >> lowest_value;
    std::cout << "Enter the maximum value for generating primes: ";
    std::cin >> highest_value;

    int p = generatePrime(lowest_value, highest_value);
    int q = generatePrime(lowest_value, highest_value);
    while (p == q) {
        q = generatePrime(lowest_value, highest_value);
    }

    int n = p * q;
    int phi_of_n = (p - 1) * (q - 1);

    srand(static_cast<unsigned int>(time(0))); // reset seed for random number generation
    int e = 3 + rand() % (phi_of_n - 4); // ensure e starts at 3
    while (gcd(e, phi_of_n) != 1) {
        e = 3 + rand() % (phi_of_n - 4);
    }

    int d = modInverse(e, phi_of_n);

    std::cout << "Public Key: " << e << std::endl;
    std::cout << "Private Key: " << d << std::endl;
    std::cout << "n: " << n << std::endl;
    std::cout << "Phi_of n: " << phi_of_n << std::endl;
    std::cout << "p: " << p << std::endl;
    std::cout << "q: " << q << std::endl;

    std::string message;
    std::cout << "Enter the message to encrypt: ";
    std::cin.ignore();
    std::getline(std::cin, message);

    std::vector<int> ciphered_text = encryptMessage(message, e, n);
    std::cout << "Encrypted Message: ";
    for (int num : ciphered_text) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::string decrypted_message = decryptMessage(ciphered_text, d, n);
    std::cout << "Decrypted Message: " << decrypted_message << std::endl;

    return 0;
}
