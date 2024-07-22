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

// Initialize PWM for motor speed control
void initPWM() {
	// Set Timer1 in Fast PWM mode, non-inverted output
	TCCR0A = (1 << COM1A1) | (1 << WGM11) | (1 << WGM10);
	TCCR0B = (1 << WGM13) | (1 << WGM12) | (1 << CS11); // Prescaler = 8
	OCR2B = 0; // Initialize duty cycle (0% initially)
	OCR1B = 0; // Initialize duty cycle (0% initially)
}
void dc_init(){
	DDRD = 0xFF;  /* Make PORTD as output Port */
	sei();   /* Enable Global Interrupt */
	TCNT0 = 0;  /* Set timer0 count zero */
	TCCR0A = (1<<WGM00)|(1<<WGM01)|(1<<COM0A0)|(1<<CS00)|(1<<CS01);/* Set Fast PWM with	Fosc/64 Timer0 clock */
	TCCR0B = (1<<WGM00)|(1<<WGM01)|(1<<COM0B0)|(1<<CS00)|(1<<CS01);/* Set Fast PWM with	Fosc/64 Timer0 clock */
}

int left_motor(int speed){
	if (speed<0){
		int sp=0-speed;
		DDRD &= ~(1 << PD2);
		PORTD |= (1 << PD3);
		OCR1B = (sp);
	}
	else{
		DDRD &= ~(1 << PD3);
		PORTD |= (1 << PD2);
		OCR1B = (speed);
	}
}
int right_motor(int speed){
	if (speed<0){
		int sp=0-speed;
		DDRD &= ~(1 << PD4);
		PORTD |= (1 << PD5);
		OCR2B = (sp);
	}
	else{
		DDRD &= ~(1 << PD5);
		PORTD |= (1 << PD4);
		OCR2B = (speed);
	}
}

#endif /* DC_MOTOR_H_ */