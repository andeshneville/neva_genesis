/*
 * Transmitter_code.c
 *
 * Created: 17/07/2023 12:01:21
 * Author : NAN
 */ 

#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <time.h>
#include <string.h>
#include "MPU6050.h"
#include "NRF24L01.h"
#include "flex.h"
#include "Servo_motor.h"

volatile uint8_t sbutton = 0;
volatile uint8_t hbutton = 0;

int main(void)
{
	DDRB = 0xFF;		// Make PORTB as output Port 
	DDRD &= ~(1<<PD2);  // Make INT0 pin as Input
	DDRD &= ~(1<<PD3);  // Make INT1 pin as Input
	EIMSK |= (1<<INT0)|(1<<INT1); /* Enable INT0 and INT1*/ 
	EIFR  |=(1<< INTF1)|(1<< INTF0);  /* Trigger INT0 and INT1 on Rising Edge triggered */
	sei();		//Enable global interrupt
	DDRC = 0x00;        /* Make ADC port as input */
	
	I2C_Init();
	Gyro_Init();
	ADC_Init();
	nrf24_init();
	servo_init();
    /* Replace with your application code */
    while (1) 
    {
		static char msg[32];
		char str1[32];
		char str2[32];
		if (sbutton){
			strcpy(str1,"R");
			strcpy(str2,"L");
			int a= right_motor();
			int b= left_motor();
			strcat(str1,a);
			strcat(str2,b);	
			nrf24_send_message(str1);
			nrf24_send_message(str2);
		}
		else{
			strcpy(str1,"A");
			if (hbutton){
				
				strcat(str1,flex(0));
				nrf24_send_message(str1);
			}
			else{
				
				strcpy(str2,"B");
				strcat(str2,flex(1));
				nrf24_send_message(str2);
			}
			}
		
    }
	return(0);
}
ISR(INT0_vect){
	sbutton = ~sbutton; 
	_delay_ms(50); 
}
ISR(INT1_vect){
	hbutton = ~hbutton;  
	_delay_ms(50);  
}


