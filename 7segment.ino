// Segment pins configuration
const int segmentPins[7] = {2, 3, 4, 5, 6, 7, 8};

// Define binary representation for each digit (0-9)
// Binary format: 0bgfedcba
const uint8_t digitMap[10] = {
    0b0111111,  // 0
    0b0000110,  // 1
    0b1011011,  // 2
    0b1001111,  // 3
    0b1100110,  // 4
    0b1101101,  // 5
    0b1111101,  // 6
    0b0000111,  // 7
    0b1111111,  // 8
    0b1101111   // 9
};

// Function to display a digit on the 7-segment display
void displayDigit(int digit) {

    uint8_t segments = digitMap[digit];
    
    for (int i = 0; i < 7; i++) {
        digitalWrite(segmentPins[i], (segments >> i) & 0x01);
    }

}

void setup() {

    // Set segment pins as outputs
    for (int i = 0; i < 7; i++) {
        pinMode(segmentPins[i], OUTPUT);
    }

    Serial.begin(9600);

}

void loop() {
    // Check if data is available on the serial port
    if (Serial.available() > 0) {

        // Read the serial input as a single byte
        int number = Serial.read() - '0';

        // Display the digit on the 7-segment display
        if (number >= 0 && number <= 9) {
            displayDigit(number);
        }
        
    }
}
