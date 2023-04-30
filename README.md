## Python porting of  Bollinger Bands TradingView Indicator


>Developed by [@edyatl](https://github.com/edyatl) April 2023 <edyatl@yandex.ru>

### Using [Python wrapper](https://github.com/TA-Lib/ta-lib-python) for [TA-LIB](http://ta-lib.org/) based on Cython instead of SWIG.

### Original Indicator code

```python
//@version=5 
indicator(shorttitle="BB", title="Bollinger Bands", overlay=true, timeframe="", timeframe_gaps=true) 

length = input.int(20, minval=1) 
src    = input(close, title="Source") 
mult   = input.float(2.0, minval=0.001, maxval=50, title="StdDev") 

basis = ta.sma(src, length) 
dev = mult * ta.stdev(src, length) 

upper = basis + dev 
lower = basis - dev 

offset = input.int(0, "Offset", minval = -500, maxval = 500) 

plot(basis, "Basis", color=#FF6D00, offset = offset) 
p1 = plot(upper, "Upper", color=#2962FF, offset = offset) 
p2 = plot(lower, "Lower", color=#2962FF, offset = offset) 

fill(p1, p2, title = "Background", color=color.rgb(33, 150, 243, 95))
```

### Original Indicator Overview

This Bollinger Bands indicator can be useful for traders who want to visualize the volatility of a financial asset's price over time. The indicator consists of three lines that are plotted based on a moving average and standard deviation. The upper band is two standard deviations above the moving average, the lower band is two standard deviations below the moving average, and the middle band is the moving average itself.

The code defines the input variables for the length of the moving average, the source of the data (close price by default), and the multiplier for the standard deviation (set to 2.0 by default). It then calculates the moving average and standard deviation using the ta.sma and ta.stdev functions provided by TradingView.

The upper and lower bands are calculated by adding and subtracting the standard deviation from the moving average, respectively. An offset can be added to the plot to shift the bands to the left or right on the chart.

Traders may use this indicator to identify potential price breakouts or to determine entry and exit points for trades. For example, if the price touches or breaks through the upper band, it may indicate that the asset is overbought and due for a price correction. Conversely, if the price touches or breaks through the lower band, it may indicate that the asset is oversold and due for a price increase.




