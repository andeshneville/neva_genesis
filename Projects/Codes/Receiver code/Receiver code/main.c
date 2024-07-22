/*
 * Receiver_code.c
 *
 * Created: 17/07/2023 12:01:21
 * Author : NAN
 */ 

#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <time.h>
#include "DC_Motor.h"
#include "Servo_motor.h"
#include "NRF24L01.h"
#include "LCD_code.h"
//NRF24L01 declarations
uint8_t nrf24_send_spi(uint8_t register_address, void *data, unsigned int bytes);
uint8_t nrf24_write(uint8_t register_address, uint8_t *data, unsigned int bytes);
uint8_t nrf24_read(uint8_t register_address, uint8_t *data, unsigned int bytes);
void nrf24_init(void);
void nrf24_state(uint8_t state);
void nrf24_start_listening(void);
unsigned int nrf24_available(void);
const char * nrf24_read_message(void);
uint8_t nrf24_send_message(const void *tx_message);
int decode(char msg[]);
//motor declarations
void initPWM();
void dc_init();
void dc_init(void);
int left_motor(int speed);
int right_motor(int speed);
//servo declarations
void servo_init(void);
int gripper(int position);
int arm_joint(int position);

int main(void)
{
	DDRD = 0xFF;		// Make PORTD as output Port 
	DDRC = 0xFF;		// Make PORTD as output Port 
	DDRB = 0x00;        /* Make PORTB as input */
	LCD_Init();
	LCD_Clear();
	//initPWM();
	//dc_init();
	//servo_init();
	nrf24_init();
    /* Replace with your application code */
    while (1) 
    {
		nrf24_start_listening();
		char rf_message[32];
		LCD_String("P");
		if(nrf24_available()){
		strcpy(rf_message,nrf24_read_message());
		LCD_String(rf_message);
		LCD_String("P");
		}
		//if(rf_message[0]=="R"){
			//int speed =decode(rf_message);
			//right_motor(speed);
		//}
		//else if(rf_message[0]=="L"){
			//int speed =decode(rf_message);
			//left_motor(speed);		
		//}
		//else if (rf_message[0]=="A"){
			//int speed =decode(rf_message);
			//arm_joint(speed);
		//}
		//else if (rf_message[0]=="G"){
			//int speed =decode(rf_message);
			//gripper(speed);
		//}
				
    }
	return(0);
}

int decode(char msg[]){
	int k=0;
	for(int i=1; i<strlen(msg);i++){
		k=k*10 + atoi(msg[i]);
	}
	
	return k;
}
