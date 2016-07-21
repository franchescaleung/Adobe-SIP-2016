int piezo_pin =5;
int note_a4= 440;
int whole_note= 1600;
void setup() {
  pinMode(5, OUTPUT);

}

void loop() {
  tone(5, 440, whole_note);

}
