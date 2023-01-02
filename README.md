# Rainfall-Prediction
Rainfall Prediction Project is an art work of Artificial Intelligence. Its blend is a mixture of regression and cloud computing. This application gives the prediction of precipitation in mm expected during current time. Yes, it gives real time prediction. Although, its accuracy is only 75%, it gives good rainfall insights.

One more additional feature is that this application has a very clean graphical user interface. User just needs to type the name of the area/town for which weather is to be predicted and then hit the submit button. Its GUI is achieved using Python tkinter library.

The dataset for model training has been downloaded from https://power.larc.nasa.gov/data-access-viewer/ which is a data access portal created by NASA to distribute satellite data. Prediction is made on the basis of following features, Dew/Frost Point at 2 Meters (C), Temperature at 2 Meters (C), Earth Skin Temperature (C), Relative Humidity at 2 Meters (g/kg), Surface Pressure (kPa), Wind Speed at 10 Meters (m/s), and Wind Direction (degrees). 

The model is built and saved using pickle built-in module of python. There is also a python file credentials.py which contains some credentials which are used to get current above mentioned atmospheric features from a satellite’s API.

The Rainfall Prediction Project has also been evolved into a portable executable (.exe) application with the help of python pyinstaller package, which only needs the trained regression model to be present inside a folder named ‘data’, the folder should be itself placed in the working directory where the executable application program is listed. 
