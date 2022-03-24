from flask import Flask
app = Flask('__name__')

@app.route('/')
def minha_primira_rota():
  return '<h1>Minha primeira rota!</h1>'

if __name__ == '__main__':
  app.run(host='0.0.0.0')