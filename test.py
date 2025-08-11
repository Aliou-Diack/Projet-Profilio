import streamlit as st
from PIL import Image

# Désactiver le menu et le header par défaut
st.set_page_config(page_title="Mon Portfolio", layout="wide")

# Masquer la barre de Streamlit
hide_default_format = """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_default_format, unsafe_allow_html=True)

# Initialisation
if "section" not in st.session_state:
    st.session_state.section = "presentation"

# Récupération depuis l'URL
if "section" in st.query_params:
    st.session_state.section = st.query_params["section"]

# CSS du menu fixe
st.markdown("""
    <style>
        .topnav {
            background-color: #007ac1;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 100;
            overflow: hidden;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 40px;
        }
        .topnav .logo {
            color: white;
            font-size: 22px;
            font-weight: bold;
        }
        .topnav a {
            color: white;
            font-size: 18px;
            text-decoration: none;
            padding: 0 16px;
        }
        .topnav a:hover {
            border-bottom: 3px solid white;
        }
        .spacer {
            height: 70px;
        }
    </style>
""", unsafe_allow_html=True)

# Menu HTML
menu_html = """
<div class="topnav">
    <div class="logo">ALIOU DIACK</div>
    <div>
        <a href="?section=presentation" target="_self">Présentation</a>
        <a href="?section=projets" target="_self">Projets</a>
        <a href="?section=CV" target="_self">CV</a>
        <a href="?section=Contact" target="_self">Contact</a>
    </div>
