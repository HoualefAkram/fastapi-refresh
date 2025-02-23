class Ui:
    @staticmethod
    def home():
        return """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connexion</title>
    <style>
        body { 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh; 
            margin: 0; 
            font-family: Arial, sans-serif; 
        }
        .container { 
            text-align: center; 
            flex-direction: column;
            align-items: center;
        }
        .input-box { 
            margin-top: 10px; 
        }
        .dashboard { 
            display: none; 
            height: 100vh; 
            width: 100vw;
        }
        .sidebar { 
            width: 200px; 
            background: #333; 
            color: white; 
            padding: 20px; 
            position: fixed; 
            left: 0; 
            top: 0; 
            bottom: 0; 
            display: flex; 
            flex-direction: column; 
            justify-content: space-between; 
        }
        .content { 
            position: absolute; 
            right: 50px; 
            top: 50%; 
            transform: translateY(-50%); 
            font-size: 24px; 
            font-weight: bold; 
        }
        .logout-btn { 
            background: red; 
            color: white; 
            padding: 10px; 
            border: none; 
            cursor: pointer; 
            text-align: center; 
            margin-top: auto; 
        }
    </style>
</head>
<body>
    <div class="container" id="loginPage">
        <img src="static/logo.jpg" alt="Logo" width="100">
        <div class="input-box">
            <input type="text" id="username" placeholder="Nom d'utilisateur">
            <button onclick="login()">Entrer</button>
        </div>
    </div>

    <div class="dashboard" id="dashboard">
        <div class="sidebar">
            <div style="text-align: center;">
                <img src="static/profile.png" alt="Profil" width="50">
                <p>Nom : <span id="userNom"></span></p>
                <p>Prénom : <span id="userPrenom"></span></p>
                <p>Classe : <span id="userClasse"></span></p>
            </div>
            <button class="logout-btn" onclick="logout()">Déconnexion</button>
        </div>
        <div class="content">EN COURS</div>
    </div>

    <script>
        const users = {
            "00": { nom: "Houalef", prenom: "Akram", classe: "GROUPE 02" },
            "01": { nom: "Larbi Essaidi", prenom: "Mohammed Mehdi", classe: "GROUPE 02" },
            "10": { nom: "Hadjazi", prenom: "Issam", classe: "GROUPE 02" },
            "11": { nom: "Fezazi", prenom: "Omar", classe: "GROUPE 02" }
        };

        function login() {
            let username = document.getElementById("username").value;
            if (users[username]) {
                document.getElementById("loginPage").style.display = "none";
                document.getElementById("dashboard").style.display = "flex";
                document.getElementById("userNom").innerText = users[username].nom;
                document.getElementById("userPrenom").innerText = users[username].prenom;
                document.getElementById("userClasse").innerText = users[username].classe;
            }
        }

        function logout() {
            document.getElementById("dashboard").style.display = "none";
            document.getElementById("loginPage").style.display = "flex";
            document.getElementById("username").value = ""; // Clear the input field
        }
    </script>
</body>
</html>
"""
