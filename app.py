from flask import Flask, request, render_template ,app, jsonify, url_for  
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np
from datetime import datetime


app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%d").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%d").month)
        # print("Journey Date : ",Journey_day, Journey_month)
        #arrival_date_str = request.form["Arrival_Time"]
        arrival_date = datetime.strptime(date_dep, "%Y-%m-%d")
        
        # Calculate days left
        today = datetime.now()
        days_left = (arrival_date - today).days

        # Departure
        Journey_Time = request.form["Journey_Time"]

        Dep_hour = int(pd.to_datetime(Journey_Time, format ="%H:%M").hour)
        Dep_min = int(pd.to_datetime(Journey_Time, format ="%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        #date_arr = request.form["Arrival_Time"]
        #Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        #Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        #dur_hour = abs(Arrival_hour - Dep_hour)
        #dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        stop = int(request.form["stops"])
        # print(Total_stops)

        # Airline

        #Vistara      
        #Air India     
        #Indigo        
        #GO FIRST      
        #AirAsia       
        #SpiceJet       
        #StarAir          


        airline=request.form['airline']
        if(airline=='Vistara'):
           Vistara =1      
           Air_India=0     
           Indigo =0       
           GO_FIRST = 0  
           AirAsia =0     
           SpiceJet =0     
           StarAir =0        


        elif (airline=='IndiGo'):
           Vistara =0    
           Air_India=0     
           Indigo =1      
           GO_FIRST = 0  
           AirAsia =0     
           SpiceJet =0     
           StarAir =0        

        elif (airline=='Air India'):
           Vistara =0     
           Air_India=1
           Indigo =0       
           GO_FIRST = 0  
           AirAsia =0     
           SpiceJet =0     
           StarAir =0                    
        
        elif (airline=='SpiceJet'):
           Vistara =0     
           Air_India=0     
           Indigo =0       
           GO_FIRST = 0  
           AirAsia =0     
           SpiceJet =1     
           StarAir =0        

        elif (airline=='GO_FIRST'):
           Vistara =0    
           Air_India=0     
           Indigo =0       
           GO_FIRST = 1  
           AirAsia =0     
           SpiceJet =0     
           StarAir =0        

        elif (airline=='AirAsia'):
           Vistara =0    
           Air_India=0     
           Indigo =0       
           GO_FIRST = 0  
           AirAsia =1   
           SpiceJet =0     
           StarAir =0        

        
           

        elif (airline=='StarAir'):
           Vistara =0    
           Air_India=0     
           Indigo =0       
           GO_FIRST = 0  
           AirAsia =0
           SpiceJet =0     
           StarAir =1       



        else:
           Vistara =0    
           Air_India=0     
           Indigo =0       
           GO_FIRST = 0  
           AirAsia =0
           SpiceJet =0     
           StarAir =0      


        # Source
        #Delhi    
        #Mumbai       
        #Bangalore    
        #Kolkata      
        #Hyderabad    
        #Chennai     

        source = request.form["Source"]
        if (source == 'Delhi'):
            s_Delhi = 1
            s_Mumbai =0      
            s_Bangalore =0   
            s_Kolkata =0     
            s_Hyderabad =0   
            s_Chennai =0


        elif (source == 'Kolkata'):
            s_Delhi = 0
            s_Mumbai =0      
            s_Bangalore =0   
            s_Kolkata =1     
            s_Hyderabad =0 
            s_Chennai =0

        elif (source == 'Mumbai'):
            s_Delhi = 0
            s_Mumbai =1     
            s_Bangalore =0   
            s_Kolkata =0     
            s_Hyderabad =0   
            s_Chennai =0

        elif (source == 'Chennai'):
            s_Delhi = 0
            s_Mumbai =0      
            s_Bangalore =0   
            s_Kolkata =0     
            s_Hyderabad =0   
            s_Chennai =1


        elif (source == 'Bangalore'):
            s_Delhi = 0
            s_Mumbai =0      
            s_Bangalore =1   
            s_Kolkata =0     
            s_Hyderabad =0   
            s_Chennai =0

        elif (source == 'Hyderabad'):
            s_Delhi = 0
            s_Mumbai =0      
            s_Bangalore =0   
            s_Kolkata =0     
            s_Hyderabad =1  
            s_Chennai =0                        

        else:
            s_Delhi = 0
            s_Mumbai =0      
            s_Bangalore =0   
            s_Kolkata =0     
            s_Hyderabad =0   
            s_Chennai =0


        # Destination
        Destination = request.form["Destination"]
        if (Destination == 'Delhi'):
            d_Delhi = 1
            d_Mumbai =0      
            d_Bangalore =0   
            d_Kolkata =0     
            d_Hyderabad =0   
            d_Chennai =0
        
        elif (Destination == 'Mumbai'):
            d_Delhi = 0
            d_Mumbai =1      
            d_Bangalore =0   
            d_Kolkata =0     
            d_Hyderabad =0   
            d_Chennai =0

        elif (Destination == 'Bangalore'):
            d_Delhi = 0
            d_Mumbai =0      
            d_Bangalore =1  
            d_Kolkata =0     
            d_Hyderabad =0   
            d_Chennai =0

        elif (Destination == 'Kolkata'):
            d_Delhi = 0
            d_Mumbai =0      
            d_Bangalore =0   
            d_Kolkata =1     
            d_Hyderabad =0   
            d_Chennai =0

        elif (Destination == 'Hyderabad'):
            d_Delhi = 0
            d_Mumbai =0      
            d_Bangalore =0   
            d_Kolkata =0     
            d_Hyderabad =1  
            d_Chennai =0

        elif (Destination == 'Chennai'):
            d_Delhi = 0
            d_Mumbai =0      
            d_Bangalore =0   
            d_Kolkata =0     
            d_Hyderabad =0   
            d_Chennai =1

        else:
            d_Delhi = 0
            d_Mumbai =0      
            d_Bangalore =0   
            d_Kolkata =0     
            d_Hyderabad =0   
            d_Chennai =0
        
        #ticket_type= request.form.get[ticket_type]
        ticket_type = request.form.get("ticket_type", "")

        if (ticket_type == 'Premium'):
            t_Premium = 1
            t_Economy =0

        elif(ticket_type=='Economy'):
            t_Premium=0
            t_Economy=1

        else:
            t_Premium=0
            t_Economy=0        
        '''
        ['stop', 'days_left', 'Journey_month', 'Journey_day', 'Dep_hour',
       'Dep_min', 'airline_AirAsia', 'airline_GO FIRST', 'airline_Indigo',
       'airline_SpiceJet', 'airline_StarAir', 'airline_Vistara',
       'ticket_type_economy', 'source_Chennai', 'source_Delhi',
       'source_Hyderabad', 'source_Kolkata', 'source_Mumbai',
       'destination_Chennai', 'destination_Delhi', 'destination_Hyderabad',
       'destination_Kolkata', 'destination_Mumbai' ]


         '''
       


        prediction=model.predict([[
            stop,
            days_left,
            Journey_month,
            Journey_day,
            Dep_hour,
            Dep_min,
            AirAsia,
            GO_FIRST,
            Indigo,
            SpiceJet,
            StarAir,
            Vistara,     
            t_Economy,
            s_Chennai,     
            s_Delhi,
            s_Hyderabad,
            s_Kolkata, 
            s_Mumbai,         
            d_Chennai,     
            d_Delhi,
            d_Hyderabad, 
            d_Kolkata,
            d_Mumbai
                    
            ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)