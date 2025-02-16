class Ui:
    @staticmethod
    def home():
        return """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page avec Image, Texte et Lien</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        img {
            width: 300px;
            height: auto;
            border-radius: 10px;
        }
        a {
            display: inline-block;
            margin-top: 15px;
            text-decoration: none;
            color: white;
            background-color: blue;
            padding: 10px 15px;
            border-radius: 5px;
        }
        a:hover {
            background-color: darkblue;
        }
    </style>
</head>
<body>
    <h1>Bienvenue sur ma page</h1>
    <p>Teste page html cour ASR 2024-2025</p>
    <img src="C:\Users\Larbi\Desktop\compus france\MEDHO.png" alt="Image Exemple">
    <br>
    <a href="https://www.univ-usto.dz/" target="_blank">Visitez le site</a>
</body>
</html>"""