import flask
from flask import Flask , render_template , send_file , request
from flask import Flask, render_template, request, session, redirect
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

import numpy as np
import Crop_model as CM

app = Flask(__name__)

model_Apple = load_model('model_Apple.h5')

def pred_Apple(Apple_data):
  test_image = load_img(Apple_data, target_size = (256, 256)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model_Apple.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)

  return pred

model_Corn = load_model('model_corn.h5')

def pred_Corn(Corn_data):
  test_image_1 = load_img(Corn_data, target_size = (256, 256)) # load image 
  print("@@ Got Image for prediction")
  
  test_image_1 = img_to_array(test_image_1)/255 # convert image to np array and normalize
  test_image_1 = np.expand_dims(test_image_1, axis = 0) # change dimention 3D to 4D
  
  result = model_Corn.predict(test_image_1) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)

  return pred

model_Grapes = load_model('model_Grape.h5')

def pred_Grapes(pred_Grapes_data):
  test_image_1 = load_img(pred_Grapes_data, target_size = (256, 256)) # load image 
  print("@@ Got Image for prediction")
  
  test_image_1 = img_to_array(test_image_1)/255 # convert image to np array and normalize
  test_image_1 = np.expand_dims(test_image_1, axis = 0) # change dimention 3D to 4D
  
  result = model_Grapes.predict(test_image_1) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)

  return pred

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/apple.html")
def apple1():
    return render_template("apple.html")

