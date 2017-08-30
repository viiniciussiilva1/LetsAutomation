
from flask import Flask, render_template

import datetime
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

tempdata = {
      'title' : 'GPIO pins are not duplex (they can read or write but not both) ... you must explicitly change it to write mode to write and read mode to read ...'
      }
 
statuspin = {'statusSaida1' : False,
			 'statusSaida2' : False,
			 'statusSaida3' : False,
			 'statusSaida4' : False
			}	  
			
pinSaida1 = 16;
pinSaida2 = 18;
pinSaida3 = 22;
pinSaida4 = 35;
pinSaida5 = 36;
pinSaida6 = 38;
pinSaida7 = 40;
pinSaida8 = 37;

GPIO.setup(pinSaida1, GPIO.OUT)
GPIO.setup(pinSaida2, GPIO.OUT)
GPIO.setup(pinSaida3, GPIO.OUT)
GPIO.setup(pinSaida4, GPIO.OUT)
GPIO.setup(pinSaida5, GPIO.OUT)
GPIO.setup(pinSaida6, GPIO.OUT)
GPIO.setup(pinSaida7, GPIO.OUT)
GPIO.setup(pinSaida8, GPIO.OUT)

GPIO.output(pinSaida1, True)
GPIO.output(pinSaida2, True)
GPIO.output(pinSaida3, True)
GPIO.output(pinSaida4, True)
GPIO.output(pinSaida5, True)
GPIO.output(pinSaida6, True)
GPIO.output(pinSaida7, True)
GPIO.output(pinSaida8, True)

@app.route("/")
def home():

   tempdata = {
      'title' : 'RPi GPIO Control'
      }    
   return retornaestatus()

   
@app.route("/saida1/on")
def actionSaida1On():		
	GPIO.output(pinSaida1, True)		  
	return retornaestatus()
	
@app.route("/saida1/off")
def actionSaida1Off():		
	GPIO.output(pinSaida1, False)		  
	return retornaestatus()	
	
	
@app.route("/saida2/on")
def actionSaida2On():		
	GPIO.output(pinSaida2, True)		  
	return retornaestatus()
	
@app.route("/saida2/off")
def actionSaida2Off():		
	GPIO.output(pinSaida2, False)		  
	return retornaestatus()		

@app.route("/saida3/on")
def actionSaida3On():		
	GPIO.output(pinSaida3, True)		  
	return retornaestatus()
	
@app.route("/saida3/off")
def actionSaida3Off():		
	GPIO.output(pinSaida3, False)		  
	return retornaestatus()	


@app.route("/saida4/on")
def actionSaida4On():		
	GPIO.output(pinSaida4, True)		  
	return retornaestatus()
	
@app.route("/saida4/off")
def actionSaida4Off():		
	GPIO.output(pinSaida4, False)		  
	return retornaestatus()		
	
@app.route("/saida5/on")
def actionSaida5On():		
	GPIO.output(pinSaida5, True)		  
	return retornaestatus()
	
@app.route("/saida5/off")
def actionSaida5Off():		
	GPIO.output(pinSaida5, False)		  
	return retornaestatus()	
	
@app.route("/saida6/on")
def actionSaida6On():		
	GPIO.output(pinSaida6, True)		  
	return retornaestatus()
	
@app.route("/saida6/off")
def actionSaida6Off():		
	GPIO.output(pinSaida6, False)		  
	return retornaestatus()	
	
@app.route("/saida7/on")
def actionSaida7On():		
	GPIO.output(pinSaida7, True)		  
	return retornaestatus()
	
@app.route("/saida7/off")
def actionSaida7Off():		
	GPIO.output(pinSaida7, False)		  
	return retornaestatus()	
	
@app.route("/saida8/on")
def actionSaida8On():		
	GPIO.output(pinSaida8, True)		  
	return retornaestatus()
	
@app.route("/saida8/off")
def actionSaida8Off():		
	GPIO.output(pinSaida8, False)		  
	return retornaestatus()	

def retornaestatus():

	statusSaida1 = GPIO.input(pinSaida1);
	statusSaida2 = GPIO.input(pinSaida2);
	statusSaida3 = GPIO.input(pinSaida3);
	statusSaida4 = GPIO.input(pinSaida4);
	statusSaida5 = GPIO.input(pinSaida5);
	statusSaida6 = GPIO.input(pinSaida6);
	statusSaida7 = GPIO.input(pinSaida7);
	statusSaida8 = GPIO.input(pinSaida8);
	
	statuspin = {'statusSaida1' : statusSaida1,
			 'statusSaida2' : statusSaida2,
			 'statusSaida3' : statusSaida3,
			 'statusSaida4' : statusSaida4,
			 'statusSaida5' : statusSaida5,
			 'statusSaida6' : statusSaida6,
			 'statusSaida7' : statusSaida7,
			 'statusSaida8' : statusSaida8
			}	  
			
	return render_template('webraspio.html', **statuspin)
	

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
   
   
   