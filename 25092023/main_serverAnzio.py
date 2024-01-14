from flask import Flask, json, request
import csv
from pathlib import Path

sFilePath = Path("anagrafe_anzio.csv").resolve()

api = Flask(__name__)

@api.route('/interrogazione', methods=['GET'])
def InterrogaAnagrafe():
    result = []
    print("interrogazione: ricevuta chiamata")
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata" + content_type)
    if content_type == 'application/json':
        req = request.json
        if isinstance(req, dict):
            print(req)
            tipo = req["Tipo"]
            valore = req["Valore"]
            with open(sFilePath, 'r') as file:
                csvreader = csv.reader(file)
                header = next(csvreader)  # Read the header
                numero_campi = len(header)
                colonna_campo = None
                for i in range(numero_campi):
                    if tipo == header[i]:
                        colonna_campo = i
                        break
                if colonna_campo is not None:
                    for row in csvreader:
                        if len(row) == numero_campi and valore in row[colonna_campo]:
                            for elemento in row[colonna_campo]:
                                if valore == elemtento:
                                    risposta = result.append(row)
                    return json.dumps(result)
                else:
                    print("Campo inserito non valido")
                    
                    return json.dumps('campo non valido')
    return json.dumps(result)

if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8080)
