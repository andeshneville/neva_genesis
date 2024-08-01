/*
 * flex.h
 *
 * Created: 26/06/2024 10:47:27
 *  Author: NAN
 */ 


#ifndef FLEX_H_
#define FLEX_H_
//Declarations
void ADC_Init();
int ADC_Read(char channel);
int flex(char channel);
void ADC_Init(){
	DDRC &= ~((1 << PC0) | (1 << PC1));        /* Make ADC port as input */
	ADCSRA = 0x87;          /* Enable ADC, with freq/128  */
	ADMUX = 0x40;           /* Vref: Avcc, ADC channel: 0 */
}

int ADC_Read(char channel)
{
	ADMUX = 0x40 | (channel & 0x07);   /* set input channel to read */
	ADCSRA |= (1<<ADSC);               /* Start ADC conversion */
	while (!(ADCSRA & (1<<ADIF)));     /* Wait until end of conversion by polling ADC interrupt flag */
	ADCSRA |= (1<<ADIF);               /* Clear interrupt flag */
	_delay_ms(1);                      /* Wait a little bit */
	return ADC;                       /* Return ADC word */
}

int flex(char channel){
	float val=ADC_Read(channel);
	int i=val/11.4;
	return i;
}
#endif /* FLEX_H_ */
