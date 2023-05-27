#include "mbed.h"
#include "board_freedom.h"
#include "adc.h"
#include "oled_ssd1322.h"
#include <cstdint>
#include <cstdio>
#include <vector>

#define MESSAGE_MAX_SIZE 50
#define OVERHEAT_TEMP 36.0
#define MAX_TEMP 35.5
#define MIN_TEMP 30.0

void display_message(u8g2_t &oled, const char* message) {
    u8g2_ClearBuffer(&oled);
    u8g2_DrawUTF8(&oled, 10, 10, message);
    u8g2_SendBuffer(&oled);
}

int main() {

    board_init();
    float voltage;
    float temp;

    int overheatCount = 0;

    DigitalOut greenLed(PTB3);
    DigitalOut redBoardLed(PTB2);
    DigitalOut heatingLed(PTC12);

    u8g2_t oled;

    u8g2_ClearBuffer(&oled);
    u8g2_SetFont(&oled, u8g2_font_6x12_mr);
    u8g2_SendBuffer(&oled);

    char message[MESSAGE_MAX_SIZE + 1];
    message[MESSAGE_MAX_SIZE] = '\0';

    PwmOut heater_power(PTA7);
    heater_power = 1;
    redBoardLed = 1;
    heatingLed = 1;

    while (true) {
        uint16_t analog_in_value = adc_read(0);
        voltage = analog_in_value * 3 / 65535.0;
        temp = ((voltage * 1000 - 400) / 19.5);

        if (analog_in_value < 3500) {
            snprintf(message, MESSAGE_MAX_SIZE, "WARNING: sensor failure. Ain: %5d", analog_in_value);
            display_message(oled, message);
            heater_power = 0;
            redBoardLed = 0;
            heatingLed = 0;
            ThisThread::sleep_for(1000ms);
            continue;
        }

        if (temp > OVERHEAT_TEMP) {
            overheatCount++;
            if (overheatCount > 4) {
                snprintf(message, MESSAGE_MAX_SIZE, "WARNING: Overheating detected. Exiting...");
                display_message(oled, message);

                break;
            }
        }
        display_message(oled, message);

        if (temp >= MIN_TEMP && temp <= MAX_TEMP) {
            redBoardLed = 0;
            greenLed = 1;
        } else if (temp > OVERHEAT_TEMP) {
            redBoardLed = 1;
            greenLed = 1;
        } else {
            redBoardLed = 1;
            greenLed = 0;
        }

        if (temp >= MAX_TEMP) {
            heater_power = 0;
            heatingLed = 0;
        } else if (temp <= MIN_TEMP + 0.5) {
            heater_power = 1;
            heatingLed = 1;
        }

        ThisThread::sleep_for(100ms);
    }
}