import random

films = {
    "Jean-Luc Godard": [
        "À bout de souffle (Breathless)",
        "Le Petit Soldat",
        "Une femme est une femme",
        "Vivre sa vie",
        "Les Carabiniers",
        "Le Mépris (Contempt)",
        "Bande à part (Band of Outsiders)",
        "Une femme mariée",
        "Alphaville",
        "Pierrot le Fou",
        "Masculin féminin",
        "Made in USA",
        "2 ou 3 choses que je sais d'elle",
        "La Chinoise",
        "Week-end",
        "Le Gai Savoir",
        "Tout va bien",
        "Numéro deux",
        "Sauve qui peut (la vie)",
        "Prénom Carmen",
        "Je vous salue, Marie",
        "Détective",
        "Nouvelle Vague",
        "Allemagne année 90 neuf zéro",
        "Histoire(s) du cinéma",
        "Éloge de l'amour",
        "Notre Musique",
        "Film Socialisme",
        "Adieu au langage",
        "Le Livre d'image"
    ],
    
    "François Truffaut": [
        "Les Quatre Cents Coups (The 400 Blows)",
        "Tirez sur le pianiste",
        "Jules et Jim",
        "La Peau douce",
        "Fahrenheit 451",
        "La Mariée était en noir",
        "Baisers volés",
        "La Sirène du Mississippi",
        "L'Enfant sauvage",
        "Domicile conjugal",
        "Les Deux Anglaises et le Continent",
        "La Nuit américaine",
        "L'Histoire d'Adèle H.",
        "L'Homme qui aimait les femmes",
        "La Chambre verte",
        "L'Amour en fuite",
        "Le Dernier Métro",
        "La Femme d'à côté",
        "Vivement dimanche!"
    ],
    
    "Alain Resnais": [
        "Hiroshima mon amour",
        "L'Année dernière à Marienbad",
        "Muriel ou le Temps d'un retour",
        "La Guerre est finie",
        "Je t'aime, je t'aime",
        "Stavisky",
        "Providence",
        "Mon oncle d'Amérique",
        "La Vie est un roman",
        "L'Amour à mort",
        "Mélo",
        "I Want to Go Home",
        "Smoking/No Smoking",
        "On connaît la chanson",
        "Pas sur la bouche",
        "Coeurs",
        "Les Herbes folles",
        "Vous n'avez encore rien vu",
        "Aimer, boire et chanter"
    ],
    
    "Agnès Varda": [
        "La Pointe Courte",
        "Cléo de 5 à 7",
        "Le Bonheur",
        "Les Créatures",
        "Lions Love",
        "L'Une chante, l'autre pas",
        "Sans toit ni loi",
        "Jane B. par Agnès V.",
        "Jacquot de Nantes",
        "Les Glaneurs et la glaneuse",
        "Les Plages d'Agnès",
        "Visages, Villages"
    ],
    
    "Claude Chabrol": [
        "Le Beau Serge",
        "Les Cousins",
        "À double tour",
        "Les Bonnes Femmes",
        "Les Godelureaux",
        "L'Œil du Malin",
        "Landru",
        "Le Boucher",
        "La Rupture",
        "Les Noces rouges",
        "Violette Nozière",
        "Une affaire de femmes",
        "Madame Bovary",
        "La Cérémonie",
        "Merci pour le chocolat",
        "La Fleur du mal",
        "La Demoiselle d'honneur",
        "L'Ivresse du pouvoir"
    ],
    
    "Eric Rohmer": [
        "Le Signe du lion",
        "La Collectionneuse",
        "Ma nuit chez Maud",
        "Le Genou de Claire",
        "L'Amour l'après-midi",
        "La Marquise d'O...",
        "Perceval le Gallois",
        "La Femme de l'aviateur",
        "Pauline à la plage",
        "Les Nuits de la pleine lune",
        "Le Rayon vert",
        "L'Ami de mon amie",
        "Conte de printemps",
        "Conte d'hiver",
        "Conte d'été",
        "Conte d'automne",
        "L'Anglaise et le Duc",
        "Triple Agent",
        "Les Amours d'Astrée et de Céladon"
    ],
    
    "Jacques Rivette": [
        "Paris nous appartient",
        "La Religieuse",
        "L'Amour fou",
        "Out 1",
        "Céline et Julie vont en bateau",
        "Duelle",
        "Noroît",
        "Merry-Go-Round",
        "Le Pont du Nord",
        "L'Amour par terre",
        "Hurlevent",
        "La Bande des quatre",
        "La Belle Noiseuse",
        "Jeanne la Pucelle",
        "Haut bas fragile",
        "Secret défense",
        "Va savoir",
        "Histoire de Marie et Julien",
        "Ne touchez pas la hache",
        "36 vues du Pic Saint-Loup"
    ],
    
    "Louis Malle": [
        "Ascenseur pour l'échafaud",
        "Les Amants",
        "Zazie dans le métro",
        "Vie privée",
        "Le Feu follet",
        "Le Voleur",
        "Lacombe, Lucien",
        "Black Moon",
        "Au revoir les enfants",
        "Milou en mai"
    ],
    
    "Chris Marker": [
        "La Jetée",
        "Le Joli Mai",
        "Sans Soleil",
        "Level Five",
        "A Grin Without a Cat",
        "One Day in the Life of Andrei Arsenevich",
        "The Case of the Grinning Cat",
        "La Mystère Koumiko"
    ],
    
    "Jacques Demy": [
        "Lola",
        "La Baie des Anges",
        "Les Parapluies de Cherbourg",
        "Les Demoiselles de Rochefort",
        "Model Shop",
        "Peau d'âne",
        "Une chambre en ville",
        "Trois places pour le 26"
    ],
    "Steven Spielberg": [
        # Theatrical Features
        "Duel (1971)",  # Made for TV but later released theatrically
        "The Sugarland Express (1974)",
        "Jaws (1975)",
        "Close Encounters of the Third Kind (1977)",
        "1941 (1979)",
        "Raiders of the Lost Ark (1981)",
        "E.T. the Extra-Terrestrial (1982)",
        "Indiana Jones and the Temple of Doom (1984)",
        "The Color Purple (1985)",
        "Empire of the Sun (1987)",
        "Indiana Jones and the Last Crusade (1989)",
        "Always (1989)",
        "Hook (1991)",
        "Jurassic Park (1993)",
        "Schindler's List (1993)",
        "The Lost World: Jurassic Park (1997)",
        "Amistad (1997)",
        "Saving Private Ryan (1998)",
        "A.I. Artificial Intelligence (2001)",
        "Minority Report (2002)",
        "Catch Me If You Can (2002)",
        "The Terminal (2004)",
        "War of the Worlds (2005)",
        "Munich (2005)",
        "Indiana Jones and the Kingdom of the Crystal Skull (2008)",
        "The Adventures of Tintin (2011)",
        "War Horse (2011)",
        "Lincoln (2012)",
        "Bridge of Spies (2015)",
        "The BFG (2016)",
        "The Post (2017)",
        "Ready Player One (2018)",
        "West Side Story (2021)",
        "The Fabelmans (2022)"
    ],
    
    "Christopher Nolan": [
        # Feature Films
        "Following (1998)",
        "Memento (2000)",
        "Insomnia (2002)",
        "Batman Begins (2005)",
        "The Prestige (2006)",
        "The Dark Knight (2008)",
        "Inception (2010)",
        "The Dark Knight Rises (2012)",
        "Interstellar (2014)",
        "Dunkirk (2017)",
        "Tenet (2020)",
        "Oppenheimer (2023)",
    ],
    
    "Stanley Kubrick": [
        # Feature Films
        "Fear and Desire (1953)",
        "Killer's Kiss (1955)",
        "The Killing (1956)",
        "Paths of Glory (1957)",
        "Spartacus (1960)",
        "Lolita (1962)",
        "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)",
        "2001: A Space Odyssey (1968)",
        "A Clockwork Orange (1971)",
        "Barry Lyndon (1975)",
        "The Shining (1980)",
        "Full Metal Jacket (1987)",
        "Eyes Wide Shut (1999)",
    ],
}

def mix(director1: str, director2: str) -> list[(str, bool)]:
    result = []
    
    # Get films for the given directors
    films_director1 = films.get(director1, [])
    films_director2 = films.get(director2, [])
    
    # Select a few films from each director
    selected_films_director1 = films_director1[:20]  # Select first 2 films
    selected_films_director2 = films_director2[:20]  # Select first 2 films
    
    # Create the result list with labels
    for film in selected_films_director1:
        result.append((film, True))
    for film in selected_films_director2:
        result.append((film, False))
    
    return random.shuffle(result)