import numpy
import pandas as pd
from sklearn import linear_model
#import tkinter as tk 
df = pd.read_excel('energyconsumption.xlsx', sheet_name='Sheet1')
x = df[["x1","x2","x3","x4","x5"]]
y= df[["y1"]]
regr = linear_model.LinearRegression()
regr.fit(x, y)
#regr.predict([[New_Interest_Rate ,New_Unemployment_Rate]])
#print("the data set : ",df)
print ("saisir les valuers des consommations xi : ")
x1 = float(input("x1="))
x2 = float(input("x2="))
x3 = float(input("x3="))
x4 = float(input("x4="))
x5 = float(input("x5="))
print("la valeur de y est : ")
s = regr.predict([[x1,x2,x3,x4,x5]])
print(s[0][0])
print("************** Le Modéle ***************")
print("les coefs de regression sont : ")
print('Coefficients: \n', regr.coef_)
''' something cool will happen here haha '''
'''
# tkinter GUI
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()
Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas1.create_window(260, 220, window=label_Intercept)
##
Coefficients_result  = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas1.create_window(260, 240, window=label_Coefficients)
##
label1 = tk.Label(root, text='x1: ')
canvas1.create_window(100, 100, window=label1)
entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(270, 100, window=entry1)
##
label2 = tk.Label(root, text=' x2: ')
canvas1.create_window(120, 120, window=label2)
entry2 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry2)
##
label3 = tk.Label(root, text=' x3: ')
canvas1.create_window(120, 120, window=label3)
entry3 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry3)
##
label4 = tk.Label(root, text=' x4: ')
canvas1.create_window(120, 120, window=label4)
entry4 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry4)
##
label5 = tk.Label(root, text=' x5: ')
canvas1.create_window(120, 120, window=label5)
entry5 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry5)

def values(): 
    global x1 
    x1 = float(entry1.get()) 
    global x2 
    x2 = float(entry2.get()) 
    global x3 
    x3 = float(entry3.get())
    global x4 
    x4 = float(entry4.get())
    global x5 
    x5 = float(entry5.get())   
    
    Prediction_result  = ('Predicted y (energy consumption): ', regr.predict([[x1,x2,x3,x4,x5]]))
    label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
    canvas1.create_window(260, 280, window=label_Prediction)
    
button1 = tk.Button (root, text='Predict Stock Index Price',command=values, bg='orange') # button to call the 'values' command above 
canvas1.create_window(270, 150, window=button1)
 

#plot 1st scatter 
figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df['Interest_Rate'].astype(float),df['Stock_Index_Price'].astype(float), color = 'r')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend() 
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')

#plot 2nd scatter 
figure4 = plt.Figure(figsize=(5,4), dpi=100)
ax4 = figure4.add_subplot(111)
ax4.scatter(df['Unemployment_Rate'].astype(float),df['Stock_Index_Price'].astype(float), color = 'g')
scatter4 = FigureCanvasTkAgg(figure4, root) 
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax4.legend() 
ax4.set_xlabel('Unemployment_Rate')
ax4.set_title('Unemployment_Rate Vs. Stock Index Price')

root.mainloop()
'''
