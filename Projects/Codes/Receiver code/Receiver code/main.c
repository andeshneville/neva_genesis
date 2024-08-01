/*
 * Receiver_code.c
 *
 * Created: 17/07/2023 12:01:21
 * Author : NAN
 */ 

#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <stdlib.h>
#include <time.h>
#include "DC_Motor.h"
#include "Servo_motor.h"
#include "NRF24L01.h"

int main(void)
{
	DDRD = 0xFF;		// Make PORTD as output Port 
	DDRC = 0xFF;		// Make PORTD as output Port 
	DDRB = 0x00;        /* Make PORTB as input */
	dc_init();
	servo_init();
	nrf24_init();
    /* Replace with your application code */
    while (1) 
    {
		
		nrf24_start_listening();
		char rf_message[32];
		if(nrf24_available()){
			strcpy(rf_message,nrf24_read_message());
			if(rf_message[0]=="R"){
				int speed =atoi(rf_message+1);
				right_motor(speed);
			}
			else if(rf_message[0]=="L"){
				int speed =atoi(rf_message+1);
				left_motor(speed);		
			}
			else if (rf_message[0]=="A"){
				dc_stop();
				int speed =atoi(rf_message+1);
				arm_joint(speed);
			}
			else if (rf_message[0]=="G"){
				dc_stop();
				int speed =atoi(rf_message+1);
				gripper(speed);
			}
		}		
    }
	return(0);
}
