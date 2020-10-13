//  for more info about hardware setup visit :
//  https://www.instructables.com/Arduino-Keypad-4x4-Tutorial/

//  to be able to use Keypad.h header file you should include
//  Keypad library from Mark Stanley, Alexander Brevig
//  here I am using version 3.1.1 of this library.

#include <Keypad.h>

const byte numRows=4;
const byte numCols=4;

char keymap[numRows][numCols]={
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'},
};

byte rowPins[numRows]={9,8,7,6};
byte colPins[numCols]={5,4,3,2};

Keypad myKeypad=Keypad(makeKeymap(keymap),rowPins,colPins,numRows,numCols);

void setup() {
  Serial.begin(9600);
}

void loop() {
  char mk=NO_KEY;
  mk = myKeypad.getKey();
  if(mk != NO_KEY)
  {
    Serial.print(mk);
  }
  delay(1);
}