@app.route("/apple.html",methods = ['GET','POST'])
def apple():
    if request.method== 'POST':
        full_name = request.form["name"]
        phone_number = request.form["phone"]
        address = request.form["address"]
        state = request.form["state"]
        region= request.form["region"]
        TypeOfSoil = request.form["soil"]
        Season = request.form["season"]
        FertilizerUsed = request.form["fertilizer"]
        
        file = request.files['diagnoseapple'] # fet input
        filename = file.filename      
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/upload', filename)
        file.save(file_path)
        print(file_path)
        X= str(pred_Apple(Apple_data=file_path))
        
        if (X=='[0]'):
            return render_template('applescab.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
        elif (X=='[1]'):
            return render_template('blackrot.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
        elif (X=='[2]'):
            return render_template('applerust.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
        else:
            return render_template('applerust.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)

@app.route("/corn.html")
def corn1():
    return render_template("corn.html")

@app.route("/corn.html",methods = ["GET","POST"])
def corn():
    if request.method== 'POST':
        full_name = request.form["name"]
        phone_number = request.form["phone"]
        address = request.form["address"]
        state = request.form["state"]
        region= request.form["region"]
        TypeOfSoil = request.form["soil"]
        Season = request.form["season"]
        FertilizerUsed = request.form["fertilizer"]
        
        file = request.files['diagnosecorn'] # fet input
        filename = file.filename      
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/upload', filename)
        file.save(file_path)
        print(file_path)
        X = str(pred_Corn(Corn_data=file_path))
        
        if (X=='[0]'):
            return render_template('grayspot.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
        elif (X=='[1]'):
            return render_template('commonrust.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
        elif X==(X=='[2]'):
            return render_template('healthy.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
        else:
            return render_template('leafblight.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
    

        #return render_template("corn.html")    

@app.route('/grapes.html')
def grapes_1():
    return render_template('grapes.html')

@app.route("/grapes.html",methods = ["GET","POST"])
def grapes():
    if request.method== 'POST':
        full_name = request.form["name"]
        phone_number = request.form["phone"]
        address = request.form["address"]
        state = request.form["state"]
        region= request.form["region"]
        TypeOfSoil = request.form["soil"]
        Season = request.form["season"]
        FertilizerUsed = request.form["fertilizer"]
        
        file = request.files['diagnosegrapes'] # fet input
        filename = file.filename     
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/upload', filename)
        file.save(file_path)

        X = str(pred_Grapes(pred_Grapes_data=file_path))

        if (X=='[0]'):
            return render_template('measles.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
        elif (X=='[1]'):
            return render_template('Grape_Healthy.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
        else:
            return render_template('idaripsis.html',name=full_name,no=phone_number,addr=address,states=state,regions=region,soil=TypeOfSoil,season=Season,Fertilizer=FertilizerUsed)
    
@app.route('/guide.html')
def guide_veiw():
    return render_template('guide.html')

@app.route('/Soil.html')
def Soils():
    return render_template('Soil.html')

@app.route('/Fertilizer.html')
def Fertilizers():
    return render_template('Fertilizer.html')


@app.route('/Crop.html')
def Crops():
    return render_template('Crop.html')

@app.route('/yield.html')
def yields():
    return render_template('yield.html')

@app.route('/Crop_pred.html')
def gyuide():
    return render_template('Crop_pred.html')

@app.route("/Crop_pred.html",methods = ["GET","POST"])
def Crops_preds():
    if request.method== 'POST':
        N = request.form["N"]
        P = request.form["P"]
        K = request.form["K"]
        temperature = request.form["temperature"]
        humidity= request.form["humidity"]
        ph = request.form["ph"]
        rainfall = request.form["rainfall"]

        X = str(CM.predict(N,P,K,temperature,humidity,ph,rainfall))

        if (X=='[0]'):
            return render_template('Crop_pred.html',data_pred='Rice is the most suitable crop for the following conditions')
        elif (X=='[1]'):
            return render_template('Crop_pred.html',data_pred='Maize is the most suitable crop for the following conditions')
        elif (X=='[2]'):
            return render_template('Crop_pred.html',data_pred='Jute is the most suitable crop for the following conditions')
        elif (X=='[3]'):
            return render_template('Crop_pred.html',data_pred='Cotton is the most suitable crop for the following conditions')
        elif (X=='[4]'):
            return render_template('Crop_pred.html',data_pred='Coconut is the most suitable crop for the following conditions')
        elif (X=='[5]'):
            return render_template('Crop_pred.html',data_pred='Papaya is the most suitable crop for the following conditions')
        elif (X=='[6]'):
            return render_template('Crop_pred.html',data_pred='Orange is the most suitable crop for the following conditions')
        elif (X=='[7]'):
            return render_template('Crop_pred.html',data_pred='Apple is the most suitable crop for the following conditions')
        elif (X=='[8]'):
            return render_template('Crop_pred.html',data_pred='Muskmelon is the most suitable crop for the following conditions')
        elif (X=='[9]'):
            return render_template('Crop_pred.html',data_pred='Watermelon is the most suitable crop for the following conditions')
        elif (X=='[10]'):
            return render_template('Crop_pred.html',data_pred='Grapes is the most suitable crop for the following conditions')
        elif (X=='[11]'):
            return render_template('Crop_pred.html',data_pred='Mango is the most suitable crop for the following conditions')
        elif (X=='[12]'):
            return render_template('Crop_pred.html',data_pred='Banana is the most suitable crop for the following conditions')
        elif (X=='[13]'):
            return render_template('Crop_pred.html',data_pred='Pomegranate is the most suitable crop for the following conditions')
        elif (X=='[14]'):
            return render_template('Crop_pred.html',data_pred='Lentil is the most suitable crop for the following conditions')
        elif (X=='[15]'):
            return render_template('Crop_pred.html',data_pred='Blackgram is the most suitable crop for the following conditions')
        elif (X=='[16]'):
            return render_template('Crop_pred.html',data_pred='Mungbean is the most suitable crop for the following conditions')
        elif (X=='[17]'):
            return render_template('Crop_pred.html',data_pred='Mothbeans are the most suitable crop for the following conditions')
        elif (X=='[18]'):
            return render_template('Crop_pred.html',data_pred='Pigeonpeas is the most suitable crop for the following conditions')
        elif (X=='[19]'):
            return render_template('Crop_pred.html',data_pred='Kidneybeans is the most suitable crop for the following conditions')
        elif (X=='[20]'):
            return render_template('Crop_pred.html',data_pred='Chickpeas is the most suitable crop for the following conditions')
        elif (X=='[21]'):
            return render_template('Crop_pred.html',data_pred='Coffee is the most suitable crop for the following conditions')
        

# @app.route("/potatoes.html",methods = ["GET","POST"])
# def potatoes():
    
#     return render_template("potatoes.html")

if __name__ == "__main__":
    app.run(debug = True) 
