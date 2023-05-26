from pywebio.input import*
from pywebio.output import*
from pywebio import config

#import all the required modules
from flask import Flask
from pywebio.platform.flask import webio_view

app = Flask(__name__)
app.secret_key = "secretkey11111"

dol = 432
eur = 435
ghc = 42

config(theme="dark")
def main():
    def dollars(dol):
        #pass
        result = dol * dol
        put_code("{:,} dollars is equal to {:,} NGN".format(dol,result),scope="disp").style("color:red;font-size:24px; width:70%")

    def euros(euro):
        #pass
        result = euro* eur
        put_code("{:,} Euros is equal to {:,} NGN".format(euro,result),scope="disp").style("color:red;font-size:24px; width:70%")

    def cedis(cd):
        result = cd * ghc
        put_code("{:,} Cedis is equal to {:,} NGN".format(cd,result),scope="disp").style("color:red;font-size:24px; width:70%")


    put_html("<h1>Currency Converter</h1>").style("text-align:center;")
    put_html("<p><b>convert to Nigerian Naira</b></p>").style("text-align:center; font-style:italic;")
    put_scope("disp")

    while True:
        options = radio("Choose Currency",["Dollar","Euro","Cedi"],inline = True, required=True)

        if options =="Dollar":
            resp = input("How many $:",type=NUMBER,onchange=lambda c: clear("disp"))
            dollars(resp)
            
        elif options == "Euro":
            resp = input("How many Euros:",type=NUMBER,onchange= lambda c: clear("disp"))
            euros(resp)
        elif options == "Cedi":
            resp = input("How many Cedis:",type=NUMBER,onchange= lambda c: clear("disp"))
            cedis(resp)

# add a flask url_rule for routing
app.add_url_rule('/', 'webio_view', webio_view(main),methods=['GET','POST']) 

if __name__ =="__main__":
    #start_server(main,debug=True)
    #run the app and enable debugging
    app.run(debug=False)