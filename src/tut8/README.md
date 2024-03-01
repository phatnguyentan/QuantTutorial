# Golden Ratio
```
1.618
0,1,1,2,3,5,8,13,221,34,55,89,144,233,377
3/2 = 1.5
8/5 = 1.6
55/34 = 1.617
377/233 = 1.618
```
# Fibonacci Retracement
```
Given 2 sides form a triangle without a base (bottom side) /\
Height is a perpendicular line from the origin to the top of an edge  |\ or |/
Example 
height1 =  233
height2 =  377
ratio = 233/377 = 0.618
```
## 3 Must-Know Algorithms for Automating Chart Pattern Trading in Python
https://www.youtube.com/watch?v=X31hyMhB-3s

# Direction Change Algorithm
Finds tops/bottoms after price has retraced by a given percentage. Time between tops/bottoms is not consider.
Harmonic Pattern  do not consider the time between tops/bottoms

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

extremes['seg_height']
conf_i
222          NaN
560       594.23
1513     3192.02
Name: seg_height, Length: 217, dtype: float64

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

#
dc_retrace
0.7078291763129876

#
xa_ad_retrace
5.034010400013437

#
def get_error