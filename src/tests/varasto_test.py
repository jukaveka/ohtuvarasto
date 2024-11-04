import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):

    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-1, -1)
        self.varasto3 = Varasto(4, 5)

    def test_negatiivinen_tilavuus_nollaus(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_negatiivinen_saldo_nollaus(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)
    
    def test_ylimaarainen_saldo_nollaus(self):
        self.assertAlmostEqual(self.varasto3.saldo, self.varasto3.tilavuus)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_onnistu(self):
        self.varasto3.lisaa_varastoon(-2)

        # saldo vastaa alkuperäistä lisättyä saldoa
        self.assertAlmostEqual(self.varasto3.saldo, 4)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_negatiivinen_ottaminen_palauttaa_nollan(self):
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_saldoa_isommalla_maaralla(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(15)

        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(saatu_maara, 5)

    def test_lisays_rajoittuu_tilavuuteen(self):
        self.varasto.lisaa_varastoon(15)
        
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_tulostus(self):
        self.varasto.lisaa_varastoon(3)
        
        self.assertEqual(str(self.varasto), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")