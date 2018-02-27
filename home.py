from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route('/home/ajwahir/imagine_cup/cfd/static/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
  app.run(debug=True)