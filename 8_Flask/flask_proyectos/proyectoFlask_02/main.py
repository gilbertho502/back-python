from flask import Flask, render_template

app = Flask(__name__)

heroes_info = {
    'spiderman': {'nombre': 'peter parker',
                  'nacionalidad': 'USA',
                  'poderes': 'telarana',
                  'fecha': 'enero 1987',
                  'picture': 'https://i0.wp.com/hipertextual.com/wp-content/uploads/2021/03/db9960b2dec9108169f86290953e15caef59dc62_s2_n1-scaled.jpeg?resize=800%2C403&ssl=1'},
    'superman': {'nombre': 'clark ken',
                  'nacionalidad': 'USA',
                  'poderes': 'fuerza',
                  'fecha': 'octubre 1980',
                  'picture': 'https://hbomax-images.warnermediacdn.com/images/GYEEGBAUseGoDLQEAAAAC/tileburnedin?size=640x360&partner=hbomaxcom&language=es-419&v=48b963927a43719ec9920cb27839b807&host=art-gallery-latam.api.hbo.com&w=640'},
    'chapulin': {'nombre': 'roberto bolanos',
                  'nacionalidad': 'mexico',
                  'poderes': 'chipote',
                  'fecha': 'octubre 1975',
                  'picture': 'https://es.web.img3.acsta.net/r_1280_720/pictures/14/06/17/11/37/020273.jpg'},   
}

@app.route('/')
def index():
    return render_template('index.html', )

@app.route('/detalles/<key>')
def detalles(key):
    return render_template('heroe.html', heroe = heroes_info[key])
    
app.run(debug=True)