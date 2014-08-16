/*Twitter Melody 
Created August 11, 2014

Plays a melody everytime there is a tweet that meets the required
parameters 

circuit: speaker
         100 ohm resistor
*/

#include "pitches.h"

//speaker pin
int speakerPin = 8;

//notes in the melody
int melody[] = {
  NOTE_C4, NOTE_G3,NOTE_G3, NOTE_A3, NOTE_G3,0, NOTE_B3, NOTE_C4};
//Note durations: 4 = quarter note, 8 = eighth note, etc
int noteDurations[] = { 4, 8, 8, 4, 4, 4, 4, 4 };

void setup(){
  pinMode(speakerPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  //wait to receive input
  while (Serial.available() == 0);
  
  //Read input
  int val = Serial.read() - '0';
  
  if (val == 1){
    //Start melody
    Serial.println("Speaker is On");
    for (int thisNote = 0; thisNote < 8; thisNote++){
      //calculate note duration
      //e.g. quarter note = 1000/4, eighth note = 1000/8
      int noteDuration = 1000/noteDurations[thisNote];
      tone(8, melody[thisNote], noteDuration);
      
      int pauseBetweenNotes = noteDuration * 1.30;
      delay(pauseBetweenNotes);
      //stop the tone playing
      noTone(8);
    }
      delay(1000);
  } else if (val == 0) {
      Serial.println("Melody is Off");
      digitalWrite(speakerPin, LOW);
      delay(1000);
  }else {
      Serial.println("Invalid!");
  }
    
    while(Serial.available() > 0) Serial.read();
}

  
