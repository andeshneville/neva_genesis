/*
 * IncFile1.h
 *
 * Created: 24/06/2024 09:03:41
 *  Author: NAN
 */ 


#ifndef INCFILE1_H_
#define INCFILE1_H_


#define F_CPU 8000000UL		/* Define CPU clock Frequency 8MHz */
#include <avr/io.h>			/* Include AVR std. library file */
#include <util/delay.h>		/* Include delay header file */
#include <inttypes.h>		/* Include integer type header file */
#include <stdlib.h>			/* Include standard library file */
#include <stdio.h>			/* Include standard I/O library file */
#include "MPU6050_res_define.h"	/* Include MPU6050 register define file */
#include "I2C_Master_H_file.h"	/* Include I2C Master header file */

float Acc_x,Acc_y,Acc_z,Temperature,Gyro_x,Gyro_y,Gyro_z;
//Declarations
void Gyro_Init();
void MPU_Start_Loc();
void Read_RawValue();
float x_accelleration(void);
float y_accelleration(void);
float direction(void);

void Gyro_Init()			/* Gyro initialization function */
{
	_delay_ms(150);			/* Power up time >100ms */
	I2C_Start(0xD0);	/* Start with device write address */
	I2C_Write(SMPLRT_DIV);	/* Write to sample rate register */
	I2C_Write(0x07);		/* 1KHz sample rate */
	I2C_Stop();

	I2C_Start(0xD0);
	I2C_Write(PWR_MGMT_1);	/* Write to power management register */
	I2C_Write(0x01);		/* X axis gyroscope reference frequency */
	I2C_Stop();

	I2C_Start(0xD0);
	I2C_Write(MCONFIG);		/* Write to Configuration register */
	I2C_Write(0x00);		/* Fs = 8KHz */
	I2C_Stop();

	I2C_Start(0xD0);
	I2C_Write(GYRO_CONFIG);	/* Write to Gyro configuration register */
	I2C_Write(0x18);		/* Full scale range +/- 2000 degree/C */
	I2C_Stop();

	I2C_Start(0xD0);
	I2C_Write(INT_ENABLE);	/* Write to interrupt enable register */
	I2C_Write(0x01);
	I2C_Stop();
}

void MPU_Start_Loc()
{
	I2C_Start(0xD0);		/* I2C start with device write address */
	I2C_Write(ACCEL_XOUT_H);	/* Write start location address from where to read */
	I2C_Repeated_Start(0xD1);	/* I2C start with device read address */
}

void Read_RawValue()
{
	MPU_Start_Loc();			/* Read Gyro values */
	Acc_x = (((int)I2C_Read_Ack()<<8) | (int)I2C_Read_Ack());
	Acc_y = (((int)I2C_Read_Ack()<<8) | (int)I2C_Read_Ack());
	Acc_z = (((int)I2C_Read_Ack()<<8) | (int)I2C_Read_Ack());
	Temperature = (((int)I2C_Read_Ack()<<8) | (int)I2C_Read_Ack());
	Gyro_x = (((int)I2C_Read_Ack()<<8) | (int)I2C_Read_Ack());
	Gyro_y = (((int)I2C_Read_Ack()<<8) | (int)I2C_Read_Ack());
	Gyro_z = (((int)I2C_Read_Ack()<<8) | (int)I2C_Read_Nack());
	I2C_Stop();
}
float right_motor(void){
	Read_RawValue();
	int Xa,Ya,speed;
	Xa=Acc_x/328;	//Map -32768 to 32767 acc. values to 0-100 PWM values
	Ya=Acc_y/328;	//Map -32768 to 32767 acc. values to 0-100 PWM values
	speed=Ya-Xa;
	return speed;	
}
float left_motor(void){
	Read_RawValue();
	int Ya,Xa,speed;
	Ya=Acc_y/328;  //Map -32768 to 32767 acc. values to 0-100 PWM values
	Xa=Acc_x/328;	//Map -32768 to 32767 acc. values to 0-100 PWM 
	speed=Ya+Xa;
	return speed;
}
float direction(void){
	float Xg=0,Yg=0;
	Xg = Gyro_x/16.4;
	Yg = Gyro_y/16.4;
}


#endif /* INCFILE1_H_ */



