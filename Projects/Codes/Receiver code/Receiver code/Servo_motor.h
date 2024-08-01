/*
 * Servo_motor.h
 *
 * Created: 16/07/2024 11:08:18
 *  Author: NAN
 */ 


#ifndef SERVO_MOTOR_H_
#define SERVO_MOTOR_H_
void servo_init(void);
void gripper(int position);
void arm_joint(int position);

void servo_init(void){
	DDRD |= (1<<PD5); // Make OC0A pin as Output
	DDRD |= (1<<PD6); // Make OC0B pin as Output
	// Configure OC0A and OC0B for Fast PWM, 8-bit
	TCCR0A |= (1 << COM0A1) | (1 << COM0B1)|(1 << WGM00) | (1 << WGM01); // Clear OC0A and OC0B on Compare Match
	TCCR0B |= (1 <<  CS01)|(1 <<   CS00);    // prescaling to 64
	TCNT0 = 0xFF;                           // Set value to compare OCR0x to
}

void gripper(int position){
	OCR0A=position;
}
void arm_joint(int position){
	OCR0B=position;
}

#endif /* SERVO_MOTOR_H_ */
