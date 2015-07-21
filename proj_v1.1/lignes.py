#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''pour se servir de ce fichier :

import lignes
for row in lignes.cheylard_valence[X][Y]:
    print(row) ou autre traitement

X = premier sous tableau (scol, vac_ete ou autres_vac)
Y = second sous tableau (scol, le cheylard/collège, le cheylard/grpscol...)
'''


Le_Cheylard_Valence = [
[['scol', 'VIDE', '1L', '2LMmJV', '3S', '4LMmJV', '5LMmJVS', '6m', '7D', '8LMmJ', '9V'], ['LE CHEYLARD', 'Collège St Louis', '0', '0', '0', '0', '0', '17:05'], ['LE CHEYLARD', 'Av.Saunier/GrpeScol.', '07:50', '08:30', '11:45', '16:20', '17:05', 'ND'], ['LE CHEYLARD', 'Av.de la libération', '08:00', '08:39', '11:55', '16:25', '17:10', '17:10'], ['LE CHEYLARD', 'Gendarmerie', '08:01', '08:40', '11:56', '16:26', '17:11', '17:11'], ['LE CHEYLARD', 'La Palisse', '08:02', '08:41', '11:57', '16:27', '17:12', '17:12'], ["ST MICHEL D'AURANCE", 'Pailhès', '08:07', '08:48', '12:02', '16:32', '17:17', '17:17'], ['ST BARTHELEMY LE MEIL', 'Sarny', '08:09', '08:50', '12:04', '16:34', '17:19', '17:19'], ['BEAUVENE', 'Pont de Chervil', '08:18', '08:59', '12:13', '16:43', '17:28', '17:28'], ['BEAUVENE', 'Le Bateau', '08:20', '09:01', '12:15', '16:45', '17:30', '17:30'], ['ST MAURICE EN C', 'Pt du Moulinas', '08:23', '09:04', '12:18', '16:48', '17:33', '17:33'], ['ST MAURICE EN C', 'La Roche St M.', '08:28', '09:06', '12:23', '16:53', '17:38', '17:38'], ['ST SAUVEUR DE MGUT', 'Centre', '08:32', '09:12', '12:27', '16:57', '17:42', '17:42'], ['ST SAUVEUR DE MGUT', 'Le Moulinon', '08:33', '09:14', '12:28', '16:58', '17:43', '17:43'], ['LES OLLIERES', 'Escoulenc', '08:35', '09:16', '12:30', '17:00', '17:45', '17:45'], ['LES OLLIERES', 'Veye', '08:36', '09:17', '12:31', '17:01', '17:46', '17:46'], ['LES OLLIERES', 'Centre', '08:37', '09:18', '12:32', '17:02', '17:47', '17:47'], ['LES OLLIERES', 'Mairie/CrtD2', '08:39', '09:20', '12:34', '17:04', '17:49', '17:49'], ['LES OLLIERES', 'Les Plots', '08:40', '09:22', '12:36', '17:06', '17:50', '17:50'], ['LES OLLIERES', 'La Pimpie', '08:40', '09:22', '12:36', '17:06', '17:50', '17:50'], ['DUNIERE/EYRIEUX', 'Centre', '08:44', '09:24', '12:40', '17:10', '17:54', '17:54'], ['DUNIERE/EYRIEUX', 'RD231/RD120', '08:46', '09:26', '12:43', '17:13', '17:56', '17:56'], ['ST FORTUNAT', 'Centre', '08:48', '09:28', '12:45', '17:15', '17:58', '17:58'], ['ST FORTUNAT', 'Mondon', '08:50', '09:30', '12:47', '17:17', '18:00', '18:00'], ['ST FORTUNAT', 'Prahy', '08:52', '09:31', '12:49', '17:19', '18:02', '18:02'], ['ST LAURENTDUPAPE', 'Hauteville', '08:55', '09:33', '12:52', '17:22', '18:05', '18:05'], ['ST LAURENTDUPAPE', 'Beaumazet', '08:56', '09:34', '12:53', '17:23', '18:06', '18:06'], ['ST LAURENTDUPAPE', 'Hautussac', '08:57', '09:35', '12:54', '17:24', '18:07', '18:07'], ['ST LAURENTDUPAPE', 'Centre', '08:58', '09:36', '12:55', '17:25', '18:08', '18:08'], ['ST LAURENTDUPAPE', 'Thoac', '08:59', '09:37', '12:57', '17:27', '18:11', '18:11'], ['BEAUCHASTEL', 'Centre', '09:02', '09:40', '13:00', '17:30', '18:15', '18:15'], ['BEAUCHASTEL', 'LesRamières', '09:03', '09:41', '13:01', '17:31', '18:16', '18:16'], ['ST GEORGES LES B', 'Chateaurouge', '09:04', '09:42', '13:02', '17:32', '18:17', '18:17'], ['ST GEORGES LES B', 'Giratoire RD 11', '09:06', '09:46', '13:04', '17:34', '18:19', '18:19'], ['CHARMES', 'Centre', '09:07', '09:48', '13:05', '17:35', '18:20', '18:20'], ['CHARMES', 'Levertel/Cités', '09:08', '09:50', '13:06', '17:36', '18:21', '18:21'], ['CHARMES', 'Les 4 chemins', '09:09', '09:51', '13:07', '17:37', '18:22', '18:22'], ['SOYONS', 'Le Vivier', '09:10', '09:52', '13:08', '17:38', '18:23', '18:23'], ['SOYONS', 'Ventre', '09:11', '09:53', '13:09', '17:39', '18:24', '18:24'], ['SOYONS', 'Les cités', '09:12', '09:54', '13:10', '17:40', '18:25', '18:25'], ['SOYONS', 'Les Freydières', '09:13', '09:56', '13:11', '17:41', '18:26', '18:26'], ['GUILHERAND GRANGES', 'Carnot', '09:15', '10:00', '13:15', '17:45', '18:30', '18:30'], ['VALENCE', 'Champ de Mars', '09:22', '10:02', '13:22', '17:52', '18:37', '18:37'], ['VALENCE', 'Gare Routière', '09:25', '10:05', '13:25', '17:55', '18:40', '18:40']],
[['autres_vac', 'VIDE', '2LMmJV', '3S', '4LMmJV', '5LMmJVS', '7D', '8LMmJ', '9ND'], ['LE CHEYLARD', 'Collège St Louis', '0', '0', '0', '0', '0', '17:05'], ['LE CHEYLARD', 'Av.Saunier/GrpeScol.', '07:50', '08:30', '11:45', '16:20', '17:05', 'ND'], ['LE CHEYLARD', 'Av.de la libération', '08:00', '08:39', '11:55', '16:25', '17:10', '17:10'], ['LE CHEYLARD', 'Gendarmerie', '08:01', '08:40', '11:56', '16:26', '17:11', '17:11'], ['LE CHEYLARD', 'La Palisse', '08:02', '08:41', '11:57', '16:27', '17:12', '17:12'], ["ST MICHEL D'AURANCE", 'Pailhès', '08:07', '08:48', '12:02', '16:32', '17:17', '17:17'], ['ST BARTHELEMY LE MEIL', 'Sarny', '08:09', '08:50', '12:04', '16:34', '17:19', '17:19'], ['BEAUVENE', 'Pont de Chervil', '08:18', '08:59', '12:13', '16:43', '17:28', '17:28'], ['BEAUVENE', 'Le Bateau', '08:20', '09:01', '12:15', '16:45', '17:30', '17:30'], ['ST MAURICE EN C', 'Pt du Moulinas', '08:23', '09:04', '12:18', '16:48', '17:33', '17:33'], ['ST MAURICE EN C', 'La Roche St M.', '08:28', '09:06', '12:23', '16:53', '17:38', '17:38'], ['ST SAUVEUR DE MGUT', 'Centre', '08:32', '09:12', '12:27', '16:57', '17:42', '17:42'], ['ST SAUVEUR DE MGUT', 'Le Moulinon', '08:33', '09:14', '12:28', '16:58', '17:43', '17:43'], ['LES OLLIERES', 'Escoulenc', '08:35', '09:16', '12:30', '17:00', '17:45', '17:45'], ['LES OLLIERES', 'Veye', '08:36', '09:17', '12:31', '17:01', '17:46', '17:46'], ['LES OLLIERES', 'Centre', '08:37', '09:18', '12:32', '17:02', '17:47', '17:47'], ['LES OLLIERES', 'Mairie/CrtD2', '08:39', '09:20', '12:34', '17:04', '17:49', '17:49'], ['LES OLLIERES', 'Les Plots', '08:40', '09:22', '12:36', '17:06', '17:50', '17:50'], ['LES OLLIERES', 'La Pimpie', '08:40', '09:22', '12:36', '17:06', '17:50', '17:50'], ['DUNIERE/EYRIEUX', 'Centre', '08:44', '09:24', '12:40', '17:10', '17:54', '17:54'], ['DUNIERE/EYRIEUX', 'RD231/RD120', '08:46', '09:26', '12:43', '17:13', '17:56', '17:56'], ['ST FORTUNAT', 'Centre', '08:48', '09:28', '12:45', '17:15', '17:58', '17:58'], ['ST FORTUNAT', 'Mondon', '08:50', '09:30', '12:47', '17:17', '18:00', '18:00'], ['ST FORTUNAT', 'Prahy', '08:52', '09:31', '12:49', '17:19', '18:02', '18:02'], ['ST LAURENTDUPAPE', 'Hauteville', '08:55', '09:33', '12:52', '17:22', '18:05', '18:05'], ['ST LAURENTDUPAPE', 'Beaumazet', '08:56', '09:34', '12:53', '17:23', '18:06', '18:06'], ['ST LAURENTDUPAPE', 'Hautussac', '08:57', '09:35', '12:54', '17:24', '18:07', '18:07'], ['ST LAURENTDUPAPE', 'Centre', '08:58', '09:36', '12:55', '17:25', '18:08', '18:08'], ['ST LAURENTDUPAPE', 'Thoac', '08:59', '09:37', '12:57', '17:27', '18:11', '18:11'], ['BEAUCHASTEL', 'Centre', '09:02', '09:40', '13:00', '17:30', '18:15', '18:15'], ['BEAUCHASTEL', 'LesRamières', '09:03', '09:41', '13:01', '17:31', '18:16', '18:16'], ['ST GEORGES LES B', 'Chateaurouge', '09:04', '09:42', '13:02', '17:32', '18:17', '18:17'], ['ST GEORGES LES B', 'Giratoire RD 11', '09:06', '09:46', '13:04', '17:34', '18:19', '18:19'], ['CHARMES', 'Centre', '09:07', '09:48', '13:05', '17:35', '18:20', '18:20'], ['CHARMES', 'Levertel/Cités', '09:08', '09:50', '13:06', '17:36', '18:21', '18:21'], ['CHARMES', 'Les 4 chemins', '09:09', '09:51', '13:07', '17:37', '18:22', '18:22'], ['SOYONS', 'Le Vivier', '09:10', '09:52', '13:08', '17:38', '18:23', '18:23'], ['SOYONS', 'Ventre', '09:11', '09:53', '13:09', '17:39', '18:24', '18:24'], ['SOYONS', 'Les cités', '09:12', '09:54', '13:10', '17:40', '18:25', '18:25'], ['SOYONS', 'Les Freydières', '09:13', '09:56', '13:11', '17:41', '18:26', '18:26'], ['GUILHERAND GRANGES', 'Carnot', '09:15', '10:00', '13:15', '17:45', '18:30', '18:30'], ['VALENCE', 'Champ de Mars', '09:22', '10:02', '13:22', '17:52', '18:37', '18:37'], ['VALENCE', 'Gare Routière', '09:25', '10:05', '13:25', '17:55', '18:40', '18:40']],
[['vac_ete', 'VIDE', '2LMmJV', '3S', '4LMmJV', '5LMmJVS', '6ND', '7D', '8LMmJ', '9ND'], ['LE CHEYLARD', 'Collège St Louis', '0', '0', '0', '0', '0', '17:05'], ['LE CHEYLARD', 'Av.Saunier/GrpeScol.', '07:50', '08:30', '11:45', '16:20', '17:05', 'ND'], ['LE CHEYLARD', 'Av.de la libération', '08:00', '08:39', '11:55', '16:25', '17:10', '17:10'], ['LE CHEYLARD', 'Gendarmerie', '08:01', '08:40', '11:56', '16:26', '17:11', '17:11'], ['LE CHEYLARD', 'La Palisse', '08:02', '08:41', '11:57', '16:27', '17:12', '17:12'], ["ST MICHEL D'AURANCE", 'Pailhès', '08:07', '08:48', '12:02', '16:32', '17:17', '17:17'], ['ST BARTHELEMY LE MEIL', 'Sarny', '08:09', '08:50', '12:04', '16:34', '17:19', '17:19'], ['BEAUVENE', 'Pont de Chervil', '08:18', '08:59', '12:13', '16:43', '17:28', '17:28'], ['BEAUVENE', 'Le Bateau', '08:20', '09:01', '12:15', '16:45', '17:30', '17:30'], ['ST MAURICE EN C', 'Pt du Moulinas', '08:23', '09:04', '12:18', '16:48', '17:33', '17:33'], ['ST MAURICE EN C', 'La Roche St M.', '08:28', '09:06', '12:23', '16:53', '17:38', '17:38'], ['ST SAUVEUR DE MGUT', 'Centre', '08:32', '09:12', '12:27', '16:57', '17:42', '17:42'], ['ST SAUVEUR DE MGUT', 'Le Moulinon', '08:33', '09:14', '12:28', '16:58', '17:43', '17:43'], ['LES OLLIERES', 'Escoulenc', '08:35', '09:16', '12:30', '17:00', '17:45', '17:45'], ['LES OLLIERES', 'Veye', '08:36', '09:17', '12:31', '17:01', '17:46', '17:46'], ['LES OLLIERES', 'Centre', '08:37', '09:18', '12:32', '17:02', '17:47', '17:47'], ['LES OLLIERES', 'Mairie/CrtD2', '08:39', '09:20', '12:34', '17:04', '17:49', '17:49'], ['LES OLLIERES', 'Les Plots', '08:40', '09:22', '12:36', '17:06', '17:50', '17:50'], ['LES OLLIERES', 'La Pimpie', '08:40', '09:22', '12:36', '17:06', '17:50', '17:50'], ['DUNIERE/EYRIEUX', 'Centre', '08:44', '09:24', '12:40', '17:10', '17:54', '17:54'], ['DUNIERE/EYRIEUX', 'RD231/RD120', '08:46', '09:26', '12:43', '17:13', '17:56', '17:56'], ['ST FORTUNAT', 'Centre', '08:48', '09:28', '12:45', '17:15', '17:58', '17:58'], ['ST FORTUNAT', 'Mondon', '08:50', '09:30', '12:47', '17:17', '18:00', '18:00'], ['ST FORTUNAT', 'Prahy', '08:52', '09:31', '12:49', '17:19', '18:02', '18:02'], ['ST LAURENTDUPAPE', 'Hauteville', '08:55', '09:33', '12:52', '17:22', '18:05', '18:05'], ['ST LAURENTDUPAPE', 'Beaumazet', '08:56', '09:34', '12:53', '17:23', '18:06', '18:06'], ['ST LAURENTDUPAPE', 'Hautussac', '08:57', '09:35', '12:54', '17:24', '18:07', '18:07'], ['ST LAURENTDUPAPE', 'Centre', '08:58', '09:36', '12:55', '17:25', '18:08', '18:08'], ['ST LAURENTDUPAPE', 'Thoac', '08:59', '09:37', '12:57', '17:27', '18:11', '18:11'], ['BEAUCHASTEL', 'Centre', '09:02', '09:40', '13:00', '17:30', '18:15', '18:15'], ['BEAUCHASTEL', 'LesRamières', '09:03', '09:41', '13:01', '17:31', '18:16', '18:16'], ['ST GEORGES LES B', 'Chateaurouge', '09:04', '09:42', '13:02', '17:32', '18:17', '18:17'], ['ST GEORGES LES B', 'Giratoire RD 11', '09:06', '09:46', '13:04', '17:34', '18:19', '18:19'], ['CHARMES', 'Centre', '09:07', '09:48', '13:05', '17:35', '18:20', '18:20'], ['CHARMES', 'Levertel/Cités', '09:08', '09:50', '13:06', '17:36', '18:21', '18:21'], ['CHARMES', 'Les 4 chemins', '09:09', '09:51', '13:07', '17:37', '18:22', '18:22'], ['SOYONS', 'Le Vivier', '09:10', '09:52', '13:08', '17:38', '18:23', '18:23'], ['SOYONS', 'Ventre', '09:11', '09:53', '13:09', '17:39', '18:24', '18:24'], ['SOYONS', 'Les cités', '09:12', '09:54', '13:10', '17:40', '18:25', '18:25'], ['SOYONS', 'Les Freydières', '09:13', '09:56', '13:11', '17:41', '18:26', '18:26'], ['GUILHERAND GRANGES', 'Carnot', '09:15', '10:00', '13:15', '17:45', '18:30', '18:30'], ['VALENCE', 'Champ de Mars', '09:22', '10:02', '13:22', '17:52', '18:37', '18:37'], ['VALENCE', 'Gare Routière', '09:25', '10:05', '13:25', '17:55', '18:40', '18:40']]]

Valence_le_cheylard = [
[['scol', 'VIDE', '1L', '2MMeJV', '3LMMeJV', '4S', '5LMMeJV', '6LMMeJV', '7S', '8D', '9LMMeJ', '10V'], ['VALENCE', 'Gare Routière', '', '09:45', '09:45', '15:00', '16:45', '17:38', '18:15', '19:05', '19:30'], ['GUILHERANDGRANGES', 'Carnot', '', '09:52', '09:52', '15:07', '16:52', '17:45', '18:22', '19:12', '19:37'], ['SOYONS', 'Les Freydières', '', '09:57', '09:57', '15:12', '16:57', '15:50', '18:27', '19:17', '19:42'], ['SOYONS', 'Les Cités', '', '09:59', '09:59', '15:14', '16:59', '17:53', '18:29', '19:19', '19:44'], ['SOYONS', 'Centre', '', '10:00', '10:00', '15:15', '17:01', '17:54', '18:30', '19:20', '19:45'], ['SOYONS', 'Le Vivier', '', '10:01', '10:01', '15:16', '17:02', '17:55', '18:31', '19:21', '19:46'], ['CHARMES', 'Les 4 Chemins', '', '10:02', '10:02', '15:17', '17:03', '17:56', '18:32', '19:22', '19:47'], ['CHARMES', 'Le Vertel / Cités', '', '10:03', '10:03', '15:18', '17:05', '17:57', '18:33', '19:23', '19:48'], ['CHARMES', 'Centre', '', '10:04', '10:04', '15:19', '17:06', '17:58', '18:34', '19:24', '19:49'], ['ST GEORGESLES B', ' Giratoire RD 11', '', '10:05', '10:05', '15:20', '17:07', '17:59', '18:35', '19:25', '19:50'], ['ST GEORGES LES B', 'Chateaurouge', '', '10:07', '10:07', '15:22', '17:09', '18:01', '18:37', '19:27', '19:52'], ['BEAUCHASTEL', 'Les Ramières', '', '10:08', '10:08', '15:23', '17:10', '18:02', '18:38', '19:28', '19:53'], ['BEAUCHASTEL', 'Centre', '', '10:09', '10:09', '15:24', '17:11', '18:03', '18:39', '19:29', '19:54'], ['LA VOULTE', 'Cités', '', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND'], ['LA VOULTE', 'Nord', '', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND'], ['ST LAURENT DU PAPE', 'Thoac', '', '10:12', '10:12', '15:27', '17:14', '18:06', '18:42', '19:32', '19:57'], ['ST LAURENT DU PAPE', 'Centre', '', '10:13', '10:13', '15:28', '17:15', '18:07', '18:43', '19:33', '19:58'], ['ST LAURENT DU PAPE', 'Hautussac', '', '10:15', '10:15', '15:30', '17:17', '18:09', '18:45', '19:35', '20:00'], ['ST LAURENT DU PAPE', 'Beaumazet', '', '10:16', '10:16', '15:31', '17:18', '18:10', '18:46', '19:36', '20:01'], ['ST LAURENT DU PAPE', 'Hauteville', '', '10:17', '10:17', '15:32', '17:19', '18:11', '18:47', '19:37', '20:02'], ['ST FORTUNAT', 'Prahy', '06:58', '10:20', '10:20', '15:35', '17:22', '18:14', '18:50', '19:40', '20:05'], ['ST FORTUNAT', 'Mondon', '07:00', '10:22', '10:22', '15:37', '17:24', '18:16', '18:52', '19:42', '20:07'], ['ST FORTUNAT', 'Centre', '07:02', '10:24', '10:24', '15:39', '17:26', '18:18', '18:54', '19:44', '20:09'], ['DUNIERE / EYRIEUX', 'RD', 'RD', '120', '07:04', '07:04', '10:26', '10:26', '15:41', '17:28', '18:20', '18:56', '19:46', '20:11'], ['DUNIERE / EYRIEUX', 'Centre', '07:05', '10:27', '10:27', '15:42', '17:29', '18:21', '18:57', '19:47', '20:12'], ['LES OLLIERES', 'La Pimpie', '07:08', '10:30', '10:30', '15:45', '17:32', '18:24', '19:00', '19:50', '20:15'], ['LES OLLIERES', 'Les Plots', '07:09', '10:31', '10:31', '15:46', '17:33', '18:25', '19:01', '19:51', '20:16'], ['LES OLLIERES', 'Mairie', 'D2', '07:10', '07:10', '10:32', '10:32', '15:47', '17:34', '18:26', '19:02', '19:52', '20:17'], ['LES OLLIERES', 'Centre', '07:11', '10:33', '10:33', '15:48', '17:35', '18:27', '19:03', '19:53', '20:18'], ['LES OLLIERES', 'Veye', '07:12', '10:34', '10:34', '15:49', '17:36', '18:28', '19:04', '19:54', '20:19'], ['LES OLLIERES', 'Escoulenc', '07:13', '10:35', '10:35', '15:50', '17:37', '18:29', '19:05', '19:55', '20:20'], ['ST SAUVEUR DE MGUT', 'Le Moulinon', '07:16', '10:39', '10:39', '15:54', '17:40', '18:33', '19:09', '19:59', '20:24'], ['ST SAUVEUR DE MGUT', 'Centre', '07:18', '10:40', '10:40', '15:55', '17:41', '18:34', '19:10', '20:00', '20:25'], ['ST MAURICE EN C', 'La Roche St M.', '07:22', '10:44', '10:44', '15:59', '17:44', '18:38', '19:14', '20:04', '20:29'], ['ST MAURICE EN C', 'Pt du Moulinas', '07:27', '10:46', '10:46', '16:01', '17:46', '18:40', '19:16', '20:06', '20:31'], ['BEAUVENE', 'Le Bateau', '07:30', '10:52', '10:52', '16:07', '17:52', '18:46', '19:22', '20:12', '20:37'], ['BEAUVENE', 'Pont de Chervil', '07:32', '10:54', '10:54', '16:09', '17:54', '18:48', '19:24', '20:14', '20:39'], ['ST BARTHELEMY LE MEIL', 'Sarny', '07:41', '11:02', '11:02', '16:18', '18:03', '18:56', '19:32', '20:23', '20:48'], ["ST MICHEL D'AURANCE", 'Pailhès', '07:47', '11:05', '11:05', '16:20', '18:05', '18:58', '19:35', '20:25', '20:50'], ['LE CHEYLARD', 'La Palisse', '07:54', '11:09', '11:09', '16:25', '18:07', '19:03', '19:39', '20:30', '20:55'], ['LE CHEYLARD', 'Gendarmerie', '07:55', '11:10', '11:10', '16:26', '18:08', '19:04', '19:40', '20:31', '20:56'], ['LE CHEYLARD', 'Av. de la Libération', '11:11', '11:11', '16:27', '(1)', '18:09', '19:05', '19:41', '20:32', '20:57'], ['LE CHEYLARD', 'Av. Saunier / Grpe scol.', '07:58', '11:12', '11:12', '16:29', '18:10', '19:07', '19:42', '20:34', '20:59']],
[['autres_vac', 'VIDE', 'ND', '3LMMeJV', '4S', '5LMMeJV', '6LMMeJV', '7S', '8D', '9LMMeJ', '10V'], ['VALENCE', 'Gare Routière', '', '09:45', '09:45', '15:00', '16:45', '17:38', '18:15', '19:05', '19:30'], ['GUILHERANDGRANGES', 'Carnot', '', '09:52', '09:52', '15:07', '16:52', '17:45', '18:22', '19:12', '19:37'], ['SOYONS', 'Les Freydières', '', '09:57', '09:57', '15:12', '16:57', '15:50', '18:27', '19:17', '19:42'], ['SOYONS', 'Les Cités', '', '09:59', '09:59', '15:14', '16:59', '17:53', '18:29', '19:19', '19:44'], ['SOYONS', 'Centre', '', '10:00', '10:00', '15:15', '17:01', '17:54', '18:30', '19:20', '19:45'], ['SOYONS', 'Le Vivier', '', '10:01', '10:01', '15:16', '17:02', '17:55', '18:31', '19:21', '19:46'], ['CHARMES', 'Les 4 Chemins', '', '10:02', '10:02', '15:17', '17:03', '17:56', '18:32', '19:22', '19:47'], ['CHARMES', 'Le Vertel / Cités', '', '10:03', '10:03', '15:18', '17:05', '17:57', '18:33', '19:23', '19:48'], ['CHARMES', 'Centre', '', '10:04', '10:04', '15:19', '17:06', '17:58', '18:34', '19:24', '19:49'], ['ST GEORGESLES B', ' Giratoire RD 11', '', '10:05', '10:05', '15:20', '17:07', '17:59', '18:35', '19:25', '19:50'], ['ST GEORGES LES B', 'Chateaurouge', '', '10:07', '10:07', '15:22', '17:09', '18:01', '18:37', '19:27', '19:52'], ['BEAUCHASTEL', 'Les Ramières', '', '10:08', '10:08', '15:23', '17:10', '18:02', '18:38', '19:28', '19:53'], ['BEAUCHASTEL', 'Centre', '', '10:09', '10:09', '15:24', '17:11', '18:03', '18:39', '19:29', '19:54'], ['LA VOULTE', 'Cités', '', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND'], ['LA VOULTE', 'Nord', '', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND'], ['ST LAURENT DU PAPE', 'Thoac', '', '10:12', '10:12', '15:27', '17:14', '18:06', '18:42', '19:32', '19:57'], ['ST LAURENT DU PAPE', 'Centre', '', '10:13', '10:13', '15:28', '17:15', '18:07', '18:43', '19:33', '19:58'], ['ST LAURENT DU PAPE', 'Hautussac', '', '10:15', '10:15', '15:30', '17:17', '18:09', '18:45', '19:35', '20:00'], ['ST LAURENT DU PAPE', 'Beaumazet', '', '10:16', '10:16', '15:31', '17:18', '18:10', '18:46', '19:36', '20:01'], ['ST LAURENT DU PAPE', 'Hauteville', '', '10:17', '10:17', '15:32', '17:19', '18:11', '18:47', '19:37', '20:02'], ['ST FORTUNAT', 'Prahy', '06:58', '10:20', '10:20', '15:35', '17:22', '18:14', '18:50', '19:40', '20:05'], ['ST FORTUNAT', 'Mondon', '07:00', '10:22', '10:22', '15:37', '17:24', '18:16', '18:52', '19:42', '20:07'], ['ST FORTUNAT', 'Centre', '07:02', '10:24', '10:24', '15:39', '17:26', '18:18', '18:54', '19:44', '20:09'], ['DUNIERE / EYRIEUX', 'RD', 'RD', '120', '07:04', '07:04', '10:26', '10:26', '15:41', '17:28', '18:20', '18:56', '19:46', '20:11'], ['DUNIERE / EYRIEUX', 'Centre', '07:05', '10:27', '10:27', '15:42', '17:29', '18:21', '18:57', '19:47', '20:12'], ['LES OLLIERES', 'La Pimpie', '07:08', '10:30', '10:30', '15:45', '17:32', '18:24', '19:00', '19:50', '20:15'], ['LES OLLIERES', 'Les Plots', '07:09', '10:31', '10:31', '15:46', '17:33', '18:25', '19:01', '19:51', '20:16'], ['LES OLLIERES', 'Mairie', 'D2', '07:10', '07:10', '10:32', '10:32', '15:47', '17:34', '18:26', '19:02', '19:52', '20:17'], ['LES OLLIERES', 'Centre', '07:11', '10:33', '10:33', '15:48', '17:35', '18:27', '19:03', '19:53', '20:18'], ['LES OLLIERES', 'Veye', '07:12', '10:34', '10:34', '15:49', '17:36', '18:28', '19:04', '19:54', '20:19'], ['LES OLLIERES', 'Escoulenc', '07:13', '10:35', '10:35', '15:50', '17:37', '18:29', '19:05', '19:55', '20:20'], ['ST SAUVEUR DE MGUT', 'Le Moulinon', '07:16', '10:39', '10:39', '15:54', '17:40', '18:33', '19:09', '19:59', '20:24'], ['ST SAUVEUR DE MGUT', 'Centre', '07:18', '10:40', '10:40', '15:55', '17:41', '18:34', '19:10', '20:00', '20:25'], ['ST MAURICE EN C', 'La Roche St M.', '07:22', '10:44', '10:44', '15:59', '17:44', '18:38', '19:14', '20:04', '20:29'], ['ST MAURICE EN C', 'Pt du Moulinas', '07:27', '10:46', '10:46', '16:01', '17:46', '18:40', '19:16', '20:06', '20:31'], ['BEAUVENE', 'Le Bateau', '07:30', '10:52', '10:52', '16:07', '17:52', '18:46', '19:22', '20:12', '20:37'], ['BEAUVENE', 'Pont de Chervil', '07:32', '10:54', '10:54', '16:09', '17:54', '18:48', '19:24', '20:14', '20:39'], ['ST BARTHELEMY LE MEIL', 'Sarny', '07:41', '11:02', '11:02', '16:18', '18:03', '18:56', '19:32', '20:23', '20:48'], ["ST MICHEL D'AURANCE", 'Pailhès', '07:47', '11:05', '11:05', '16:20', '18:05', '18:58', '19:35', '20:25', '20:50'], ['LE CHEYLARD', 'La Palisse', '07:54', '11:09', '11:09', '16:25', '18:07', '19:03', '19:39', '20:30', '20:55'], ['LE CHEYLARD', 'Gendarmerie', '07:55', '11:10', '11:10', '16:26', '18:08', '19:04', '19:40', '20:31', '20:56'], ['LE CHEYLARD', 'Av. de la Libération', '11:11', '11:11', '16:27', '(1)', '18:09', '19:05', '19:41', '20:32', '20:57'], ['LE CHEYLARD', 'Av. Saunier / Grpe scol.', '07:58', '11:12', '11:12', '16:29', '18:10', '19:07', '19:42', '20:34', '20:59']],
[['vac_ete', 'VIDE', 'ND', '3LMMeJV', '4S', '5LMMeJV', '6LMMeJV', '7S', '8D', '9LMMeJ', '10V'], ['VALENCE', 'Gare Routière', '', '09:45', '09:45', '15:00', '16:45', '17:38', '18:15', '19:05', '19:30'], ['GUILHERANDGRANGES', 'Carnot', '', '09:52', '09:52', '15:07', '16:52', '17:45', '18:22', '19:12', '19:37'], ['SOYONS', 'Les Freydières', '', '09:57', '09:57', '15:12', '16:57', '15:50', '18:27', '19:17', '19:42'], ['SOYONS', 'Les Cités', '', '09:59', '09:59', '15:14', '16:59', '17:53', '18:29', '19:19', '19:44'], ['SOYONS', 'Centre', '', '10:00', '10:00', '15:15', '17:01', '17:54', '18:30', '19:20', '19:45'], ['SOYONS', 'Le Vivier', '', '10:01', '10:01', '15:16', '17:02', '17:55', '18:31', '19:21', '19:46'], ['CHARMES', 'Les 4 Chemins', '', '10:02', '10:02', '15:17', '17:03', '17:56', '18:32', '19:22', '19:47'], ['CHARMES', 'Le Vertel / Cités', '', '10:03', '10:03', '15:18', '17:05', '17:57', '18:33', '19:23', '19:48'], ['CHARMES', 'Centre', '', '10:04', '10:04', '15:19', '17:06', '17:58', '18:34', '19:24', '19:49'], ['ST GEORGESLES B', ' Giratoire RD 11', '', '10:05', '10:05', '15:20', '17:07', '17:59', '18:35', '19:25', '19:50'], ['ST GEORGES LES B', 'Chateaurouge', '', '10:07', '10:07', '15:22', '17:09', '18:01', '18:37', '19:27', '19:52'], ['BEAUCHASTEL', 'Les Ramières', '', '10:08', '10:08', '15:23', '17:10', '18:02', '18:38', '19:28', '19:53'], ['BEAUCHASTEL', 'Centre', '', '10:09', '10:09', '15:24', '17:11', '18:03', '18:39', '19:29', '19:54'], ['LA VOULTE', 'Cités', '', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND'], ['LA VOULTE', 'Nord', '', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND', 'ND'], ['ST LAURENT DU PAPE', 'Thoac', '', '10:12', '10:12', '15:27', '17:14', '18:06', '18:42', '19:32', '19:57'], ['ST LAURENT DU PAPE', 'Centre', '', '10:13', '10:13', '15:28', '17:15', '18:07', '18:43', '19:33', '19:58'], ['ST LAURENT DU PAPE', 'Hautussac', '', '10:15', '10:15', '15:30', '17:17', '18:09', '18:45', '19:35', '20:00'], ['ST LAURENT DU PAPE', 'Beaumazet', '', '10:16', '10:16', '15:31', '17:18', '18:10', '18:46', '19:36', '20:01'], ['ST LAURENT DU PAPE', 'Hauteville', '', '10:17', '10:17', '15:32', '17:19', '18:11', '18:47', '19:37', '20:02'], ['ST FORTUNAT', 'Prahy', '06:58', '10:20', '10:20', '15:35', '17:22', '18:14', '18:50', '19:40', '20:05'], ['ST FORTUNAT', 'Mondon', '07:00', '10:22', '10:22', '15:37', '17:24', '18:16', '18:52', '19:42', '20:07'], ['ST FORTUNAT', 'Centre', '07:02', '10:24', '10:24', '15:39', '17:26', '18:18', '18:54', '19:44', '20:09'], ['DUNIERE / EYRIEUX', 'RD', 'RD', '120', '07:04', '07:04', '10:26', '10:26', '15:41', '17:28', '18:20', '18:56', '19:46', '20:11'], ['DUNIERE / EYRIEUX', 'Centre', '07:05', '10:27', '10:27', '15:42', '17:29', '18:21', '18:57', '19:47', '20:12'], ['LES OLLIERES', 'La Pimpie', '07:08', '10:30', '10:30', '15:45', '17:32', '18:24', '19:00', '19:50', '20:15'], ['LES OLLIERES', 'Les Plots', '07:09', '10:31', '10:31', '15:46', '17:33', '18:25', '19:01', '19:51', '20:16'], ['LES OLLIERES', 'Mairie', 'D2', '07:10', '07:10', '10:32', '10:32', '15:47', '17:34', '18:26', '19:02', '19:52', '20:17'], ['LES OLLIERES', 'Centre', '07:11', '10:33', '10:33', '15:48', '17:35', '18:27', '19:03', '19:53', '20:18'], ['LES OLLIERES', 'Veye', '07:12', '10:34', '10:34', '15:49', '17:36', '18:28', '19:04', '19:54', '20:19'], ['LES OLLIERES', 'Escoulenc', '07:13', '10:35', '10:35', '15:50', '17:37', '18:29', '19:05', '19:55', '20:20'], ['ST SAUVEUR DE MGUT', 'Le Moulinon', '07:16', '10:39', '10:39', '15:54', '17:40', '18:33', '19:09', '19:59', '20:24'], ['ST SAUVEUR DE MGUT', 'Centre', '07:18', '10:40', '10:40', '15:55', '17:41', '18:34', '19:10', '20:00', '20:25'], ['ST MAURICE EN C', 'La Roche St M.', '07:22', '10:44', '10:44', '15:59', '17:44', '18:38', '19:14', '20:04', '20:29'], ['ST MAURICE EN C', 'Pt du Moulinas', '07:27', '10:46', '10:46', '16:01', '17:46', '18:40', '19:16', '20:06', '20:31'], ['BEAUVENE', 'Le Bateau', '07:30', '10:52', '10:52', '16:07', '17:52', '18:46', '19:22', '20:12', '20:37'], ['BEAUVENE', 'Pont de Chervil', '07:32', '10:54', '10:54', '16:09', '17:54', '18:48', '19:24', '20:14', '20:39'], ['ST BARTHELEMY LE MEIL', 'Sarny', '07:41', '11:02', '11:02', '16:18', '18:03', '18:56', '19:32', '20:23', '20:48'], ["ST MICHEL D'AURANCE", 'Pailhès', '07:47', '11:05', '11:05', '16:20', '18:05', '18:58', '19:35', '20:25', '20:50'], ['LE CHEYLARD', 'La Palisse', '07:54', '11:09', '11:09', '16:25', '18:07', '19:03', '19:39', '20:30', '20:55'], ['LE CHEYLARD', 'Gendarmerie', '07:55', '11:10', '11:10', '16:26', '18:08', '19:04', '19:40', '20:31', '20:56'], ['LE CHEYLARD', 'Av. de la Libération', '11:11', '11:11', '16:27', '(1)', '18:09', '19:05', '19:41', '20:32', '20:57'], ['LE CHEYLARD', 'Av. Saunier / Grpe scol.', '07:58', '11:12', '11:12', '16:29', '18:10', '19:07', '19:42', '20:34', '20:59']]]


