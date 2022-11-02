from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Obtener el texto ingresado del requerimiento POST.
    input_text = request.jason.get("text")
    
    if not input_text:
        # Respuesta para enviar si input_text está indefinido.
       response = {
        "Status":"error",
        "message":"Por Favor Ingresa Algun Texto Por que sI"
       }
       return jasonify(response)
    else:
        predicted_emotion,predicted_emotion_img_url = (input_text)

        response = {
            "status":"success",
            "data":{
                "predicted_emotion": predicted_emotion,
                "predocted_emotion_img_url":predicted_emotion_img_url
            }
        }
        return jasonify(response)
        
        # Respuesta para enviar si input_text no está indefinido.
        
        # Enviar respuesta.         
        
       
    app.run(debug=True)



    