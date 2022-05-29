-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : Dim 29 mai 2022 à 12:59
-- Version du serveur :  10.4.13-MariaDB
-- Version de PHP : 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `tipe`
--

-- --------------------------------------------------------

--
-- Structure de la table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `utilisateur1_id` int(11) NOT NULL,
  `utilisateur2_id` int(11) NOT NULL,
  `contamination` int(11) NOT NULL
)

-- --------------------------------------------------------

--
-- Structure de la table `donnee_de_sante_categories`
--

CREATE TABLE `donnee_de_sante_categories` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
)

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
)

--
-- Déchargement des données de la table `données_de_sante`
--

INSERT INTO `données_de_sante` (`id`, `nom`, `categorie`) VALUES
(1, 'antécédents médicaux', 1),
(2, 'maladie', 1),
(3, 'traitement', 1),
(4, 'handicap', 1),
(5, 'environnement sain', 2),
(6, 'IMC', 3),
(7, 'alcool', 3),
(8, 'tabac', 3),
(9, 'école', 3);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

CREATE TABLE `utilisateurs` (
  `id` int(11) NOT NULL,
  `etat` varchar(255) NOT NULL
)

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_données_de_sante`
--

CREATE TABLE `utilisateurs_données_de_sante` (
  `utilisateur_id` int(11) NOT NULL,
  `donnee_id` int(11) NOT NULL,
  `valeur` int(11) NOT NULL,
  `info_supplementaire` varchar(255) NOT NULL DEFAULT ' '
)

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

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
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
