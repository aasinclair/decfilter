# decfilter
A tool that generates coefficients for the Freescale/NXP decimation filter module

Currently generates a second order bandpass butterworth filter.


## Usage

decfilter.py [-graph] [-scale SCALE] sample low high

-graph
<br>&nbsp;&nbsp;&nbsp;&nbsp;Display frequency response graph

-scale SCALE
<br>&nbsp;&nbsp;&nbsp;&nbsp;Coefficient scaling, default 8

sample
<br>&nbsp;&nbsp;&nbsp;&nbsp;Sample frequency

low
<br>&nbsp;&nbsp;&nbsp;&nbsp;low cutoff frequency

high
<br>&nbsp;&nbsp;&nbsp;&nbsp;high cutoff frequency


## Example

Command

```./decfilter.py 50000 3000 4000```

Output

```
Scaled coefficients
0.000452710189366
0.0
-0.000905420378732
0.0
0.000452710189366
0.433214572706
-0.603867529311
0.396311140567
-0.104647706407
Hex coefficients
0x000ED5
0x000000
0xFFE255
0x000000
0x000ED5
0x377392
0xB2B479
0x32BA52
0xF29AE8
