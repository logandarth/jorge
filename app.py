from flask import Flask,render_template


app = Flask("meu app")

posts = [{
"Titulo":"minha primeira postagem",
"Texto":"teste"

},
{
"Titulo":"segundo Post",
"Texto":"Outro teste"

}]
@app.route("/")
def exibir_entradas():
    entradas=posts #mock
    return render_template('exibir_entradas.html',entradas = entradas)