</div>
"""
st.markdown(menu_html, unsafe_allow_html=True)

# Espacement
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Contenu dynamique
if st.session_state.section == "presentation":
    st.header("Présentation")
     # Image de fond
    imageprofile = Image.open("profil aliou diack.jpg")

    import base64
    from io import BytesIO

    # Charger et redimensionner l'image avec PIL (exemple hauteur 300 px)
    hauteur = 500
    rapport = hauteur / imageprofile.height
    largeur = int(imageprofile.width * rapport)
    imageprofile = imageprofile.resize((largeur, hauteur))

    # Convertir en base64
    buffered = BytesIO()
    imageprofile.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Code HTML avec centrage
    html = f'''
    <div style="text-align:center;">
        <img src="data:profil aliou diack/jpg;base64,{img_str}" />
    </div>
    '''

    # Afficher dans Streamlit
    st.markdown(html, unsafe_allow_html=True)

    # Titre principal
    st.title("🎓 Aliou Diack – Portfolio")

    st.markdown("""
    Bonjour je me nomme **Aliou Diack**,
    Originaire du Sénégal, j'ai été animé dès mon jeune âge par une passion pour l'informatique et les mathématiques.  
    Conscient du pouvoir de ces disciplines pour transformer les entreprises, j'ai très tôt décidé de devenir **Data Scientist** afin d'aider les sociétés locales à prospérer en prenant de meilleures décisions.

    Actuellement en **Master 2 Statistique et Informatique Décisionnelle de l'Université Alioune Diop de Bambey**, j’ai acquis un socle solide de compétences en **analyse de données**, **Visualisation des Données**, **modélisation statistique** et **administration de bases de données**.  
    Rigoureux et curieux, je maîtrise des outils essentiels comme **Python**, **R**, **SPSS**, **Excel**, **Power BI** et **Tableau**, et je suis capable de déployer des applications interactives avec des frameworks comme **Streamlit**.

    Je m’intéresse particulièrement aux **domaines d’application de la data science** tels que :  
    - 🏥 **La santé**, pour la prédiction des risques médicaux ou l’optimisation des soins  
    - 💰 **La finance**, pour l’analyse des fraudes ou la segmentation des clients  
    - 🛍️ **Le commerce**, pour l’analyse des ventes, les recommandations produits et la fidélisation  
    - 🌾 **L’agriculture**, pour l’anticipation des rendements ou la gestion intelligente des ressources  
    - 🎓 **L’éducation**, pour suivre les performances et prévenir le décrochage scolaire  
    - 🌍 Et plus largement, tout projet à fort impact social ou économique au Sénégal

    Mon objectif est de continuer à affiner mes compétences.  
    Je suis actuellement à la recherche de nouvelles opportunités, que ce soit sous forme de stage, d’emploi ou toute autre opportunité de collaboration professionnelle, afin d’enrichir mon expérience pratique.
    Je suis déterminé à mettre mes connaissances au service des entreprises et des institutions pour les aider à prendre des **décisions stratégiques fondées sur les données**.
    """)

    # Signature
    st.markdown("---")
    st.markdown("**Aliou Diack**  \nÉtudiant | Analyste de données en devenir | Passionné par l'impact social des technologies")

elif st.session_state.section == "projets":
    st.header("Projets")
    st.write("Dans cette page, vous pouvez consulter les différentes projets sur lesquels j'ai travaillé pour mettre en pratiques les connaissances acquisent au cours de mon cursus scolaire.")
    st.markdown("---")
    st.title("🛍️ Projet 1: Tableau de bord d’analyse des ventes d’une boutique en ligne")

    st.markdown("""
    Dans le cadre de cette étude, l’objectif principal était de développer un **tableau de bord interactif** permettant de visualiser et d’analyser l’évolution des ventes d’une boutique en ligne.

    Le travail a été structuré selon les étapes suivantes :
    """)

    st.subheader("1. Chargement et préparation des données")
    st.markdown("""
    Les différents fichiers Excel contenant les **données de ventes**, de **produits**, de **clients** et de **transactions** ont été importés dans **Power BI**.

    Des transformations ont été appliquées dans **Power Query** pour assurer la qualité des données :
    - Suppression des doublons  
    - Renommage cohérent des colonnes  
    - Traitement des valeurs manquantes  
    - Formatage des dates, etc.
    """)

    st.subheader("2. Création d’une table de dimension calendrier")
    st.markdown("""
    Une table de calendrier a été générée directement dans **Power Query** en utilisant le langage **M**.

    Cette table comprend :
    - L’ensemble des dates couvrant la période d’analyse
    - Des colonnes dérivées : année, mois, trimestre, jour de la semaine…

    Elle permet d’effectuer des **analyses temporelles** précises dans Power BI.
    """)

    st.subheader("3. Création de mesures et visualisations pertinentes")
    st.markdown("""
    Des mesures en **DAX** ont été développées pour suivre des indicateurs clés :
    - Chiffre d’affaires total  
    - Nombre de commandes  
    - Panier moyen  
    - Variation mensuelle, etc.

    Ces mesures sont représentées sous forme de **graphiques dynamiques** :
    - Barres, lignes, KPI  
    - Cartes de chaleur, matrices  

    Le tout est intégré dans un **tableau de bord interactif** avec des filtres pour explorer les données par **produit**, **période**, **région** ou **catégorie**.

    Ce tableau de bord :
    - Permet une **lecture rapide des tendances de vente**
    - Met en évidence les **performances des produits**
    - Facilite la **prise de décision stratégique** pour les équipes commerciales.
    """)
    image = Image.open("powerbi.png")
    st.image(image, caption="image_ecommerce")

    st.markdown("---")

    # Titre principal
    st.title("🏅 Projet : Analyse des performances des Jeux Olympiques (1896 – 2008)")
    st.markdown("**Outil utilisé : Tableau Desktop**")

    # Introduction
    st.markdown("""
    Ce projet a pour objectif de visualiser les performances olympiques de différents pays, sports et athlètes entre 1896 et 2008 à travers un **tableau de bord interactif réalisé sous Tableau Desktop**.  
    L’analyse repose sur les données historiques des médailles attribuées lors des Jeux Olympiques modernes.
    """)

    # Objectifs
    st.subheader("📌 Objectifs :")
    st.markdown("""
    - Identifier les pays les plus performants par nombre total de médailles.  
    - Suivre l’évolution des performances par année et par type de médaille (or, argent, bronze).  
    - Comparer les disciplines sportives en fonction du nombre de médailles obtenues.  
    - Mettre en avant les athlètes les plus médaillés.
    """)

    # Description des visualisations
    st.subheader("📊 Description des visualisations :")

    st.markdown("""
    **📍 Carte des médailles par pays**  
    Une carte géographique (carte de chaleur) affiche le **nombre total de médailles** gagnées par chaque pays.  
    Les pays les plus performants (comme les États-Unis, l'URSS ou la Chine) sont mis en évidence par une coloration plus foncée.

    **📍 Évolution des médailles par année et type**  
    Un graphique en aires empilées présente la répartition des médailles (**or, argent, bronze**) par édition des Jeux Olympiques.  
    Il permet de visualiser la croissance globale du nombre de médailles au fil du temps ainsi que les périodes historiques marquantes (guerres, boycotts, etc.).

    **📍 Répartition des médailles par sport**  
    Un graphique en bulles (**bubble chart**) illustre les sports les plus récompensés en termes de médailles.  
    Les disciplines comme l’athlétisme, la natation (aquatics), ou la gymnastique ressortent comme les plus dominantes.

    **📍 Top 10 des athlètes les plus médaillés**  
    Un graphique à barres horizontal classe les **10 athlètes ayant obtenu le plus de médailles** sur la période étudiée.  
    Il permet de comparer les performances individuelles remarquables (par exemple, Michael Phelps, Nurmi, et d'autres figures emblématiques).
    """)

    # Légende finale
    st.markdown("""
    📷 **Figure 12 :** Tableau de bord réalisé sous Tableau Desktop pour l’analyse des performances olympiques entre 1896 et 2008.  
    Ce tableau de bord permet une analyse **multi-niveaux (pays, années, sports, athlètes)** et met en lumière les tendances historiques et les pays/sports dominants dans l’histoire des Jeux Olympiques.
    """)

    image = Image.open("tableau de bord Tableau.png")
    st.image(image, caption="jeux olympiques")


    st.markdown("---")
    st.title("🛍️ Projet : Application d’analyse des ventes et segmentation client")
    st.markdown("**Outils : Python, Streamlit, K-means, RFM, FP-Growth**")

    st.markdown("""
    Cette application interactive développée avec **Streamlit** permet d’explorer des données de ventes, de visualiser les tendances d’achat et d’appliquer des techniques de **segmentation client**.

    Elle est structurée autour d’un **menu de navigation** qui donne accès à plusieurs modules analytiques.

    ---

    ### 📂 Fonctionnalités principales :

    #### 1. À propos de nous  
    - Présentation de l’objectif de l’application et des concepteurs du projet.

    #### 2. Statistiques descriptives  
    - Affichage des **10 premières lignes** du dataset.  
    - Détails sur les **dimensions** de la base (ex. : 541909 lignes, 9 colonnes).  
    - Calcul des **statistiques** : quantité, prix unitaire, montant.  
    - Détection et traitement des **valeurs manquantes**.

    #### 3. Visualisation des données  
    - 📊 **Top 5 des produits les plus vendus** (diagramme en barres)  
    - 🗓️ **Transactions par jour de la semaine**  
    - 📈 **Évolution du chiffre d’affaires journalier**  
    - 👥 **Top 5 des clients ayant le plus acheté**

    #### 4. Modélisations et prédictions

    ##### a. K-means (Segmentation non supervisée)  
    - Méthode du **coude** pour déterminer le nombre optimal de classes.  
    - Affichage des **centres de classes**, **distributions** et **appartenance client**.  
    - **Stabilité du modèle** : score d’environ 0.90.  
    - Suivi de l’évolution des **scores hebdomadaires** pour modéliser un contrat de maintenance.

    ##### b. RFM (Segmentation comportementale)  
    - Segmentation basée sur la **récence**, **fréquence** et **montant**.  
    - Classement des clients selon leur profil d’achat.

    ##### c. FP-Growth (Règles d'association)  
    - Génération de **règles d’association** à partir des achats.  
    - **Recommandations de produits** selon les habitudes d’achat des clients.

    ---

    ### ✅ Résultat :
    Cette application fournit une vision globale et interactive du comportement des clients, facilitant les décisions marketing et commerciales basées sur les données.
    """)

    image = Image.open("Application data mining.png")
    st.image(image, caption="image_ecommerce")

    # lien pour l'application

    st.link_button("Visiter le site", "https://projet-data-mining-ku8nh5lnx4rvhqnhgqmzpb.streamlit.app/", icon="🔗")
     # le fichier PDF à télécharger
    pdf_data = open("C:/Users/HP/Desktop/COURS M2SID/Data Mining approche Informatique/Examen/Projet Data Mining/donnees_ecommerce.xlsx", "rb").read()
    # Créer un bouton de téléchargement
    st.download_button(
        label="📥 Télécharger les données",
        data=pdf_data,
        file_name="donnees_ecommerce.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    


    st.markdown("---")
    st.title("🧠 Projet : Application de Prédiction des Risques de Décès après Traitement")
    st.markdown("**Outil : Python & Streamlit | Modèle : Decision Tree Classifier**")

    st.markdown("""
    Dans ce projet, j’ai développé et déployé une **application web interactive avec Streamlit** pour prédire les risques de décès après un traitement médical, en fonction des caractéristiques cliniques des patients.

    L’application permet aux utilisateurs non techniques de :
    - 📂 Charger et explorer les données brutes.  
    - 📈 Visualiser des **graphes de performance du modèle** (Matrice de confusion, Courbe ROC, etc.).  
    - 🧾 Remplir un **formulaire de prédiction** pour un nouveau patient.

    Le modèle utilisé est un **DecisionTreeClassifier** entraîné avec `scikit-learn`.  
    L'application affiche les **indicateurs de performance** du modèle :
    - **Accuracy**
    - **Précision**
    - **Recall**
    """)
 
    image = Image.open("app boistatiatique.png")
    st.image(image, caption="image_ecommerce")

elif st.session_state.section == "CV":
    st.header("CV")
    # Photo et Informations personnelles
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("profil aliou diack.jpg", width=200)  # Remplace par le chemin de ta photo
        
        st.markdown("\n\n\n\n\n\n")
        st.markdown("""
        ### **Information Personnelle**
        - **Localisation :** Tambacounda
        - **Téléphone :** 78 294 83 35
        - **Email :** [diackaliou4@gmail.com](mailto:diackaliou4@gmail.com)
        - **LinkedIn :** [Aliou Diack](https://www.linkedin.com/in/aliou-diack-977771241/)
        - **GitHub :** [Aliou Diack](https://github.com/Aliou-Diack)
        - **Sexe :** Homme
        - **Date de naissance :** 08/11/2000
        - **Lieu de Naissance :** Tambacounda
        """)

        st.markdown("\n\n\n\n\n\n")

        st.markdown("""
        ### **Langues**
        - Français : ⭐⭐⭐⭐
        - Anglais : ⭐⭐⭐
        - Wolof : ⭐⭐⭐⭐
        """)

        st.markdown("\n\n\n\n\n\n")

        st.markdown("""
        ### **Centre d'intérêt**
        - Sport
        - Musique
        - Lecture
        """)

        st.markdown("\n\n\n\n\n\n")

        st.markdown("""
        ### **Logiciels**
        EXCEL, WORLD, POWERBI, TABLEAU, RSTUDIO, MYSQL, SPSS, POWERAMC, 
                    PHPMYADMIN, WAMP, CISCO PACKET TRACER, TALEND OPEN STUDIO, PYTHON 
        """)

    with col2:
        st.markdown("""
        # **ALIOU DIACK**
        """)
        st.markdown("""
        ## **Profil**
        Actuellement étudiant en master 2 en Statistique et Informatique Décisionnelle. 
        J'ai de solides aptitudes techniques et un excellent esprit d'analyse. Je suis 
        rigoureux, dynamique, ponctuel et motivé, des qualités que j'utilise dans tout 
        ce que j'entreprends.
        """)

        st.markdown("---")
        st.markdown("## **Formation**")
        st.markdown("""
        - **Master 2 :** Statistique et Informatique Décisionnelle, Université Alioune Diop Bambey-Sénégal (Déc 2023-2024)
        - **Master 1 :** Statistique et Informatique Décisionnelle, Université Alioune Diop Bambey-Sénégal (Déc 2022-2023)
        - **Licence 3 :** Statistique et Informatique Décisionnelle, Université Alioune Diop Bambey-Sénégal (Déc 2021-2022)
        - **Licence 2 :** Statistique et Informatique Décisionnelle, Université Alioune Diop Bambey-Sénégal (Déc 2020-2021)
        - **Licence 1 :** Mathematique Physique Chimie et Informatique, Université Alioune Diop Bambey-Sénégal (Déc 2019-2020)
        - **Baccalauréat :** Série S2 (Déc 2018-2019)
        """)

        st.markdown("---")
        st.markdown("## **Compétences**")
        st.markdown("""
        ### Compétence Statistique
        - Exploration, Traitement et Analyse de données
        - Modélisation de données
        - Sondage
        - Technique d'enquête
        
        ### Compétence Informatique Décisionnelle
        - Système d'information
        - Visualisation des données
        - Réseaux informatiques
        - Gestion des bases de données
        - Programmation (Java, C, C++, R, SQL, SCALA, Python, HTML, PHP)
        - Machine Learning
        - Big Data
        - Biostatistique
        """)

        st.markdown("### Compétence Personnelle")
        st.markdown("""
        - Esprit Critique  
        - Curiosité et Apprentissage Continu  
        - Travail en Équipe  
        - Gestion de Projet
        - Communication Efficace
        - Adaptabilité et Flexibilitéd""")

        st.markdown("---")
        st.markdown("## **Expérience Professionnelle**")
        st.markdown("""
        - **Nov 2023 - Déc 2023 :** Stage à la Société de Développement et des Fibres Textiles - Système d'information et Réseau
        - **Oct 2023 - Déc 2023 :** Stage à l'Agence Régionale de Développement - Analyse de l'efficacité interne de l'éducation du secteur moyen
        - **Sep 2024 - Déc 2024 :** Stage au Programme d'Appui au Développement Agricole et à l'Entrepreneuriat Rural (PAADER II) - Passation des Marchés
        """)

    # Footer ou message personnalisé
    st.markdown("---")

    # le fichier PDF à télécharger
    pdf_data = open("CV_Aliou_Diack.pdf", "rb").read()
    # Créer un bouton de téléchargement
    st.download_button(
        label="📥 Télécharger le fichier PDF",
        data=pdf_data,
        file_name="CV_Aliou_Diack.pdf",
        mime="application/pdf"
    )

elif st.session_state.section == "Contact":
    st.header("Contact")
    st.markdown("""
    Vous souhaitez me contacter pour une **opportunité professionnelle**, un **projet collaboratif**, ou simplement pour échanger ?  
    N'hésitez pas à utiliser les informations ci-dessous ou à me laisser un message via mes réseaux.

    ---  

    📍 **Localisation :** Tambacounda, Sénégal  
    📧 **Email :** [diackaliou4@gmail.com](mailto:diackaliou4@gmail.com)  
    📞 **Téléphone :** +221 78 294 83 35  

    🔗 **LinkedIn :** [Aliou Diack](https://www.linkedin.com/in/aliou-diack-977771241/)  
    💻 **GitHub :** [Aliou-Diack](https://github.com/Aliou-Diack)

    ---  

    Si vous le souhaitez, vous pouvez aussi télécharger mon CV ci-dessous :
    """)

    # Bouton de téléchargement du CV
    with open("CV_Aliou_Diack.pdf", "rb") as pdf_file:
        pdf_data = pdf_file.read()

    st.download_button(
        label="📄 Télécharger mon CV",
        data=pdf_data,
        file_name="CV_Aliou_Diack.pdf",
        mime="application/pdf"
    )

    st.markdown("---")
    st.markdown("Merci pour votre visite ! 👋")
