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
int sbutton = 0;
int hbutton = 0;

uint8_t nrf24_send_spi(uint8_t register_address, void *data, unsigned int bytes);
uint8_t nrf24_write(uint8_t register_address, uint8_t *data, unsigned int bytes);
uint8_t nrf24_read(uint8_t register_address, uint8_t *data, unsigned int bytes);
void nrf24_init(void);
void nrf24_state(uint8_t state);
void nrf24_start_listening(void);
unsigned int nrf24_available(void);
const char * nrf24_read_message(void);
uint8_t nrf24_send_message(const void *tx_message);
void MSelect(void);
void HSelect(void);
void Gyro_Init();
void Read_RawValue();
float x_accelleration(void);
float y_accelleration(void);
void I2C_Init();
char I2C_Read_Ack();
void ADC_Init();
int ADC_Read(char channel);
int flex(char channel);

int main(void)
{
	DDRB = 0xFF;		// Make PORTB as output Port 
	DDRD &= ~(1<<PD2);  // Make PD2 pin as Input
	DDRD &= ~(1<<PD3);  // Make PD3 pin as Input
	PORTD = PORTD | (1<<PD2) | (1<<PD3); /* Enable pull-up on PD2 by writing 1 to it */
	DDRC = 0x00;        /* Make ADC port as input */
	
	I2C_Init();
	Gyro_Init();
	ADC_Init();
	nrf24_init();
	
    /* Replace with your application code */
    while (1) 
    {
		MSelect();
		char msg[32];
		memset(msg,0,32);
		if (sbutton){
			char str1[32]="R";
			memset(str1,1,32);
			char str2[32]="L";
			memset(str2,1,32);
			int a= y_accelleration();
			int b= x_accelleration();
			strcat(str1,a);
			strcat(str2,b);	
			nrf24_send_message(str1);
			nrf24_send_message(str2);
		}
		else{
			HSelect();
			char str1[32]="A";
			if (hbutton){
				memset(str1,1,32);
				strcat(str1,flex(0));
				nrf24_send_message(str1);
			}
			else{
				char str2[32]="B";
				memset(str2,1,32);
				strcat(str2,flex(1));
				nrf24_send_message(str2);
			}
			}
		
    }
	return(0);
}
void MSelect(void){
	if (PD2==1){
		sbutton=1;
	}
	else{
		sbutton=0;
	}
}
void HSelect(void){
	if (PD3==1){
		hbutton=1;
	}
	else{
		hbutton=0;
	}
}

