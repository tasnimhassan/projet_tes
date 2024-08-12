<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<?php
//Déclaration des variables pour stocker le nom du serveur, utilisateur, base
$servername = "localhost";
$username = "root";
$password = "";
$database = "vente";
// Création de la connexion au serveur et à la base des données
$conn = mysqli_connect($servername, $username, $password, $database);
// Vérification de la connexion
if (!$conn) {
      die("Échec de la connexion : " . mysqli_connect_error());
}
 echo "Connexion réussie";
//Récupération des données au formulaire
 $num =$_POST['identifiant'];
 $nom =$_POST['nom'];
 $email =$_POST['email'];
 $avis =$_POST['avis'];
//création de la requête sql
$sql = "INSERT INTO etudiant (numero_etudiant, nom_etudiant, mail, opinion) VALUES ('$num', '$nom', '$email', '$avis')";
//Vérification de l’exécution de la requête
if (mysqli_query($conn, $sql)) {
      echo "Nouveau enregistrement créé avec succès";
} else {
      echo "Erreur : " . $sql . "<br>" . mysqli_error($conn);
}
//Fermeture de la connexion 
mysqli_close($conn);
?>

</html>