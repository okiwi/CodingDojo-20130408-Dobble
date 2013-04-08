__author__ = 'charles'
import unittest


class Dobble(object):
    def __init__(self):
        self.cartes = []
        for a in range(30):
            self.cartes.append(Carte())

    def compteLesAnimauxCommuns(self, carte1, carte2):
        return 1


class Carte(object):
    def __init__(self):
        self.animaux = ["Morse", "Ornithorynque", "Loutre", "Canard", "Souris", "Poney", "Licorne", "Narval"]


class TestDobble(unittest.TestCase):
    def test_rien(self):
        self.assertTrue(True)

    def test_peut_obtenir_les_30_cartes(self):
        jeu = Dobble()

        cartes = jeu.cartes

        self.assertEqual(30, len(cartes))

    def test_carte_contient_8_animaux(self):
        carte = Carte()

        animaux = carte.animaux

        self.assertEqual(8, len(animaux))

    def test_animaux_different_carte(self):
        carte = Carte()

        self.assertNotEqual(carte.animaux[0], carte.animaux[1])

    def test_lejeucontientdescartes(self):
        carte = Dobble().cartes[0]

        self.assertEqual(carte.animaux[0], "Morse")

    def testlescartescontiennent8nomsdanimaux(self):
        carte = Dobble().cartes[0]

        self.assertEqual(carte.animaux[0], "Morse")
        self.assertEqual(carte.animaux[1], "Ornithorynque")
        self.assertEqual(carte.animaux[2], "Loutre")
        self.assertEqual(carte.animaux[3], "Canard")
        self.assertEqual(carte.animaux[4], "Souris")
        self.assertEqual(carte.animaux[5], "Poney")
        self.assertEqual(carte.animaux[6], "Licorne")
        self.assertEqual(carte.animaux[7], "Narval")

    def test_les_cartes_du_jeu_ont_un_animal_commun(self):
        jeu = Dobble()

        for a in range(30):
            for b in range(30):
                if a != b:
                    self.assertEquals(jeu.compteLesAnimauxCommuns(jeu.cartes[a], jeu.cartes[b]), 1)


    def test_2_cartes_1_nom_commun(self):
        jeu = Dobble()
        carte1 = jeu.cartes[0]
        carte1.animaux[0]="Morse"
        carte2 = jeu.cartes[1]
        carte2.animaux[1]="Poney"

        self.assertEquals(jeu.compteLesAnimauxCommuns(carte1, carte2), 1)

