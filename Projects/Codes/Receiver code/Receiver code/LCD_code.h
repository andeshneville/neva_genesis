/*
 * LCD_code.c
 *
 * Created: 14/03/2023 12:23:04
 * Author : NAN
 */ 
#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>
#define LCD_Port PORTD
#define LCD_Dir DDRD
#define EN PD1
#define RS PD0

void LCD_Cmd(unsigned char cmd);
void LCD_Char(unsigned char data);
void LCD_Init (void);
void LCD_String(char *str);
void LCD_String_xy(char row, char pos, char *str);

void LCD_Cmd(unsigned char cmd){
	LCD_Port=(LCD_Port & 0x0F)|(cmd & 0xF0);
	LCD_Port &=~(1<<RS);
	LCD_Port |=(1<<EN);
	_delay_ms(1);
	LCD_Port &=~(1<<EN);
	LCD_Port=(LCD_Port & 0x0F)|(cmd<<4);
	LCD_Port |=(1<<EN);
	_delay_ms(1);
	LCD_Port &=~(1<<EN);
	_delay_ms(1);
}
void LCD_Char(unsigned char data){
	LCD_Port=(LCD_Port & 0x0F)|(data & 0xF0);
	LCD_Port |=(1<<RS);
	LCD_Port |=(1<<EN);
	_delay_ms(1);
	LCD_Port &=~(1<<EN);
	LCD_Port=(LCD_Port & 0x0F)|(data <<4);
	LCD_Port |=(1<<EN);
	_delay_ms(1);
	LCD_Port &=~(1<<EN);
	_delay_ms(1);
}
void LCD_Init (void){
	LCD_Dir=0xFF;
	_delay_ms(2);
	LCD_Cmd(0x02);
	LCD_Cmd(0x28);
	LCD_Cmd(0x0C);
	LCD_Cmd(0x06);
	LCD_Cmd(0x01);
}
void LCD_String(char *str){
	int i;
	for(i=0;str[i]!=0;i++){
		LCD_Char(str[i]);
	}
}
void LCD_String_xy(char row, char pos, char *str){
	if (row==0 && pos <16){
		LCD_Cmd((pos &0x0F)|0x80);
	}
	else if(row==1 && pos <16){
		LCD_Cmd((pos & 0x0F)| 0xC0);
	}
			LCD_String(str);
}
void LCD_Clear(void){
	LCD_Cmd(0x01); /* clear display */
	LCD_Cmd(0x02); /* Return display to its home position */
}
	
	