/*
 * MyoCoach - Arduino firmware
 *
 * Reads two Ottobock 13E202 EMG sensors on analog inputs A0 and A1,
 * converts them to volts and streams them over USB serial as "EMG0:EMG1".
 */

const int EMG0_PIN = A0;
const int EMG1_PIN = A1;
const float ADC_TO_VOLTS = 5.0 / 1023.0;
const int SAMPLE_PERIOD_MS = 20;   // 50 Hz

void setup() {
  Serial.begin(115200);
}

void loop() {
  float emg0 = analogRead(EMG0_PIN) * ADC_TO_VOLTS;
  float emg1 = analogRead(EMG1_PIN) * ADC_TO_VOLTS;

  Serial.print(emg0, 3);
  Serial.print(":");
  Serial.println(emg1, 3);

  delay(SAMPLE_PERIOD_MS);
}
