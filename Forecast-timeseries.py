import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('dataset.xlsx')

pd.DataFrame(df.values.flatten())

pd.DataFrame(df.values.flatten()).plot(color='r')

pd.date_range(start='1/1/2012', end='10/1/2018', freq='M')

pd.DataFrame(df.values.flatten(), index = pd.date_range(start='1/1/2012', end='1/1/2019', freq='M'))


# Annual revenue plot 

plt.figure(figsize=(18,10))
pd.DataFrame(df.values.flatten(), index = pd.date_range(start='1/1/2012', end='1/1/2019', freq='M')).plot()
plt.ylabel('million')
plt.title('Revenue')
plt.show()

# Prophet 2019 Forecast
import fbprophet 

df = data.rename(columns={'index': 'ds', 'rev': 'y'}) 

fbp.fit(df)

df_forecast = fbp.make_future_dataframe(periods=12,freq='M') 
df_forecast = fbp.predict(df_forecast) 
fbp.plot(df_forecast, xlabel = 'Date', ylabel = 'Turnover') 
plt.title('Plot of 2019 Foreacast')

#This code helps to compile forecast plot as previous code
fig1=fbp.plot(df_forecast)

# time series components 
fig2=fbp.plot_components(df_forecast)

# change points 

fbp.plot(df_forecast, xlabel = 'Date', ylabel = 'Turnover') 
plt.vlines([str(date) for date in fbp.changepoints], 
ymin = 0, ymax= 3e8, color='r',         
linestyles = 'dashed')
plt.title('Restonet') 
print('Change points:') 
print(fbp.changepoints)

# holiday effects
holiday = pd.DataFrame({   'ds': pd.to_datetime(['2015-09-01', '2016-07-01','2012-08-01', '2012-10-01',
                        '2013-08-01', '2014-07-01', '2014-10-01',
                        '2015-07-01', '2015-09-01', '2016-07-01',
                        '2016-09-01', '2017-06-01', '2017-09-01']),  
                        'holiday': 'start',   'lower_window': 0,   'upper_window': 3, }) 
holiday.head()

# holiday effects 
fbp = fbprophet.Prophet(holidays=holiday) 
fbp.fit(df) 
df_forecast = fbp.make_future_dataframe(periods=24,freq='M') 
df_forecast2 = fbp.predict(df_forecast) 
fbp.plot(df_forecast2, xlabel = 'Date', ylabel = 'Turnover') 
plt.title('Holiday Effectcs')


# Holiday Effects Forecasts Components
fig3=fbp.plot_components(df_forecast2)


# Correlation plot

a,x = plt.subplots(figsize=(16, 7))
corr = df.corr() max_corr = corr.nlargest(10, 'y_yes')['y_yes'].index cm = np.corrcoef(df[max_corr].values.T) 
matrix = sns.heatmap(cm, annot=True, square=True, fmt='.2f',              
linewidths= 0.1, vmax = 1, cmap = 'RdBu',               
yticklabels=max_corr.values, xticklabels=max_corr.values, ax = x) plt.show()




