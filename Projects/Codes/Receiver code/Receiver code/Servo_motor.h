/*
 * Servo_motor.h
 *
 * Created: 16/07/2024 11:08:18
 *  Author: NAN
 */ 


#ifndef SERVO_MOTOR_H_
#define SERVO_MOTOR_H_


void servo_init(void){
	/* GPIO setup */
	DDRB |= (1<<PB1); // Make OC1A pin as Output
	DDRB |= (1<<PB2); // Make OC1B pin as Output
	/* PWM setup */
	TCCR1A = (1<<WGM00)|(1<<WGM01)|(1<<COM1A0)|(1<<CS02); // Set Fast PWM with Fosc/256Timer0 clock
	TCCR1B = (1<<WGM00)|(1<<WGM01)|(1<<COM1B0)|(1<<CS02); // Set Fast PWM with Fosc/256Timer0 clock
	OCR0B = 0; // Initialize duty cycle (0% initially)
	OCR0A = 0; // Initialize duty cycle (0% initially)
}

int gripper(int position){
	OCR0A=position;
}
int arm_joint(int position){
	OCR0B=position;
}

#endif /* SERVO_MOTOR_H_ */