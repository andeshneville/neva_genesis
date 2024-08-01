/*
 * DC_Motor.h
 *
 * Created: 15/07/2024 13:14:02
 *  Author: NAN
 */ 


#ifndef DC_MOTOR_H_
#define DC_MOTOR_H_

#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdio.h>

//Declarations
void dc_init();
void dc_init(void);
void left_motor(int speed);
void right_motor(int speed);
//void motor_control(int motor, int speed);
volatile int Direction =0;
// Initialize PWM for motor speed control

void dc_init(){
	// Set motor control pins (IN1, IN2, IN3, IN4) as output
	DDRC =0xFF;
	DDRB |= (1 << PB2);// Set PWM pins (ENA, ENB) to output for speed control (Fast PWM mode)
	DDRD |= (1 << PD3);
	TCCR1A |= (1 << COM1B1) | (1 << COM1A1)|(1 << WGM11) | (1 << WGM10); // Clear OC1B on Compare Match
	TCCR2A |= (1 << COM2B1) | (1 << COM2A1)|(1 << WGM21) | (1 << WGM20); // Clear OC1B on Compare Match
	TCCR2B |= (1<<CS22);        // No prescaling (clk/1)
	TCCR1B |= (1<<CS12);        // No prescaling (clk/1)
	//Initial Motor Speeds
	right_motor(50);
	left_motor(120);
}

void left_motor(int speed){
	if (speed<0){
		int sp=0-speed;
		PORTC &= ~(1 << PC2);
		PORTC |= (1 << PC3);
		OCR1B = (sp);
	}
	else{
		PORTC &= ~(1 << PC3);
		PORTC |= (1 << PC2);
		OCR1B = (speed);
	}
}
void right_motor(int speed){
	if (speed<0){
		int sp=0-speed;
		PORTC &= ~(1 << PC0);
		PORTC |= (1 << PC1);
		OCR2B = (sp);
	}
	else{
		PORTC &= ~(1 << PC1);
		PORTC |= (1 << PC0);
		OCR2B = (speed);
	}
}
void dc_stop(){
	OCR2B=0;
	OCR1B=0;
}

	
#endif /* DC_MOTOR_H_ */
