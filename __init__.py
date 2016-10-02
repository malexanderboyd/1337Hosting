from flask import Flask, render_template, request, url_for, redirect
import os,subprocess
app = Flask(__name__)

@app.route("/genImage", methods=['POST'])
def genImage():
    imgCode = request.json['img']
    if imgCode is not None:
        with open('../../../var/local/var.txt', 'r') as f:
            incrementNum = f.read().splitlines()
            if incrementNum > 0:
                writepath = '../../../../var/www/imageHot/imageHot/templates/gallery/' + str(incrementNum[0]) + ".html"
            else:
                f.close()
        with open(writepath, "a+") as f:
            htmlHeaders = "<!doctype html><html lang='en'><head><meta charset='utf-8'><title>1337Site</title><meta name='description' content='We host images lulz'></head><body>\n"
            styles = '<link rel="stylesheet" href="https://code.getmdl.io/1.1.3/material.blue-green.min.css" /><link rel="stylesheet" href="{{ url_for(\'static\', filename=\'style.css\')}}" /><link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">    <link href="https://fonts.googleapis.com/css?family=Exo+2" rel="stylesheet">"\n'
            htmlFooter = "</body></html>"
            imageBox = "<div id=\"experienceBox\" class=\"mdl-cell mdl-cell--4-col mdl-shadow--2dp\">\n"
            linkBox = "<div id=\"linkBox\" class=\"mdl-cell mdl-cell--4-col mdl-shadow--2dp\">\n"
            link = "<input id='link' type='text' value='http://104.131.183.72/gallery/" + str(incrementNum[0]) + "'/>"
            f.write(htmlHeaders)
            f.write(styles)
            f.write(imageBox)
            f.write("<img src=\"" + str(imgCode) + "\"/>\n")
            f.write("</div>\n")
            f.write(linkBox)
            f.write(link)
            f.write("</div>\n")
            f.write(htmlFooter)
            if(subprocess.call("../../../var/local/GenClean.sh", shell=True)):
                return str(incrementNum[0])
            else:
                return "1337:bashError"
    else:
        return 'No image code'


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/gallery/<int:imageId>")
def galleryRoute(imageId):
    imageURL = "/gallery/" + str(imageId) + ".html"
    return render_template(imageURL);



if __name__ == "__main__":
    app.config.update(
        PROPAGATE_EXCEPTIONS=True
    )
    app.run(debug=True)
