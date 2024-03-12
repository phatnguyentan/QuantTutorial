# Golden Ratio
```
1.618
0,1,1,2,3,5,8,13,221,34,55,89,144,233,377,610,987
3/2 = 1.5
8/5 = 1.6
55/34 = 1.617
377/233 = 1.618
233/377 = 0.618
377/610 = 0.618
```
# Other Ratio
```
610/233 = 2.618
987/377 = 2.618

233/610 = 0.382
987/377 = 0.382
```
# Ratio Calculate
```
Given 2 consecutive price movement form a triangle without a base (bottom side) /\
Height is a perpendicular line from the origin to the top of a price movement  |\ or |/.
We call it AB and BC
Ratio = height_bc/height_ab
Example 
height_ab =  233
height_bc =  377
Ratio = 377/233 = 1.618
```
## 3 Must-Know Algorithms for Automating Chart Pattern Trading in Python
https://www.youtube.com/watch?v=X31hyMhB-3s

# Direction Change Algorithm
Finds tops/bottoms after price has retraced by a given percentage. Time between tops/bottoms is not consider.
Harmonic Pattern  do not consider the time between tops/bottoms

# Harmonic pattern
The ULTIMATE Beginner's Guide to HARMONIC PATTERNS
https://www.youtube.com/watch?v=ir3XB3CGdYU
Harmonic pattern is price action pattern where a sequence of price movements follow well-defined ranges of Fibonacci ratios. When consecutive price movements respect these ratios, price enters the Price Reversal Zone, which is a zone with higher probability of reversal due to the convergence of several Fibonacci ratios

https://www.vietcap.com.vn/kien-thuc/mo-hinh-harmonic-la-gi-nhung-mo-hinh-harmonic-pho-bien-va-cach-giao-dich

## Bullish Bat (Double Top)
XABCD /\/\
AB/XA = 38.2% - 50%
BC/AB = 38.2% - 88.6%
CD/BC = 161.8% - 261.8%
AD/XA = 88.6%
After D trend will up /

## Bearish Bat (Double Bottom)
XABCD \/\/
AB/XA = 38.2% - 50%
BC/AB = 38.2% - 88.6%
CD/BC = 161.8% - 261.8%
AD/XA = 88.6%
After D trend will down \

## Bullish/Bearish ALT Bat
XABCD 
AB/XA = 38.2% 
BC/AB = 38.2% - 88.6%
CD/BC = 200% - 361.8%
AD/XA = 113%
After D trend will up / or down \

## Bullish/Bearish Butterfly
XABCD
AB/XA = 78.6%
BC/AB = 38.2% - 88.6%
CD/BC = 161.8% - 224%
AD/XA = 88.6%
After D trend will up / or down \

## Bullish/Bearish Crab
XABCD
AB/XA = 38.2% - 61.8%
BC/AB = 38.2% - 88.6%
CD/BC = 261.8% - 361.8%
AD/XA = 161.8%
After D trend will up / or down \

## Bullish/Bearish Deep Crab
XABCD
AB/XA = 88.6%
BC/AB = 38.2% - 88.6%
CD/BC = 200% - 361.8%
AD/XA = 161.8%
After D trend will up / or down \

## Bullish/Bearish Gartley
XABCD
AB/XA = 61.8%
BC/AB = 38.2% - 88.6%
CD/BC = 113% - 161.8%
AD/XA = 78.6%
After D trend will up / or down \

## Bullish/Bearish Shark
XABCD
AB/XA = N/A
BC/AB = 113% - 161.8%
CD/BC = 161.8% - 224%
AD/XA = 88.6% - 113%
After D trend will up / or down \

## Bullish/Bearish Cypher
XABCD
AB/XA = 38.2% - 61.8%
BC/AB = 113% - 141%
CD/BC = 127% - 200%
AD/XA = 78.6%
After D trend will up / or down \

## Bullish/Bearish 5-0
0XABCD
AB/XA = 113% - 161.8%
BC/AB = 161.8% - 224%
CD/BC = 50%
AD/XA = N/A
After D trend will up / or down \

## Bullish/Bearish AB=CD
ABCD
BC/AB = 38.2% - 88.6%
CD/BC = 113% - 261.8%
After D trend will up / or down \

## Bullish/Bearish Three Drives
0XABCD \/\/\
XA/0X = N/A
AB/XA = 127% - 161.8%
CD/BC = 127% - 161.8%
AD/XA = N/A
After D trend will up / or down \

# Coding
extremes
        ext_i     ext_p  type  seg_height  retrace_ratio
conf_i                                                  
222        98  42775.00     1         NaN            NaN
560       356  42180.77    -1      594.23            NaN
1513     1508  45372.79     1     3192.02       5.371691
1593     1549  44686.00    -1      686.79       0.215158
2137     1986  45879.63     1     1193.63       1.737984
[217 rows x 5 columns]

```
extremes['seg_height']
conf_i
222          NaN
560       594.23
1513     3192.02
Name: seg_height, Length: 217, dtype: float64
formula: height2 - height1 
```


extremes['retrace_ratio']
conf_i
222           NaN
560           NaN
1513     5.371691
1593     0.215158
Name: retrace_ratio, Length: 217, dtype: float64

ohlc
                          open      high       low     close         r
date                                                                  
55969-09-28 00:00:00  42283.58  42298.62  42261.02  42298.61  0.000506
55969-09-28 16:40:00  42298.62  42320.00  42298.61  42320.00  0.000130
55969-09-29 09:20:00  42319.99  42331.54  42319.99  42325.50  0.001003
55969-09-30 02:00:00  42325.50  42368.00  42325.49  42367.99  0.000690

output
{'Gartley': {'bull_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bull_patterns': [...], 'bear_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bear_patterns': [...]}, 'Bat': {'bull_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bull_patterns': [...], 'bear_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bear_patterns': [...]}, 'Butterfly': {'bull_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bull_patterns': [...], 'bear_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bear_patterns': [...]}, 'Crab': {'bull_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bull_patterns': [...], 'bear_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bear_patterns': [...]}, 'Deep Crab': {'bull_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bull_patterns': [...], 'bear_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bear_patterns': [...]}, 'Cypher': {'bull_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bull_patterns': [...], 'bear_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bear_patterns': [...]}, 'Shark': {'bull_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bull_patterns': [...], 'bear_signal': array([0., 0., 0., ..., 0., 0., 0.]), 'bear_patterns': [...]}}

# Get 
# i 220 => 44640
```
if extremes.index[extreme_i + 1] == i:
            entry_taken = 0
            extreme_i += 1
```
Step i = 560
extremes.index[extreme_i + 1] = 560
entry_taken = 0
extreme_i = 1

Step i = 1513
extremes.index[extreme_i + 1] = 1513
entry_taken = 0
extreme_i = 2

Step i = 1593
extremes.index[extreme_i + 1] = 1593
entry_taken = 0
extreme_i = 3

# D_price
Current high or current low depend on type

#
dc_retrace
0.7078291763129876

#
xa_ad_retrace
5.034010400013437

#
def get_error