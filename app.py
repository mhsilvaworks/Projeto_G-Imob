import os
import base64
from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///gerimovel.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        acao = request.form.get("acao")
        
        # --- CADASTROS ---
        if acao == "CadastrarImovel":
            nome = request.form.get("nome_imovel")
            endereco = request.form.get("endereco")
            cep = request.form.get("cep")
            foto = request.files.get("foto_imovel")
            foto_bytes = foto.read() if foto else None
            if not nome or not endereco: return redirect("/")
            db.execute("INSERT INTO Imovel (nome, endereco, cep, foto) VALUES (?, ?, ?, ?)", nome, endereco, cep, foto_bytes)
            return redirect("/")

        elif acao == "CadastrarInquilino":
            nome = request.form.get("nome_inquilino")
            cpf = request.form.get("cpf")
            descricao = request.form.get("descricao")
            nasc = request.form.get("data_nascimento")
            tel = request.form.get("telefone")
            foto = request.files.get("foto_inquilino")
            foto_bytes = foto.read() if foto else None
            if not nome: return redirect("/")
            db.execute("INSERT INTO Inquilino (nome, cpf, descricao, data_nascimento, telefone, foto) VALUES (?, ?, ?, ?, ?, ?)", nome, cpf, descricao, nasc, tel, foto_bytes)
            return redirect("/")

        elif acao == "CadastrarContrato":
            inquilino_id = request.form.get("inquilino_contrato")
            imovel_id = request.form.get("imovel_contrato")
            inicio = request.form.get("data_inicio")
            fim = request.form.get("data_fim")
            valor = request.form.get("valor_contrato")
            dia = request.form.get("dia_pagamento")
            if not inquilino_id or not imovel_id: return redirect("/")
            db.execute("INSERT INTO Contrato (inquilino_id, imovel_id, data_inicio, data_fim, valor, dia_pagamento) VALUES (?, ?, ?, ?, ?, ?)", inquilino_id, imovel_id, inicio, fim, valor, dia)
            return redirect("/")

        return redirect("/")

    else:
        # --- GET: TELA PRINCIPAL ---
        itens = db.execute("""
            SELECT 
                Imovel.id AS imovel_id, Imovel.nome AS nome_imovel, Imovel.foto AS foto_imovel,
                Inquilino.nome AS nome_inquilino, Inquilino.foto AS foto_inquilino
            FROM Imovel
            LEFT JOIN Contrato ON Imovel.id = Contrato.imovel_id
            LEFT JOIN Inquilino ON Contrato.inquilino_id = Inquilino.id
        """)

        # Processar fotos do GRID
        for item in itens:
            if item["foto_imovel"]:
                b64 = base64.b64encode(item["foto_imovel"]).decode('utf-8')
                item["foto_imovel"] = f"data:image/jpeg;base64,{b64}"
            else:
                item["foto_imovel"] = "/static/images/unnamed.jpg"

            if item["foto_inquilino"]:
                b64 = base64.b64encode(item["foto_inquilino"]).decode('utf-8')
                item["foto_inquilino"] = f"data:image/jpeg;base64,{b64}"
            else:
                # CORREÇÃO AQUI: Mudei para .jpg
                item["foto_inquilino"] = "/static/images/user.jpg" 

        # Listas para Modais e Menu
        lista_imoveis = db.execute("SELECT id, nome FROM Imovel")
        lista_inquilinos = db.execute("SELECT id, nome, cpf, foto FROM Inquilino")
        
        # Processar fotos do MENU LATERAL
        for inq in lista_inquilinos:
            if inq["foto"]:
                b64 = base64.b64encode(inq["foto"]).decode('utf-8')
                inq["foto"] = f"data:image/jpeg;base64,{b64}"
            else:
                # CORREÇÃO AQUI: Mudei para .jpg
                inq["foto"] = "/static/images/user.jpg"

        return render_template("index.html", itens=itens, lista_imoveis=lista_imoveis, lista_inquilinos=lista_inquilinos)

# --- DETALHES DO IMÓVEL ---
@app.route("/detalhes/<int:id>")
def detalhes(id):
    dados = db.execute("""
        SELECT 
            Imovel.id, Imovel.nome, Imovel.endereco, Imovel.cep, Imovel.foto AS foto_imovel,
            Contrato.data_inicio, Contrato.data_fim, Contrato.valor, Contrato.dia_pagamento,
            Inquilino.nome AS nome_inquilino, Inquilino.cpf, Inquilino.telefone, Inquilino.foto AS foto_inquilino
        FROM Imovel
        LEFT JOIN Contrato ON Imovel.id = Contrato.imovel_id
        LEFT JOIN Inquilino ON Contrato.inquilino_id = Inquilino.id
        WHERE Imovel.id = ?
    """, id)

    if not dados: return redirect("/")
    imovel = dados[0]

    if imovel["foto_imovel"]:
        b64 = base64.b64encode(imovel["foto_imovel"]).decode('utf-8')
        imovel["foto_imovel"] = f"data:image/jpeg;base64,{b64}"
    else:
        imovel["foto_imovel"] = "/static/images/unnamed.jpg"

    if imovel["foto_inquilino"]:
        b64 = base64.b64encode(imovel["foto_inquilino"]).decode('utf-8')
        imovel["foto_inquilino"] = f"data:image/jpeg;base64,{b64}"
    else:
        # CORREÇÃO AQUI: Mudei para .jpg
        imovel["foto_inquilino"] = "/static/images/user.jpg"

    return render_template("detalhes.html", imovel=imovel)

# --- DETALHES DO INQUILINO ---
@app.route("/inquilino/<int:id>")
def inquilino(id):
    dados = db.execute("""
        SELECT Inquilino.*, Imovel.nome AS morando_em
        FROM Inquilino
        LEFT JOIN Contrato ON Inquilino.id = Contrato.inquilino_id
        LEFT JOIN Imovel ON Contrato.imovel_id = Imovel.id
        WHERE Inquilino.id = ?
    """, id)

    if not dados: return redirect("/")
    inq = dados[0]

    if inq["foto"]:
        b64 = base64.b64encode(inq["foto"]).decode('utf-8')
        inq["foto"] = f"data:image/jpeg;base64,{b64}"
    else:
        # CORREÇÃO AQUI: Mudei para .jpg
        inq["foto"] = "/static/images/user.jpg"

    return render_template("inquilino.html", inquilino=inq)