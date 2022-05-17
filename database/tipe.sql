--
-- Base de données : `tipe`
--

-- --------------------------------------------------------

--
-- Structure de la table `donnee_de_sante_categories`
--

CREATE TABLE `donnee_de_sante_categories` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `donnee_de_sante_categories`
--

INSERT INTO `donnee_de_sante_categories` (`id`, `nom`) VALUES
(1, 'données de santé'),
(2, 'facteurs extrinsèques'),
(3, 'données de contextualisation relative à la santé');

-- --------------------------------------------------------

--
-- Structure de la table `données_de_sante`
--

CREATE TABLE `données_de_sante` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `categorie` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `données_de_sante`
--

INSERT INTO `données_de_sante` (`id`, `nom`, `categorie`) VALUES
(1, 'antécédents médicaux', 1),
(2, 'maladie', 1),
(3, 'traitement', 1),
(4, 'handicap', 1),
(5, 'qualité de l\'environnement', 2),
(6, 'IMC', 3),
(7, 'alcool', 3),
(8, 'tabac', 3),
(9, 'école', 3),
(10, 'catégorie socioprofessionnelle', 3);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

CREATE TABLE `utilisateurs` (
  `id` int(11) NOT NULL,
  `contamine` enum('Sain','Infecté','Rétabli') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_données_de_sante`
--

CREATE TABLE `utilisateurs_données_de_sante` (
  `utilisateur_id` int(11) NOT NULL,
  `donnee_id` int(11) NOT NULL,
  `valeur` int(11) NOT NULL,
  `info_supplementaire` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `donnee_de_sante_categories`
--
ALTER TABLE `donnee_de_sante_categories`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `données_de_sante`
--
ALTER TABLE `données_de_sante`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `donnee_de_sante_categories`
--
ALTER TABLE `donnee_de_sante_categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `données_de_sante`
--
ALTER TABLE `données_de_sante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
