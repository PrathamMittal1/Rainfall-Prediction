from tkinter import *
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import requests
import sys
sys.path.append('data')
import credentials

loc = False


def predict():
    with open(credentials.model_path, 'rb') as fl:
        regressor = pickle.load(fl)           # loading trained model
    global loc
    try:                                      # fetching current weather conditions
        request = requests.request(method='GET',
                                   url='http://api.weatherapi.com/v1/forecast.json?key=' + credentials.APIKEY +
                                       '&q=' + city.get() + '&days=1&aqi=no&alerts=no').json()
        loc, current = request['location'], request['current']
        print(loc, '\n', current)
        dew_point = request['forecast']['forecastday'][0]['hour'][5]['dewpoint_c']
        print('dew_point: ', dew_point)
    except:
        l2.config(text='An error occurred!\nCould not connect to server.\nTry checking your internet connection.')

    if loc:
        l2.config(text=loc['name'] + '\n' + loc['region'] + ', ' + loc['country'] + '\nlat: ' +
                       str(loc['lat']) + ', lon: ' + str(loc['lon']) + '\nTime: ' + str(loc['localtime']))
        x_pred = np.array([[current['humidity'], current['wind_kph'] / 3.6,  # wind in mps
                            current['pressure_mb'] / 10, current['temp_c'],  # pressure in KPa
                            dew_point, current['wind_degree']]])
        y_pred = regressor.predict(x_pred)
        print('Predicted precipitation: ', y_pred)
        l3.config(text='Humidity: ' + str(current['humidity']) + '%, Pressure: ' + str(
            current['pressure_mb'] / 10) + ' KPa\n' +
                       'Temperature: ' + str(current['temp_c']) + ' Celsius\n' +
                       'Wind: ' + str(round(current['wind_kph'] / 3.6, 2)) + ' mps\nDew/Frost point: ' + str(
            dew_point) + ' Celsius')
        l1.config(text=str(round(y_pred[0], 2)) + ' mm Rainfall Predicted')


def main():
    window = Tk()
    window.configure(bg='#ffffff')
    window.title(credentials.TITLE)
    window.geometry('400x400-500+250')
    window.resizable(False, False)
    global l1, city, l2, l3
    l1 = Label(window, text='Click on the button to get rainfall prediction', font=('comic sans ms', 12),
               fg='#03e8fc', bg='#00889c', width=300, height=4)
    l1.pack()
    Label(window, text='\n\nCity/Area', bg='#ffffff').pack()
    city = StringVar()
    city_entry = Entry(window, textvariable=city)
    city_entry.pack()
    city_entry.insert(0, 'Saharanpur')
    button = Button(window, text='Predict Weather', command=predict, bg='#03e8fc', width=25, fg='#ffffff',
                    activebackground='#ff8800', font=('times', 11, 'bold'))
    button.pack(pady=50)
    l2 = Label(window, font=('times', 10), fg='#16366e', bg='#ffffff')
    l2.place(x=10, y=290)
    l3 = Label(window, font=('times', 10), fg='#fa3232', bg='#ffffff')
    l3.place(x=200, y=290)
    mainloop()


if __name__ == '__main__':
    main()
