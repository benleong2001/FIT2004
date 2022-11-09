import unittest
from assignment1 import analyze


class TestMethods(unittest.TestCase):
    # a roster of 2 characters
    roster = 2
    # results with 20 matches
    results = [
        ['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
        ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
        ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
        ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
        ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
        ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
        ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]
    ]

    def test_1(self):
        # looking for a score of 64
        score = 64

        result = [
            [['ABB', 'AAB', 70],
             ['ABB', 'BBB', 68],
             ['AAB', 'BBB', 67],
             ['AAB', 'AAB', 65],
             ['AAB', 'AAA', 64],
             ['ABB', 'ABB', 64],
             ['AAA', 'AAA', 62],
             ['AAB', 'AAA', 58],
             ['ABB', 'ABB', 58],
             ['AAB', 'ABB', 57]],
            [['AAB', 'AAA', 64], ['ABB', 'ABB', 64]]
        ]
        self.assertEqual(analyze(self.results, self.roster, score), result)

    def test_2(self):
        # looking for a score of 63
        score = 63

        result = [
            [['ABB', 'AAB', 70],
             ['ABB', 'BBB', 68],
             ['AAB', 'BBB', 67],
             ['AAB', 'AAB', 65],
             ['AAB', 'AAA', 64],
             ['ABB', 'ABB', 64],
             ['AAA', 'AAA', 62],
             ['AAB', 'AAA', 58],
             ['ABB', 'ABB', 58],
             ['AAB', 'ABB', 57]],
            [['AAB', 'AAA', 64], ['ABB', 'ABB', 64]]
        ]

        self.assertEqual(analyze(self.results, self.roster, score), result)

    def test_3(self):
        # looking for a score of 71
        score = 71

        result = [
            [['ABB', 'AAB', 70],
             ['ABB', 'BBB', 68],
             ['AAB', 'BBB', 67],
             ['AAB', 'AAB', 65],
             ['AAB', 'AAA', 64],
             ['ABB', 'ABB', 64],
             ['AAA', 'AAA', 62],
             ['AAB', 'AAA', 58],
             ['ABB', 'ABB', 58],
             ['AAB', 'ABB', 57]],
            []
        ]

        self.assertEqual(analyze(self.results, self.roster, score), result)

    def test_4(self):
        # looking for a score of 0
        score = 0

        result = [
            [['ABB', 'AAB', 70],
             ['ABB', 'BBB', 68],
             ['AAB', 'BBB', 67],
             ['AAB', 'AAB', 65],
             ['AAB', 'AAA', 64],
             ['ABB', 'ABB', 64],
             ['AAA', 'AAA', 62],
             ['AAB', 'AAA', 58],
             ['ABB', 'ABB', 58],
             ['AAB', 'ABB', 57]],
            [['AAB', 'ABB', 30]]
        ]

        self.assertEqual(analyze(self.results, self.roster, score), result)

    def test_5(self):
        results = [
            ['ABC', 'ADE', 30],
            ['AAC', 'ACE', 30],
            ['AAC', 'AAE', 30]
        ]

        result = [
            [['AAE', 'AAC', 70],
             ['ACE', 'AAC', 70],
             ['ADE', 'ABC', 70],
             ['AAC', 'AAE', 30],
             ['AAC', 'ACE', 30],
             ['ABC', 'ADE', 30]],
            [['AAE', 'AAC', 70], ['ACE', 'AAC', 70], ['ADE', 'ABC', 70]]
        ]

        self.assertEqual(analyze(results, 5, 40), result)

    def test_6(self):
        results = [
            ['AB', 'BB', 30],
            ['BA', 'AA', 30]
        ]

        result = [
            [['AA', 'AB', 70],
             ['BB', 'AB', 70],
             ['AB', 'AA', 30],
             ['AB', 'BB', 30]],
            [['AA', 'AB', 70], ['BB', 'AB', 70]]
        ]

        self.assertEqual(analyze(results, 2, 40), result)

    def test_7(self):
        results = [
            ['A', 'B', 30],
            ['C', 'A', 40]
        ]

        result = [
            [['B', 'A', 70],
             ['A', 'C', 60],
             ['C', 'A', 40],
             ['A', 'B', 30]],
            [['B', 'A', 70]]
        ]

        self.assertEqual(analyze(results, 3, 70), result)

    def test_8(self):
        results = [
            ['A', 'A', 30],
            ['A', 'A', 70],
            ['A', 'A', 40]
        ]

        result = [
            [['A', 'A', 70],
             ['A', 'A', 60],
             ['A', 'A', 40],
             ['A', 'A', 30]],
            [['A', 'A', 70]]
        ]

        self.assertEqual(analyze(results, 1, 70), result)

    def test_9(self):
        results = [
            ['A', 'B', 50],
        ]

        result = [
            [['A', 'B', 50],
             ['B', 'A', 50]],
            []
        ]

        self.assertEqual(analyze(results, 2, 70), result)

    def test_10(self):
        results = [
            ['A', 'A', 50],
        ]

        result = [
            [['A', 'A', 50]],
            [['A', 'A', 50]]
        ]

        self.assertEqual(analyze(results, 1, 50), result)

    def test_11(self):
        results = [
            ['A', 'B', 50],
        ]

        result = [
            [['A', 'B', 50],
             ['B', 'A', 50]],
            [['A', 'B', 50], ['B', 'A', 50]]
        ]

        self.assertEqual(analyze(results, 2, 50), result)

    def test_12(self):
        results = [
            ['A', 'B', 100],
        ]

        result = [
            [['A', 'B', 100],
             ['B', 'A', 0]],
            [['A', 'B', 100]]
        ]

        self.assertEqual(analyze(results, 2, 50), result)

    def test_13(self):
        results = [
            ['A', 'B', 100],
        ]

        result = [
            [['A', 'B', 100],
             ['B', 'A', 0]],
            [['B', 'A', 0]]
        ]

        self.assertEqual(analyze(results, 2, 0), result)

    def test_14(self):
        results = [
            ['A', 'A', 100],
        ]

        result = [
            [['A', 'A', 100],
             ['A', 'A', 0]],
            [['A', 'A', 0]]
        ]

        self.assertEqual(analyze(results, 1, 0), result)

    def test_15(self):
        results = [
            ['A', 'A', 100],
        ]

        result = [
            [['A', 'A', 100],
             ['A', 'A', 0]],
            [['A', 'A', 100]]
        ]

        self.assertEqual(analyze(results, 1, 1), result)

    def test_16(self):
        results = [
            ['AACDEFGHIJKLMNOPQRSTUVWXYZZ', 'ABCDEFGHIJKLMNOPQRSTUVWXZZZ', 35],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZZ', 'ABCDEFGHIJKLMNOPQRSTUVWXZZZ', 35]
        ]

        result = [
            [['ABCDEFGHIJKLMNOPQRSTUVWXZZZ', 'AACDEFGHIJKLMNOPQRSTUVWXYZZ', 65],
             ['ABCDEFGHIJKLMNOPQRSTUVWXZZZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZZ', 65],
             ['AACDEFGHIJKLMNOPQRSTUVWXYZZ', 'ABCDEFGHIJKLMNOPQRSTUVWXZZZ', 35],
             ['ABCDEFGHIJKLMNOPQRSTUVWXYZZ', 'ABCDEFGHIJKLMNOPQRSTUVWXZZZ', 35]],
            [['ABCDEFGHIJKLMNOPQRSTUVWXZZZ', 'AACDEFGHIJKLMNOPQRSTUVWXYZZ', 65],
             ['ABCDEFGHIJKLMNOPQRSTUVWXZZZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZZ', 65]]
        ]

        self.assertEqual(analyze(results, 26, 65), result)
        
    def test_17(self):
        results = [['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42], ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36], ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49], ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46], ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36], ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30], ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]

        result = [[['ABB', 'AAB', 70], ['ABB', 'BBB', 68], ['AAB', 'BBB', 67], ['AAB', 'AAB', 65], ['AAB', 'AAA', 64], ['ABB', 'ABB', 64], ['AAA', 'AAA', 62], ['AAB', 'AAA', 58], ['ABB', 'ABB', 58], ['AAB', 'ABB', 57]], [['AAB', 'AAA', 64], ['ABB', 'ABB', 64]]]
        
        self.assertEqual(analyze(results, 2, 64), result)
        
    def test_18(self):
        results = [['AAB', 'AAB', 35],['AAB', 'BBA', 49], ['BAB', 'BAB', 42], ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36], ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49], ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46], ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36], ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30], ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]

        result = [[['ABB', 'AAB', 70], ['ABB', 'BBB', 68], ['AAB', 'BBB', 67], ['AAB', 'AAB', 65], ['AAB', 'AAA', 64], ['ABB', 'ABB', 64], ['AAA', 'AAA', 62], ['AAB', 'AAA', 58], ['ABB', 'ABB', 58], ['AAB', 'ABB', 57]], [['AAB', 'AAA', 64], ['ABB', 'ABB', 64]]]
        
        self.assertEqual(analyze(results, 2, 63), result)
        
    def test_19(self):
        results = [['AAB', 'AAB', 35],['AAB', 'BBA', 49], ['BAB', 'BAB', 42], ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36], ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49], ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46], ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36], ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30], ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]

        result = [[['ABB', 'AAB', 70], ['ABB', 'BBB', 68], ['AAB', 'BBB', 67], ['AAB', 'AAB', 65], ['AAB', 'AAA', 64], ['ABB', 'ABB', 64], ['AAA', 'AAA', 62], ['AAB', 'AAA', 58], ['ABB', 'ABB', 58], ['AAB', 'ABB', 57]], []]
        
        self.assertEqual(analyze(results, 2, 71), result)
        
    def test_20(self):
        results = [['AAB', 'AAB', 35],['AAB', 'BBA', 49], ['BAB', 'BAB', 42], ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36], ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49], ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46], ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36], ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30], ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]

        result = [[['ABB', 'AAB', 70], ['ABB', 'BBB', 68], ['AAB', 'BBB', 67], ['AAB', 'AAB', 65], ['AAB', 'AAA', 64], ['ABB', 'ABB', 64], ['AAA', 'AAA', 62], ['AAB', 'AAA', 58], ['ABB', 'ABB', 58], ['AAB', 'ABB', 57]], [['AAB', 'ABB', 30]]]
        
        self.assertEqual(analyze(results, 2, 0), result)
        
    def test_21(self):
        results = [['XDTRW', 'GMXUD', 55], ['EGEGO', 'WXAKY', 49], ['OQVLA', 'FDXOW', 84], ['IZVZY', 'ROOMF', 24], ['NLCIV', 'QPDXZ', 50], ['QPDXZ', 'NLCIV', 50], ['XPHGI', 'JFLIP', 32], ['WQYVS', 'WKLEY', 76], ['IOSTQ', 'HAIMK', 71], ['ZSOWF', 'LMCUM', 1], ['VMINV', 'ONSGR', 24], ['FUSNX', 'WHGBT', 47], ['XKAZV', 'ENLAT', 50], ['CYBAZ', 'KYBGH', 44], ['VWRSX', 'JOGJI', 44], ['SQJVU', 'JFEAY', 15], ['RGZNK', 'XHGVC', 99], ['NLGWP', 'IOUDM', 0], ['DIMDG', 'SBJWM', 81], ['PVPCP', 'FJWIG', 49]]

        result = [[['DIMOU', 'GLNPW', 100], ['CLMMU', 'FOSWZ', 99], ['GKNRZ', 'CGHVX', 99], ['AEFJY', 'JQSUV', 85], ['ALOQV', 'DFOWX', 84], ['DDGIM', 'BJMSW', 81], ['FMOOR', 'IVYZZ', 76], ['GNORS', 'IMNVV', 76], ['QSVWY', 'EKLWY', 76], ['IOQST', 'AHIKM', 71]], [['DIMOU', 'GLNPW', 100]]]
        
        self.assertEqual(analyze(results, 26, 100), result)
        
    def test_22(self):
        results = [['RJI', 'DMK', 100]]

        result = [[['IJR', 'DKM', 100], ['DKM', 'IJR', 0]], [['IJR', 'DKM', 100]]]
        
        self.assertEqual(analyze(results, 26, 50), result)
        
    def test_23(self):
        results = [['RJI', 'DMK', 100]]

        result = [[['IJR', 'DKM', 100], ['DKM', 'IJR', 0]], [['IJR', 'DKM', 100]]]
        
        self.assertEqual(analyze(results, 26, 100), result)
        
    def test_24(self):
        results = [['RJI', 'DMK', 100]]

        result = [[['IJR', 'DKM', 100], ['DKM', 'IJR', 0]], [['DKM', 'IJR', 0]]]
        
        self.assertEqual(analyze(results, 26, 0), result)
        
    def test_25(self):
        results = [['RJI', 'DMK', 100], ['KJN', 'RCE', 100], ['EEJ', 'DOK', 100], ['AUH', 'ODN', 100], ['VFW', 'CDK', 100], ['TKC', 'EVP', 100], ['VJE', 'BLJ', 100], ['GKG', 'NES', 100], ['IXQ', 'AJF', 100], ['GTB', 'HFE', 100], ['LVC', 'QNL', 100], ['STO', 'VPS', 100], ['OFN', 'DAY', 100], ['FEL', 'HOO', 100], ['GXA', 'FRT', 100], ['GKX', 'FSR', 100], ['KXG', 'BVJ', 100], ['RAG', 'EAO', 100], ['SJU', 'SHE', 100], ['SUB', 'OXH', 100]]

        result = [[['AGR', 'AEO', 100], ['AGX', 'FRT', 100], ['AHU', 'DNO', 100], ['BGT', 'EFH', 100], ['BSU', 'HOX', 100], ['CKT', 'EPV', 100], ['CLV', 'LNQ', 100], ['EEJ', 'DKO', 100], ['EFL', 'HOO', 100], ['EJV', 'BJL', 100]], [['AGR', 'AEO', 100], ['AGX', 'FRT', 100], ['AHU', 'DNO', 100], ['BGT', 'EFH', 100], ['BSU', 'HOX', 100], ['CKT', 'EPV', 100], ['CLV', 'LNQ', 100], ['EEJ', 'DKO', 100], ['EFL', 'HOO', 100], ['EJV', 'BJL', 100], ['FNO', 'ADY', 100], ['FVW', 'CDK', 100], ['GGK', 'ENS', 100], ['GKX', 'BJV', 100], ['GKX', 'FRS', 100], ['IJR', 'DKM', 100], ['IQX', 'AFJ', 100], ['JKN', 'CER', 100], ['JSU', 'EHS', 100], ['OST', 'PSV', 100]]]
        
        self.assertEqual(analyze(results, 26, 50), result)
        
    def test_26(self):
        results = [['RJI', 'DMK', 100], ['KJN', 'RCE', 100], ['EEJ', 'DOK', 100], ['AUH', 'ODN', 100]]

        result = [[['AHU', 'DNO', 100], ['EEJ', 'DKO', 100], ['IJR', 'DKM', 100], ['JKN', 'CER', 100], ['CER', 'JKN', 0], ['DKM', 'IJR', 0], ['DKO', 'EEJ', 0], ['DNO', 'AHU', 0]], [['AHU', 'DNO', 100], ['EEJ', 'DKO', 100], ['IJR', 'DKM', 100], ['JKN', 'CER', 100]]]
        
        self.assertEqual(analyze(results, 26, 1), result)
        
    def test_27(self):
        results = [['RJI', 'DMK', 100], ['KJN', 'RCE', 100], ['EEJ', 'DOK', 100], ['AUH', 'ODN', 100]]

        result = [[['AHU', 'DNO', 100], ['EEJ', 'DKO', 100], ['IJR', 'DKM', 100], ['JKN', 'CER', 100], ['CER', 'JKN', 0], ['DKM', 'IJR', 0], ['DKO', 'EEJ', 0], ['DNO', 'AHU', 0]], [['CER', 'JKN', 0], ['DKM', 'IJR', 0], ['DKO', 'EEJ', 0], ['DNO', 'AHU', 0]]]
        
        self.assertEqual(analyze(results, 26, 0), result)
        
    def test_28(self):
        results = [['GFLB', 'DAMK', 69], ['GFEN', 'COPE', 40], ['OLKN', 'HPCC', 58], ['IFAD', 'HECJ', 61], ['EFEP', 'MLDN', 34], ['OMGN', 'GEIB', 6], ['OHHN', 'CLLO', 13], ['CCIM', 'ADFA', 67], ['FJCO', 'JPCD', 22], ['IDHN', 'IGOJ', 36], ['KHLP', 'DMDB', 70], ['GPNE', 'KBMB', 15], ['BJEE', 'IKJH', 33], ['FKFB', 'BNAF', 89], ['BIFN', 'KGHL', 7], ['NDEI', 'BIFD', 94], ['EMIJ', 'NGOD', 8], ['IGEM', 'DBEA', 95], ['JKEC', 'EGLF', 10], ['PAFH', 'GACE', 47], ['DBHO', 'KMAB', 8], ['JDND', 'KFPF', 8], ['LDCN', 'NLKJ', 72], ['LEFG', 'MPPE', 20], ['LKIH', 'AFMG', 92], ['JMGA', 'PEJA', 26], ['KJJA', 'HPIM', 81], ['OIEC', 'MMOI', 96], ['NEEN', 'PGFF', 38], ['LFDA', 'BDHM', 70], ['OCCC', 'EHFC', 96], ['KOIB', 'BJEK', 89], ['KDNP', 'OBEK', 19], ['CMDB', 'GNAA', 62], ['NGDH', 'NAIK', 17], ['EEHA', 'FMCG', 93], ['DKNL', 'IPGN', 29], ['MJDP', 'AFEC', 44], ['KPNF', 'AKBH', 45], ['MCFO', 'POOD', 83], ['LBEC', 'DICB', 34], ['FEFI', 'JDAE', 88], ['AINL', 'DGDJ', 3], ['ALPN', 'KGAK', 66], ['DNMI', 'CMBK', 9], ['OLDC', 'EEHG', 58], ['HMNI', 'CEHN', 48], ['PBHC', 'ADPC', 53], ['HKIK', 'JODD', 59], ['DBOK', 'MEKC', 2], ['IBGJ', 'MBFM', 87], ['BCBA', 'AKDA', 45], ['GFPB', 'AKAH', 76], ['AHCJ', 'ILLJ', 79], ['HNHB', 'DGCL', 83], ['BNDB', 'GDNJ', 82], ['PFGG', 'GKCO', 65], ['OHLE', 'MGDM', 44], ['LGJH', 'EBCC', 31], ['KMCL', 'MNGL', 2], ['LAGA', 'JCNP', 36], ['CEON', 'GFNL', 72], ['FKGB', 'LIHN', 25], ['FIJL', 'KGMP', 63], ['GEOB', 'FFDE', 56], ['FFOO', 'INGI', 69], ['FHKI', 'BGMB', 49], ['MIFF', 'FCOA', 65], ['BNKA', 'LEPF', 92], ['EINN', 'LLDF', 40], ['JEMN', 'MMEP', 75], ['DECF', 'KGMG', 37], ['JCFG', 'JEHC', 49], ['GGFA', 'MMKP', 91], ['BMCM', 'LAOG', 4], ['DEPF', 'HJPH', 70], ['POBI', 'JKND', 5], ['DCHD', 'LKKJ', 52], ['NNFP', 'FOFL', 26], ['LOJB', 'NKPE', 10], ['KOAP', 'ABCK', 26], ['PDKJ', 'JENF', 11], ['LHCI', 'ENMI', 4], ['EBCJ', 'COLG', 73], ['NGCA', 'DDMP', 1], ['EFHN', 'ANBH', 88], ['LFLK', 'AGED', 98], ['JKHI', 'DKND', 47], ['MDLA', 'EOMP', 31], ['KHAJ', 'HIGJ', 15], ['PEAI', 'HMFK', 98], ['NDMH', 'NAJM', 40], ['MCLO', 'JDEC', 43], ['JPBA', 'IGDD', 36], ['EJHM', 'GEPN', 59], ['JAGM', 'IGJL', 86], ['BFNF', 'EHOH', 22], ['BEDK', 'NMAJ', 54], ['FLGK', 'AGKH', 49], ['ICBB', 'EAEO', 2]]

        result = [[['DDMP', 'ACGN', 99], ['AEEO', 'BBCI', 98], ['AEIP', 'FHKM', 98], ['CEKM', 'BDKO', 98], ['FKLL', 'ADEG', 98], ['GLMN', 'CKLM', 98], ['DDGJ', 'AILN', 97], ['AGLO', 'BCMM', 96], ['CCCO', 'CEFH', 96], ['CEIO', 'IMMO', 96]], [['CFGJ', 'CEHJ', 49], ['FGKL', 'AGHK', 49], ['FHIK', 'BBGM', 49]]]
        
        self.assertEqual(analyze(results, 26, 49), result)
        
    def test_29(self):
        results = [['GFLB', 'DAMK', 69], ['GFEN', 'COPE', 40], ['OLKN', 'HPCC', 58], ['IFAD', 'HECJ', 61], ['EFEP', 'MLDN', 34], ['OMGN', 'GEIB', 6], ['OHHN', 'CLLO', 13], ['CCIM', 'ADFA', 67], ['FJCO', 'JPCD', 22], ['IDHN', 'IGOJ', 36], ['KHLP', 'DMDB', 70], ['GPNE', 'KBMB', 15], ['BJEE', 'IKJH', 33], ['FKFB', 'BNAF', 89], ['BIFN', 'KGHL', 7], ['NDEI', 'BIFD', 94], ['EMIJ', 'NGOD', 8], ['IGEM', 'DBEA', 95], ['JKEC', 'EGLF', 10], ['PAFH', 'GACE', 47], ['DBHO', 'KMAB', 8], ['JDND', 'KFPF', 8], ['LDCN', 'NLKJ', 72], ['LEFG', 'MPPE', 20], ['LKIH', 'AFMG', 92], ['JMGA', 'PEJA', 26], ['KJJA', 'HPIM', 81], ['OIEC', 'MMOI', 96], ['NEEN', 'PGFF', 38], ['LFDA', 'BDHM', 70], ['OCCC', 'EHFC', 96], ['KOIB', 'BJEK', 89], ['KDNP', 'OBEK', 19], ['CMDB', 'GNAA', 62], ['NGDH', 'NAIK', 17], ['EEHA', 'FMCG', 93], ['DKNL', 'IPGN', 29], ['MJDP', 'AFEC', 44], ['KPNF', 'AKBH', 45], ['MCFO', 'POOD', 83], ['LBEC', 'DICB', 34], ['FEFI', 'JDAE', 88], ['AINL', 'DGDJ', 3], ['ALPN', 'KGAK', 66], ['DNMI', 'CMBK', 9], ['OLDC', 'EEHG', 58], ['HMNI', 'CEHN', 48], ['PBHC', 'ADPC', 53], ['HKIK', 'JODD', 59], ['DBOK', 'MEKC', 2], ['IBGJ', 'MBFM', 87], ['BCBA', 'AKDA', 45], ['GFPB', 'AKAH', 76], ['AHCJ', 'ILLJ', 79], ['HNHB', 'DGCL', 83], ['BNDB', 'GDNJ', 82], ['PFGG', 'GKCO', 65], ['OHLE', 'MGDM', 44], ['LGJH', 'EBCC', 31], ['KMCL', 'MNGL', 2], ['LAGA', 'JCNP', 36], ['CEON', 'GFNL', 72], ['FKGB', 'LIHN', 25], ['FIJL', 'KGMP', 63], ['GEOB', 'FFDE', 56], ['FFOO', 'INGI', 69], ['FHKI', 'BGMB', 49], ['MIFF', 'FCOA', 65], ['BNKA', 'LEPF', 92], ['EINN', 'LLDF', 40], ['JEMN', 'MMEP', 75], ['DECF', 'KGMG', 37], ['JCFG', 'JEHC', 49], ['GGFA', 'MMKP', 91], ['BMCM', 'LAOG', 4], ['DEPF', 'HJPH', 70], ['POBI', 'JKND', 5], ['DCHD', 'LKKJ', 52], ['NNFP', 'FOFL', 26], ['LOJB', 'NKPE', 10], ['KOAP', 'ABCK', 26], ['PDKJ', 'JENF', 11], ['LHCI', 'ENMI', 4], ['EBCJ', 'COLG', 73], ['NGCA', 'DDMP', 1], ['EFHN', 'ANBH', 88], ['LFLK', 'AGED', 98], ['JKHI', 'DKND', 47], ['MDLA', 'EOMP', 31], ['KHAJ', 'HIGJ', 15], ['PEAI', 'HMFK', 98], ['NDMH', 'NAJM', 40], ['MCLO', 'JDEC', 43], ['JPBA', 'IGDD', 36], ['EJHM', 'GEPN', 59], ['JAGM', 'IGJL', 86], ['BFNF', 'EHOH', 22], ['BEDK', 'NMAJ', 54], ['FLGK', 'AGKH', 49], ['ICBB', 'EAEO', 2]]

        result = [[['DDMP', 'ACGN', 99], ['AEEO', 'BBCI', 98], ['AEIP', 'FHKM', 98], ['CEKM', 'BDKO', 98], ['FKLL', 'ADEG', 98], ['GLMN', 'CKLM', 98], ['DDGJ', 'AILN', 97], ['AGLO', 'BCMM', 96], ['CCCO', 'CEFH', 96], ['CEIO', 'IMMO', 96]], []]
        
        self.assertEqual(analyze(results, 26, 100), result)
        
    def test_30(self):
        results = [['GFLB', 'DAMK', 69], ['GFEN', 'COPE', 40], ['OLKN', 'HPCC', 58], ['IFAD', 'HECJ', 61], ['EFEP', 'MLDN', 34], ['OMGN', 'GEIB', 6], ['OHHN', 'CLLO', 13], ['CCIM', 'ADFA', 67], ['FJCO', 'JPCD', 22], ['IDHN', 'IGOJ', 36], ['KHLP', 'DMDB', 70], ['GPNE', 'KBMB', 15], ['BJEE', 'IKJH', 33], ['FKFB', 'BNAF', 89], ['BIFN', 'KGHL', 7], ['NDEI', 'BIFD', 94], ['EMIJ', 'NGOD', 8], ['IGEM', 'DBEA', 95], ['JKEC', 'EGLF', 10], ['PAFH', 'GACE', 47], ['DBHO', 'KMAB', 8], ['JDND', 'KFPF', 8], ['LDCN', 'NLKJ', 72], ['LEFG', 'MPPE', 20], ['LKIH', 'AFMG', 92], ['JMGA', 'PEJA', 26], ['KJJA', 'HPIM', 81], ['OIEC', 'MMOI', 96], ['NEEN', 'PGFF', 38], ['LFDA', 'BDHM', 70], ['OCCC', 'EHFC', 96], ['KOIB', 'BJEK', 89], ['KDNP', 'OBEK', 19], ['CMDB', 'GNAA', 62], ['NGDH', 'NAIK', 17], ['EEHA', 'FMCG', 93], ['DKNL', 'IPGN', 29], ['MJDP', 'AFEC', 44], ['KPNF', 'AKBH', 45], ['MCFO', 'POOD', 83], ['LBEC', 'DICB', 34], ['FEFI', 'JDAE', 88], ['AINL', 'DGDJ', 3], ['ALPN', 'KGAK', 66], ['DNMI', 'CMBK', 9], ['OLDC', 'EEHG', 58], ['HMNI', 'CEHN', 48], ['PBHC', 'ADPC', 53], ['HKIK', 'JODD', 59], ['DBOK', 'MEKC', 2], ['IBGJ', 'MBFM', 87], ['BCBA', 'AKDA', 45], ['GFPB', 'AKAH', 76], ['AHCJ', 'ILLJ', 79], ['HNHB', 'DGCL', 83], ['BNDB', 'GDNJ', 82], ['PFGG', 'GKCO', 65], ['OHLE', 'MGDM', 44], ['LGJH', 'EBCC', 31], ['KMCL', 'MNGL', 2], ['LAGA', 'JCNP', 36], ['CEON', 'GFNL', 72], ['FKGB', 'LIHN', 25], ['FIJL', 'KGMP', 63], ['GEOB', 'FFDE', 56], ['FFOO', 'INGI', 69], ['FHKI', 'BGMB', 49], ['MIFF', 'FCOA', 65], ['BNKA', 'LEPF', 92], ['EINN', 'LLDF', 40], ['JEMN', 'MMEP', 75], ['DECF', 'KGMG', 37], ['JCFG', 'JEHC', 49], ['GGFA', 'MMKP', 91], ['BMCM', 'LAOG', 4], ['DEPF', 'HJPH', 70], ['POBI', 'JKND', 5], ['DCHD', 'LKKJ', 52], ['NNFP', 'FOFL', 26], ['LOJB', 'NKPE', 10], ['KOAP', 'ABCK', 26], ['PDKJ', 'JENF', 11], ['LHCI', 'ENMI', 4], ['EBCJ', 'COLG', 73], ['NGCA', 'DDMP', 1], ['EFHN', 'ANBH', 88], ['LFLK', 'AGED', 98], ['JKHI', 'DKND', 47], ['MDLA', 'EOMP', 31], ['KHAJ', 'HIGJ', 15], ['PEAI', 'HMFK', 98], ['NDMH', 'NAJM', 40], ['MCLO', 'JDEC', 43], ['JPBA', 'IGDD', 36], ['EJHM', 'GEPN', 59], ['JAGM', 'IGJL', 86], ['BFNF', 'EHOH', 22], ['BEDK', 'NMAJ', 54], ['FLGK', 'AGKH', 49], ['ICBB', 'EAEO', 2]]

        result = [[['DDMP', 'ACGN', 99], ['AEEO', 'BBCI', 98], ['AEIP', 'FHKM', 98], ['CEKM', 'BDKO', 98], ['FKLL', 'ADEG', 98], ['GLMN', 'CKLM', 98], ['DDGJ', 'AILN', 97], ['AGLO', 'BCMM', 96], ['CCCO', 'CEFH', 96], ['CEIO', 'IMMO', 96]], [['AGHK', 'FGKL', 51], ['BBGM', 'FHIK', 51], ['CEHJ', 'CFGJ', 51]]]
        
        self.assertEqual(analyze(results, 26, 50), result)
        
    def test_31(self):
        results = [['GFLB', 'DAMK', 69], ['GFEN', 'COPE', 40], ['OLKN', 'HPCC', 58], ['IFAD', 'HECJ', 61], ['EFEP', 'MLDN', 34], ['OMGN', 'GEIB', 6], ['OHHN', 'CLLO', 13], ['CCIM', 'ADFA', 67], ['FJCO', 'JPCD', 22], ['IDHN', 'IGOJ', 36], ['KHLP', 'DMDB', 70], ['GPNE', 'KBMB', 15], ['BJEE', 'IKJH', 33], ['FKFB', 'BNAF', 89], ['BIFN', 'KGHL', 7], ['NDEI', 'BIFD', 94], ['EMIJ', 'NGOD', 8], ['IGEM', 'DBEA', 95], ['JKEC', 'EGLF', 10], ['PAFH', 'GACE', 47], ['DBHO', 'KMAB', 8], ['JDND', 'KFPF', 8], ['LDCN', 'NLKJ', 72], ['LEFG', 'MPPE', 20], ['LKIH', 'AFMG', 92], ['JMGA', 'PEJA', 26], ['KJJA', 'HPIM', 81], ['OIEC', 'MMOI', 96], ['NEEN', 'PGFF', 38], ['LFDA', 'BDHM', 70], ['OCCC', 'EHFC', 96], ['KOIB', 'BJEK', 89], ['KDNP', 'OBEK', 19], ['CMDB', 'GNAA', 62], ['NGDH', 'NAIK', 17], ['EEHA', 'FMCG', 93], ['DKNL', 'IPGN', 29], ['MJDP', 'AFEC', 44], ['KPNF', 'AKBH', 45], ['MCFO', 'POOD', 83], ['LBEC', 'DICB', 34], ['FEFI', 'JDAE', 88], ['AINL', 'DGDJ', 3], ['ALPN', 'KGAK', 66], ['DNMI', 'CMBK', 9], ['OLDC', 'EEHG', 58], ['HMNI', 'CEHN', 48], ['PBHC', 'ADPC', 53], ['HKIK', 'JODD', 59], ['DBOK', 'MEKC', 2], ['IBGJ', 'MBFM', 87], ['BCBA', 'AKDA', 45], ['GFPB', 'AKAH', 76], ['AHCJ', 'ILLJ', 79], ['HNHB', 'DGCL', 83], ['BNDB', 'GDNJ', 82], ['PFGG', 'GKCO', 65], ['OHLE', 'MGDM', 44], ['LGJH', 'EBCC', 31], ['KMCL', 'MNGL', 2], ['LAGA', 'JCNP', 36], ['CEON', 'GFNL', 72], ['FKGB', 'LIHN', 25], ['FIJL', 'KGMP', 63], ['GEOB', 'FFDE', 56], ['FFOO', 'INGI', 69], ['FHKI', 'BGMB', 49], ['MIFF', 'FCOA', 65], ['BNKA', 'LEPF', 92], ['EINN', 'LLDF', 40], ['JEMN', 'MMEP', 75], ['DECF', 'KGMG', 37], ['JCFG', 'JEHC', 49], ['GGFA', 'MMKP', 91], ['BMCM', 'LAOG', 4], ['DEPF', 'HJPH', 70], ['POBI', 'JKND', 5], ['DCHD', 'LKKJ', 52], ['NNFP', 'FOFL', 26], ['LOJB', 'NKPE', 10], ['KOAP', 'ABCK', 26], ['PDKJ', 'JENF', 11], ['LHCI', 'ENMI', 4], ['EBCJ', 'COLG', 73], ['NGCA', 'DDMP', 1], ['EFHN', 'ANBH', 88], ['LFLK', 'AGED', 98], ['JKHI', 'DKND', 47], ['MDLA', 'EOMP', 31], ['KHAJ', 'HIGJ', 15], ['PEAI', 'HMFK', 98], ['NDMH', 'NAJM', 40], ['MCLO', 'JDEC', 43], ['JPBA', 'IGDD', 36], ['EJHM', 'GEPN', 59], ['JAGM', 'IGJL', 86], ['BFNF', 'EHOH', 22], ['BEDK', 'NMAJ', 54], ['FLGK', 'AGKH', 49], ['ICBB', 'EAEO', 2]]

        result = [[['DDMP', 'ACGN', 99], ['AEEO', 'BBCI', 98], ['AEIP', 'FHKM', 98], ['CEKM', 'BDKO', 98], ['FKLL', 'ADEG', 98], ['GLMN', 'CKLM', 98], ['DDGJ', 'AILN', 97], ['AGLO', 'BCMM', 96], ['CCCO', 'CEFH', 96], ['CEIO', 'IMMO', 96]], [['ADEG', 'FKLL', 2], ['BBCI', 'AEEO', 2], ['BDKO', 'CEKM', 2], ['CKLM', 'GLMN', 2], ['FHKM', 'AEIP', 2]]]
        
        self.assertEqual(analyze(results, 26, 2), result)
        
    def test_32(self):
        results = [['GFLB', 'DAMK', 69], ['GFEN', 'COPE', 40], ['OLKN', 'HPCC', 58], ['IFAD', 'HECJ', 61], ['EFEP', 'MLDN', 34], ['OMGN', 'GEIB', 6], ['OHHN', 'CLLO', 13], ['CCIM', 'ADFA', 67], ['FJCO', 'JPCD', 22], ['IDHN', 'IGOJ', 36], ['KHLP', 'DMDB', 70], ['GPNE', 'KBMB', 15], ['BJEE', 'IKJH', 33], ['FKFB', 'BNAF', 89], ['BIFN', 'KGHL', 7], ['NDEI', 'BIFD', 94], ['EMIJ', 'NGOD', 8], ['IGEM', 'DBEA', 95], ['JKEC', 'EGLF', 10], ['PAFH', 'GACE', 47], ['DBHO', 'KMAB', 8], ['JDND', 'KFPF', 8], ['LDCN', 'NLKJ', 72], ['LEFG', 'MPPE', 20], ['LKIH', 'AFMG', 92], ['JMGA', 'PEJA', 26], ['KJJA', 'HPIM', 81], ['OIEC', 'MMOI', 96], ['NEEN', 'PGFF', 38], ['LFDA', 'BDHM', 70], ['OCCC', 'EHFC', 96], ['KOIB', 'BJEK', 89], ['KDNP', 'OBEK', 19], ['CMDB', 'GNAA', 62], ['NGDH', 'NAIK', 17], ['EEHA', 'FMCG', 93], ['DKNL', 'IPGN', 29], ['MJDP', 'AFEC', 44], ['KPNF', 'AKBH', 45], ['MCFO', 'POOD', 83], ['LBEC', 'DICB', 34], ['FEFI', 'JDAE', 88], ['AINL', 'DGDJ', 3], ['ALPN', 'KGAK', 66], ['DNMI', 'CMBK', 9], ['OLDC', 'EEHG', 58], ['HMNI', 'CEHN', 48], ['PBHC', 'ADPC', 53], ['HKIK', 'JODD', 59], ['DBOK', 'MEKC', 2], ['IBGJ', 'MBFM', 87], ['BCBA', 'AKDA', 45], ['GFPB', 'AKAH', 76], ['AHCJ', 'ILLJ', 79], ['HNHB', 'DGCL', 83], ['BNDB', 'GDNJ', 82], ['PFGG', 'GKCO', 65], ['OHLE', 'MGDM', 44], ['LGJH', 'EBCC', 31], ['KMCL', 'MNGL', 2], ['LAGA', 'JCNP', 36], ['CEON', 'GFNL', 72], ['FKGB', 'LIHN', 25], ['FIJL', 'KGMP', 63], ['GEOB', 'FFDE', 56], ['FFOO', 'INGI', 69], ['FHKI', 'BGMB', 49], ['MIFF', 'FCOA', 65], ['BNKA', 'LEPF', 92], ['EINN', 'LLDF', 40], ['JEMN', 'MMEP', 75], ['DECF', 'KGMG', 37], ['JCFG', 'JEHC', 49], ['GGFA', 'MMKP', 91], ['BMCM', 'LAOG', 4], ['DEPF', 'HJPH', 70], ['POBI', 'JKND', 5], ['DCHD', 'LKKJ', 52], ['NNFP', 'FOFL', 26], ['LOJB', 'NKPE', 10], ['KOAP', 'ABCK', 26], ['PDKJ', 'JENF', 11], ['LHCI', 'ENMI', 4], ['EBCJ', 'COLG', 73], ['NGCA', 'DDMP', 1], ['EFHN', 'ANBH', 88], ['LFLK', 'AGED', 98], ['JKHI', 'DKND', 47], ['MDLA', 'EOMP', 31], ['KHAJ', 'HIGJ', 15], ['PEAI', 'HMFK', 98], ['NDMH', 'NAJM', 40], ['MCLO', 'JDEC', 43], ['JPBA', 'IGDD', 36], ['EJHM', 'GEPN', 59], ['JAGM', 'IGJL', 86], ['BFNF', 'EHOH', 22], ['BEDK', 'NMAJ', 54], ['FLGK', 'AGKH', 49], ['ICBB', 'EAEO', 2]]

        result = [[['DDMP', 'ACGN', 99], ['AEEO', 'BBCI', 98], ['AEIP', 'FHKM', 98], ['CEKM', 'BDKO', 98], ['FKLL', 'ADEG', 98], ['GLMN', 'CKLM', 98], ['DDGJ', 'AILN', 97], ['AGLO', 'BCMM', 96], ['CCCO', 'CEFH', 96], ['CEIO', 'IMMO', 96]], [['CDLN', 'JKLN', 72], ['CENO', 'FGLN', 72]]]
        
        self.assertEqual(analyze(results, 26, 72), result)
        
    def test_33(self):
        results = [['BAB', 'ABA', 60], ['BAB', 'ABB', 57], ['BAA', 'AAB', 67], ['BBB', 'AAA', 92], 
                    ['BBA', 'BBB', 45], ['ACB', 'BAA', 80], ['ABB', 'ABA', 84], ['BAA', 'BBB', 85], 
                    ['CCB', 'BBB', 77], ['BAA', 'BBA', 64], ['BAB', 'BAA', 56], ['CAA', 'BAB', 87], 
                    ['BBB', 'BAA', 40], ['AAC', 'ABB', 89], ['BAA', 'BAB', 63], ['CBB', 'BBA', 96], 
                    ['CCC', 'AAA', 100], ['BBB', 'AAA', 44], ['BBB', 'BAB', 39], ['CBC', 'AAA', 76],
                    ['BAA', 'AAA', 68], ['ABA', 'BAA', 96], ['ABB', 'ABB', 73], ['BAA', 'ABA', 68], 
                    ['ABB', 'BAA', 72], ['BBA', 'ABA', 52], ['BAA', 'BAA', 64], ['BBB', 'AAB', 43], 
                    ['ABC', 'BBA', 88], ['BCB', 'ABA', 76], ['BBB', 'BBA', 40], ['BBA', 'BAA', 48], 
                    ['BBB', 'ABA', 44], ['AAA', 'BAB', 95], ['BAB', 'AAA', 60], ['AAB', 'AAB', 83], 
                    ['BBB', 'ABB', 41], ['BAA', 'BBB', 61], ['ABB', 'BBB', 69], ['BBB', 'BBB', 37], 
                    ['BCC', 'BBA', 80], ['BCA', 'ABA', 100], ['CAC', 'BBB', 93], ['BAB', 'AAB', 59],
                    ['BAB', 'BAA', 88], ['BAB', 'BAB', 55], ['BBA', 'BAB', 79], ['BAB', 'BBA', 56], 
                    ['CCA', 'AAB', 99], ['BBA', 'BBA', 48], ['BAA', 'ABB', 65], ['BAC', 'ABB', 97], 
                    ['ABB', 'BAB', 71], ['BBC', 'AAB', 75], ['BBA', 'AAA', 52], ['ACC', 'AAB', 91], 
                    ['BBA', 'BAB', 47], ['BAB', 'BBB', 53], ['ABB', 'BBA', 72], ['BBA', 'ABB', 49], 
                    ['CAB', 'AAA', 84], ['CBA', 'ABB', 81], ['ACA', 'ABA', 92], ['BBA', 'AAB', 51]]

        result = [[['ABC', 'AAB', 100], ['CCC', 'AAA', 100], ['ACC', 'AAB', 99], ['ABC', 'ABB', 97], ['AAB', 'AAB', 96], ['BBC', 'ABB', 96],  ['AAA', 'ABB', 95], ['ACC', 'BBB', 93], ['AAC', 'AAB', 92], ['BBB', 'AAA', 92]], [['AAA', 'CCC', 0], ['AAB', 'ABC', 0]]]
        
        self.assertEqual(analyze(results, 3, -1), result)
        
    def test_34(self):
        results = [['BAB', 'ABA', 60], ['BAB', 'ABB', 57], ['BAA', 'AAB', 67], ['BBB', 'AAA', 92], 
                    ['BBA', 'BBB', 45], ['ACB', 'BAA', 80], ['ABB', 'ABA', 84], ['BAA', 'BBB', 85], 
                    ['CCB', 'BBB', 77], ['BAA', 'BBA', 64], ['BAB', 'BAA', 56], ['CAA', 'BAB', 87], 
                    ['BBB', 'BAA', 40], ['AAC', 'ABB', 89], ['BAA', 'BAB', 63], ['CBB', 'BBA', 96], 
                    ['CCC', 'AAA', 100], ['BBB', 'AAA', 44], ['BBB', 'BAB', 39], ['CBC', 'AAA', 76],
                    ['BAA', 'AAA', 68], ['ABA', 'BAA', 96], ['ABB', 'ABB', 73], ['BAA', 'ABA', 68], 
                    ['ABB', 'BAA', 72], ['BBA', 'ABA', 52], ['BAA', 'BAA', 64], ['BBB', 'AAB', 43], 
                    ['ABC', 'BBA', 88], ['BCB', 'ABA', 76], ['BBB', 'BBA', 40], ['BBA', 'BAA', 48], 
                    ['BBB', 'ABA', 44], ['AAA', 'BAB', 95], ['BAB', 'AAA', 60], ['AAB', 'AAB', 83], 
                    ['BBB', 'ABB', 41], ['BAA', 'BBB', 61], ['ABB', 'BBB', 69], ['BBB', 'BBB', 37], 
                    ['BCC', 'BBA', 80], ['BCA', 'ABA', 100], ['CAC', 'BBB', 93], ['BAB', 'AAB', 59],
                    ['BAB', 'BAA', 88], ['BAB', 'BAB', 55], ['BBA', 'BAB', 79], ['BAB', 'BBA', 56], 
                    ['CCA', 'AAB', 99], ['BBA', 'BBA', 48], ['BAA', 'ABB', 65], ['BAC', 'ABB', 97], 
                    ['ABB', 'BAB', 71], ['BBC', 'AAB', 75], ['BBA', 'AAA', 52], ['ACC', 'AAB', 91], 
                    ['BBA', 'BAB', 47], ['BAB', 'BBB', 53], ['ABB', 'BBA', 72], ['BBA', 'ABB', 49], 
                    ['CAB', 'AAA', 84], ['CBA', 'ABB', 81], ['ACA', 'ABA', 92], ['BBA', 'AAB', 51]]

        result = [[['ABC', 'AAB', 100], ['CCC', 'AAA', 100], ['ACC', 'AAB', 99], ['ABC', 'ABB', 97], ['AAB', 'AAB', 96], ['BBC', 'ABB', 96],  ['AAA', 'ABB', 95], ['ACC', 'BBB', 93], ['AAC', 'AAB', 92], ['BBB', 'AAA', 92]], [['AAA', 'CCC', 0], ['AAB', 'ABC', 0]]]
        
        self.assertEqual(analyze(results, 3, 0), result)

    def test_35(self):
        results = [['BAB', 'ABA', 60], ['BAB', 'ABB', 57], ['BAA', 'AAB', 67], ['BBB', 'AAA', 92], 
                    ['BBA', 'BBB', 45], ['ACB', 'BAA', 80], ['ABB', 'ABA', 84], ['BAA', 'BBB', 85], 
                    ['CCB', 'BBB', 77], ['BAA', 'BBA', 64], ['BAB', 'BAA', 56], ['CAA', 'BAB', 87], 
                    ['BBB', 'BAA', 40], ['AAC', 'ABB', 89], ['BAA', 'BAB', 63], ['CBB', 'BBA', 96], 
                    ['CCC', 'AAA', 100], ['BBB', 'AAA', 44], ['BBB', 'BAB', 39], ['CBC', 'AAA', 76],
                    ['BAA', 'AAA', 68], ['ABA', 'BAA', 96], ['ABB', 'ABB', 73], ['BAA', 'ABA', 68], 
                    ['ABB', 'BAA', 72], ['BBA', 'ABA', 52], ['BAA', 'BAA', 64], ['BBB', 'AAB', 43], 
                    ['ABC', 'BBA', 88], ['BCB', 'ABA', 76], ['BBB', 'BBA', 40], ['BBA', 'BAA', 48], 
                    ['BBB', 'ABA', 44], ['AAA', 'BAB', 95], ['BAB', 'AAA', 60], ['AAB', 'AAB', 83], 
                    ['BBB', 'ABB', 41], ['BAA', 'BBB', 61], ['ABB', 'BBB', 69], ['BBB', 'BBB', 37], 
                    ['BCC', 'BBA', 80], ['BCA', 'ABA', 100], ['CAC', 'BBB', 93], ['BAB', 'AAB', 59],
                    ['BAB', 'BAA', 88], ['BAB', 'BAB', 55], ['BBA', 'BAB', 79], ['BAB', 'BBA', 56], 
                    ['CCA', 'AAB', 99], ['BBA', 'BBA', 48], ['BAA', 'ABB', 65], ['BAC', 'ABB', 97], 
                    ['ABB', 'BAB', 71], ['BBC', 'AAB', 75], ['BBA', 'AAA', 52], ['ACC', 'AAB', 91], 
                    ['BBA', 'BAB', 47], ['BAB', 'BBB', 53], ['ABB', 'BBA', 72], ['BBA', 'ABB', 49], 
                    ['CAB', 'AAA', 84], ['CBA', 'ABB', 81], ['ACA', 'ABA', 92], ['BBA', 'AAB', 51]]

        result = [[['ABC', 'AAB', 100], ['CCC', 'AAA', 100], ['ACC', 'AAB', 99], ['ABC', 'ABB', 97], ['AAB', 'AAB', 96], ['BBC', 'ABB', 96],  ['AAA', 'ABB', 95], ['ACC', 'BBB', 93], ['AAC', 'AAB', 92], ['BBB', 'AAA', 92]], [['BBB', 'ACC', 7]]]
        
        self.assertEqual(analyze(results, 3, 6), result)

    def test_36(self):
        results = [['BAB', 'ABA', 60], ['BAB', 'ABB', 57], ['BAA', 'AAB', 67], ['BBB', 'AAA', 92], 
                    ['BBA', 'BBB', 45], ['ACB', 'BAA', 80], ['ABB', 'ABA', 84], ['BAA', 'BBB', 85], 
                    ['CCB', 'BBB', 77], ['BAA', 'BBA', 64], ['BAB', 'BAA', 56], ['CAA', 'BAB', 87], 
                    ['BBB', 'BAA', 40], ['AAC', 'ABB', 89], ['BAA', 'BAB', 63], ['CBB', 'BBA', 96], 
                    ['CCC', 'AAA', 100], ['BBB', 'AAA', 44], ['BBB', 'BAB', 39], ['CBC', 'AAA', 76],
                    ['BAA', 'AAA', 68], ['ABA', 'BAA', 96], ['ABB', 'ABB', 73], ['BAA', 'ABA', 68], 
                    ['ABB', 'BAA', 72], ['BBA', 'ABA', 52], ['BAA', 'BAA', 64], ['BBB', 'AAB', 43], 
                    ['ABC', 'BBA', 88], ['BCB', 'ABA', 76], ['BBB', 'BBA', 40], ['BBA', 'BAA', 48], 
                    ['BBB', 'ABA', 44], ['AAA', 'BAB', 95], ['BAB', 'AAA', 60], ['AAB', 'AAB', 83], 
                    ['BBB', 'ABB', 41], ['BAA', 'BBB', 61], ['ABB', 'BBB', 69], ['BBB', 'BBB', 37], 
                    ['BCC', 'BBA', 80], ['BCA', 'ABA', 100], ['CAC', 'BBB', 93], ['BAB', 'AAB', 59],
                    ['BAB', 'BAA', 88], ['BAB', 'BAB', 55], ['BBA', 'BAB', 79], ['BAB', 'BBA', 56], 
                    ['CCA', 'AAB', 99], ['BBA', 'BBA', 48], ['BAA', 'ABB', 65], ['BAC', 'ABB', 97], 
                    ['ABB', 'BAB', 71], ['BBC', 'AAB', 75], ['BBA', 'AAA', 52], ['ACC', 'AAB', 91], 
                    ['BBA', 'BAB', 47], ['BAB', 'BBB', 53], ['ABB', 'BBA', 72], ['BBA', 'ABB', 49], 
                    ['CAB', 'AAA', 84], ['CBA', 'ABB', 81], ['ACA', 'ABA', 92], ['BBA', 'AAB', 51]]

        result = [[['ABC', 'AAB', 100], ['CCC', 'AAA', 100], ['ACC', 'AAB', 99], ['ABC', 'ABB', 97], ['AAB', 'AAB', 96], ['BBC', 'ABB', 96],  ['AAA', 'ABB', 95], ['ACC', 'BBB', 93], ['AAC', 'AAB', 92], ['BBB', 'AAA', 92]], [['AAB', 'ABB', 49], ['ABB', 'ABB', 49]]]
        
        self.assertEqual(analyze(results, 3, 49), result)
        
    def test_37(self):
        results = [['BAB', 'ABA', 60], ['BAB', 'ABB', 57], ['BAA', 'AAB', 67], ['BBB', 'AAA', 92], 
                    ['BBA', 'BBB', 45], ['ACB', 'BAA', 80], ['ABB', 'ABA', 84], ['BAA', 'BBB', 85], 
                    ['CCB', 'BBB', 77], ['BAA', 'BBA', 64], ['BAB', 'BAA', 56], ['CAA', 'BAB', 87], 
                    ['BBB', 'BAA', 40], ['AAC', 'ABB', 89], ['BAA', 'BAB', 63], ['CBB', 'BBA', 96], 
                    ['CCC', 'AAA', 100], ['BBB', 'AAA', 44], ['BBB', 'BAB', 39], ['CBC', 'AAA', 76],
                    ['BAA', 'AAA', 68], ['ABA', 'BAA', 96], ['ABB', 'ABB', 73], ['BAA', 'ABA', 68], 
                    ['ABB', 'BAA', 72], ['BBA', 'ABA', 52], ['BAA', 'BAA', 64], ['BBB', 'AAB', 43], 
                    ['ABC', 'BBA', 88], ['BCB', 'ABA', 76], ['BBB', 'BBA', 40], ['BBA', 'BAA', 48], 
                    ['BBB', 'ABA', 44], ['AAA', 'BAB', 95], ['BAB', 'AAA', 60], ['AAB', 'AAB', 83], 
                    ['BBB', 'ABB', 41], ['BAA', 'BBB', 61], ['ABB', 'BBB', 69], ['BBB', 'BBB', 37], 
                    ['BCC', 'BBA', 80], ['BCA', 'ABA', 100], ['CAC', 'BBB', 93], ['BAB', 'AAB', 59],
                    ['BAB', 'BAA', 88], ['BAB', 'BAB', 55], ['BBA', 'BAB', 79], ['BAB', 'BBA', 56], 
                    ['CCA', 'AAB', 99], ['BBA', 'BBA', 48], ['BAA', 'ABB', 65], ['BAC', 'ABB', 97], 
                    ['ABB', 'BAB', 71], ['BBC', 'AAB', 75], ['BBA', 'AAA', 52], ['ACC', 'AAB', 91], 
                    ['BBA', 'BAB', 47], ['BAB', 'BBB', 53], ['ABB', 'BBA', 72], ['BBA', 'ABB', 49], 
                    ['CAB', 'AAA', 84], ['CBA', 'ABB', 81], ['ACA', 'ABA', 92], ['BBA', 'AAB', 51]]

        result = [[['ABC', 'AAB', 100], ['CCC', 'AAA', 100], ['ACC', 'AAB', 99], ['ABC', 'ABB', 97], ['AAB', 'AAB', 96], ['BBC', 'ABB', 96],  ['AAA', 'ABB', 95], ['ACC', 'BBB', 93], ['AAC', 'AAB', 92], ['BBB', 'AAA', 92]], [['AAB', 'ABB', 52], ['ABB', 'AAA', 52], ['ABB', 'AAB', 52], ['ABB', 'ABB', 52]]]
        
        self.assertEqual(analyze(results, 3, 52), result)
        
    def test_38(self):
        results = [['BAB', 'ABA', 60], ['BAB', 'ABB', 57], ['BAA', 'AAB', 67], ['BBB', 'AAA', 92], 
                    ['BBA', 'BBB', 45], ['ACB', 'BAA', 80], ['ABB', 'ABA', 84], ['BAA', 'BBB', 85], 
                    ['CCB', 'BBB', 77], ['BAA', 'BBA', 64], ['BAB', 'BAA', 56], ['CAA', 'BAB', 87], 
                    ['BBB', 'BAA', 40], ['AAC', 'ABB', 89], ['BAA', 'BAB', 63], ['CBB', 'BBA', 96], 
                    ['CCC', 'AAA', 100], ['BBB', 'AAA', 44], ['BBB', 'BAB', 39], ['CBC', 'AAA', 76],
                    ['BAA', 'AAA', 68], ['ABA', 'BAA', 96], ['ABB', 'ABB', 73], ['BAA', 'ABA', 68], 
                    ['ABB', 'BAA', 72], ['BBA', 'ABA', 52], ['BAA', 'BAA', 64], ['BBB', 'AAB', 43], 
                    ['ABC', 'BBA', 88], ['BCB', 'ABA', 76], ['BBB', 'BBA', 40], ['BBA', 'BAA', 48], 
                    ['BBB', 'ABA', 44], ['AAA', 'BAB', 95], ['BAB', 'AAA', 60], ['AAB', 'AAB', 83], 
                    ['BBB', 'ABB', 41], ['BAA', 'BBB', 61], ['ABB', 'BBB', 69], ['BBB', 'BBB', 37], 
                    ['BCC', 'BBA', 80], ['BCA', 'ABA', 100], ['CAC', 'BBB', 93], ['BAB', 'AAB', 59],
                    ['BAB', 'BAA', 88], ['BAB', 'BAB', 55], ['BBA', 'BAB', 79], ['BAB', 'BBA', 56], 
                    ['CCA', 'AAB', 99], ['BBA', 'BBA', 48], ['BAA', 'ABB', 65], ['BAC', 'ABB', 97], 
                    ['ABB', 'BAB', 71], ['BBC', 'AAB', 75], ['BBA', 'AAA', 52], ['ACC', 'AAB', 91], 
                    ['BBA', 'BAB', 47], ['BAB', 'BBB', 53], ['ABB', 'BBA', 72], ['BBA', 'ABB', 49], 
                    ['CAB', 'AAA', 84], ['CBA', 'ABB', 81], ['ACA', 'ABA', 92], ['BBA', 'AAB', 51]]

        result = [[['ABC', 'AAB', 100], ['CCC', 'AAA', 100], ['ACC', 'AAB', 99], ['ABC', 'ABB', 97], ['AAB', 'AAB', 96], ['BBC', 'ABB', 96],  ['AAA', 'ABB', 95], ['ACC', 'BBB', 93], ['AAC', 'AAB', 92], ['BBB', 'AAA', 92]], [['ABC', 'AAB', 100], ['CCC', 'AAA', 100]]]
        
        self.assertEqual(analyze(results, 3, 100), result)
        
    def test_39(self):
        results = [['BAB', 'ABA', 60], ['BAB', 'ABB', 57], ['BAA', 'AAB', 67], ['BBB', 'AAA', 92], 
                    ['BBA', 'BBB', 45], ['ACB', 'BAA', 80], ['ABB', 'ABA', 84], ['BAA', 'BBB', 85], 
                    ['CCB', 'BBB', 77], ['BAA', 'BBA', 64], ['BAB', 'BAA', 56], ['CAA', 'BAB', 87], 
                    ['BBB', 'BAA', 40], ['AAC', 'ABB', 89], ['BAA', 'BAB', 63], ['CBB', 'BBA', 96], 
                    ['CCC', 'AAA', 100], ['BBB', 'AAA', 44], ['BBB', 'BAB', 39], ['CBC', 'AAA', 76],
                    ['BAA', 'AAA', 68], ['ABA', 'BAA', 96], ['ABB', 'ABB', 73], ['BAA', 'ABA', 68], 
                    ['ABB', 'BAA', 72], ['BBA', 'ABA', 52], ['BAA', 'BAA', 64], ['BBB', 'AAB', 43], 
                    ['ABC', 'BBA', 88], ['BCB', 'ABA', 76], ['BBB', 'BBA', 40], ['BBA', 'BAA', 48], 
                    ['BBB', 'ABA', 44], ['AAA', 'BAB', 95], ['BAB', 'AAA', 60], ['AAB', 'AAB', 83], 
                    ['BBB', 'ABB', 41], ['BAA', 'BBB', 61], ['ABB', 'BBB', 69], ['BBB', 'BBB', 37], 
                    ['BCC', 'BBA', 80], ['BCA', 'ABA', 100], ['CAC', 'BBB', 93], ['BAB', 'AAB', 59],
                    ['BAB', 'BAA', 88], ['BAB', 'BAB', 55], ['BBA', 'BAB', 79], ['BAB', 'BBA', 56], 
                    ['CCA', 'AAB', 99], ['BBA', 'BBA', 48], ['BAA', 'ABB', 65], ['BAC', 'ABB', 97], 
                    ['ABB', 'BAB', 71], ['BBC', 'AAB', 75], ['BBA', 'AAA', 52], ['ACC', 'AAB', 91], 
                    ['BBA', 'BAB', 47], ['BAB', 'BBB', 53], ['ABB', 'BBA', 72], ['BBA', 'ABB', 49], 
                    ['CAB', 'AAA', 84], ['CBA', 'ABB', 81], ['ACA', 'ABA', 92], ['BBA', 'AAB', 51]]

        result = [[['ABC', 'AAB', 100], ['CCC', 'AAA', 100], ['ACC', 'AAB', 99], ['ABC', 'ABB', 97], ['AAB', 'AAB', 96], ['BBC', 'ABB', 96],  ['AAA', 'ABB', 95], ['ACC', 'BBB', 93], ['AAC', 'AAB', 92], ['BBB', 'AAA', 92]], []]
        
        self.assertEqual(analyze(results, 3, 101), result)
    
    
    def test_40(self):
        results = [['ZVJUKWHPNIQO', 'BRJCVKEMTRKU', 63], ['YIQJXUCATBIY', 'GOEBKTNEQOXU', 39], ['MHUVYBQSAQLC', 'NTNKUQYWYMIV', 58], ['YTVHOGSGFHQK', 'KLDMPPXWRVXK', 39], ['QYJZIZLVZBJR', 'HHRFSLDRCYBR', 66], ['NABGULQKKPSC', 'MYARMIMWUPQI', 33], ['MQEFHYWEQEQF', 'SKWTRINZKNHZ', 56], ['CFVLWYEPIHTD', 'VNVMOTETFNZS', 97], ['LUYFGOTQDNUW', 'LNOTZYAMBJDY', 15], ['AXLIHDJFQCND', 'SKAHGGPLJQDW', 26], ['XBAAGNTXAIKR', 'THCSSZBZUENU', 77], ['CHRKLIGSILMJ', 'DAIZUYKLLWRF', 48], ['SOXUJJGBOMOL', 'GMPUWAUQISEV', 74], ['BPYNVMYYQQRC', 'ALOAEDBOCYKS', 76], ['NFLVFKOJSKRO', 'LXOJVBXVZOZK', 16], ['PPVCXTPBMAEL', 'ZHFMTHBQFHXS', 76], ['ZKGHDFGCWFRG', 'SUTCSDSIFJTK', 88], ['OYVFIGWMZOWI', 'YGECHBKNYUWR', 44], ['KNXDGJJMKKPA', 'NGWWWPFNVXQM', 74], ['GABAUOHHKISI', 'WQCTSYPTQOAO', 46], ['MWYGNZAZUGKW', 'HICKBOFGUBBU', 81], ['IPLPYFHHDKCQ', 'YILGAMWIXWLS', 29], ['FKYXDSJIWQWX', 'XGOSDDUZJRAX', 8], ['PTICQYGEBHIH', 'WNXOHQMVOFSQ', 51], ['SVTGRKABFLVT', 'YQDMWUHWPTQW', 24], ['IRMMHZESILHY', 'HISSLSKXZQYI', 51], ['HLPQTTWPZQHH', 'LNWBQTBBXFYR', 47], ['BZMCBVIQMTRD', 'RXOFFOLYCNCW', 94], ['MHVWDCDUYNDG', 'PPUZPAUKVECW', 47], ['NCKGDMIOUCFA', 'AUEKROBRPTOS', 59], ['WNBNPIVCHGMR', 'ENLHLBAAYOJY', 93], ['WMKTQJWKKFDX', 'IIFOLFTGDCBP', 78], ['OIWAFYULUVBA', 'PPXMNMDOHQJY', 29], ['BGPZBTDUEVLY', 'BJZACXREPIEP', 79], ['QZHDRHLREVZF', 'YTQKJWOMDSBK', 0], ['YFHFNWUMQTXO', 'JUIIRSDRKZVG', 64], ['YTBJVGNBIANK', 'ZZWGRLMLTFQK', 6], ['FJZKABDMBXQR', 'XWHMHSEWPVUI', 9], ['RLTMZFUMVPFD', 'SAPFUDVUXMWN', 12], ['RBFMNUDAFXQT', 'RSFCBRKAAXTK', 60], ['DFDZJAYUBNIY', 'QAKYJQNDVSFJ', 0], ['AIUDHAIJMOUZ', 'NVEFIMYYMGYK', 19], ['JKNOADVQUTZY', 'AMDZPGUVRXAO', 14], ['RWZGJXAGRZIB', 'FHXYNYLTPCDJ', 21], ['RIMHNHUDCHYE', 'YVFOYMXOMPWL', 70], ['OTDPYQXTRZPY', 'LGECGEVJRRCB', 11], ['NACUFYQRJKBG', 'XVWKPSNJJFIM', 95], ['FDTBYTDUSOGQ', 'ZGKXDRSFIWLI', 32], ['BBFPVZINOPQH', 'DIJULBSCJMGR', 40], ['PBTBHRWXXADT', 'NRNIHRQDAHWD', 68], ['LUVBIWYQDHUM', 'OMZKEPTSFFFT', 72], ['UBATNOWFHMNP', 'GNGHHBDMOMSS', 43], ['QAZVAHCKMBTT', 'KWIIUHIWYRLM', 45], ['AKJVIHICULQT', 'OUOMMNQYMQVL', 55], ['GTEKJMWYQTEG', 'HKYVMPNPNTOX', 3], ['BXYSZCOUZAYK', 'RXGQIBOPRALN', 17], ['VZPSHAYQBAYJ', 'DAZENTPOGGLP', 91], ['EIPVUJZPSSWW', 'LLCAEBHPCIFM', 18], ['YHOBYPDCVDRF', 'IZDKIUXPZYAF', 90], ['OTPWEYCKGWCF', 'ZPRLOMKQEFIH', 52], ['OSPAVMUOOHCC', 'CYKDYDZNFBSY', 51], ['RWQSGDJSXABZ', 'PRYRYLWEVLPA', 13], ['YTDIZCYNYDMH', 'JRVZAPAJJAJR', 32], ['CDPZWKHBUJHN', 'VWLROBUEHZGZ', 67], ['KBWEVADGOVBJ', 'LJDEZUFSAXUX', 38], ['IFRNHGUUCCVP', 'UQWVTEUMTRXJ', 55], ['NIXPFMTBOTQD', 'JHGONFJBUBRS', 19], ['TDVPBBEYIRUT', 'CJBVVHEKSMPN', 56], ['PKGUXCSPOJIY', 'RRZPXELGRUOY', 34], ['OCIQLOBFSBBV', 'ZDZDCDDKFJPI', 97], ['ARZKETUFBBSJ', 'LPACWUGWHHXR', 14], ['VMCCGGFFCNHL', 'KDQKZCXEZXKV', 48], ['AFMZATESMICM', 'YRBBLDBRKIBG', 20], ['EXCIFGHIIIYW', 'TLATBFPWSUOY', 64], ['XMNYYPFSVXTV', 'TQUCEWLXSXPF', 36], ['JOWOIHWLSBSU', 'OFPCBACEAFLZ', 91], ['XGJNWDAZNQBS', 'JLACETXZZFGC', 48], ['BOANPTJMQYSX', 'VHIZOYILVBQO', 74], ['VGYBNQECUPEO', 'RABRJTMZGBFZ', 40], ['OAYGMXISJXWN', 'FUXYIJEZIAOK', 81], ['KDQXAPPLQLYH', 'AHNKYNEAGJAE', 5], ['EFXJEEAWXKFM', 'XMQLCIMRECNC', 53], ['TQRAWTGOWJAD', 'LEREHCJKZWOW', 37], ['PDMDWVNCRSET', 'PFORZIONAEGN', 86], ['EJSLEVABTAOW', 'TRERGQLWOTFV', 49], ['JDSKXIVTLQZS', 'VSEUXFTKEUVE', 63], ['ZWCUCUFPOUFR', 'CXLUZQMJINCL', 65], ['JHYRUBTEHPED', 'RUWQCOFYAFUT', 91], ['MJFHURPYVOBI', 'ABYZRFGISGHP', 7], ['HYEWEUDNRVES', 'YXPIPIEMLPFK', 34], ['FOTWRBBNMNAO', 'SRIPDFOAVPWN', 24], ['QUBPNNZYXDTC', 'EDWMRLJJSPWW', 51], ['ALFULLUZZOEZ', 'JSMOKLVIEMPM', 99], ['VGENYRDSSZAT', 'ZGWDOBDQZPEJ', 60], ['EQSRFRDPPHHX', 'FMRZAIKGCIRC', 20], ['ZTQJIKNXWALY', 'ORFLBEOXGQJP', 40], ['ZJRPZWYURGHL', 'JLNQTCDOUXTR', 12], ['TIOLRGSUORMX', 'CVLUSNOWXISR', 84], ['JIDEXUNBJCGP', 'UOCAHXYEPOGG', 92], ['OLALVLCSFSOE', 'YZTLJJQOXLFY', 27], ['PSEEIUELNNDT', 'JNHFOVHHTCUX', 93], ['XDZOGZVXUJTC', 'QGSCUBNUVVFT', 88], ['WYIMCWRCTCWH', 'AWIPZLCCEBCO', 26], ['MUYMPOAIIAWF', 'VUCVZMFXRNJD', 63], ['DRYASDRMEQIB', 'DVMVOQLZBRDN', 80], ['XULOEINLHWCP', 'PAPQYCJROHQJ', 86], ['FTMOXXOFFHGL', 'ZFLTESOYUFJO', 16], ['USDEKGIOUXQM', 'YNCMEJTXOGUM', 49], ['RFSMPQGIMUEL', 'QIKNHJAOGIRS', 30], ['YIUQGDTHJNXD', 'JJILUWKIGDJT', 47], ['IZUBECJNGOZB', 'JRZKKKOQZNXM', 64], ['AVKNGKGRHMPU', 'EKHFXQZJSOVG', 30], ['KOIEPBAUZYZB', 'XIDDPKYZVCHC', 82], ['QDZKPZWTCIHE', 'ILSCHPEGGFQT', 83], ['NNSEHTVORIKF', 'YPJIWWXHQIXE', 28], ['JUQFMHNKTOXL', 'UQILUJDHRYVC', 25], ['LHZZWWIYJOQX', 'ZTXEQXPLZIIY', 82], ['MLHOCNBGZFPN', 'WSUKNZZVULEY', 75], ['IPRIJBWJNDLA', 'DLQPCMJGQOOJ', 38], ['WOKUNBQGBMZA', 'XQFWTTFUORFB', 43], ['UGMWZVZAVVBS', 'WZVWEZXFFKXP', 12], ['MLDFTBNIOGYD', 'QQFSLOOOXKSN', 88], ['XCQKBAWZRKOF', 'IGBVSIXJHVEX', 44], ['QSEUPFOGOYSE', 'JQTDLAUVFLFA', 35], ['ZXDNYLCQPKKT', 'EOCNQEVWESMJ', 87], ['YJFEXXCSRXCS', 'MXJKZBRWOWKF', 59], ['GDXQIVFTCCKO', 'EUZLCEOCBOWR', 20], ['NDSAEWFLAFXH', 'NJMSNTZVVGVQ', 75], ['UGLAJTODYOUO', 'DHOHAEBOCRZD', 91], ['XEXVTTIHKROW', 'LWGJMWICFYGF', 91], ['JYDUTEPDRNCC', 'BQIQZRDVMPRU', 89], ['DRNTIKRELSHE', 'QRSYTIGRAINQ', 75], ['MALRDSBKORZG', 'QFVKPCFGVTPA', 26], ['PETLEOFDBZWH', 'FTRRUKQSCEOS', 27], ['VKNRYELHCUAG', 'PEVMRPGIOJOK', 20], ['MZHLEZOJTUWQ', 'CIPFVXTRXAPH', 43], ['PJJKWPRCOEKI', 'XADTFXXHEKRI', 80], ['RHWURHROGOWY', 'XHQIVCBMNYVS', 96], ['XRANUHKYWXYE', 'TYYGMFWXUVCW', 80], ['TZHLYSADSXYR', 'YCKSMCXEDZJT', 56], ['JWUGJCUYPMDY', 'OQRTKBPEEYZV', 44], ['HXEMIAWIWRFG', 'DXURSCEZQWEG', 75], ['ZXVCXJRCRYEW', 'DEEXOKUAQBCS', 79], ['DAGEKGVKUBSS', 'DORQRHMCFALM', 27], ['AOWNHNHVPAEV', 'PLORKAPBSHBO', 29], ['OASCAWUDMPYU', 'CAYMUKJZZNHI', 17], ['INSNPQZRIVNF', 'HGIMUAABFQLL', 96], ['QXQZATGRXNRO', 'SNOVHLHPWHHI', 17], ['WQSCSAQFHZMC', 'XUYEPZEGYKVM', 85], ['VAZKGFMJLHVA', 'AFFPZQARTBXY', 25], ['EXZKVFDJPSNW', 'TMODETZRFHSZ', 39], ['DKBAVHDSHYGP', 'LODBCMPVGWCO', 55], ['YSAYBCTQTJTI', 'AOTLCUDEQADK', 44], ['INLTVBNZFXRJ', 'RPOTFECPDQDD', 61], ['AHILJJIDTIDB', 'MHCQPHMCSSOZ', 77], ['XUUDZKURKMKP', 'BMUATKHQUCCZ', 94], ['ATHVASPCLCNM', 'QZSGVKCRJCCM', 83], ['WMSEQIOLXAFF', 'LVKHUNSKZFLI', 34], ['OOPCXYPNPJGP', 'YWUMMTSSDDJO', 83], ['KAZZTFDIAZLV', 'UFBKUMAVSFDT', 64], ['IADDKCJCLNVY', 'GDZHQZRZPHMG', 61], ['KEIDIFMUNPKU', 'DAZXEGUMLBRH', 54], ['IRZIQMFIQQTS', 'JYNGYRESTLDN', 33], ['VNDOEZQPAMPR', 'XUWVJPJRBZGT', 87], ['DKHUAKBFXVHW', 'PHZYCBWZLMQN', 91], ['KBFXTXXTEZTJ', 'PFBUIZZZASSP', 24], ['QPPWLGBHWOZJ', 'YYBFQZOFUREF', 41], ['WJKOZGBFREDI', 'XCNZYKNTIKJX', 12], ['JBYKRECCKOTQ', 'TTADHSPCHGIC', 61], ['YZDCTAHATJIM', 'TLOMOPFGGGTL', 56], ['QBKFDHRHREEC', 'FKGZFTZMKUHD', 20], ['PHCPBWKJCZSY', 'HTCKFHMBRISG', 54], ['VJUYETWQNZTU', 'ABOMMEYJJPDH', 29], ['BGRUTYSNBFMO', 'KSMYQWZNPKYF', 40], ['YVQQYQCUCPQF', 'PRXEJXRZBOXF', 22], ['EZNKHWKAORVA', 'DOSMAUKTZANY', 97], ['JZKSPKZTSPHQ', 'SMPTXRCXKTUU', 92], ['EMDLPRWYDRFF', 'RHRTJNNHKUFY', 62], ['BDXGAKKBNIKP', 'LTSKARDJKEXM', 27], ['AQKDGWNWKQLI', 'FHGUSFDCCFRF', 60], ['BKHUYGIWOOWK', 'HQOIGDLMNRMP', 70], ['XPUXMXPYCMAE', 'OTDYUKQESXMJ', 84], ['PVPBFDSSJJIW', 'NGQUFBJRSGDS', 23], ['KQWMRVTKVDKD', 'CREYZUNQGRDP', 14], ['MEBCNCWHFVLR', 'SQCFMQFOYBBG', 96], ['VQMQHHBGCSPK', 'FBIPFKRACFZA', 62], ['RKTEZERYVOCV', 'MOGMHRDSVHHW', 66], ['NSOTWGHPXPZS', 'JXQOWYKVIUTU', 44], ['NEEQAVOGSPXL', 'DQSAKMCMCLXK', 47], ['GSTVFRZOTGZU', 'RNVZWJLJNUKX', 21], ['RPALLVBJTXTP', 'ESTPLPLVZMZX', 62], ['ZDMWXVOFOQFU', 'XGBFTMXMZWWX', 12], ['QRISGPZADVPZ', 'ISIJEGJKVVEM', 64], ['LXUCXORRWWJF', 'BNUGSBZLJWUN', 24], ['PQNPFSNQFEZL', 'VOAMJAZQYVLM', 64], ['XDPCTAJFYGOF', 'ALDCHSWOHEBO', 71], ['TYVLIQODJMWJ', 'RELFFIYRIYAO', 66], ['EXVXEONOPKCY', 'COPRUNMWCXIV', 0], ['EENOUAXSMYUW', 'EVFNDLFJTDXU', 40], ['DTZMYGMAREYS', 'GLCLSZUVLBAF', 37], ['QGGPIZEVBVNY', 'KNFKEJQMHZKF', 2], ['QZCAINSSYWGH', 'MOMJLYDDGAWU', 47], ['PDYWQMRVTLAS', 'TJGGNJVQJRHY', 64], ['EVDLZUWFWRSJ', 'WDUFNRLEOFCO', 62], ['OMOCWGWYDFRF', 'PKUAMTMHMTUS', 26], ['XHCFQWRXSABR', 'DIAQJWBGMXXA', 64], ['FWNFPYZXSKIC', 'TGVVVQAQLAFR', 14], ['YUYQBIHFIUPH', 'RCJZQCANMNUW', 41], ['CZHFAJJMFTRK', 'OEDRIRAEOQIO', 90], ['XFJBNEJMILXP', 'PPLOCJPZFUPO', 85], ['ONJPZZWCJZMN', 'EROACCLBTFRT', 55], ['BWSPJPUXIDPJ', 'UIRFUUZCIKFS', 74], ['VNWNOCNHLKKZ', 'IXPCFZFWOYXK', 93], ['PMGSDDSTWWLF', 'FAELUNYMJBSQ', 44], ['VRKNNQCCNFZJ', 'RSIJMRLTVPPE', 42], ['RYVJGEQJXYGN', 'QJWXNJNBLZYM', 79], ['WLEOAQHSIOOD', 'LEWJRPLLGUST', 68], ['VBTQXEPWPQRH', 'JCDGHAWUHMXM', 22], ['FWCDQIBPTNVT', 'AMMYXKCLVEDK', 42], ['PRYIUYGUOOJW', 'KVRKUMLTSIVK', 65], ['DTIXJVKCMSUO', 'ATOHXUZTQJVC', 44], ['AEHMIBTJALBY', 'BTPOPXBLCUQG', 83], ['UUULFVDLTOTQ', 'KJAAJBPNDYWO', 21], ['SUSAWWEQCTZO', 'GSDQVWBAHESZ', 56], ['EEKFAHRPAJWV', 'MWCPISRXTUXQ', 92], ['PJGGGANUJUUS', 'VHPCHCKOJLZM', 82], ['LPALKRMGZHNV', 'UVOFJMHGHDZW', 77], ['DGWINEOBFQEY', 'RXWNSTZDULIK', 95], ['XKRWJFWRKJLK', 'SWOARSWGNYOD', 9], ['JGAZTICEQXRQ', 'AZUFYWQLDUTI', 3], ['GOJQESZSQOTL', 'BVKUZVMZOWNW', 80], ['YRWIGZHBEOXU', 'JGCURNPNQYUL', 37], ['VUXKHVIDSSHM', 'ZCBVRHAEYBYO', 37], ['RFTCNHTLJPTQ', 'FRPOUKZSPFML', 42], ['CQSUDPPCXZBS', 'EGQKQTYHQLPU', 61], ['ZKAIWRMITYDK', 'YBPMZNUTTRSB', 41], ['VLKVYMAJJXNW', 'QXXNYZENZBSI', 12], ['XAJVPBEMJKIE', 'WNUOESCDBOFH', 46], ['MOPXQDNCQLJN', 'EFGPOOEIUYWI', 76], ['CDZAYGSUGLSF', 'RJNONOJLGWTE', 23], ['SVDVVNUEGFZO', 'JKTKAYKCZEJV', 59], ['BPVZEYAYTCND', 'VSSTIKPKJGWA', 88], ['UIJWHIRZJJPH', 'FDZROLKLUUTU', 1], ['JEJWUUDSRDYB', 'WLOYXLSMWWWP', 82], ['XJKLUFLNJHMB', 'SEJHHADSFCAV', 35], ['TNAUMQXVAIKG', 'NJHHECVUFSXP', 5], ['TEXQZHMRIBJJ', 'LTIKLHFCIYDG', 70], ['IFWDVELUZJPT', 'TKMJDTHNUUMV', 16], ['JSWSVFIMEGJD', 'NEVAWFETYEPX', 1], ['TYETFFHVMSRH', 'ZNPUIMFMJFOQ', 96], ['CYESZGQGULJX', 'OLYURDBNRLZN', 10], ['QQSEBLMUDMMY', 'AIFQGZSPVHFS', 87], ['AKIVOQRVWWHC', 'MGUAFANTFGXO', 96], ['UJYXUCKMLSPE', 'CVSZAWBZGJOE', 73], ['FFYLWNJUWAOG', 'LQFOEYORIGIX', 94], ['YTBRHSVOAFAN', 'OKSGIBWGINWG', 47], ['LBYBYNEZFSWC', 'RYWUXXXUDKFV', 71], ['NVQIRYUAMRPA', 'UMBBRXSEFLFJ', 76], ['YGMKAAXWEGDO', 'MGWBEVNKLNDU', 60], ['PJSXEWSUTMWY', 'GQLXDDDJSTZX', 14], ['PXEWJFZNYFZD', 'OFGIYIPCNZOV', 88], ['XMNNWJFKDNNY', 'OHWWGGUEMLEL', 86], ['YCTAFKDICTYS', 'MYOLGZAUHCSX', 50], ['CHNVVCCZDPMH', 'HWLTUIEGLYVF', 24], ['OTKWBBGJSNPA', 'QBGIVIBVWJMY', 66], ['QTBOBWNEWWFN', 'JWSSSABAZKUH', 27], ['FTZBRTFCSFDW', 'QZPPBZVFKGND', 22], ['FTZFMYEXLUSI', 'XXZOEGEEWMUV', 4], ['XFLWCIAHWDCS', 'RHLFOMQHJGGT', 56], ['ONMSFTVWORGY', 'QUZXHQBVNHPD', 34], ['YZNELIDKXOKZ', 'QQGNUMCCVVHX', 51], ['HILZQSLFQLOW', 'EHUKYRQBKXMM', 81], ['UZISCTZBQYJZ', 'LUIEUOCGBHQS', 7], ['CWOSNKCMWGWG', 'XZINXKTIQMHT', 89], ['LLAMJWCBKQLZ', 'LDWVFXHIHOBQ', 9], ['GCRWLKALQVIV', 'WDUBOLURXDZU', 61], ['FEOCEWYGSVMD', 'YTWRLUKXMTMI', 79], ['JJRBJLLDKQDY', 'CYQHREFHOMUY', 90], ['EPTNQCGMILWR', 'ROBKYNKBRGXC', 57], ['SVJUAEUEWBPH', 'SCNXWJTHOBDS', 11], ['SFYELCAPXORD', 'JDLWNTAFDKIZ', 81], ['BUIYPSSYTGPL', 'GBICJNPCGAOZ', 18], ['YDZYQEMSQYFT', 'GTPIDZSFVBQW', 15], ['OFLDJCONONTM', 'HHONUZLAVETD', 18], ['RZCPGDJPWWUC', 'HEHYNTNSMPUI', 44], ['YNKZPLEROAEA', 'KBWRJMTHXXXP', 20], ['SQXVDDSWXKBL', 'XXJHUURDHFRU', 34], ['IXHKUDZRRHQA', 'HWJKXQVHGDKS', 68], ['FAIGFYMXSVZS', 'MSJGYIWHDRIQ', 79], ['RJPVHDDGHHMR', 'SQRYJJGONAVD', 79], ['MWHNSSVDCSEW', 'CUQKAYHEKWMA', 79], ['TUFKJNHDXNRX', 'EOSTNXSFCHCP', 46], ['GMBZEFVYMBSR', 'XPENZFUZNKAA', 56], ['PPVCPIVDIIDM', 'ZUTZETIFWQXG', 67], ['HESHVGPDLWMR', 'FACCACTUGVTL', 5], ['TGXYJLAZJUGH', 'UAXDMQSEQMTA', 49], ['AYJJLCHXWVXX', 'OYCSGZZXWPTK', 39]]

        result = [[['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100], ['AEEEFNPTVWXY', 'DEFGIJJMSSVW', 99], ['AEFLLLOUUZZZ', 'EIJKLMMMOPSV', 99], ['DFKLLORTUUUZ', 'HHIIJJJPRUWZ', 99], ['EFFHJKKKMNQZ', 'BEGGINPQVVYZ', 98], ['AAEHKKNORVWZ', 'AADKMNOSTUYZ', 97], ['ADFILQTUUWYZ', 'ACEGIJQQRTXZ', 97], ['BBBCFILOOQSV', 'CDDDDFIJKPZZ', 97]], [['AGHIIJKNOQRS', 'EFGILMMPQRSU', 70], ['BEHIJJMQRTXZ', 'CDFGHIIKLLTY', 70], ['BGHIKKOOUWWY', 'DGHILMMNOPQR', 70], ['CDEHHHIMNRUY', 'FLMMOOPVWXYY', 70], ['EFGHJKOQSVXZ', 'AGGHKKMNPRUV', 70]]]
        
        self.assertEqual(analyze(results, 26, 69), result)
        
    def test_40(self):
        results = [['ZVJUKWHPNIQO', 'BRJCVKEMTRKU', 63], ['YIQJXUCATBIY', 'GOEBKTNEQOXU', 39], ['MHUVYBQSAQLC', 'NTNKUQYWYMIV', 58], ['YTVHOGSGFHQK', 'KLDMPPXWRVXK', 39], ['QYJZIZLVZBJR', 'HHRFSLDRCYBR', 66], ['NABGULQKKPSC', 'MYARMIMWUPQI', 33], ['MQEFHYWEQEQF', 'SKWTRINZKNHZ', 56], ['CFVLWYEPIHTD', 'VNVMOTETFNZS', 97], ['LUYFGOTQDNUW', 'LNOTZYAMBJDY', 15], ['AXLIHDJFQCND', 'SKAHGGPLJQDW', 26], ['XBAAGNTXAIKR', 'THCSSZBZUENU', 77], ['CHRKLIGSILMJ', 'DAIZUYKLLWRF', 48], ['SOXUJJGBOMOL', 'GMPUWAUQISEV', 74], ['BPYNVMYYQQRC', 'ALOAEDBOCYKS', 76], ['NFLVFKOJSKRO', 'LXOJVBXVZOZK', 16], ['PPVCXTPBMAEL', 'ZHFMTHBQFHXS', 76], ['ZKGHDFGCWFRG', 'SUTCSDSIFJTK', 88], ['OYVFIGWMZOWI', 'YGECHBKNYUWR', 44], ['KNXDGJJMKKPA', 'NGWWWPFNVXQM', 74], ['GABAUOHHKISI', 'WQCTSYPTQOAO', 46], ['MWYGNZAZUGKW', 'HICKBOFGUBBU', 81], ['IPLPYFHHDKCQ', 'YILGAMWIXWLS', 29], ['FKYXDSJIWQWX', 'XGOSDDUZJRAX', 8], ['PTICQYGEBHIH', 'WNXOHQMVOFSQ', 51], ['SVTGRKABFLVT', 'YQDMWUHWPTQW', 24], ['IRMMHZESILHY', 'HISSLSKXZQYI', 51], ['HLPQTTWPZQHH', 'LNWBQTBBXFYR', 47], ['BZMCBVIQMTRD', 'RXOFFOLYCNCW', 94], ['MHVWDCDUYNDG', 'PPUZPAUKVECW', 47], ['NCKGDMIOUCFA', 'AUEKROBRPTOS', 59], ['WNBNPIVCHGMR', 'ENLHLBAAYOJY', 93], ['WMKTQJWKKFDX', 'IIFOLFTGDCBP', 78], ['OIWAFYULUVBA', 'PPXMNMDOHQJY', 29], ['BGPZBTDUEVLY', 'BJZACXREPIEP', 79], ['QZHDRHLREVZF', 'YTQKJWOMDSBK', 0], ['YFHFNWUMQTXO', 'JUIIRSDRKZVG', 64], ['YTBJVGNBIANK', 'ZZWGRLMLTFQK', 6], ['FJZKABDMBXQR', 'XWHMHSEWPVUI', 9], ['RLTMZFUMVPFD', 'SAPFUDVUXMWN', 12], ['RBFMNUDAFXQT', 'RSFCBRKAAXTK', 60], ['DFDZJAYUBNIY', 'QAKYJQNDVSFJ', 0], ['AIUDHAIJMOUZ', 'NVEFIMYYMGYK', 19], ['JKNOADVQUTZY', 'AMDZPGUVRXAO', 14], ['RWZGJXAGRZIB', 'FHXYNYLTPCDJ', 21], ['RIMHNHUDCHYE', 'YVFOYMXOMPWL', 70], ['OTDPYQXTRZPY', 'LGECGEVJRRCB', 11], ['NACUFYQRJKBG', 'XVWKPSNJJFIM', 95], ['FDTBYTDUSOGQ', 'ZGKXDRSFIWLI', 32], ['BBFPVZINOPQH', 'DIJULBSCJMGR', 40], ['PBTBHRWXXADT', 'NRNIHRQDAHWD', 68], ['LUVBIWYQDHUM', 'OMZKEPTSFFFT', 72], ['UBATNOWFHMNP', 'GNGHHBDMOMSS', 43], ['QAZVAHCKMBTT', 'KWIIUHIWYRLM', 45], ['AKJVIHICULQT', 'OUOMMNQYMQVL', 55], ['GTEKJMWYQTEG', 'HKYVMPNPNTOX', 3], ['BXYSZCOUZAYK', 'RXGQIBOPRALN', 17], ['VZPSHAYQBAYJ', 'DAZENTPOGGLP', 91], ['EIPVUJZPSSWW', 'LLCAEBHPCIFM', 18], ['YHOBYPDCVDRF', 'IZDKIUXPZYAF', 90], ['OTPWEYCKGWCF', 'ZPRLOMKQEFIH', 52], ['OSPAVMUOOHCC', 'CYKDYDZNFBSY', 51], ['RWQSGDJSXABZ', 'PRYRYLWEVLPA', 13], ['YTDIZCYNYDMH', 'JRVZAPAJJAJR', 32], ['CDPZWKHBUJHN', 'VWLROBUEHZGZ', 67], ['KBWEVADGOVBJ', 'LJDEZUFSAXUX', 38], ['IFRNHGUUCCVP', 'UQWVTEUMTRXJ', 55], ['NIXPFMTBOTQD', 'JHGONFJBUBRS', 19], ['TDVPBBEYIRUT', 'CJBVVHEKSMPN', 56], ['PKGUXCSPOJIY', 'RRZPXELGRUOY', 34], ['OCIQLOBFSBBV', 'ZDZDCDDKFJPI', 97], ['ARZKETUFBBSJ', 'LPACWUGWHHXR', 14], ['VMCCGGFFCNHL', 'KDQKZCXEZXKV', 48], ['AFMZATESMICM', 'YRBBLDBRKIBG', 20], ['EXCIFGHIIIYW', 'TLATBFPWSUOY', 64], ['XMNYYPFSVXTV', 'TQUCEWLXSXPF', 36], ['JOWOIHWLSBSU', 'OFPCBACEAFLZ', 91], ['XGJNWDAZNQBS', 'JLACETXZZFGC', 48], ['BOANPTJMQYSX', 'VHIZOYILVBQO', 74], ['VGYBNQECUPEO', 'RABRJTMZGBFZ', 40], ['OAYGMXISJXWN', 'FUXYIJEZIAOK', 81], ['KDQXAPPLQLYH', 'AHNKYNEAGJAE', 5], ['EFXJEEAWXKFM', 'XMQLCIMRECNC', 53], ['TQRAWTGOWJAD', 'LEREHCJKZWOW', 37], ['PDMDWVNCRSET', 'PFORZIONAEGN', 86], ['EJSLEVABTAOW', 'TRERGQLWOTFV', 49], ['JDSKXIVTLQZS', 'VSEUXFTKEUVE', 63], ['ZWCUCUFPOUFR', 'CXLUZQMJINCL', 65], ['JHYRUBTEHPED', 'RUWQCOFYAFUT', 91], ['MJFHURPYVOBI', 'ABYZRFGISGHP', 7], ['HYEWEUDNRVES', 'YXPIPIEMLPFK', 34], ['FOTWRBBNMNAO', 'SRIPDFOAVPWN', 24], ['QUBPNNZYXDTC', 'EDWMRLJJSPWW', 51], ['ALFULLUZZOEZ', 'JSMOKLVIEMPM', 99], ['VGENYRDSSZAT', 'ZGWDOBDQZPEJ', 60], ['EQSRFRDPPHHX', 'FMRZAIKGCIRC', 20], ['ZTQJIKNXWALY', 'ORFLBEOXGQJP', 40], ['ZJRPZWYURGHL', 'JLNQTCDOUXTR', 12], ['TIOLRGSUORMX', 'CVLUSNOWXISR', 84], ['JIDEXUNBJCGP', 'UOCAHXYEPOGG', 92], ['OLALVLCSFSOE', 'YZTLJJQOXLFY', 27], ['PSEEIUELNNDT', 'JNHFOVHHTCUX', 93], ['XDZOGZVXUJTC', 'QGSCUBNUVVFT', 88], ['WYIMCWRCTCWH', 'AWIPZLCCEBCO', 26], ['MUYMPOAIIAWF', 'VUCVZMFXRNJD', 63], ['DRYASDRMEQIB', 'DVMVOQLZBRDN', 80], ['XULOEINLHWCP', 'PAPQYCJROHQJ', 86], ['FTMOXXOFFHGL', 'ZFLTESOYUFJO', 16], ['USDEKGIOUXQM', 'YNCMEJTXOGUM', 49], ['RFSMPQGIMUEL', 'QIKNHJAOGIRS', 30], ['YIUQGDTHJNXD', 'JJILUWKIGDJT', 47], ['IZUBECJNGOZB', 'JRZKKKOQZNXM', 64], ['AVKNGKGRHMPU', 'EKHFXQZJSOVG', 30], ['KOIEPBAUZYZB', 'XIDDPKYZVCHC', 82], ['QDZKPZWTCIHE', 'ILSCHPEGGFQT', 83], ['NNSEHTVORIKF', 'YPJIWWXHQIXE', 28], ['JUQFMHNKTOXL', 'UQILUJDHRYVC', 25], ['LHZZWWIYJOQX', 'ZTXEQXPLZIIY', 82], ['MLHOCNBGZFPN', 'WSUKNZZVULEY', 75], ['IPRIJBWJNDLA', 'DLQPCMJGQOOJ', 38], ['WOKUNBQGBMZA', 'XQFWTTFUORFB', 43], ['UGMWZVZAVVBS', 'WZVWEZXFFKXP', 12], ['MLDFTBNIOGYD', 'QQFSLOOOXKSN', 88], ['XCQKBAWZRKOF', 'IGBVSIXJHVEX', 44], ['QSEUPFOGOYSE', 'JQTDLAUVFLFA', 35], ['ZXDNYLCQPKKT', 'EOCNQEVWESMJ', 87], ['YJFEXXCSRXCS', 'MXJKZBRWOWKF', 59], ['GDXQIVFTCCKO', 'EUZLCEOCBOWR', 20], ['NDSAEWFLAFXH', 'NJMSNTZVVGVQ', 75], ['UGLAJTODYOUO', 'DHOHAEBOCRZD', 91], ['XEXVTTIHKROW', 'LWGJMWICFYGF', 91], ['JYDUTEPDRNCC', 'BQIQZRDVMPRU', 89], ['DRNTIKRELSHE', 'QRSYTIGRAINQ', 75], ['MALRDSBKORZG', 'QFVKPCFGVTPA', 26], ['PETLEOFDBZWH', 'FTRRUKQSCEOS', 27], ['VKNRYELHCUAG', 'PEVMRPGIOJOK', 20], ['MZHLEZOJTUWQ', 'CIPFVXTRXAPH', 43], ['PJJKWPRCOEKI', 'XADTFXXHEKRI', 80], ['RHWURHROGOWY', 'XHQIVCBMNYVS', 96], ['XRANUHKYWXYE', 'TYYGMFWXUVCW', 80], ['TZHLYSADSXYR', 'YCKSMCXEDZJT', 56], ['JWUGJCUYPMDY', 'OQRTKBPEEYZV', 44], ['HXEMIAWIWRFG', 'DXURSCEZQWEG', 75], ['ZXVCXJRCRYEW', 'DEEXOKUAQBCS', 79], ['DAGEKGVKUBSS', 'DORQRHMCFALM', 27], ['AOWNHNHVPAEV', 'PLORKAPBSHBO', 29], ['OASCAWUDMPYU', 'CAYMUKJZZNHI', 17], ['INSNPQZRIVNF', 'HGIMUAABFQLL', 96], ['QXQZATGRXNRO', 'SNOVHLHPWHHI', 17], ['WQSCSAQFHZMC', 'XUYEPZEGYKVM', 85], ['VAZKGFMJLHVA', 'AFFPZQARTBXY', 25], ['EXZKVFDJPSNW', 'TMODETZRFHSZ', 39], ['DKBAVHDSHYGP', 'LODBCMPVGWCO', 55], ['YSAYBCTQTJTI', 'AOTLCUDEQADK', 44], ['INLTVBNZFXRJ', 'RPOTFECPDQDD', 61], ['AHILJJIDTIDB', 'MHCQPHMCSSOZ', 77], ['XUUDZKURKMKP', 'BMUATKHQUCCZ', 94], ['ATHVASPCLCNM', 'QZSGVKCRJCCM', 83], ['WMSEQIOLXAFF', 'LVKHUNSKZFLI', 34], ['OOPCXYPNPJGP', 'YWUMMTSSDDJO', 83], ['KAZZTFDIAZLV', 'UFBKUMAVSFDT', 64], ['IADDKCJCLNVY', 'GDZHQZRZPHMG', 61], ['KEIDIFMUNPKU', 'DAZXEGUMLBRH', 54], ['IRZIQMFIQQTS', 'JYNGYRESTLDN', 33], ['VNDOEZQPAMPR', 'XUWVJPJRBZGT', 87], ['DKHUAKBFXVHW', 'PHZYCBWZLMQN', 91], ['KBFXTXXTEZTJ', 'PFBUIZZZASSP', 24], ['QPPWLGBHWOZJ', 'YYBFQZOFUREF', 41], ['WJKOZGBFREDI', 'XCNZYKNTIKJX', 12], ['JBYKRECCKOTQ', 'TTADHSPCHGIC', 61], ['YZDCTAHATJIM', 'TLOMOPFGGGTL', 56], ['QBKFDHRHREEC', 'FKGZFTZMKUHD', 20], ['PHCPBWKJCZSY', 'HTCKFHMBRISG', 54], ['VJUYETWQNZTU', 'ABOMMEYJJPDH', 29], ['BGRUTYSNBFMO', 'KSMYQWZNPKYF', 40], ['YVQQYQCUCPQF', 'PRXEJXRZBOXF', 22], ['EZNKHWKAORVA', 'DOSMAUKTZANY', 97], ['JZKSPKZTSPHQ', 'SMPTXRCXKTUU', 92], ['EMDLPRWYDRFF', 'RHRTJNNHKUFY', 62], ['BDXGAKKBNIKP', 'LTSKARDJKEXM', 27], ['AQKDGWNWKQLI', 'FHGUSFDCCFRF', 60], ['BKHUYGIWOOWK', 'HQOIGDLMNRMP', 70], ['XPUXMXPYCMAE', 'OTDYUKQESXMJ', 84], ['PVPBFDSSJJIW', 'NGQUFBJRSGDS', 23], ['KQWMRVTKVDKD', 'CREYZUNQGRDP', 14], ['MEBCNCWHFVLR', 'SQCFMQFOYBBG', 96], ['VQMQHHBGCSPK', 'FBIPFKRACFZA', 62], ['RKTEZERYVOCV', 'MOGMHRDSVHHW', 66], ['NSOTWGHPXPZS', 'JXQOWYKVIUTU', 44], ['NEEQAVOGSPXL', 'DQSAKMCMCLXK', 47], ['GSTVFRZOTGZU', 'RNVZWJLJNUKX', 21], ['RPALLVBJTXTP', 'ESTPLPLVZMZX', 62], ['ZDMWXVOFOQFU', 'XGBFTMXMZWWX', 12], ['QRISGPZADVPZ', 'ISIJEGJKVVEM', 64], ['LXUCXORRWWJF', 'BNUGSBZLJWUN', 24], ['PQNPFSNQFEZL', 'VOAMJAZQYVLM', 64], ['XDPCTAJFYGOF', 'ALDCHSWOHEBO', 71], ['TYVLIQODJMWJ', 'RELFFIYRIYAO', 66], ['EXVXEONOPKCY', 'COPRUNMWCXIV', 0], ['EENOUAXSMYUW', 'EVFNDLFJTDXU', 40], ['DTZMYGMAREYS', 'GLCLSZUVLBAF', 37], ['QGGPIZEVBVNY', 'KNFKEJQMHZKF', 2], ['QZCAINSSYWGH', 'MOMJLYDDGAWU', 47], ['PDYWQMRVTLAS', 'TJGGNJVQJRHY', 64], ['EVDLZUWFWRSJ', 'WDUFNRLEOFCO', 62], ['OMOCWGWYDFRF', 'PKUAMTMHMTUS', 26], ['XHCFQWRXSABR', 'DIAQJWBGMXXA', 64], ['FWNFPYZXSKIC', 'TGVVVQAQLAFR', 14], ['YUYQBIHFIUPH', 'RCJZQCANMNUW', 41], ['CZHFAJJMFTRK', 'OEDRIRAEOQIO', 90], ['XFJBNEJMILXP', 'PPLOCJPZFUPO', 85], ['ONJPZZWCJZMN', 'EROACCLBTFRT', 55], ['BWSPJPUXIDPJ', 'UIRFUUZCIKFS', 74], ['VNWNOCNHLKKZ', 'IXPCFZFWOYXK', 93], ['PMGSDDSTWWLF', 'FAELUNYMJBSQ', 44], ['VRKNNQCCNFZJ', 'RSIJMRLTVPPE', 42], ['RYVJGEQJXYGN', 'QJWXNJNBLZYM', 79], ['WLEOAQHSIOOD', 'LEWJRPLLGUST', 68], ['VBTQXEPWPQRH', 'JCDGHAWUHMXM', 22], ['FWCDQIBPTNVT', 'AMMYXKCLVEDK', 42], ['PRYIUYGUOOJW', 'KVRKUMLTSIVK', 65], ['DTIXJVKCMSUO', 'ATOHXUZTQJVC', 44], ['AEHMIBTJALBY', 'BTPOPXBLCUQG', 83], ['UUULFVDLTOTQ', 'KJAAJBPNDYWO', 21], ['SUSAWWEQCTZO', 'GSDQVWBAHESZ', 56], ['EEKFAHRPAJWV', 'MWCPISRXTUXQ', 92], ['PJGGGANUJUUS', 'VHPCHCKOJLZM', 82], ['LPALKRMGZHNV', 'UVOFJMHGHDZW', 77], ['DGWINEOBFQEY', 'RXWNSTZDULIK', 95], ['XKRWJFWRKJLK', 'SWOARSWGNYOD', 9], ['JGAZTICEQXRQ', 'AZUFYWQLDUTI', 3], ['GOJQESZSQOTL', 'BVKUZVMZOWNW', 80], ['YRWIGZHBEOXU', 'JGCURNPNQYUL', 37], ['VUXKHVIDSSHM', 'ZCBVRHAEYBYO', 37], ['RFTCNHTLJPTQ', 'FRPOUKZSPFML', 42], ['CQSUDPPCXZBS', 'EGQKQTYHQLPU', 61], ['ZKAIWRMITYDK', 'YBPMZNUTTRSB', 41], ['VLKVYMAJJXNW', 'QXXNYZENZBSI', 12], ['XAJVPBEMJKIE', 'WNUOESCDBOFH', 46], ['MOPXQDNCQLJN', 'EFGPOOEIUYWI', 76], ['CDZAYGSUGLSF', 'RJNONOJLGWTE', 23], ['SVDVVNUEGFZO', 'JKTKAYKCZEJV', 59], ['BPVZEYAYTCND', 'VSSTIKPKJGWA', 88], ['UIJWHIRZJJPH', 'FDZROLKLUUTU', 1], ['JEJWUUDSRDYB', 'WLOYXLSMWWWP', 82], ['XJKLUFLNJHMB', 'SEJHHADSFCAV', 35], ['TNAUMQXVAIKG', 'NJHHECVUFSXP', 5], ['TEXQZHMRIBJJ', 'LTIKLHFCIYDG', 70], ['IFWDVELUZJPT', 'TKMJDTHNUUMV', 16], ['JSWSVFIMEGJD', 'NEVAWFETYEPX', 1], ['TYETFFHVMSRH', 'ZNPUIMFMJFOQ', 96], ['CYESZGQGULJX', 'OLYURDBNRLZN', 10], ['QQSEBLMUDMMY', 'AIFQGZSPVHFS', 87], ['AKIVOQRVWWHC', 'MGUAFANTFGXO', 96], ['UJYXUCKMLSPE', 'CVSZAWBZGJOE', 73], ['FFYLWNJUWAOG', 'LQFOEYORIGIX', 94], ['YTBRHSVOAFAN', 'OKSGIBWGINWG', 47], ['LBYBYNEZFSWC', 'RYWUXXXUDKFV', 71], ['NVQIRYUAMRPA', 'UMBBRXSEFLFJ', 76], ['YGMKAAXWEGDO', 'MGWBEVNKLNDU', 60], ['PJSXEWSUTMWY', 'GQLXDDDJSTZX', 14], ['PXEWJFZNYFZD', 'OFGIYIPCNZOV', 88], ['XMNNWJFKDNNY', 'OHWWGGUEMLEL', 86], ['YCTAFKDICTYS', 'MYOLGZAUHCSX', 50], ['CHNVVCCZDPMH', 'HWLTUIEGLYVF', 24], ['OTKWBBGJSNPA', 'QBGIVIBVWJMY', 66], ['QTBOBWNEWWFN', 'JWSSSABAZKUH', 27], ['FTZBRTFCSFDW', 'QZPPBZVFKGND', 22], ['FTZFMYEXLUSI', 'XXZOEGEEWMUV', 4], ['XFLWCIAHWDCS', 'RHLFOMQHJGGT', 56], ['ONMSFTVWORGY', 'QUZXHQBVNHPD', 34], ['YZNELIDKXOKZ', 'QQGNUMCCVVHX', 51], ['HILZQSLFQLOW', 'EHUKYRQBKXMM', 81], ['UZISCTZBQYJZ', 'LUIEUOCGBHQS', 7], ['CWOSNKCMWGWG', 'XZINXKTIQMHT', 89], ['LLAMJWCBKQLZ', 'LDWVFXHIHOBQ', 9], ['GCRWLKALQVIV', 'WDUBOLURXDZU', 61], ['FEOCEWYGSVMD', 'YTWRLUKXMTMI', 79], ['JJRBJLLDKQDY', 'CYQHREFHOMUY', 90], ['EPTNQCGMILWR', 'ROBKYNKBRGXC', 57], ['SVJUAEUEWBPH', 'SCNXWJTHOBDS', 11], ['SFYELCAPXORD', 'JDLWNTAFDKIZ', 81], ['BUIYPSSYTGPL', 'GBICJNPCGAOZ', 18], ['YDZYQEMSQYFT', 'GTPIDZSFVBQW', 15], ['OFLDJCONONTM', 'HHONUZLAVETD', 18], ['RZCPGDJPWWUC', 'HEHYNTNSMPUI', 44], ['YNKZPLEROAEA', 'KBWRJMTHXXXP', 20], ['SQXVDDSWXKBL', 'XXJHUURDHFRU', 34], ['IXHKUDZRRHQA', 'HWJKXQVHGDKS', 68], ['FAIGFYMXSVZS', 'MSJGYIWHDRIQ', 79], ['RJPVHDDGHHMR', 'SQRYJJGONAVD', 79], ['MWHNSSVDCSEW', 'CUQKAYHEKWMA', 79], ['TUFKJNHDXNRX', 'EOSTNXSFCHCP', 46], ['GMBZEFVYMBSR', 'XPENZFUZNKAA', 56], ['PPVCPIVDIIDM', 'ZUTZETIFWQXG', 67], ['HESHVGPDLWMR', 'FACCACTUGVTL', 5], ['TGXYJLAZJUGH', 'UAXDMQSEQMTA', 49], ['AYJJLCHXWVXX', 'OYCSGZZXWPTK', 39]]

        result = [[['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100], ['AEEEFNPTVWXY', 'DEFGIJJMSSVW', 99], ['AEFLLLOUUZZZ', 'EIJKLMMMOPSV', 99], ['DFKLLORTUUUZ', 'HHIIJJJPRUWZ', 99], ['EFFHJKKKMNQZ', 'BEGGINPQVVYZ', 98], ['AAEHKKNORVWZ', 'AADKMNOSTUYZ', 97], ['ADFILQTUUWYZ', 'ACEGIJQQRTXZ', 97], ['BBBCFILOOQSV', 'CDDDDFIJKPZZ', 97]], [['AGHIIJKNOQRS', 'EFGILMMPQRSU', 70], ['BEHIJJMQRTXZ', 'CDFGHIIKLLTY', 70], ['BGHIKKOOUWWY', 'DGHILMMNOPQR', 70], ['CDEHHHIMNRUY', 'FLMMOOPVWXYY', 70], ['EFGHJKOQSVXZ', 'AGGHKKMNPRUV', 70]]]
        
        self.assertEqual(analyze(results, 26, 69), result)

    def test_41(self):
        results = [['ZVJUKWHPNIQO', 'BRJCVKEMTRKU', 63], ['YIQJXUCATBIY', 'GOEBKTNEQOXU', 39], ['MHUVYBQSAQLC', 'NTNKUQYWYMIV', 58], ['YTVHOGSGFHQK', 'KLDMPPXWRVXK', 39], ['QYJZIZLVZBJR', 'HHRFSLDRCYBR', 66], ['NABGULQKKPSC', 'MYARMIMWUPQI', 33], ['MQEFHYWEQEQF', 'SKWTRINZKNHZ', 56], ['CFVLWYEPIHTD', 'VNVMOTETFNZS', 97], ['LUYFGOTQDNUW', 'LNOTZYAMBJDY', 15], ['AXLIHDJFQCND', 'SKAHGGPLJQDW', 26], ['XBAAGNTXAIKR', 'THCSSZBZUENU', 77], ['CHRKLIGSILMJ', 'DAIZUYKLLWRF', 48], ['SOXUJJGBOMOL', 'GMPUWAUQISEV', 74], ['BPYNVMYYQQRC', 'ALOAEDBOCYKS', 76], ['NFLVFKOJSKRO', 'LXOJVBXVZOZK', 16], ['PPVCXTPBMAEL', 'ZHFMTHBQFHXS', 76], ['ZKGHDFGCWFRG', 'SUTCSDSIFJTK', 88], ['OYVFIGWMZOWI', 'YGECHBKNYUWR', 44], ['KNXDGJJMKKPA', 'NGWWWPFNVXQM', 74], ['GABAUOHHKISI', 'WQCTSYPTQOAO', 46], ['MWYGNZAZUGKW', 'HICKBOFGUBBU', 81], ['IPLPYFHHDKCQ', 'YILGAMWIXWLS', 29], ['FKYXDSJIWQWX', 'XGOSDDUZJRAX', 8], ['PTICQYGEBHIH', 'WNXOHQMVOFSQ', 51], ['SVTGRKABFLVT', 'YQDMWUHWPTQW', 24], ['IRMMHZESILHY', 'HISSLSKXZQYI', 51], ['HLPQTTWPZQHH', 'LNWBQTBBXFYR', 47], ['BZMCBVIQMTRD', 'RXOFFOLYCNCW', 94], ['MHVWDCDUYNDG', 'PPUZPAUKVECW', 47], ['NCKGDMIOUCFA', 'AUEKROBRPTOS', 59], ['WNBNPIVCHGMR', 'ENLHLBAAYOJY', 93], ['WMKTQJWKKFDX', 'IIFOLFTGDCBP', 78], ['OIWAFYULUVBA', 'PPXMNMDOHQJY', 29], ['BGPZBTDUEVLY', 'BJZACXREPIEP', 79], ['QZHDRHLREVZF', 'YTQKJWOMDSBK', 0], ['YFHFNWUMQTXO', 'JUIIRSDRKZVG', 64], ['YTBJVGNBIANK', 'ZZWGRLMLTFQK', 6], ['FJZKABDMBXQR', 'XWHMHSEWPVUI', 9], ['RLTMZFUMVPFD', 'SAPFUDVUXMWN', 12], ['RBFMNUDAFXQT', 'RSFCBRKAAXTK', 60], ['DFDZJAYUBNIY', 'QAKYJQNDVSFJ', 0], ['AIUDHAIJMOUZ', 'NVEFIMYYMGYK', 19], ['JKNOADVQUTZY', 'AMDZPGUVRXAO', 14], ['RWZGJXAGRZIB', 'FHXYNYLTPCDJ', 21], ['RIMHNHUDCHYE', 'YVFOYMXOMPWL', 70], ['OTDPYQXTRZPY', 'LGECGEVJRRCB', 11], ['NACUFYQRJKBG', 'XVWKPSNJJFIM', 95], ['FDTBYTDUSOGQ', 'ZGKXDRSFIWLI', 32], ['BBFPVZINOPQH', 'DIJULBSCJMGR', 40], ['PBTBHRWXXADT', 'NRNIHRQDAHWD', 68], ['LUVBIWYQDHUM', 'OMZKEPTSFFFT', 72], ['UBATNOWFHMNP', 'GNGHHBDMOMSS', 43], ['QAZVAHCKMBTT', 'KWIIUHIWYRLM', 45], ['AKJVIHICULQT', 'OUOMMNQYMQVL', 55], ['GTEKJMWYQTEG', 'HKYVMPNPNTOX', 3], ['BXYSZCOUZAYK', 'RXGQIBOPRALN', 17], ['VZPSHAYQBAYJ', 'DAZENTPOGGLP', 91], ['EIPVUJZPSSWW', 'LLCAEBHPCIFM', 18], ['YHOBYPDCVDRF', 'IZDKIUXPZYAF', 90], ['OTPWEYCKGWCF', 'ZPRLOMKQEFIH', 52], ['OSPAVMUOOHCC', 'CYKDYDZNFBSY', 51], ['RWQSGDJSXABZ', 'PRYRYLWEVLPA', 13], ['YTDIZCYNYDMH', 'JRVZAPAJJAJR', 32], ['CDPZWKHBUJHN', 'VWLROBUEHZGZ', 67], ['KBWEVADGOVBJ', 'LJDEZUFSAXUX', 38], ['IFRNHGUUCCVP', 'UQWVTEUMTRXJ', 55], ['NIXPFMTBOTQD', 'JHGONFJBUBRS', 19], ['TDVPBBEYIRUT', 'CJBVVHEKSMPN', 56], ['PKGUXCSPOJIY', 'RRZPXELGRUOY', 34], ['OCIQLOBFSBBV', 'ZDZDCDDKFJPI', 97], ['ARZKETUFBBSJ', 'LPACWUGWHHXR', 14], ['VMCCGGFFCNHL', 'KDQKZCXEZXKV', 48], ['AFMZATESMICM', 'YRBBLDBRKIBG', 20], ['EXCIFGHIIIYW', 'TLATBFPWSUOY', 64], ['XMNYYPFSVXTV', 'TQUCEWLXSXPF', 36], ['JOWOIHWLSBSU', 'OFPCBACEAFLZ', 91], ['XGJNWDAZNQBS', 'JLACETXZZFGC', 48], ['BOANPTJMQYSX', 'VHIZOYILVBQO', 74], ['VGYBNQECUPEO', 'RABRJTMZGBFZ', 40], ['OAYGMXISJXWN', 'FUXYIJEZIAOK', 81], ['KDQXAPPLQLYH', 'AHNKYNEAGJAE', 5], ['EFXJEEAWXKFM', 'XMQLCIMRECNC', 53], ['TQRAWTGOWJAD', 'LEREHCJKZWOW', 37], ['PDMDWVNCRSET', 'PFORZIONAEGN', 86], ['EJSLEVABTAOW', 'TRERGQLWOTFV', 49], ['JDSKXIVTLQZS', 'VSEUXFTKEUVE', 63], ['ZWCUCUFPOUFR', 'CXLUZQMJINCL', 65], ['JHYRUBTEHPED', 'RUWQCOFYAFUT', 91], ['MJFHURPYVOBI', 'ABYZRFGISGHP', 7], ['HYEWEUDNRVES', 'YXPIPIEMLPFK', 34], ['FOTWRBBNMNAO', 'SRIPDFOAVPWN', 24], ['QUBPNNZYXDTC', 'EDWMRLJJSPWW', 51], ['ALFULLUZZOEZ', 'JSMOKLVIEMPM', 99], ['VGENYRDSSZAT', 'ZGWDOBDQZPEJ', 60], ['EQSRFRDPPHHX', 'FMRZAIKGCIRC', 20], ['ZTQJIKNXWALY', 'ORFLBEOXGQJP', 40], ['ZJRPZWYURGHL', 'JLNQTCDOUXTR', 12], ['TIOLRGSUORMX', 'CVLUSNOWXISR', 84], ['JIDEXUNBJCGP', 'UOCAHXYEPOGG', 92], ['OLALVLCSFSOE', 'YZTLJJQOXLFY', 27], ['PSEEIUELNNDT', 'JNHFOVHHTCUX', 93], ['XDZOGZVXUJTC', 'QGSCUBNUVVFT', 88], ['WYIMCWRCTCWH', 'AWIPZLCCEBCO', 26], ['MUYMPOAIIAWF', 'VUCVZMFXRNJD', 63], ['DRYASDRMEQIB', 'DVMVOQLZBRDN', 80], ['XULOEINLHWCP', 'PAPQYCJROHQJ', 86], ['FTMOXXOFFHGL', 'ZFLTESOYUFJO', 16], ['USDEKGIOUXQM', 'YNCMEJTXOGUM', 49], ['RFSMPQGIMUEL', 'QIKNHJAOGIRS', 30], ['YIUQGDTHJNXD', 'JJILUWKIGDJT', 47], ['IZUBECJNGOZB', 'JRZKKKOQZNXM', 64], ['AVKNGKGRHMPU', 'EKHFXQZJSOVG', 30], ['KOIEPBAUZYZB', 'XIDDPKYZVCHC', 82], ['QDZKPZWTCIHE', 'ILSCHPEGGFQT', 83], ['NNSEHTVORIKF', 'YPJIWWXHQIXE', 28], ['JUQFMHNKTOXL', 'UQILUJDHRYVC', 25], ['LHZZWWIYJOQX', 'ZTXEQXPLZIIY', 82], ['MLHOCNBGZFPN', 'WSUKNZZVULEY', 75], ['IPRIJBWJNDLA', 'DLQPCMJGQOOJ', 38], ['WOKUNBQGBMZA', 'XQFWTTFUORFB', 43], ['UGMWZVZAVVBS', 'WZVWEZXFFKXP', 12], ['MLDFTBNIOGYD', 'QQFSLOOOXKSN', 88], ['XCQKBAWZRKOF', 'IGBVSIXJHVEX', 44], ['QSEUPFOGOYSE', 'JQTDLAUVFLFA', 35], ['ZXDNYLCQPKKT', 'EOCNQEVWESMJ', 87], ['YJFEXXCSRXCS', 'MXJKZBRWOWKF', 59], ['GDXQIVFTCCKO', 'EUZLCEOCBOWR', 20], ['NDSAEWFLAFXH', 'NJMSNTZVVGVQ', 75], ['UGLAJTODYOUO', 'DHOHAEBOCRZD', 91], ['XEXVTTIHKROW', 'LWGJMWICFYGF', 91], ['JYDUTEPDRNCC', 'BQIQZRDVMPRU', 89], ['DRNTIKRELSHE', 'QRSYTIGRAINQ', 75], ['MALRDSBKORZG', 'QFVKPCFGVTPA', 26], ['PETLEOFDBZWH', 'FTRRUKQSCEOS', 27], ['VKNRYELHCUAG', 'PEVMRPGIOJOK', 20], ['MZHLEZOJTUWQ', 'CIPFVXTRXAPH', 43], ['PJJKWPRCOEKI', 'XADTFXXHEKRI', 80], ['RHWURHROGOWY', 'XHQIVCBMNYVS', 96], ['XRANUHKYWXYE', 'TYYGMFWXUVCW', 80], ['TZHLYSADSXYR', 'YCKSMCXEDZJT', 56], ['JWUGJCUYPMDY', 'OQRTKBPEEYZV', 44], ['HXEMIAWIWRFG', 'DXURSCEZQWEG', 75], ['ZXVCXJRCRYEW', 'DEEXOKUAQBCS', 79], ['DAGEKGVKUBSS', 'DORQRHMCFALM', 27], ['AOWNHNHVPAEV', 'PLORKAPBSHBO', 29], ['OASCAWUDMPYU', 'CAYMUKJZZNHI', 17], ['INSNPQZRIVNF', 'HGIMUAABFQLL', 96], ['QXQZATGRXNRO', 'SNOVHLHPWHHI', 17], ['WQSCSAQFHZMC', 'XUYEPZEGYKVM', 85], ['VAZKGFMJLHVA', 'AFFPZQARTBXY', 25], ['EXZKVFDJPSNW', 'TMODETZRFHSZ', 39], ['DKBAVHDSHYGP', 'LODBCMPVGWCO', 55], ['YSAYBCTQTJTI', 'AOTLCUDEQADK', 44], ['INLTVBNZFXRJ', 'RPOTFECPDQDD', 61], ['AHILJJIDTIDB', 'MHCQPHMCSSOZ', 77], ['XUUDZKURKMKP', 'BMUATKHQUCCZ', 94], ['ATHVASPCLCNM', 'QZSGVKCRJCCM', 83], ['WMSEQIOLXAFF', 'LVKHUNSKZFLI', 34], ['OOPCXYPNPJGP', 'YWUMMTSSDDJO', 83], ['KAZZTFDIAZLV', 'UFBKUMAVSFDT', 64], ['IADDKCJCLNVY', 'GDZHQZRZPHMG', 61], ['KEIDIFMUNPKU', 'DAZXEGUMLBRH', 54], ['IRZIQMFIQQTS', 'JYNGYRESTLDN', 33], ['VNDOEZQPAMPR', 'XUWVJPJRBZGT', 87], ['DKHUAKBFXVHW', 'PHZYCBWZLMQN', 91], ['KBFXTXXTEZTJ', 'PFBUIZZZASSP', 24], ['QPPWLGBHWOZJ', 'YYBFQZOFUREF', 41], ['WJKOZGBFREDI', 'XCNZYKNTIKJX', 12], ['JBYKRECCKOTQ', 'TTADHSPCHGIC', 61], ['YZDCTAHATJIM', 'TLOMOPFGGGTL', 56], ['QBKFDHRHREEC', 'FKGZFTZMKUHD', 20], ['PHCPBWKJCZSY', 'HTCKFHMBRISG', 54], ['VJUYETWQNZTU', 'ABOMMEYJJPDH', 29], ['BGRUTYSNBFMO', 'KSMYQWZNPKYF', 40], ['YVQQYQCUCPQF', 'PRXEJXRZBOXF', 22], ['EZNKHWKAORVA', 'DOSMAUKTZANY', 97], ['JZKSPKZTSPHQ', 'SMPTXRCXKTUU', 92], ['EMDLPRWYDRFF', 'RHRTJNNHKUFY', 62], ['BDXGAKKBNIKP', 'LTSKARDJKEXM', 27], ['AQKDGWNWKQLI', 'FHGUSFDCCFRF', 60], ['BKHUYGIWOOWK', 'HQOIGDLMNRMP', 70], ['XPUXMXPYCMAE', 'OTDYUKQESXMJ', 84], ['PVPBFDSSJJIW', 'NGQUFBJRSGDS', 23], ['KQWMRVTKVDKD', 'CREYZUNQGRDP', 14], ['MEBCNCWHFVLR', 'SQCFMQFOYBBG', 96], ['VQMQHHBGCSPK', 'FBIPFKRACFZA', 62], ['RKTEZERYVOCV', 'MOGMHRDSVHHW', 66], ['NSOTWGHPXPZS', 'JXQOWYKVIUTU', 44], ['NEEQAVOGSPXL', 'DQSAKMCMCLXK', 47], ['GSTVFRZOTGZU', 'RNVZWJLJNUKX', 21], ['RPALLVBJTXTP', 'ESTPLPLVZMZX', 62], ['ZDMWXVOFOQFU', 'XGBFTMXMZWWX', 12], ['QRISGPZADVPZ', 'ISIJEGJKVVEM', 64], ['LXUCXORRWWJF', 'BNUGSBZLJWUN', 24], ['PQNPFSNQFEZL', 'VOAMJAZQYVLM', 64], ['XDPCTAJFYGOF', 'ALDCHSWOHEBO', 71], ['TYVLIQODJMWJ', 'RELFFIYRIYAO', 66], ['EXVXEONOPKCY', 'COPRUNMWCXIV', 0], ['EENOUAXSMYUW', 'EVFNDLFJTDXU', 40], ['DTZMYGMAREYS', 'GLCLSZUVLBAF', 37], ['QGGPIZEVBVNY', 'KNFKEJQMHZKF', 2], ['QZCAINSSYWGH', 'MOMJLYDDGAWU', 47], ['PDYWQMRVTLAS', 'TJGGNJVQJRHY', 64], ['EVDLZUWFWRSJ', 'WDUFNRLEOFCO', 62], ['OMOCWGWYDFRF', 'PKUAMTMHMTUS', 26], ['XHCFQWRXSABR', 'DIAQJWBGMXXA', 64], ['FWNFPYZXSKIC', 'TGVVVQAQLAFR', 14], ['YUYQBIHFIUPH', 'RCJZQCANMNUW', 41], ['CZHFAJJMFTRK', 'OEDRIRAEOQIO', 90], ['XFJBNEJMILXP', 'PPLOCJPZFUPO', 85], ['ONJPZZWCJZMN', 'EROACCLBTFRT', 55], ['BWSPJPUXIDPJ', 'UIRFUUZCIKFS', 74], ['VNWNOCNHLKKZ', 'IXPCFZFWOYXK', 93], ['PMGSDDSTWWLF', 'FAELUNYMJBSQ', 44], ['VRKNNQCCNFZJ', 'RSIJMRLTVPPE', 42], ['RYVJGEQJXYGN', 'QJWXNJNBLZYM', 79], ['WLEOAQHSIOOD', 'LEWJRPLLGUST', 68], ['VBTQXEPWPQRH', 'JCDGHAWUHMXM', 22], ['FWCDQIBPTNVT', 'AMMYXKCLVEDK', 42], ['PRYIUYGUOOJW', 'KVRKUMLTSIVK', 65], ['DTIXJVKCMSUO', 'ATOHXUZTQJVC', 44], ['AEHMIBTJALBY', 'BTPOPXBLCUQG', 83], ['UUULFVDLTOTQ', 'KJAAJBPNDYWO', 21], ['SUSAWWEQCTZO', 'GSDQVWBAHESZ', 56], ['EEKFAHRPAJWV', 'MWCPISRXTUXQ', 92], ['PJGGGANUJUUS', 'VHPCHCKOJLZM', 82], ['LPALKRMGZHNV', 'UVOFJMHGHDZW', 77], ['DGWINEOBFQEY', 'RXWNSTZDULIK', 95], ['XKRWJFWRKJLK', 'SWOARSWGNYOD', 9], ['JGAZTICEQXRQ', 'AZUFYWQLDUTI', 3], ['GOJQESZSQOTL', 'BVKUZVMZOWNW', 80], ['YRWIGZHBEOXU', 'JGCURNPNQYUL', 37], ['VUXKHVIDSSHM', 'ZCBVRHAEYBYO', 37], ['RFTCNHTLJPTQ', 'FRPOUKZSPFML', 42], ['CQSUDPPCXZBS', 'EGQKQTYHQLPU', 61], ['ZKAIWRMITYDK', 'YBPMZNUTTRSB', 41], ['VLKVYMAJJXNW', 'QXXNYZENZBSI', 12], ['XAJVPBEMJKIE', 'WNUOESCDBOFH', 46], ['MOPXQDNCQLJN', 'EFGPOOEIUYWI', 76], ['CDZAYGSUGLSF', 'RJNONOJLGWTE', 23], ['SVDVVNUEGFZO', 'JKTKAYKCZEJV', 59], ['BPVZEYAYTCND', 'VSSTIKPKJGWA', 88], ['UIJWHIRZJJPH', 'FDZROLKLUUTU', 1], ['JEJWUUDSRDYB', 'WLOYXLSMWWWP', 82], ['XJKLUFLNJHMB', 'SEJHHADSFCAV', 35], ['TNAUMQXVAIKG', 'NJHHECVUFSXP', 5], ['TEXQZHMRIBJJ', 'LTIKLHFCIYDG', 70], ['IFWDVELUZJPT', 'TKMJDTHNUUMV', 16], ['JSWSVFIMEGJD', 'NEVAWFETYEPX', 1], ['TYETFFHVMSRH', 'ZNPUIMFMJFOQ', 96], ['CYESZGQGULJX', 'OLYURDBNRLZN', 10], ['QQSEBLMUDMMY', 'AIFQGZSPVHFS', 87], ['AKIVOQRVWWHC', 'MGUAFANTFGXO', 96], ['UJYXUCKMLSPE', 'CVSZAWBZGJOE', 73], ['FFYLWNJUWAOG', 'LQFOEYORIGIX', 94], ['YTBRHSVOAFAN', 'OKSGIBWGINWG', 47], ['LBYBYNEZFSWC', 'RYWUXXXUDKFV', 71], ['NVQIRYUAMRPA', 'UMBBRXSEFLFJ', 76], ['YGMKAAXWEGDO', 'MGWBEVNKLNDU', 60], ['PJSXEWSUTMWY', 'GQLXDDDJSTZX', 14], ['PXEWJFZNYFZD', 'OFGIYIPCNZOV', 88], ['XMNNWJFKDNNY', 'OHWWGGUEMLEL', 86], ['YCTAFKDICTYS', 'MYOLGZAUHCSX', 50], ['CHNVVCCZDPMH', 'HWLTUIEGLYVF', 24], ['OTKWBBGJSNPA', 'QBGIVIBVWJMY', 66], ['QTBOBWNEWWFN', 'JWSSSABAZKUH', 27], ['FTZBRTFCSFDW', 'QZPPBZVFKGND', 22], ['FTZFMYEXLUSI', 'XXZOEGEEWMUV', 4], ['XFLWCIAHWDCS', 'RHLFOMQHJGGT', 56], ['ONMSFTVWORGY', 'QUZXHQBVNHPD', 34], ['YZNELIDKXOKZ', 'QQGNUMCCVVHX', 51], ['HILZQSLFQLOW', 'EHUKYRQBKXMM', 81], ['UZISCTZBQYJZ', 'LUIEUOCGBHQS', 7], ['CWOSNKCMWGWG', 'XZINXKTIQMHT', 89], ['LLAMJWCBKQLZ', 'LDWVFXHIHOBQ', 9], ['GCRWLKALQVIV', 'WDUBOLURXDZU', 61], ['FEOCEWYGSVMD', 'YTWRLUKXMTMI', 79], ['JJRBJLLDKQDY', 'CYQHREFHOMUY', 90], ['EPTNQCGMILWR', 'ROBKYNKBRGXC', 57], ['SVJUAEUEWBPH', 'SCNXWJTHOBDS', 11], ['SFYELCAPXORD', 'JDLWNTAFDKIZ', 81], ['BUIYPSSYTGPL', 'GBICJNPCGAOZ', 18], ['YDZYQEMSQYFT', 'GTPIDZSFVBQW', 15], ['OFLDJCONONTM', 'HHONUZLAVETD', 18], ['RZCPGDJPWWUC', 'HEHYNTNSMPUI', 44], ['YNKZPLEROAEA', 'KBWRJMTHXXXP', 20], ['SQXVDDSWXKBL', 'XXJHUURDHFRU', 34], ['IXHKUDZRRHQA', 'HWJKXQVHGDKS', 68], ['FAIGFYMXSVZS', 'MSJGYIWHDRIQ', 79], ['RJPVHDDGHHMR', 'SQRYJJGONAVD', 79], ['MWHNSSVDCSEW', 'CUQKAYHEKWMA', 79], ['TUFKJNHDXNRX', 'EOSTNXSFCHCP', 46], ['GMBZEFVYMBSR', 'XPENZFUZNKAA', 56], ['PPVCPIVDIIDM', 'ZUTZETIFWQXG', 67], ['HESHVGPDLWMR', 'FACCACTUGVTL', 5], ['TGXYJLAZJUGH', 'UAXDMQSEQMTA', 49], ['AYJJLCHXWVXX', 'OYCSGZZXWPTK', 39]]

        result = [[['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100], ['AEEEFNPTVWXY', 'DEFGIJJMSSVW', 99], ['AEFLLLOUUZZZ', 'EIJKLMMMOPSV', 99], ['DFKLLORTUUUZ', 'HHIIJJJPRUWZ', 99], ['EFFHJKKKMNQZ', 'BEGGINPQVVYZ', 98], ['AAEHKKNORVWZ', 'AADKMNOSTUYZ', 97], ['ADFILQTUUWYZ', 'ACEGIJQQRTXZ', 97], ['BBBCFILOOQSV', 'CDDDDFIJKPZZ', 97]], [['ADDHHINNQRRW', 'ABBDHPRTTWXX', 32], ['BDDFGOQSTTUY', 'DFGIIKLRSWXZ', 32], ['CDDHIMNTYYYZ', 'AAAJJJJPRRVZ', 32], ['DGHHJKKQSVWX', 'ADHHIKQRRUXZ', 32], ['EGJLLLPRSTUW', 'ADEHILOOOQSW', 32]]]
        
        self.assertEqual(analyze(results, 26, 31), result)
        
    def test_42(self):
        results = [['ZVJUKWHPNIQO', 'BRJCVKEMTRKU', 63], ['YIQJXUCATBIY', 'GOEBKTNEQOXU', 39], ['MHUVYBQSAQLC', 'NTNKUQYWYMIV', 58], ['YTVHOGSGFHQK', 'KLDMPPXWRVXK', 39], ['QYJZIZLVZBJR', 'HHRFSLDRCYBR', 66], ['NABGULQKKPSC', 'MYARMIMWUPQI', 33], ['MQEFHYWEQEQF', 'SKWTRINZKNHZ', 56], ['CFVLWYEPIHTD', 'VNVMOTETFNZS', 97], ['LUYFGOTQDNUW', 'LNOTZYAMBJDY', 15], ['AXLIHDJFQCND', 'SKAHGGPLJQDW', 26], ['XBAAGNTXAIKR', 'THCSSZBZUENU', 77], ['CHRKLIGSILMJ', 'DAIZUYKLLWRF', 48], ['SOXUJJGBOMOL', 'GMPUWAUQISEV', 74], ['BPYNVMYYQQRC', 'ALOAEDBOCYKS', 76], ['NFLVFKOJSKRO', 'LXOJVBXVZOZK', 16], ['PPVCXTPBMAEL', 'ZHFMTHBQFHXS', 76], ['ZKGHDFGCWFRG', 'SUTCSDSIFJTK', 88], ['OYVFIGWMZOWI', 'YGECHBKNYUWR', 44], ['KNXDGJJMKKPA', 'NGWWWPFNVXQM', 74], ['GABAUOHHKISI', 'WQCTSYPTQOAO', 46], ['MWYGNZAZUGKW', 'HICKBOFGUBBU', 81], ['IPLPYFHHDKCQ', 'YILGAMWIXWLS', 29], ['FKYXDSJIWQWX', 'XGOSDDUZJRAX', 8], ['PTICQYGEBHIH', 'WNXOHQMVOFSQ', 51], ['SVTGRKABFLVT', 'YQDMWUHWPTQW', 24], ['IRMMHZESILHY', 'HISSLSKXZQYI', 51], ['HLPQTTWPZQHH', 'LNWBQTBBXFYR', 47], ['BZMCBVIQMTRD', 'RXOFFOLYCNCW', 94], ['MHVWDCDUYNDG', 'PPUZPAUKVECW', 47], ['NCKGDMIOUCFA', 'AUEKROBRPTOS', 59], ['WNBNPIVCHGMR', 'ENLHLBAAYOJY', 93], ['WMKTQJWKKFDX', 'IIFOLFTGDCBP', 78], ['OIWAFYULUVBA', 'PPXMNMDOHQJY', 29], ['BGPZBTDUEVLY', 'BJZACXREPIEP', 79], ['QZHDRHLREVZF', 'YTQKJWOMDSBK', 0], ['YFHFNWUMQTXO', 'JUIIRSDRKZVG', 64], ['YTBJVGNBIANK', 'ZZWGRLMLTFQK', 6], ['FJZKABDMBXQR', 'XWHMHSEWPVUI', 9], ['RLTMZFUMVPFD', 'SAPFUDVUXMWN', 12], ['RBFMNUDAFXQT', 'RSFCBRKAAXTK', 60], ['DFDZJAYUBNIY', 'QAKYJQNDVSFJ', 0], ['AIUDHAIJMOUZ', 'NVEFIMYYMGYK', 19], ['JKNOADVQUTZY', 'AMDZPGUVRXAO', 14], ['RWZGJXAGRZIB', 'FHXYNYLTPCDJ', 21], ['RIMHNHUDCHYE', 'YVFOYMXOMPWL', 70], ['OTDPYQXTRZPY', 'LGECGEVJRRCB', 11], ['NACUFYQRJKBG', 'XVWKPSNJJFIM', 95], ['FDTBYTDUSOGQ', 'ZGKXDRSFIWLI', 32], ['BBFPVZINOPQH', 'DIJULBSCJMGR', 40], ['PBTBHRWXXADT', 'NRNIHRQDAHWD', 68], ['LUVBIWYQDHUM', 'OMZKEPTSFFFT', 72], ['UBATNOWFHMNP', 'GNGHHBDMOMSS', 43], ['QAZVAHCKMBTT', 'KWIIUHIWYRLM', 45], ['AKJVIHICULQT', 'OUOMMNQYMQVL', 55], ['GTEKJMWYQTEG', 'HKYVMPNPNTOX', 3], ['BXYSZCOUZAYK', 'RXGQIBOPRALN', 17], ['VZPSHAYQBAYJ', 'DAZENTPOGGLP', 91], ['EIPVUJZPSSWW', 'LLCAEBHPCIFM', 18], ['YHOBYPDCVDRF', 'IZDKIUXPZYAF', 90], ['OTPWEYCKGWCF', 'ZPRLOMKQEFIH', 52], ['OSPAVMUOOHCC', 'CYKDYDZNFBSY', 51], ['RWQSGDJSXABZ', 'PRYRYLWEVLPA', 13], ['YTDIZCYNYDMH', 'JRVZAPAJJAJR', 32], ['CDPZWKHBUJHN', 'VWLROBUEHZGZ', 67], ['KBWEVADGOVBJ', 'LJDEZUFSAXUX', 38], ['IFRNHGUUCCVP', 'UQWVTEUMTRXJ', 55], ['NIXPFMTBOTQD', 'JHGONFJBUBRS', 19], ['TDVPBBEYIRUT', 'CJBVVHEKSMPN', 56], ['PKGUXCSPOJIY', 'RRZPXELGRUOY', 34], ['OCIQLOBFSBBV', 'ZDZDCDDKFJPI', 97], ['ARZKETUFBBSJ', 'LPACWUGWHHXR', 14], ['VMCCGGFFCNHL', 'KDQKZCXEZXKV', 48], ['AFMZATESMICM', 'YRBBLDBRKIBG', 20], ['EXCIFGHIIIYW', 'TLATBFPWSUOY', 64], ['XMNYYPFSVXTV', 'TQUCEWLXSXPF', 36], ['JOWOIHWLSBSU', 'OFPCBACEAFLZ', 91], ['XGJNWDAZNQBS', 'JLACETXZZFGC', 48], ['BOANPTJMQYSX', 'VHIZOYILVBQO', 74], ['VGYBNQECUPEO', 'RABRJTMZGBFZ', 40], ['OAYGMXISJXWN', 'FUXYIJEZIAOK', 81], ['KDQXAPPLQLYH', 'AHNKYNEAGJAE', 5], ['EFXJEEAWXKFM', 'XMQLCIMRECNC', 53], ['TQRAWTGOWJAD', 'LEREHCJKZWOW', 37], ['PDMDWVNCRSET', 'PFORZIONAEGN', 86], ['EJSLEVABTAOW', 'TRERGQLWOTFV', 49], ['JDSKXIVTLQZS', 'VSEUXFTKEUVE', 63], ['ZWCUCUFPOUFR', 'CXLUZQMJINCL', 65], ['JHYRUBTEHPED', 'RUWQCOFYAFUT', 91], ['MJFHURPYVOBI', 'ABYZRFGISGHP', 7], ['HYEWEUDNRVES', 'YXPIPIEMLPFK', 34], ['FOTWRBBNMNAO', 'SRIPDFOAVPWN', 24], ['QUBPNNZYXDTC', 'EDWMRLJJSPWW', 51], ['ALFULLUZZOEZ', 'JSMOKLVIEMPM', 99], ['VGENYRDSSZAT', 'ZGWDOBDQZPEJ', 60], ['EQSRFRDPPHHX', 'FMRZAIKGCIRC', 20], ['ZTQJIKNXWALY', 'ORFLBEOXGQJP', 40], ['ZJRPZWYURGHL', 'JLNQTCDOUXTR', 12], ['TIOLRGSUORMX', 'CVLUSNOWXISR', 84], ['JIDEXUNBJCGP', 'UOCAHXYEPOGG', 92], ['OLALVLCSFSOE', 'YZTLJJQOXLFY', 27], ['PSEEIUELNNDT', 'JNHFOVHHTCUX', 93], ['XDZOGZVXUJTC', 'QGSCUBNUVVFT', 88], ['WYIMCWRCTCWH', 'AWIPZLCCEBCO', 26], ['MUYMPOAIIAWF', 'VUCVZMFXRNJD', 63], ['DRYASDRMEQIB', 'DVMVOQLZBRDN', 80], ['XULOEINLHWCP', 'PAPQYCJROHQJ', 86], ['FTMOXXOFFHGL', 'ZFLTESOYUFJO', 16], ['USDEKGIOUXQM', 'YNCMEJTXOGUM', 49], ['RFSMPQGIMUEL', 'QIKNHJAOGIRS', 30], ['YIUQGDTHJNXD', 'JJILUWKIGDJT', 47], ['IZUBECJNGOZB', 'JRZKKKOQZNXM', 64], ['AVKNGKGRHMPU', 'EKHFXQZJSOVG', 30], ['KOIEPBAUZYZB', 'XIDDPKYZVCHC', 82], ['QDZKPZWTCIHE', 'ILSCHPEGGFQT', 83], ['NNSEHTVORIKF', 'YPJIWWXHQIXE', 28], ['JUQFMHNKTOXL', 'UQILUJDHRYVC', 25], ['LHZZWWIYJOQX', 'ZTXEQXPLZIIY', 82], ['MLHOCNBGZFPN', 'WSUKNZZVULEY', 75], ['IPRIJBWJNDLA', 'DLQPCMJGQOOJ', 38], ['WOKUNBQGBMZA', 'XQFWTTFUORFB', 43], ['UGMWZVZAVVBS', 'WZVWEZXFFKXP', 12], ['MLDFTBNIOGYD', 'QQFSLOOOXKSN', 88], ['XCQKBAWZRKOF', 'IGBVSIXJHVEX', 44], ['QSEUPFOGOYSE', 'JQTDLAUVFLFA', 35], ['ZXDNYLCQPKKT', 'EOCNQEVWESMJ', 87], ['YJFEXXCSRXCS', 'MXJKZBRWOWKF', 59], ['GDXQIVFTCCKO', 'EUZLCEOCBOWR', 20], ['NDSAEWFLAFXH', 'NJMSNTZVVGVQ', 75], ['UGLAJTODYOUO', 'DHOHAEBOCRZD', 91], ['XEXVTTIHKROW', 'LWGJMWICFYGF', 91], ['JYDUTEPDRNCC', 'BQIQZRDVMPRU', 89], ['DRNTIKRELSHE', 'QRSYTIGRAINQ', 75], ['MALRDSBKORZG', 'QFVKPCFGVTPA', 26], ['PETLEOFDBZWH', 'FTRRUKQSCEOS', 27], ['VKNRYELHCUAG', 'PEVMRPGIOJOK', 20], ['MZHLEZOJTUWQ', 'CIPFVXTRXAPH', 43], ['PJJKWPRCOEKI', 'XADTFXXHEKRI', 80], ['RHWURHROGOWY', 'XHQIVCBMNYVS', 96], ['XRANUHKYWXYE', 'TYYGMFWXUVCW', 80], ['TZHLYSADSXYR', 'YCKSMCXEDZJT', 56], ['JWUGJCUYPMDY', 'OQRTKBPEEYZV', 44], ['HXEMIAWIWRFG', 'DXURSCEZQWEG', 75], ['ZXVCXJRCRYEW', 'DEEXOKUAQBCS', 79], ['DAGEKGVKUBSS', 'DORQRHMCFALM', 27], ['AOWNHNHVPAEV', 'PLORKAPBSHBO', 29], ['OASCAWUDMPYU', 'CAYMUKJZZNHI', 17], ['INSNPQZRIVNF', 'HGIMUAABFQLL', 96], ['QXQZATGRXNRO', 'SNOVHLHPWHHI', 17], ['WQSCSAQFHZMC', 'XUYEPZEGYKVM', 85], ['VAZKGFMJLHVA', 'AFFPZQARTBXY', 25], ['EXZKVFDJPSNW', 'TMODETZRFHSZ', 39], ['DKBAVHDSHYGP', 'LODBCMPVGWCO', 55], ['YSAYBCTQTJTI', 'AOTLCUDEQADK', 44], ['INLTVBNZFXRJ', 'RPOTFECPDQDD', 61], ['AHILJJIDTIDB', 'MHCQPHMCSSOZ', 77], ['XUUDZKURKMKP', 'BMUATKHQUCCZ', 94], ['ATHVASPCLCNM', 'QZSGVKCRJCCM', 83], ['WMSEQIOLXAFF', 'LVKHUNSKZFLI', 34], ['OOPCXYPNPJGP', 'YWUMMTSSDDJO', 83], ['KAZZTFDIAZLV', 'UFBKUMAVSFDT', 64], ['IADDKCJCLNVY', 'GDZHQZRZPHMG', 61], ['KEIDIFMUNPKU', 'DAZXEGUMLBRH', 54], ['IRZIQMFIQQTS', 'JYNGYRESTLDN', 33], ['VNDOEZQPAMPR', 'XUWVJPJRBZGT', 87], ['DKHUAKBFXVHW', 'PHZYCBWZLMQN', 91], ['KBFXTXXTEZTJ', 'PFBUIZZZASSP', 24], ['QPPWLGBHWOZJ', 'YYBFQZOFUREF', 41], ['WJKOZGBFREDI', 'XCNZYKNTIKJX', 12], ['JBYKRECCKOTQ', 'TTADHSPCHGIC', 61], ['YZDCTAHATJIM', 'TLOMOPFGGGTL', 56], ['QBKFDHRHREEC', 'FKGZFTZMKUHD', 20], ['PHCPBWKJCZSY', 'HTCKFHMBRISG', 54], ['VJUYETWQNZTU', 'ABOMMEYJJPDH', 29], ['BGRUTYSNBFMO', 'KSMYQWZNPKYF', 40], ['YVQQYQCUCPQF', 'PRXEJXRZBOXF', 22], ['EZNKHWKAORVA', 'DOSMAUKTZANY', 97], ['JZKSPKZTSPHQ', 'SMPTXRCXKTUU', 92], ['EMDLPRWYDRFF', 'RHRTJNNHKUFY', 62], ['BDXGAKKBNIKP', 'LTSKARDJKEXM', 27], ['AQKDGWNWKQLI', 'FHGUSFDCCFRF', 60], ['BKHUYGIWOOWK', 'HQOIGDLMNRMP', 70], ['XPUXMXPYCMAE', 'OTDYUKQESXMJ', 84], ['PVPBFDSSJJIW', 'NGQUFBJRSGDS', 23], ['KQWMRVTKVDKD', 'CREYZUNQGRDP', 14], ['MEBCNCWHFVLR', 'SQCFMQFOYBBG', 96], ['VQMQHHBGCSPK', 'FBIPFKRACFZA', 62], ['RKTEZERYVOCV', 'MOGMHRDSVHHW', 66], ['NSOTWGHPXPZS', 'JXQOWYKVIUTU', 44], ['NEEQAVOGSPXL', 'DQSAKMCMCLXK', 47], ['GSTVFRZOTGZU', 'RNVZWJLJNUKX', 21], ['RPALLVBJTXTP', 'ESTPLPLVZMZX', 62], ['ZDMWXVOFOQFU', 'XGBFTMXMZWWX', 12], ['QRISGPZADVPZ', 'ISIJEGJKVVEM', 64], ['LXUCXORRWWJF', 'BNUGSBZLJWUN', 24], ['PQNPFSNQFEZL', 'VOAMJAZQYVLM', 64], ['XDPCTAJFYGOF', 'ALDCHSWOHEBO', 71], ['TYVLIQODJMWJ', 'RELFFIYRIYAO', 66], ['EXVXEONOPKCY', 'COPRUNMWCXIV', 0], ['EENOUAXSMYUW', 'EVFNDLFJTDXU', 40], ['DTZMYGMAREYS', 'GLCLSZUVLBAF', 37], ['QGGPIZEVBVNY', 'KNFKEJQMHZKF', 2], ['QZCAINSSYWGH', 'MOMJLYDDGAWU', 47], ['PDYWQMRVTLAS', 'TJGGNJVQJRHY', 64], ['EVDLZUWFWRSJ', 'WDUFNRLEOFCO', 62], ['OMOCWGWYDFRF', 'PKUAMTMHMTUS', 26], ['XHCFQWRXSABR', 'DIAQJWBGMXXA', 64], ['FWNFPYZXSKIC', 'TGVVVQAQLAFR', 14], ['YUYQBIHFIUPH', 'RCJZQCANMNUW', 41], ['CZHFAJJMFTRK', 'OEDRIRAEOQIO', 90], ['XFJBNEJMILXP', 'PPLOCJPZFUPO', 85], ['ONJPZZWCJZMN', 'EROACCLBTFRT', 55], ['BWSPJPUXIDPJ', 'UIRFUUZCIKFS', 74], ['VNWNOCNHLKKZ', 'IXPCFZFWOYXK', 93], ['PMGSDDSTWWLF', 'FAELUNYMJBSQ', 44], ['VRKNNQCCNFZJ', 'RSIJMRLTVPPE', 42], ['RYVJGEQJXYGN', 'QJWXNJNBLZYM', 79], ['WLEOAQHSIOOD', 'LEWJRPLLGUST', 68], ['VBTQXEPWPQRH', 'JCDGHAWUHMXM', 22], ['FWCDQIBPTNVT', 'AMMYXKCLVEDK', 42], ['PRYIUYGUOOJW', 'KVRKUMLTSIVK', 65], ['DTIXJVKCMSUO', 'ATOHXUZTQJVC', 44], ['AEHMIBTJALBY', 'BTPOPXBLCUQG', 83], ['UUULFVDLTOTQ', 'KJAAJBPNDYWO', 21], ['SUSAWWEQCTZO', 'GSDQVWBAHESZ', 56], ['EEKFAHRPAJWV', 'MWCPISRXTUXQ', 92], ['PJGGGANUJUUS', 'VHPCHCKOJLZM', 82], ['LPALKRMGZHNV', 'UVOFJMHGHDZW', 77], ['DGWINEOBFQEY', 'RXWNSTZDULIK', 95], ['XKRWJFWRKJLK', 'SWOARSWGNYOD', 9], ['JGAZTICEQXRQ', 'AZUFYWQLDUTI', 3], ['GOJQESZSQOTL', 'BVKUZVMZOWNW', 80], ['YRWIGZHBEOXU', 'JGCURNPNQYUL', 37], ['VUXKHVIDSSHM', 'ZCBVRHAEYBYO', 37], ['RFTCNHTLJPTQ', 'FRPOUKZSPFML', 42], ['CQSUDPPCXZBS', 'EGQKQTYHQLPU', 61], ['ZKAIWRMITYDK', 'YBPMZNUTTRSB', 41], ['VLKVYMAJJXNW', 'QXXNYZENZBSI', 12], ['XAJVPBEMJKIE', 'WNUOESCDBOFH', 46], ['MOPXQDNCQLJN', 'EFGPOOEIUYWI', 76], ['CDZAYGSUGLSF', 'RJNONOJLGWTE', 23], ['SVDVVNUEGFZO', 'JKTKAYKCZEJV', 59], ['BPVZEYAYTCND', 'VSSTIKPKJGWA', 88], ['UIJWHIRZJJPH', 'FDZROLKLUUTU', 1], ['JEJWUUDSRDYB', 'WLOYXLSMWWWP', 82], ['XJKLUFLNJHMB', 'SEJHHADSFCAV', 35], ['TNAUMQXVAIKG', 'NJHHECVUFSXP', 5], ['TEXQZHMRIBJJ', 'LTIKLHFCIYDG', 70], ['IFWDVELUZJPT', 'TKMJDTHNUUMV', 16], ['JSWSVFIMEGJD', 'NEVAWFETYEPX', 1], ['TYETFFHVMSRH', 'ZNPUIMFMJFOQ', 96], ['CYESZGQGULJX', 'OLYURDBNRLZN', 10], ['QQSEBLMUDMMY', 'AIFQGZSPVHFS', 87], ['AKIVOQRVWWHC', 'MGUAFANTFGXO', 96], ['UJYXUCKMLSPE', 'CVSZAWBZGJOE', 73], ['FFYLWNJUWAOG', 'LQFOEYORIGIX', 94], ['YTBRHSVOAFAN', 'OKSGIBWGINWG', 47], ['LBYBYNEZFSWC', 'RYWUXXXUDKFV', 71], ['NVQIRYUAMRPA', 'UMBBRXSEFLFJ', 76], ['YGMKAAXWEGDO', 'MGWBEVNKLNDU', 60], ['PJSXEWSUTMWY', 'GQLXDDDJSTZX', 14], ['PXEWJFZNYFZD', 'OFGIYIPCNZOV', 88], ['XMNNWJFKDNNY', 'OHWWGGUEMLEL', 86], ['YCTAFKDICTYS', 'MYOLGZAUHCSX', 50], ['CHNVVCCZDPMH', 'HWLTUIEGLYVF', 24], ['OTKWBBGJSNPA', 'QBGIVIBVWJMY', 66], ['QTBOBWNEWWFN', 'JWSSSABAZKUH', 27], ['FTZBRTFCSFDW', 'QZPPBZVFKGND', 22], ['FTZFMYEXLUSI', 'XXZOEGEEWMUV', 4], ['XFLWCIAHWDCS', 'RHLFOMQHJGGT', 56], ['ONMSFTVWORGY', 'QUZXHQBVNHPD', 34], ['YZNELIDKXOKZ', 'QQGNUMCCVVHX', 51], ['HILZQSLFQLOW', 'EHUKYRQBKXMM', 81], ['UZISCTZBQYJZ', 'LUIEUOCGBHQS', 7], ['CWOSNKCMWGWG', 'XZINXKTIQMHT', 89], ['LLAMJWCBKQLZ', 'LDWVFXHIHOBQ', 9], ['GCRWLKALQVIV', 'WDUBOLURXDZU', 61], ['FEOCEWYGSVMD', 'YTWRLUKXMTMI', 79], ['JJRBJLLDKQDY', 'CYQHREFHOMUY', 90], ['EPTNQCGMILWR', 'ROBKYNKBRGXC', 57], ['SVJUAEUEWBPH', 'SCNXWJTHOBDS', 11], ['SFYELCAPXORD', 'JDLWNTAFDKIZ', 81], ['BUIYPSSYTGPL', 'GBICJNPCGAOZ', 18], ['YDZYQEMSQYFT', 'GTPIDZSFVBQW', 15], ['OFLDJCONONTM', 'HHONUZLAVETD', 18], ['RZCPGDJPWWUC', 'HEHYNTNSMPUI', 44], ['YNKZPLEROAEA', 'KBWRJMTHXXXP', 20], ['SQXVDDSWXKBL', 'XXJHUURDHFRU', 34], ['IXHKUDZRRHQA', 'HWJKXQVHGDKS', 68], ['FAIGFYMXSVZS', 'MSJGYIWHDRIQ', 79], ['RJPVHDDGHHMR', 'SQRYJJGONAVD', 79], ['MWHNSSVDCSEW', 'CUQKAYHEKWMA', 79], ['TUFKJNHDXNRX', 'EOSTNXSFCHCP', 46], ['GMBZEFVYMBSR', 'XPENZFUZNKAA', 56], ['PPVCPIVDIIDM', 'ZUTZETIFWQXG', 67], ['HESHVGPDLWMR', 'FACCACTUGVTL', 5], ['TGXYJLAZJUGH', 'UAXDMQSEQMTA', 49], ['AYJJLCHXWVXX', 'OYCSGZZXWPTK', 39]]

        result = [[['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100], ['AEEEFNPTVWXY', 'DEFGIJJMSSVW', 99], ['AEFLLLOUUZZZ', 'EIJKLMMMOPSV', 99], ['DFKLLORTUUUZ', 'HHIIJJJPRUWZ', 99], ['EFFHJKKKMNQZ', 'BEGGINPQVVYZ', 98], ['AAEHKKNORVWZ', 'AADKMNOSTUYZ', 97], ['ADFILQTUUWYZ', 'ACEGIJQQRTXZ', 97], ['BBBCFILOOQSV', 'CDDDDFIJKPZZ', 97]], []]
        
        self.assertEqual(analyze(results, 26, 138), result)

    def test_43(self):
        results = [['ZVJUKWHPNIQO', 'BRJCVKEMTRKU', 63], ['YIQJXUCATBIY', 'GOEBKTNEQOXU', 39], ['MHUVYBQSAQLC', 'NTNKUQYWYMIV', 58], ['YTVHOGSGFHQK', 'KLDMPPXWRVXK', 39], ['QYJZIZLVZBJR', 'HHRFSLDRCYBR', 66], ['NABGULQKKPSC', 'MYARMIMWUPQI', 33], ['MQEFHYWEQEQF', 'SKWTRINZKNHZ', 56], ['CFVLWYEPIHTD', 'VNVMOTETFNZS', 97], ['LUYFGOTQDNUW', 'LNOTZYAMBJDY', 15], ['AXLIHDJFQCND', 'SKAHGGPLJQDW', 26], ['XBAAGNTXAIKR', 'THCSSZBZUENU', 77], ['CHRKLIGSILMJ', 'DAIZUYKLLWRF', 48], ['SOXUJJGBOMOL', 'GMPUWAUQISEV', 74], ['BPYNVMYYQQRC', 'ALOAEDBOCYKS', 76], ['NFLVFKOJSKRO', 'LXOJVBXVZOZK', 16], ['PPVCXTPBMAEL', 'ZHFMTHBQFHXS', 76], ['ZKGHDFGCWFRG', 'SUTCSDSIFJTK', 88], ['OYVFIGWMZOWI', 'YGECHBKNYUWR', 44], ['KNXDGJJMKKPA', 'NGWWWPFNVXQM', 74], ['GABAUOHHKISI', 'WQCTSYPTQOAO', 46], ['MWYGNZAZUGKW', 'HICKBOFGUBBU', 81], ['IPLPYFHHDKCQ', 'YILGAMWIXWLS', 29], ['FKYXDSJIWQWX', 'XGOSDDUZJRAX', 8], ['PTICQYGEBHIH', 'WNXOHQMVOFSQ', 51], ['SVTGRKABFLVT', 'YQDMWUHWPTQW', 24], ['IRMMHZESILHY', 'HISSLSKXZQYI', 51], ['HLPQTTWPZQHH', 'LNWBQTBBXFYR', 47], ['BZMCBVIQMTRD', 'RXOFFOLYCNCW', 94], ['MHVWDCDUYNDG', 'PPUZPAUKVECW', 47], ['NCKGDMIOUCFA', 'AUEKROBRPTOS', 59], ['WNBNPIVCHGMR', 'ENLHLBAAYOJY', 93], ['WMKTQJWKKFDX', 'IIFOLFTGDCBP', 78], ['OIWAFYULUVBA', 'PPXMNMDOHQJY', 29], ['BGPZBTDUEVLY', 'BJZACXREPIEP', 79], ['QZHDRHLREVZF', 'YTQKJWOMDSBK', 0], ['YFHFNWUMQTXO', 'JUIIRSDRKZVG', 64], ['YTBJVGNBIANK', 'ZZWGRLMLTFQK', 6], ['FJZKABDMBXQR', 'XWHMHSEWPVUI', 9], ['RLTMZFUMVPFD', 'SAPFUDVUXMWN', 12], ['RBFMNUDAFXQT', 'RSFCBRKAAXTK', 60], ['DFDZJAYUBNIY', 'QAKYJQNDVSFJ', 0], ['AIUDHAIJMOUZ', 'NVEFIMYYMGYK', 19], ['JKNOADVQUTZY', 'AMDZPGUVRXAO', 14], ['RWZGJXAGRZIB', 'FHXYNYLTPCDJ', 21], ['RIMHNHUDCHYE', 'YVFOYMXOMPWL', 70], ['OTDPYQXTRZPY', 'LGECGEVJRRCB', 11], ['NACUFYQRJKBG', 'XVWKPSNJJFIM', 95], ['FDTBYTDUSOGQ', 'ZGKXDRSFIWLI', 32], ['BBFPVZINOPQH', 'DIJULBSCJMGR', 40], ['PBTBHRWXXADT', 'NRNIHRQDAHWD', 68], ['LUVBIWYQDHUM', 'OMZKEPTSFFFT', 72], ['UBATNOWFHMNP', 'GNGHHBDMOMSS', 43], ['QAZVAHCKMBTT', 'KWIIUHIWYRLM', 45], ['AKJVIHICULQT', 'OUOMMNQYMQVL', 55], ['GTEKJMWYQTEG', 'HKYVMPNPNTOX', 3], ['BXYSZCOUZAYK', 'RXGQIBOPRALN', 17], ['VZPSHAYQBAYJ', 'DAZENTPOGGLP', 91], ['EIPVUJZPSSWW', 'LLCAEBHPCIFM', 18], ['YHOBYPDCVDRF', 'IZDKIUXPZYAF', 90], ['OTPWEYCKGWCF', 'ZPRLOMKQEFIH', 52], ['OSPAVMUOOHCC', 'CYKDYDZNFBSY', 51], ['RWQSGDJSXABZ', 'PRYRYLWEVLPA', 13], ['YTDIZCYNYDMH', 'JRVZAPAJJAJR', 32], ['CDPZWKHBUJHN', 'VWLROBUEHZGZ', 67], ['KBWEVADGOVBJ', 'LJDEZUFSAXUX', 38], ['IFRNHGUUCCVP', 'UQWVTEUMTRXJ', 55], ['NIXPFMTBOTQD', 'JHGONFJBUBRS', 19], ['TDVPBBEYIRUT', 'CJBVVHEKSMPN', 56], ['PKGUXCSPOJIY', 'RRZPXELGRUOY', 34], ['OCIQLOBFSBBV', 'ZDZDCDDKFJPI', 97], ['ARZKETUFBBSJ', 'LPACWUGWHHXR', 14], ['VMCCGGFFCNHL', 'KDQKZCXEZXKV', 48], ['AFMZATESMICM', 'YRBBLDBRKIBG', 20], ['EXCIFGHIIIYW', 'TLATBFPWSUOY', 64], ['XMNYYPFSVXTV', 'TQUCEWLXSXPF', 36], ['JOWOIHWLSBSU', 'OFPCBACEAFLZ', 91], ['XGJNWDAZNQBS', 'JLACETXZZFGC', 48], ['BOANPTJMQYSX', 'VHIZOYILVBQO', 74], ['VGYBNQECUPEO', 'RABRJTMZGBFZ', 40], ['OAYGMXISJXWN', 'FUXYIJEZIAOK', 81], ['KDQXAPPLQLYH', 'AHNKYNEAGJAE', 5], ['EFXJEEAWXKFM', 'XMQLCIMRECNC', 53], ['TQRAWTGOWJAD', 'LEREHCJKZWOW', 37], ['PDMDWVNCRSET', 'PFORZIONAEGN', 86], ['EJSLEVABTAOW', 'TRERGQLWOTFV', 49], ['JDSKXIVTLQZS', 'VSEUXFTKEUVE', 63], ['ZWCUCUFPOUFR', 'CXLUZQMJINCL', 65], ['JHYRUBTEHPED', 'RUWQCOFYAFUT', 91], ['MJFHURPYVOBI', 'ABYZRFGISGHP', 7], ['HYEWEUDNRVES', 'YXPIPIEMLPFK', 34], ['FOTWRBBNMNAO', 'SRIPDFOAVPWN', 24], ['QUBPNNZYXDTC', 'EDWMRLJJSPWW', 51], ['ALFULLUZZOEZ', 'JSMOKLVIEMPM', 99], ['VGENYRDSSZAT', 'ZGWDOBDQZPEJ', 60], ['EQSRFRDPPHHX', 'FMRZAIKGCIRC', 20], ['ZTQJIKNXWALY', 'ORFLBEOXGQJP', 40], ['ZJRPZWYURGHL', 'JLNQTCDOUXTR', 12], ['TIOLRGSUORMX', 'CVLUSNOWXISR', 84], ['JIDEXUNBJCGP', 'UOCAHXYEPOGG', 92], ['OLALVLCSFSOE', 'YZTLJJQOXLFY', 27], ['PSEEIUELNNDT', 'JNHFOVHHTCUX', 93], ['XDZOGZVXUJTC', 'QGSCUBNUVVFT', 88], ['WYIMCWRCTCWH', 'AWIPZLCCEBCO', 26], ['MUYMPOAIIAWF', 'VUCVZMFXRNJD', 63], ['DRYASDRMEQIB', 'DVMVOQLZBRDN', 80], ['XULOEINLHWCP', 'PAPQYCJROHQJ', 86], ['FTMOXXOFFHGL', 'ZFLTESOYUFJO', 16], ['USDEKGIOUXQM', 'YNCMEJTXOGUM', 49], ['RFSMPQGIMUEL', 'QIKNHJAOGIRS', 30], ['YIUQGDTHJNXD', 'JJILUWKIGDJT', 47], ['IZUBECJNGOZB', 'JRZKKKOQZNXM', 64], ['AVKNGKGRHMPU', 'EKHFXQZJSOVG', 30], ['KOIEPBAUZYZB', 'XIDDPKYZVCHC', 82], ['QDZKPZWTCIHE', 'ILSCHPEGGFQT', 83], ['NNSEHTVORIKF', 'YPJIWWXHQIXE', 28], ['JUQFMHNKTOXL', 'UQILUJDHRYVC', 25], ['LHZZWWIYJOQX', 'ZTXEQXPLZIIY', 82], ['MLHOCNBGZFPN', 'WSUKNZZVULEY', 75], ['IPRIJBWJNDLA', 'DLQPCMJGQOOJ', 38], ['WOKUNBQGBMZA', 'XQFWTTFUORFB', 43], ['UGMWZVZAVVBS', 'WZVWEZXFFKXP', 12], ['MLDFTBNIOGYD', 'QQFSLOOOXKSN', 88], ['XCQKBAWZRKOF', 'IGBVSIXJHVEX', 44], ['QSEUPFOGOYSE', 'JQTDLAUVFLFA', 35], ['ZXDNYLCQPKKT', 'EOCNQEVWESMJ', 87], ['YJFEXXCSRXCS', 'MXJKZBRWOWKF', 59], ['GDXQIVFTCCKO', 'EUZLCEOCBOWR', 20], ['NDSAEWFLAFXH', 'NJMSNTZVVGVQ', 75], ['UGLAJTODYOUO', 'DHOHAEBOCRZD', 91], ['XEXVTTIHKROW', 'LWGJMWICFYGF', 91], ['JYDUTEPDRNCC', 'BQIQZRDVMPRU', 89], ['DRNTIKRELSHE', 'QRSYTIGRAINQ', 75], ['MALRDSBKORZG', 'QFVKPCFGVTPA', 26], ['PETLEOFDBZWH', 'FTRRUKQSCEOS', 27], ['VKNRYELHCUAG', 'PEVMRPGIOJOK', 20], ['MZHLEZOJTUWQ', 'CIPFVXTRXAPH', 43], ['PJJKWPRCOEKI', 'XADTFXXHEKRI', 80], ['RHWURHROGOWY', 'XHQIVCBMNYVS', 96], ['XRANUHKYWXYE', 'TYYGMFWXUVCW', 80], ['TZHLYSADSXYR', 'YCKSMCXEDZJT', 56], ['JWUGJCUYPMDY', 'OQRTKBPEEYZV', 44], ['HXEMIAWIWRFG', 'DXURSCEZQWEG', 75], ['ZXVCXJRCRYEW', 'DEEXOKUAQBCS', 79], ['DAGEKGVKUBSS', 'DORQRHMCFALM', 27], ['AOWNHNHVPAEV', 'PLORKAPBSHBO', 29], ['OASCAWUDMPYU', 'CAYMUKJZZNHI', 17], ['INSNPQZRIVNF', 'HGIMUAABFQLL', 96], ['QXQZATGRXNRO', 'SNOVHLHPWHHI', 17], ['WQSCSAQFHZMC', 'XUYEPZEGYKVM', 85], ['VAZKGFMJLHVA', 'AFFPZQARTBXY', 25], ['EXZKVFDJPSNW', 'TMODETZRFHSZ', 39], ['DKBAVHDSHYGP', 'LODBCMPVGWCO', 55], ['YSAYBCTQTJTI', 'AOTLCUDEQADK', 44], ['INLTVBNZFXRJ', 'RPOTFECPDQDD', 61], ['AHILJJIDTIDB', 'MHCQPHMCSSOZ', 77], ['XUUDZKURKMKP', 'BMUATKHQUCCZ', 94], ['ATHVASPCLCNM', 'QZSGVKCRJCCM', 83], ['WMSEQIOLXAFF', 'LVKHUNSKZFLI', 34], ['OOPCXYPNPJGP', 'YWUMMTSSDDJO', 83], ['KAZZTFDIAZLV', 'UFBKUMAVSFDT', 64], ['IADDKCJCLNVY', 'GDZHQZRZPHMG', 61], ['KEIDIFMUNPKU', 'DAZXEGUMLBRH', 54], ['IRZIQMFIQQTS', 'JYNGYRESTLDN', 33], ['VNDOEZQPAMPR', 'XUWVJPJRBZGT', 87], ['DKHUAKBFXVHW', 'PHZYCBWZLMQN', 91], ['KBFXTXXTEZTJ', 'PFBUIZZZASSP', 24], ['QPPWLGBHWOZJ', 'YYBFQZOFUREF', 41], ['WJKOZGBFREDI', 'XCNZYKNTIKJX', 12], ['JBYKRECCKOTQ', 'TTADHSPCHGIC', 61], ['YZDCTAHATJIM', 'TLOMOPFGGGTL', 56], ['QBKFDHRHREEC', 'FKGZFTZMKUHD', 20], ['PHCPBWKJCZSY', 'HTCKFHMBRISG', 54], ['VJUYETWQNZTU', 'ABOMMEYJJPDH', 29], ['BGRUTYSNBFMO', 'KSMYQWZNPKYF', 40], ['YVQQYQCUCPQF', 'PRXEJXRZBOXF', 22], ['EZNKHWKAORVA', 'DOSMAUKTZANY', 97], ['JZKSPKZTSPHQ', 'SMPTXRCXKTUU', 92], ['EMDLPRWYDRFF', 'RHRTJNNHKUFY', 62], ['BDXGAKKBNIKP', 'LTSKARDJKEXM', 27], ['AQKDGWNWKQLI', 'FHGUSFDCCFRF', 60], ['BKHUYGIWOOWK', 'HQOIGDLMNRMP', 70], ['XPUXMXPYCMAE', 'OTDYUKQESXMJ', 84], ['PVPBFDSSJJIW', 'NGQUFBJRSGDS', 23], ['KQWMRVTKVDKD', 'CREYZUNQGRDP', 14], ['MEBCNCWHFVLR', 'SQCFMQFOYBBG', 96], ['VQMQHHBGCSPK', 'FBIPFKRACFZA', 62], ['RKTEZERYVOCV', 'MOGMHRDSVHHW', 66], ['NSOTWGHPXPZS', 'JXQOWYKVIUTU', 44], ['NEEQAVOGSPXL', 'DQSAKMCMCLXK', 47], ['GSTVFRZOTGZU', 'RNVZWJLJNUKX', 21], ['RPALLVBJTXTP', 'ESTPLPLVZMZX', 62], ['ZDMWXVOFOQFU', 'XGBFTMXMZWWX', 12], ['QRISGPZADVPZ', 'ISIJEGJKVVEM', 64], ['LXUCXORRWWJF', 'BNUGSBZLJWUN', 24], ['PQNPFSNQFEZL', 'VOAMJAZQYVLM', 64], ['XDPCTAJFYGOF', 'ALDCHSWOHEBO', 71], ['TYVLIQODJMWJ', 'RELFFIYRIYAO', 66], ['EXVXEONOPKCY', 'COPRUNMWCXIV', 0], ['EENOUAXSMYUW', 'EVFNDLFJTDXU', 40], ['DTZMYGMAREYS', 'GLCLSZUVLBAF', 37], ['QGGPIZEVBVNY', 'KNFKEJQMHZKF', 2], ['QZCAINSSYWGH', 'MOMJLYDDGAWU', 47], ['PDYWQMRVTLAS', 'TJGGNJVQJRHY', 64], ['EVDLZUWFWRSJ', 'WDUFNRLEOFCO', 62], ['OMOCWGWYDFRF', 'PKUAMTMHMTUS', 26], ['XHCFQWRXSABR', 'DIAQJWBGMXXA', 64], ['FWNFPYZXSKIC', 'TGVVVQAQLAFR', 14], ['YUYQBIHFIUPH', 'RCJZQCANMNUW', 41], ['CZHFAJJMFTRK', 'OEDRIRAEOQIO', 90], ['XFJBNEJMILXP', 'PPLOCJPZFUPO', 85], ['ONJPZZWCJZMN', 'EROACCLBTFRT', 55], ['BWSPJPUXIDPJ', 'UIRFUUZCIKFS', 74], ['VNWNOCNHLKKZ', 'IXPCFZFWOYXK', 93], ['PMGSDDSTWWLF', 'FAELUNYMJBSQ', 44], ['VRKNNQCCNFZJ', 'RSIJMRLTVPPE', 42], ['RYVJGEQJXYGN', 'QJWXNJNBLZYM', 79], ['WLEOAQHSIOOD', 'LEWJRPLLGUST', 68], ['VBTQXEPWPQRH', 'JCDGHAWUHMXM', 22], ['FWCDQIBPTNVT', 'AMMYXKCLVEDK', 42], ['PRYIUYGUOOJW', 'KVRKUMLTSIVK', 65], ['DTIXJVKCMSUO', 'ATOHXUZTQJVC', 44], ['AEHMIBTJALBY', 'BTPOPXBLCUQG', 83], ['UUULFVDLTOTQ', 'KJAAJBPNDYWO', 21], ['SUSAWWEQCTZO', 'GSDQVWBAHESZ', 56], ['EEKFAHRPAJWV', 'MWCPISRXTUXQ', 92], ['PJGGGANUJUUS', 'VHPCHCKOJLZM', 82], ['LPALKRMGZHNV', 'UVOFJMHGHDZW', 77], ['DGWINEOBFQEY', 'RXWNSTZDULIK', 95], ['XKRWJFWRKJLK', 'SWOARSWGNYOD', 9], ['JGAZTICEQXRQ', 'AZUFYWQLDUTI', 3], ['GOJQESZSQOTL', 'BVKUZVMZOWNW', 80], ['YRWIGZHBEOXU', 'JGCURNPNQYUL', 37], ['VUXKHVIDSSHM', 'ZCBVRHAEYBYO', 37], ['RFTCNHTLJPTQ', 'FRPOUKZSPFML', 42], ['CQSUDPPCXZBS', 'EGQKQTYHQLPU', 61], ['ZKAIWRMITYDK', 'YBPMZNUTTRSB', 41], ['VLKVYMAJJXNW', 'QXXNYZENZBSI', 12], ['XAJVPBEMJKIE', 'WNUOESCDBOFH', 46], ['MOPXQDNCQLJN', 'EFGPOOEIUYWI', 76], ['CDZAYGSUGLSF', 'RJNONOJLGWTE', 23], ['SVDVVNUEGFZO', 'JKTKAYKCZEJV', 59], ['BPVZEYAYTCND', 'VSSTIKPKJGWA', 88], ['UIJWHIRZJJPH', 'FDZROLKLUUTU', 1], ['JEJWUUDSRDYB', 'WLOYXLSMWWWP', 82], ['XJKLUFLNJHMB', 'SEJHHADSFCAV', 35], ['TNAUMQXVAIKG', 'NJHHECVUFSXP', 5], ['TEXQZHMRIBJJ', 'LTIKLHFCIYDG', 70], ['IFWDVELUZJPT', 'TKMJDTHNUUMV', 16], ['JSWSVFIMEGJD', 'NEVAWFETYEPX', 1], ['TYETFFHVMSRH', 'ZNPUIMFMJFOQ', 96], ['CYESZGQGULJX', 'OLYURDBNRLZN', 10], ['QQSEBLMUDMMY', 'AIFQGZSPVHFS', 87], ['AKIVOQRVWWHC', 'MGUAFANTFGXO', 96], ['UJYXUCKMLSPE', 'CVSZAWBZGJOE', 73], ['FFYLWNJUWAOG', 'LQFOEYORIGIX', 94], ['YTBRHSVOAFAN', 'OKSGIBWGINWG', 47], ['LBYBYNEZFSWC', 'RYWUXXXUDKFV', 71], ['NVQIRYUAMRPA', 'UMBBRXSEFLFJ', 76], ['YGMKAAXWEGDO', 'MGWBEVNKLNDU', 60], ['PJSXEWSUTMWY', 'GQLXDDDJSTZX', 14], ['PXEWJFZNYFZD', 'OFGIYIPCNZOV', 88], ['XMNNWJFKDNNY', 'OHWWGGUEMLEL', 86], ['YCTAFKDICTYS', 'MYOLGZAUHCSX', 50], ['CHNVVCCZDPMH', 'HWLTUIEGLYVF', 24], ['OTKWBBGJSNPA', 'QBGIVIBVWJMY', 66], ['QTBOBWNEWWFN', 'JWSSSABAZKUH', 27], ['FTZBRTFCSFDW', 'QZPPBZVFKGND', 22], ['FTZFMYEXLUSI', 'XXZOEGEEWMUV', 4], ['XFLWCIAHWDCS', 'RHLFOMQHJGGT', 56], ['ONMSFTVWORGY', 'QUZXHQBVNHPD', 34], ['YZNELIDKXOKZ', 'QQGNUMCCVVHX', 51], ['HILZQSLFQLOW', 'EHUKYRQBKXMM', 81], ['UZISCTZBQYJZ', 'LUIEUOCGBHQS', 7], ['CWOSNKCMWGWG', 'XZINXKTIQMHT', 89], ['LLAMJWCBKQLZ', 'LDWVFXHIHOBQ', 9], ['GCRWLKALQVIV', 'WDUBOLURXDZU', 61], ['FEOCEWYGSVMD', 'YTWRLUKXMTMI', 79], ['JJRBJLLDKQDY', 'CYQHREFHOMUY', 90], ['EPTNQCGMILWR', 'ROBKYNKBRGXC', 57], ['SVJUAEUEWBPH', 'SCNXWJTHOBDS', 11], ['SFYELCAPXORD', 'JDLWNTAFDKIZ', 81], ['BUIYPSSYTGPL', 'GBICJNPCGAOZ', 18], ['YDZYQEMSQYFT', 'GTPIDZSFVBQW', 15], ['OFLDJCONONTM', 'HHONUZLAVETD', 18], ['RZCPGDJPWWUC', 'HEHYNTNSMPUI', 44], ['YNKZPLEROAEA', 'KBWRJMTHXXXP', 20], ['SQXVDDSWXKBL', 'XXJHUURDHFRU', 34], ['IXHKUDZRRHQA', 'HWJKXQVHGDKS', 68], ['FAIGFYMXSVZS', 'MSJGYIWHDRIQ', 79], ['RJPVHDDGHHMR', 'SQRYJJGONAVD', 79], ['MWHNSSVDCSEW', 'CUQKAYHEKWMA', 79], ['TUFKJNHDXNRX', 'EOSTNXSFCHCP', 46], ['GMBZEFVYMBSR', 'XPENZFUZNKAA', 56], ['PPVCPIVDIIDM', 'ZUTZETIFWQXG', 67], ['HESHVGPDLWMR', 'FACCACTUGVTL', 5], ['TGXYJLAZJUGH', 'UAXDMQSEQMTA', 49], ['AYJJLCHXWVXX', 'OYCSGZZXWPTK', 39]]

        result = [[['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100], ['AEEEFNPTVWXY', 'DEFGIJJMSSVW', 99], ['AEFLLLOUUZZZ', 'EIJKLMMMOPSV', 99], ['DFKLLORTUUUZ', 'HHIIJJJPRUWZ', 99], ['EFFHJKKKMNQZ', 'BEGGINPQVVYZ', 98], ['AAEHKKNORVWZ', 'AADKMNOSTUYZ', 97], ['ADFILQTUUWYZ', 'ACEGIJQQRTXZ', 97], ['BBBCFILOOQSV', 'CDDDDFIJKPZZ', 97]], [['ACDFGGLSSUYZ', 'EGJJLNNOORTW', 23], ['BCEHNSSTUUZZ', 'AAABGIKNRTXX', 23], ['BDFIJJPPSSVW', 'BDFGGJNQRSSU', 23], ['CCHHMMOPQSSZ', 'ABDDHIIIJJLT', 23], ['DFGHHJMOUVWZ', 'AGHKLLMNPRVZ', 23]]]
        
        self.assertEqual(analyze(results, 26, 23), result)
        
    def test_44(self):
        results = [['ZVJUKWHPNIQO', 'BRJCVKEMTRKU', 63], ['YIQJXUCATBIY', 'GOEBKTNEQOXU', 39], ['MHUVYBQSAQLC', 'NTNKUQYWYMIV', 58], ['YTVHOGSGFHQK', 'KLDMPPXWRVXK', 39], ['QYJZIZLVZBJR', 'HHRFSLDRCYBR', 66], ['NABGULQKKPSC', 'MYARMIMWUPQI', 33], ['MQEFHYWEQEQF', 'SKWTRINZKNHZ', 56], ['CFVLWYEPIHTD', 'VNVMOTETFNZS', 97], ['LUYFGOTQDNUW', 'LNOTZYAMBJDY', 15], ['AXLIHDJFQCND', 'SKAHGGPLJQDW', 26], ['XBAAGNTXAIKR', 'THCSSZBZUENU', 77], ['CHRKLIGSILMJ', 'DAIZUYKLLWRF', 48], ['SOXUJJGBOMOL', 'GMPUWAUQISEV', 74], ['BPYNVMYYQQRC', 'ALOAEDBOCYKS', 76], ['NFLVFKOJSKRO', 'LXOJVBXVZOZK', 16], ['PPVCXTPBMAEL', 'ZHFMTHBQFHXS', 76], ['ZKGHDFGCWFRG', 'SUTCSDSIFJTK', 88], ['OYVFIGWMZOWI', 'YGECHBKNYUWR', 44], ['KNXDGJJMKKPA', 'NGWWWPFNVXQM', 74], ['GABAUOHHKISI', 'WQCTSYPTQOAO', 46], ['MWYGNZAZUGKW', 'HICKBOFGUBBU', 81], ['IPLPYFHHDKCQ', 'YILGAMWIXWLS', 29], ['FKYXDSJIWQWX', 'XGOSDDUZJRAX', 8], ['PTICQYGEBHIH', 'WNXOHQMVOFSQ', 51], ['SVTGRKABFLVT', 'YQDMWUHWPTQW', 24], ['IRMMHZESILHY', 'HISSLSKXZQYI', 51], ['HLPQTTWPZQHH', 'LNWBQTBBXFYR', 47], ['BZMCBVIQMTRD', 'RXOFFOLYCNCW', 94], ['MHVWDCDUYNDG', 'PPUZPAUKVECW', 47], ['NCKGDMIOUCFA', 'AUEKROBRPTOS', 59], ['WNBNPIVCHGMR', 'ENLHLBAAYOJY', 93], ['WMKTQJWKKFDX', 'IIFOLFTGDCBP', 78], ['OIWAFYULUVBA', 'PPXMNMDOHQJY', 29], ['BGPZBTDUEVLY', 'BJZACXREPIEP', 79], ['QZHDRHLREVZF', 'YTQKJWOMDSBK', 0], ['YFHFNWUMQTXO', 'JUIIRSDRKZVG', 64], ['YTBJVGNBIANK', 'ZZWGRLMLTFQK', 6], ['FJZKABDMBXQR', 'XWHMHSEWPVUI', 9], ['RLTMZFUMVPFD', 'SAPFUDVUXMWN', 12], ['RBFMNUDAFXQT', 'RSFCBRKAAXTK', 60], ['DFDZJAYUBNIY', 'QAKYJQNDVSFJ', 0], ['AIUDHAIJMOUZ', 'NVEFIMYYMGYK', 19], ['JKNOADVQUTZY', 'AMDZPGUVRXAO', 14], ['RWZGJXAGRZIB', 'FHXYNYLTPCDJ', 21], ['RIMHNHUDCHYE', 'YVFOYMXOMPWL', 70], ['OTDPYQXTRZPY', 'LGECGEVJRRCB', 11], ['NACUFYQRJKBG', 'XVWKPSNJJFIM', 95], ['FDTBYTDUSOGQ', 'ZGKXDRSFIWLI', 32], ['BBFPVZINOPQH', 'DIJULBSCJMGR', 40], ['PBTBHRWXXADT', 'NRNIHRQDAHWD', 68], ['LUVBIWYQDHUM', 'OMZKEPTSFFFT', 72], ['UBATNOWFHMNP', 'GNGHHBDMOMSS', 43], ['QAZVAHCKMBTT', 'KWIIUHIWYRLM', 45], ['AKJVIHICULQT', 'OUOMMNQYMQVL', 55], ['GTEKJMWYQTEG', 'HKYVMPNPNTOX', 3], ['BXYSZCOUZAYK', 'RXGQIBOPRALN', 17], ['VZPSHAYQBAYJ', 'DAZENTPOGGLP', 91], ['EIPVUJZPSSWW', 'LLCAEBHPCIFM', 18], ['YHOBYPDCVDRF', 'IZDKIUXPZYAF', 90], ['OTPWEYCKGWCF', 'ZPRLOMKQEFIH', 52], ['OSPAVMUOOHCC', 'CYKDYDZNFBSY', 51], ['RWQSGDJSXABZ', 'PRYRYLWEVLPA', 13], ['YTDIZCYNYDMH', 'JRVZAPAJJAJR', 32], ['CDPZWKHBUJHN', 'VWLROBUEHZGZ', 67], ['KBWEVADGOVBJ', 'LJDEZUFSAXUX', 38], ['IFRNHGUUCCVP', 'UQWVTEUMTRXJ', 55], ['NIXPFMTBOTQD', 'JHGONFJBUBRS', 19], ['TDVPBBEYIRUT', 'CJBVVHEKSMPN', 56], ['PKGUXCSPOJIY', 'RRZPXELGRUOY', 34], ['OCIQLOBFSBBV', 'ZDZDCDDKFJPI', 97], ['ARZKETUFBBSJ', 'LPACWUGWHHXR', 14], ['VMCCGGFFCNHL', 'KDQKZCXEZXKV', 48], ['AFMZATESMICM', 'YRBBLDBRKIBG', 20], ['EXCIFGHIIIYW', 'TLATBFPWSUOY', 64], ['XMNYYPFSVXTV', 'TQUCEWLXSXPF', 36], ['JOWOIHWLSBSU', 'OFPCBACEAFLZ', 91], ['XGJNWDAZNQBS', 'JLACETXZZFGC', 48], ['BOANPTJMQYSX', 'VHIZOYILVBQO', 74], ['VGYBNQECUPEO', 'RABRJTMZGBFZ', 40], ['OAYGMXISJXWN', 'FUXYIJEZIAOK', 81], ['KDQXAPPLQLYH', 'AHNKYNEAGJAE', 5], ['EFXJEEAWXKFM', 'XMQLCIMRECNC', 53], ['TQRAWTGOWJAD', 'LEREHCJKZWOW', 37], ['PDMDWVNCRSET', 'PFORZIONAEGN', 86], ['EJSLEVABTAOW', 'TRERGQLWOTFV', 49], ['JDSKXIVTLQZS', 'VSEUXFTKEUVE', 63], ['ZWCUCUFPOUFR', 'CXLUZQMJINCL', 65], ['JHYRUBTEHPED', 'RUWQCOFYAFUT', 91], ['MJFHURPYVOBI', 'ABYZRFGISGHP', 7], ['HYEWEUDNRVES', 'YXPIPIEMLPFK', 34], ['FOTWRBBNMNAO', 'SRIPDFOAVPWN', 24], ['QUBPNNZYXDTC', 'EDWMRLJJSPWW', 51], ['ALFULLUZZOEZ', 'JSMOKLVIEMPM', 99], ['VGENYRDSSZAT', 'ZGWDOBDQZPEJ', 60], ['EQSRFRDPPHHX', 'FMRZAIKGCIRC', 20], ['ZTQJIKNXWALY', 'ORFLBEOXGQJP', 40], ['ZJRPZWYURGHL', 'JLNQTCDOUXTR', 12], ['TIOLRGSUORMX', 'CVLUSNOWXISR', 84], ['JIDEXUNBJCGP', 'UOCAHXYEPOGG', 92], ['OLALVLCSFSOE', 'YZTLJJQOXLFY', 27], ['PSEEIUELNNDT', 'JNHFOVHHTCUX', 93], ['XDZOGZVXUJTC', 'QGSCUBNUVVFT', 88], ['WYIMCWRCTCWH', 'AWIPZLCCEBCO', 26], ['MUYMPOAIIAWF', 'VUCVZMFXRNJD', 63], ['DRYASDRMEQIB', 'DVMVOQLZBRDN', 80], ['XULOEINLHWCP', 'PAPQYCJROHQJ', 86], ['FTMOXXOFFHGL', 'ZFLTESOYUFJO', 16], ['USDEKGIOUXQM', 'YNCMEJTXOGUM', 49], ['RFSMPQGIMUEL', 'QIKNHJAOGIRS', 30], ['YIUQGDTHJNXD', 'JJILUWKIGDJT', 47], ['IZUBECJNGOZB', 'JRZKKKOQZNXM', 64], ['AVKNGKGRHMPU', 'EKHFXQZJSOVG', 30], ['KOIEPBAUZYZB', 'XIDDPKYZVCHC', 82], ['QDZKPZWTCIHE', 'ILSCHPEGGFQT', 83], ['NNSEHTVORIKF', 'YPJIWWXHQIXE', 28], ['JUQFMHNKTOXL', 'UQILUJDHRYVC', 25], ['LHZZWWIYJOQX', 'ZTXEQXPLZIIY', 82], ['MLHOCNBGZFPN', 'WSUKNZZVULEY', 75], ['IPRIJBWJNDLA', 'DLQPCMJGQOOJ', 38], ['WOKUNBQGBMZA', 'XQFWTTFUORFB', 43], ['UGMWZVZAVVBS', 'WZVWEZXFFKXP', 12], ['MLDFTBNIOGYD', 'QQFSLOOOXKSN', 88], ['XCQKBAWZRKOF', 'IGBVSIXJHVEX', 44], ['QSEUPFOGOYSE', 'JQTDLAUVFLFA', 35], ['ZXDNYLCQPKKT', 'EOCNQEVWESMJ', 87], ['YJFEXXCSRXCS', 'MXJKZBRWOWKF', 59], ['GDXQIVFTCCKO', 'EUZLCEOCBOWR', 20], ['NDSAEWFLAFXH', 'NJMSNTZVVGVQ', 75], ['UGLAJTODYOUO', 'DHOHAEBOCRZD', 91], ['XEXVTTIHKROW', 'LWGJMWICFYGF', 91], ['JYDUTEPDRNCC', 'BQIQZRDVMPRU', 89], ['DRNTIKRELSHE', 'QRSYTIGRAINQ', 75], ['MALRDSBKORZG', 'QFVKPCFGVTPA', 26], ['PETLEOFDBZWH', 'FTRRUKQSCEOS', 27], ['VKNRYELHCUAG', 'PEVMRPGIOJOK', 20], ['MZHLEZOJTUWQ', 'CIPFVXTRXAPH', 43], ['PJJKWPRCOEKI', 'XADTFXXHEKRI', 80], ['RHWURHROGOWY', 'XHQIVCBMNYVS', 96], ['XRANUHKYWXYE', 'TYYGMFWXUVCW', 80], ['TZHLYSADSXYR', 'YCKSMCXEDZJT', 56], ['JWUGJCUYPMDY', 'OQRTKBPEEYZV', 44], ['HXEMIAWIWRFG', 'DXURSCEZQWEG', 75], ['ZXVCXJRCRYEW', 'DEEXOKUAQBCS', 79], ['DAGEKGVKUBSS', 'DORQRHMCFALM', 27], ['AOWNHNHVPAEV', 'PLORKAPBSHBO', 29], ['OASCAWUDMPYU', 'CAYMUKJZZNHI', 17], ['INSNPQZRIVNF', 'HGIMUAABFQLL', 96], ['QXQZATGRXNRO', 'SNOVHLHPWHHI', 17], ['WQSCSAQFHZMC', 'XUYEPZEGYKVM', 85], ['VAZKGFMJLHVA', 'AFFPZQARTBXY', 25], ['EXZKVFDJPSNW', 'TMODETZRFHSZ', 39], ['DKBAVHDSHYGP', 'LODBCMPVGWCO', 55], ['YSAYBCTQTJTI', 'AOTLCUDEQADK', 44], ['INLTVBNZFXRJ', 'RPOTFECPDQDD', 61], ['AHILJJIDTIDB', 'MHCQPHMCSSOZ', 77], ['XUUDZKURKMKP', 'BMUATKHQUCCZ', 94], ['ATHVASPCLCNM', 'QZSGVKCRJCCM', 83], ['WMSEQIOLXAFF', 'LVKHUNSKZFLI', 34], ['OOPCXYPNPJGP', 'YWUMMTSSDDJO', 83], ['KAZZTFDIAZLV', 'UFBKUMAVSFDT', 64], ['IADDKCJCLNVY', 'GDZHQZRZPHMG', 61], ['KEIDIFMUNPKU', 'DAZXEGUMLBRH', 54], ['IRZIQMFIQQTS', 'JYNGYRESTLDN', 33], ['VNDOEZQPAMPR', 'XUWVJPJRBZGT', 87], ['DKHUAKBFXVHW', 'PHZYCBWZLMQN', 91], ['KBFXTXXTEZTJ', 'PFBUIZZZASSP', 24], ['QPPWLGBHWOZJ', 'YYBFQZOFUREF', 41], ['WJKOZGBFREDI', 'XCNZYKNTIKJX', 12], ['JBYKRECCKOTQ', 'TTADHSPCHGIC', 61], ['YZDCTAHATJIM', 'TLOMOPFGGGTL', 56], ['QBKFDHRHREEC', 'FKGZFTZMKUHD', 20], ['PHCPBWKJCZSY', 'HTCKFHMBRISG', 54], ['VJUYETWQNZTU', 'ABOMMEYJJPDH', 29], ['BGRUTYSNBFMO', 'KSMYQWZNPKYF', 40], ['YVQQYQCUCPQF', 'PRXEJXRZBOXF', 22], ['EZNKHWKAORVA', 'DOSMAUKTZANY', 97], ['JZKSPKZTSPHQ', 'SMPTXRCXKTUU', 92], ['EMDLPRWYDRFF', 'RHRTJNNHKUFY', 62], ['BDXGAKKBNIKP', 'LTSKARDJKEXM', 27], ['AQKDGWNWKQLI', 'FHGUSFDCCFRF', 60], ['BKHUYGIWOOWK', 'HQOIGDLMNRMP', 70], ['XPUXMXPYCMAE', 'OTDYUKQESXMJ', 84], ['PVPBFDSSJJIW', 'NGQUFBJRSGDS', 23], ['KQWMRVTKVDKD', 'CREYZUNQGRDP', 14], ['MEBCNCWHFVLR', 'SQCFMQFOYBBG', 96], ['VQMQHHBGCSPK', 'FBIPFKRACFZA', 62], ['RKTEZERYVOCV', 'MOGMHRDSVHHW', 66], ['NSOTWGHPXPZS', 'JXQOWYKVIUTU', 44], ['NEEQAVOGSPXL', 'DQSAKMCMCLXK', 47], ['GSTVFRZOTGZU', 'RNVZWJLJNUKX', 21], ['RPALLVBJTXTP', 'ESTPLPLVZMZX', 62], ['ZDMWXVOFOQFU', 'XGBFTMXMZWWX', 12], ['QRISGPZADVPZ', 'ISIJEGJKVVEM', 64], ['LXUCXORRWWJF', 'BNUGSBZLJWUN', 24], ['PQNPFSNQFEZL', 'VOAMJAZQYVLM', 64], ['XDPCTAJFYGOF', 'ALDCHSWOHEBO', 71], ['TYVLIQODJMWJ', 'RELFFIYRIYAO', 66], ['EXVXEONOPKCY', 'COPRUNMWCXIV', 0], ['EENOUAXSMYUW', 'EVFNDLFJTDXU', 40], ['DTZMYGMAREYS', 'GLCLSZUVLBAF', 37], ['QGGPIZEVBVNY', 'KNFKEJQMHZKF', 2], ['QZCAINSSYWGH', 'MOMJLYDDGAWU', 47], ['PDYWQMRVTLAS', 'TJGGNJVQJRHY', 64], ['EVDLZUWFWRSJ', 'WDUFNRLEOFCO', 62], ['OMOCWGWYDFRF', 'PKUAMTMHMTUS', 26], ['XHCFQWRXSABR', 'DIAQJWBGMXXA', 64], ['FWNFPYZXSKIC', 'TGVVVQAQLAFR', 14], ['YUYQBIHFIUPH', 'RCJZQCANMNUW', 41], ['CZHFAJJMFTRK', 'OEDRIRAEOQIO', 90], ['XFJBNEJMILXP', 'PPLOCJPZFUPO', 85], ['ONJPZZWCJZMN', 'EROACCLBTFRT', 55], ['BWSPJPUXIDPJ', 'UIRFUUZCIKFS', 74], ['VNWNOCNHLKKZ', 'IXPCFZFWOYXK', 93], ['PMGSDDSTWWLF', 'FAELUNYMJBSQ', 44], ['VRKNNQCCNFZJ', 'RSIJMRLTVPPE', 42], ['RYVJGEQJXYGN', 'QJWXNJNBLZYM', 79], ['WLEOAQHSIOOD', 'LEWJRPLLGUST', 68], ['VBTQXEPWPQRH', 'JCDGHAWUHMXM', 22], ['FWCDQIBPTNVT', 'AMMYXKCLVEDK', 42], ['PRYIUYGUOOJW', 'KVRKUMLTSIVK', 65], ['DTIXJVKCMSUO', 'ATOHXUZTQJVC', 44], ['AEHMIBTJALBY', 'BTPOPXBLCUQG', 83], ['UUULFVDLTOTQ', 'KJAAJBPNDYWO', 21], ['SUSAWWEQCTZO', 'GSDQVWBAHESZ', 56], ['EEKFAHRPAJWV', 'MWCPISRXTUXQ', 92], ['PJGGGANUJUUS', 'VHPCHCKOJLZM', 82], ['LPALKRMGZHNV', 'UVOFJMHGHDZW', 77], ['DGWINEOBFQEY', 'RXWNSTZDULIK', 95], ['XKRWJFWRKJLK', 'SWOARSWGNYOD', 9], ['JGAZTICEQXRQ', 'AZUFYWQLDUTI', 3], ['GOJQESZSQOTL', 'BVKUZVMZOWNW', 80], ['YRWIGZHBEOXU', 'JGCURNPNQYUL', 37], ['VUXKHVIDSSHM', 'ZCBVRHAEYBYO', 37], ['RFTCNHTLJPTQ', 'FRPOUKZSPFML', 42], ['CQSUDPPCXZBS', 'EGQKQTYHQLPU', 61], ['ZKAIWRMITYDK', 'YBPMZNUTTRSB', 41], ['VLKVYMAJJXNW', 'QXXNYZENZBSI', 12], ['XAJVPBEMJKIE', 'WNUOESCDBOFH', 46], ['MOPXQDNCQLJN', 'EFGPOOEIUYWI', 76], ['CDZAYGSUGLSF', 'RJNONOJLGWTE', 23], ['SVDVVNUEGFZO', 'JKTKAYKCZEJV', 59], ['BPVZEYAYTCND', 'VSSTIKPKJGWA', 88], ['UIJWHIRZJJPH', 'FDZROLKLUUTU', 1], ['JEJWUUDSRDYB', 'WLOYXLSMWWWP', 82], ['XJKLUFLNJHMB', 'SEJHHADSFCAV', 35], ['TNAUMQXVAIKG', 'NJHHECVUFSXP', 5], ['TEXQZHMRIBJJ', 'LTIKLHFCIYDG', 70], ['IFWDVELUZJPT', 'TKMJDTHNUUMV', 16], ['JSWSVFIMEGJD', 'NEVAWFETYEPX', 1], ['TYETFFHVMSRH', 'ZNPUIMFMJFOQ', 96], ['CYESZGQGULJX', 'OLYURDBNRLZN', 10], ['QQSEBLMUDMMY', 'AIFQGZSPVHFS', 87], ['AKIVOQRVWWHC', 'MGUAFANTFGXO', 96], ['UJYXUCKMLSPE', 'CVSZAWBZGJOE', 73], ['FFYLWNJUWAOG', 'LQFOEYORIGIX', 94], ['YTBRHSVOAFAN', 'OKSGIBWGINWG', 47], ['LBYBYNEZFSWC', 'RYWUXXXUDKFV', 71], ['NVQIRYUAMRPA', 'UMBBRXSEFLFJ', 76], ['YGMKAAXWEGDO', 'MGWBEVNKLNDU', 60], ['PJSXEWSUTMWY', 'GQLXDDDJSTZX', 14], ['PXEWJFZNYFZD', 'OFGIYIPCNZOV', 88], ['XMNNWJFKDNNY', 'OHWWGGUEMLEL', 86], ['YCTAFKDICTYS', 'MYOLGZAUHCSX', 50], ['CHNVVCCZDPMH', 'HWLTUIEGLYVF', 24], ['OTKWBBGJSNPA', 'QBGIVIBVWJMY', 66], ['QTBOBWNEWWFN', 'JWSSSABAZKUH', 27], ['FTZBRTFCSFDW', 'QZPPBZVFKGND', 22], ['FTZFMYEXLUSI', 'XXZOEGEEWMUV', 4], ['XFLWCIAHWDCS', 'RHLFOMQHJGGT', 56], ['ONMSFTVWORGY', 'QUZXHQBVNHPD', 34], ['YZNELIDKXOKZ', 'QQGNUMCCVVHX', 51], ['HILZQSLFQLOW', 'EHUKYRQBKXMM', 81], ['UZISCTZBQYJZ', 'LUIEUOCGBHQS', 7], ['CWOSNKCMWGWG', 'XZINXKTIQMHT', 89], ['LLAMJWCBKQLZ', 'LDWVFXHIHOBQ', 9], ['GCRWLKALQVIV', 'WDUBOLURXDZU', 61], ['FEOCEWYGSVMD', 'YTWRLUKXMTMI', 79], ['JJRBJLLDKQDY', 'CYQHREFHOMUY', 90], ['EPTNQCGMILWR', 'ROBKYNKBRGXC', 57], ['SVJUAEUEWBPH', 'SCNXWJTHOBDS', 11], ['SFYELCAPXORD', 'JDLWNTAFDKIZ', 81], ['BUIYPSSYTGPL', 'GBICJNPCGAOZ', 18], ['YDZYQEMSQYFT', 'GTPIDZSFVBQW', 15], ['OFLDJCONONTM', 'HHONUZLAVETD', 18], ['RZCPGDJPWWUC', 'HEHYNTNSMPUI', 44], ['YNKZPLEROAEA', 'KBWRJMTHXXXP', 20], ['SQXVDDSWXKBL', 'XXJHUURDHFRU', 34], ['IXHKUDZRRHQA', 'HWJKXQVHGDKS', 68], ['FAIGFYMXSVZS', 'MSJGYIWHDRIQ', 79], ['RJPVHDDGHHMR', 'SQRYJJGONAVD', 79], ['MWHNSSVDCSEW', 'CUQKAYHEKWMA', 79], ['TUFKJNHDXNRX', 'EOSTNXSFCHCP', 46], ['GMBZEFVYMBSR', 'XPENZFUZNKAA', 56], ['PPVCPIVDIIDM', 'ZUTZETIFWQXG', 67], ['HESHVGPDLWMR', 'FACCACTUGVTL', 5], ['TGXYJLAZJUGH', 'UAXDMQSEQMTA', 49], ['AYJJLCHXWVXX', 'OYCSGZZXWPTK', 39]]

        result = [[['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100], ['AEEEFNPTVWXY', 'DEFGIJJMSSVW', 99], ['AEFLLLOUUZZZ', 'EIJKLMMMOPSV', 99], ['DFKLLORTUUUZ', 'HHIIJJJPRUWZ', 99], ['EFFHJKKKMNQZ', 'BEGGINPQVVYZ', 98], ['AAEHKKNORVWZ', 'AADKMNOSTUYZ', 97], ['ADFILQTUUWYZ', 'ACEGIJQQRTXZ', 97], ['BBBCFILOOQSV', 'CDDDDFIJKPZZ', 97]], [['ABDDFIJNUYYZ', 'ADFJJKNQQSVY', 0], ['CEEKNOOPVXXY', 'CCIMNOPRUVWX', 0], ['DEFHHLQRRVZZ', 'BDJKKMOQSTWY', 0]]]
        
        self.assertEqual(analyze(results, 26, 0), result)
        
    def test_45(self):
        results = [['ZVJUKWHPNIQO', 'BRJCVKEMTRKU', 63], ['YIQJXUCATBIY', 'GOEBKTNEQOXU', 39], ['MHUVYBQSAQLC', 'NTNKUQYWYMIV', 58], ['YTVHOGSGFHQK', 'KLDMPPXWRVXK', 39], ['QYJZIZLVZBJR', 'HHRFSLDRCYBR', 66], ['NABGULQKKPSC', 'MYARMIMWUPQI', 33], ['MQEFHYWEQEQF', 'SKWTRINZKNHZ', 56], ['CFVLWYEPIHTD', 'VNVMOTETFNZS', 97], ['LUYFGOTQDNUW', 'LNOTZYAMBJDY', 15], ['AXLIHDJFQCND', 'SKAHGGPLJQDW', 26], ['XBAAGNTXAIKR', 'THCSSZBZUENU', 77], ['CHRKLIGSILMJ', 'DAIZUYKLLWRF', 48], ['SOXUJJGBOMOL', 'GMPUWAUQISEV', 74], ['BPYNVMYYQQRC', 'ALOAEDBOCYKS', 76], ['NFLVFKOJSKRO', 'LXOJVBXVZOZK', 16], ['PPVCXTPBMAEL', 'ZHFMTHBQFHXS', 76], ['ZKGHDFGCWFRG', 'SUTCSDSIFJTK', 88], ['OYVFIGWMZOWI', 'YGECHBKNYUWR', 44], ['KNXDGJJMKKPA', 'NGWWWPFNVXQM', 74], ['GABAUOHHKISI', 'WQCTSYPTQOAO', 46], ['MWYGNZAZUGKW', 'HICKBOFGUBBU', 81], ['IPLPYFHHDKCQ', 'YILGAMWIXWLS', 29], ['FKYXDSJIWQWX', 'XGOSDDUZJRAX', 8], ['PTICQYGEBHIH', 'WNXOHQMVOFSQ', 51], ['SVTGRKABFLVT', 'YQDMWUHWPTQW', 24], ['IRMMHZESILHY', 'HISSLSKXZQYI', 51], ['HLPQTTWPZQHH', 'LNWBQTBBXFYR', 47], ['BZMCBVIQMTRD', 'RXOFFOLYCNCW', 94], ['MHVWDCDUYNDG', 'PPUZPAUKVECW', 47], ['NCKGDMIOUCFA', 'AUEKROBRPTOS', 59], ['WNBNPIVCHGMR', 'ENLHLBAAYOJY', 93], ['WMKTQJWKKFDX', 'IIFOLFTGDCBP', 78], ['OIWAFYULUVBA', 'PPXMNMDOHQJY', 29], ['BGPZBTDUEVLY', 'BJZACXREPIEP', 79], ['QZHDRHLREVZF', 'YTQKJWOMDSBK', 0], ['YFHFNWUMQTXO', 'JUIIRSDRKZVG', 64], ['YTBJVGNBIANK', 'ZZWGRLMLTFQK', 6], ['FJZKABDMBXQR', 'XWHMHSEWPVUI', 9], ['RLTMZFUMVPFD', 'SAPFUDVUXMWN', 12], ['RBFMNUDAFXQT', 'RSFCBRKAAXTK', 60], ['DFDZJAYUBNIY', 'QAKYJQNDVSFJ', 0], ['AIUDHAIJMOUZ', 'NVEFIMYYMGYK', 19], ['JKNOADVQUTZY', 'AMDZPGUVRXAO', 14], ['RWZGJXAGRZIB', 'FHXYNYLTPCDJ', 21], ['RIMHNHUDCHYE', 'YVFOYMXOMPWL', 70], ['OTDPYQXTRZPY', 'LGECGEVJRRCB', 11], ['NACUFYQRJKBG', 'XVWKPSNJJFIM', 95], ['FDTBYTDUSOGQ', 'ZGKXDRSFIWLI', 32], ['BBFPVZINOPQH', 'DIJULBSCJMGR', 40], ['PBTBHRWXXADT', 'NRNIHRQDAHWD', 68], ['LUVBIWYQDHUM', 'OMZKEPTSFFFT', 72], ['UBATNOWFHMNP', 'GNGHHBDMOMSS', 43], ['QAZVAHCKMBTT', 'KWIIUHIWYRLM', 45], ['AKJVIHICULQT', 'OUOMMNQYMQVL', 55], ['GTEKJMWYQTEG', 'HKYVMPNPNTOX', 3], ['BXYSZCOUZAYK', 'RXGQIBOPRALN', 17], ['VZPSHAYQBAYJ', 'DAZENTPOGGLP', 91], ['EIPVUJZPSSWW', 'LLCAEBHPCIFM', 18], ['YHOBYPDCVDRF', 'IZDKIUXPZYAF', 90], ['OTPWEYCKGWCF', 'ZPRLOMKQEFIH', 52], ['OSPAVMUOOHCC', 'CYKDYDZNFBSY', 51], ['RWQSGDJSXABZ', 'PRYRYLWEVLPA', 13], ['YTDIZCYNYDMH', 'JRVZAPAJJAJR', 32], ['CDPZWKHBUJHN', 'VWLROBUEHZGZ', 67], ['KBWEVADGOVBJ', 'LJDEZUFSAXUX', 38], ['IFRNHGUUCCVP', 'UQWVTEUMTRXJ', 55], ['NIXPFMTBOTQD', 'JHGONFJBUBRS', 19], ['TDVPBBEYIRUT', 'CJBVVHEKSMPN', 56], ['PKGUXCSPOJIY', 'RRZPXELGRUOY', 34], ['OCIQLOBFSBBV', 'ZDZDCDDKFJPI', 97], ['ARZKETUFBBSJ', 'LPACWUGWHHXR', 14], ['VMCCGGFFCNHL', 'KDQKZCXEZXKV', 48], ['AFMZATESMICM', 'YRBBLDBRKIBG', 20], ['EXCIFGHIIIYW', 'TLATBFPWSUOY', 64], ['XMNYYPFSVXTV', 'TQUCEWLXSXPF', 36], ['JOWOIHWLSBSU', 'OFPCBACEAFLZ', 91], ['XGJNWDAZNQBS', 'JLACETXZZFGC', 48], ['BOANPTJMQYSX', 'VHIZOYILVBQO', 74], ['VGYBNQECUPEO', 'RABRJTMZGBFZ', 40], ['OAYGMXISJXWN', 'FUXYIJEZIAOK', 81], ['KDQXAPPLQLYH', 'AHNKYNEAGJAE', 5], ['EFXJEEAWXKFM', 'XMQLCIMRECNC', 53], ['TQRAWTGOWJAD', 'LEREHCJKZWOW', 37], ['PDMDWVNCRSET', 'PFORZIONAEGN', 86], ['EJSLEVABTAOW', 'TRERGQLWOTFV', 49], ['JDSKXIVTLQZS', 'VSEUXFTKEUVE', 63], ['ZWCUCUFPOUFR', 'CXLUZQMJINCL', 65], ['JHYRUBTEHPED', 'RUWQCOFYAFUT', 91], ['MJFHURPYVOBI', 'ABYZRFGISGHP', 7], ['HYEWEUDNRVES', 'YXPIPIEMLPFK', 34], ['FOTWRBBNMNAO', 'SRIPDFOAVPWN', 24], ['QUBPNNZYXDTC', 'EDWMRLJJSPWW', 51], ['ALFULLUZZOEZ', 'JSMOKLVIEMPM', 99], ['VGENYRDSSZAT', 'ZGWDOBDQZPEJ', 60], ['EQSRFRDPPHHX', 'FMRZAIKGCIRC', 20], ['ZTQJIKNXWALY', 'ORFLBEOXGQJP', 40], ['ZJRPZWYURGHL', 'JLNQTCDOUXTR', 12], ['TIOLRGSUORMX', 'CVLUSNOWXISR', 84], ['JIDEXUNBJCGP', 'UOCAHXYEPOGG', 92], ['OLALVLCSFSOE', 'YZTLJJQOXLFY', 27], ['PSEEIUELNNDT', 'JNHFOVHHTCUX', 93], ['XDZOGZVXUJTC', 'QGSCUBNUVVFT', 88], ['WYIMCWRCTCWH', 'AWIPZLCCEBCO', 26], ['MUYMPOAIIAWF', 'VUCVZMFXRNJD', 63], ['DRYASDRMEQIB', 'DVMVOQLZBRDN', 80], ['XULOEINLHWCP', 'PAPQYCJROHQJ', 86], ['FTMOXXOFFHGL', 'ZFLTESOYUFJO', 16], ['USDEKGIOUXQM', 'YNCMEJTXOGUM', 49], ['RFSMPQGIMUEL', 'QIKNHJAOGIRS', 30], ['YIUQGDTHJNXD', 'JJILUWKIGDJT', 47], ['IZUBECJNGOZB', 'JRZKKKOQZNXM', 64], ['AVKNGKGRHMPU', 'EKHFXQZJSOVG', 30], ['KOIEPBAUZYZB', 'XIDDPKYZVCHC', 82], ['QDZKPZWTCIHE', 'ILSCHPEGGFQT', 83], ['NNSEHTVORIKF', 'YPJIWWXHQIXE', 28], ['JUQFMHNKTOXL', 'UQILUJDHRYVC', 25], ['LHZZWWIYJOQX', 'ZTXEQXPLZIIY', 82], ['MLHOCNBGZFPN', 'WSUKNZZVULEY', 75], ['IPRIJBWJNDLA', 'DLQPCMJGQOOJ', 38], ['WOKUNBQGBMZA', 'XQFWTTFUORFB', 43], ['UGMWZVZAVVBS', 'WZVWEZXFFKXP', 12], ['MLDFTBNIOGYD', 'QQFSLOOOXKSN', 88], ['XCQKBAWZRKOF', 'IGBVSIXJHVEX', 44], ['QSEUPFOGOYSE', 'JQTDLAUVFLFA', 35], ['ZXDNYLCQPKKT', 'EOCNQEVWESMJ', 87], ['YJFEXXCSRXCS', 'MXJKZBRWOWKF', 59], ['GDXQIVFTCCKO', 'EUZLCEOCBOWR', 20], ['NDSAEWFLAFXH', 'NJMSNTZVVGVQ', 75], ['UGLAJTODYOUO', 'DHOHAEBOCRZD', 91], ['XEXVTTIHKROW', 'LWGJMWICFYGF', 91], ['JYDUTEPDRNCC', 'BQIQZRDVMPRU', 89], ['DRNTIKRELSHE', 'QRSYTIGRAINQ', 75], ['MALRDSBKORZG', 'QFVKPCFGVTPA', 26], ['PETLEOFDBZWH', 'FTRRUKQSCEOS', 27], ['VKNRYELHCUAG', 'PEVMRPGIOJOK', 20], ['MZHLEZOJTUWQ', 'CIPFVXTRXAPH', 43], ['PJJKWPRCOEKI', 'XADTFXXHEKRI', 80], ['RHWURHROGOWY', 'XHQIVCBMNYVS', 96], ['XRANUHKYWXYE', 'TYYGMFWXUVCW', 80], ['TZHLYSADSXYR', 'YCKSMCXEDZJT', 56], ['JWUGJCUYPMDY', 'OQRTKBPEEYZV', 44], ['HXEMIAWIWRFG', 'DXURSCEZQWEG', 75], ['ZXVCXJRCRYEW', 'DEEXOKUAQBCS', 79], ['DAGEKGVKUBSS', 'DORQRHMCFALM', 27], ['AOWNHNHVPAEV', 'PLORKAPBSHBO', 29], ['OASCAWUDMPYU', 'CAYMUKJZZNHI', 17], ['INSNPQZRIVNF', 'HGIMUAABFQLL', 96], ['QXQZATGRXNRO', 'SNOVHLHPWHHI', 17], ['WQSCSAQFHZMC', 'XUYEPZEGYKVM', 85], ['VAZKGFMJLHVA', 'AFFPZQARTBXY', 25], ['EXZKVFDJPSNW', 'TMODETZRFHSZ', 39], ['DKBAVHDSHYGP', 'LODBCMPVGWCO', 55], ['YSAYBCTQTJTI', 'AOTLCUDEQADK', 44], ['INLTVBNZFXRJ', 'RPOTFECPDQDD', 61], ['AHILJJIDTIDB', 'MHCQPHMCSSOZ', 77], ['XUUDZKURKMKP', 'BMUATKHQUCCZ', 94], ['ATHVASPCLCNM', 'QZSGVKCRJCCM', 83], ['WMSEQIOLXAFF', 'LVKHUNSKZFLI', 34], ['OOPCXYPNPJGP', 'YWUMMTSSDDJO', 83], ['KAZZTFDIAZLV', 'UFBKUMAVSFDT', 64], ['IADDKCJCLNVY', 'GDZHQZRZPHMG', 61], ['KEIDIFMUNPKU', 'DAZXEGUMLBRH', 54], ['IRZIQMFIQQTS', 'JYNGYRESTLDN', 33], ['VNDOEZQPAMPR', 'XUWVJPJRBZGT', 87], ['DKHUAKBFXVHW', 'PHZYCBWZLMQN', 91], ['KBFXTXXTEZTJ', 'PFBUIZZZASSP', 24], ['QPPWLGBHWOZJ', 'YYBFQZOFUREF', 41], ['WJKOZGBFREDI', 'XCNZYKNTIKJX', 12], ['JBYKRECCKOTQ', 'TTADHSPCHGIC', 61], ['YZDCTAHATJIM', 'TLOMOPFGGGTL', 56], ['QBKFDHRHREEC', 'FKGZFTZMKUHD', 20], ['PHCPBWKJCZSY', 'HTCKFHMBRISG', 54], ['VJUYETWQNZTU', 'ABOMMEYJJPDH', 29], ['BGRUTYSNBFMO', 'KSMYQWZNPKYF', 40], ['YVQQYQCUCPQF', 'PRXEJXRZBOXF', 22], ['EZNKHWKAORVA', 'DOSMAUKTZANY', 97], ['JZKSPKZTSPHQ', 'SMPTXRCXKTUU', 92], ['EMDLPRWYDRFF', 'RHRTJNNHKUFY', 62], ['BDXGAKKBNIKP', 'LTSKARDJKEXM', 27], ['AQKDGWNWKQLI', 'FHGUSFDCCFRF', 60], ['BKHUYGIWOOWK', 'HQOIGDLMNRMP', 70], ['XPUXMXPYCMAE', 'OTDYUKQESXMJ', 84], ['PVPBFDSSJJIW', 'NGQUFBJRSGDS', 23], ['KQWMRVTKVDKD', 'CREYZUNQGRDP', 14], ['MEBCNCWHFVLR', 'SQCFMQFOYBBG', 96], ['VQMQHHBGCSPK', 'FBIPFKRACFZA', 62], ['RKTEZERYVOCV', 'MOGMHRDSVHHW', 66], ['NSOTWGHPXPZS', 'JXQOWYKVIUTU', 44], ['NEEQAVOGSPXL', 'DQSAKMCMCLXK', 47], ['GSTVFRZOTGZU', 'RNVZWJLJNUKX', 21], ['RPALLVBJTXTP', 'ESTPLPLVZMZX', 62], ['ZDMWXVOFOQFU', 'XGBFTMXMZWWX', 12], ['QRISGPZADVPZ', 'ISIJEGJKVVEM', 64], ['LXUCXORRWWJF', 'BNUGSBZLJWUN', 24], ['PQNPFSNQFEZL', 'VOAMJAZQYVLM', 64], ['XDPCTAJFYGOF', 'ALDCHSWOHEBO', 71], ['TYVLIQODJMWJ', 'RELFFIYRIYAO', 66], ['EXVXEONOPKCY', 'COPRUNMWCXIV', 0], ['EENOUAXSMYUW', 'EVFNDLFJTDXU', 40], ['DTZMYGMAREYS', 'GLCLSZUVLBAF', 37], ['QGGPIZEVBVNY', 'KNFKEJQMHZKF', 2], ['QZCAINSSYWGH', 'MOMJLYDDGAWU', 47], ['PDYWQMRVTLAS', 'TJGGNJVQJRHY', 64], ['EVDLZUWFWRSJ', 'WDUFNRLEOFCO', 62], ['OMOCWGWYDFRF', 'PKUAMTMHMTUS', 26], ['XHCFQWRXSABR', 'DIAQJWBGMXXA', 64], ['FWNFPYZXSKIC', 'TGVVVQAQLAFR', 14], ['YUYQBIHFIUPH', 'RCJZQCANMNUW', 41], ['CZHFAJJMFTRK', 'OEDRIRAEOQIO', 90], ['XFJBNEJMILXP', 'PPLOCJPZFUPO', 85], ['ONJPZZWCJZMN', 'EROACCLBTFRT', 55], ['BWSPJPUXIDPJ', 'UIRFUUZCIKFS', 74], ['VNWNOCNHLKKZ', 'IXPCFZFWOYXK', 93], ['PMGSDDSTWWLF', 'FAELUNYMJBSQ', 44], ['VRKNNQCCNFZJ', 'RSIJMRLTVPPE', 42], ['RYVJGEQJXYGN', 'QJWXNJNBLZYM', 79], ['WLEOAQHSIOOD', 'LEWJRPLLGUST', 68], ['VBTQXEPWPQRH', 'JCDGHAWUHMXM', 22], ['FWCDQIBPTNVT', 'AMMYXKCLVEDK', 42], ['PRYIUYGUOOJW', 'KVRKUMLTSIVK', 65], ['DTIXJVKCMSUO', 'ATOHXUZTQJVC', 44], ['AEHMIBTJALBY', 'BTPOPXBLCUQG', 83], ['UUULFVDLTOTQ', 'KJAAJBPNDYWO', 21], ['SUSAWWEQCTZO', 'GSDQVWBAHESZ', 56], ['EEKFAHRPAJWV', 'MWCPISRXTUXQ', 92], ['PJGGGANUJUUS', 'VHPCHCKOJLZM', 82], ['LPALKRMGZHNV', 'UVOFJMHGHDZW', 77], ['DGWINEOBFQEY', 'RXWNSTZDULIK', 95], ['XKRWJFWRKJLK', 'SWOARSWGNYOD', 9], ['JGAZTICEQXRQ', 'AZUFYWQLDUTI', 3], ['GOJQESZSQOTL', 'BVKUZVMZOWNW', 80], ['YRWIGZHBEOXU', 'JGCURNPNQYUL', 37], ['VUXKHVIDSSHM', 'ZCBVRHAEYBYO', 37], ['RFTCNHTLJPTQ', 'FRPOUKZSPFML', 42], ['CQSUDPPCXZBS', 'EGQKQTYHQLPU', 61], ['ZKAIWRMITYDK', 'YBPMZNUTTRSB', 41], ['VLKVYMAJJXNW', 'QXXNYZENZBSI', 12], ['XAJVPBEMJKIE', 'WNUOESCDBOFH', 46], ['MOPXQDNCQLJN', 'EFGPOOEIUYWI', 76], ['CDZAYGSUGLSF', 'RJNONOJLGWTE', 23], ['SVDVVNUEGFZO', 'JKTKAYKCZEJV', 59], ['BPVZEYAYTCND', 'VSSTIKPKJGWA', 88], ['UIJWHIRZJJPH', 'FDZROLKLUUTU', 1], ['JEJWUUDSRDYB', 'WLOYXLSMWWWP', 82], ['XJKLUFLNJHMB', 'SEJHHADSFCAV', 35], ['TNAUMQXVAIKG', 'NJHHECVUFSXP', 5], ['TEXQZHMRIBJJ', 'LTIKLHFCIYDG', 70], ['IFWDVELUZJPT', 'TKMJDTHNUUMV', 16], ['JSWSVFIMEGJD', 'NEVAWFETYEPX', 1], ['TYETFFHVMSRH', 'ZNPUIMFMJFOQ', 96], ['CYESZGQGULJX', 'OLYURDBNRLZN', 10], ['QQSEBLMUDMMY', 'AIFQGZSPVHFS', 87], ['AKIVOQRVWWHC', 'MGUAFANTFGXO', 96], ['UJYXUCKMLSPE', 'CVSZAWBZGJOE', 73], ['FFYLWNJUWAOG', 'LQFOEYORIGIX', 94], ['YTBRHSVOAFAN', 'OKSGIBWGINWG', 47], ['LBYBYNEZFSWC', 'RYWUXXXUDKFV', 71], ['NVQIRYUAMRPA', 'UMBBRXSEFLFJ', 76], ['YGMKAAXWEGDO', 'MGWBEVNKLNDU', 60], ['PJSXEWSUTMWY', 'GQLXDDDJSTZX', 14], ['PXEWJFZNYFZD', 'OFGIYIPCNZOV', 88], ['XMNNWJFKDNNY', 'OHWWGGUEMLEL', 86], ['YCTAFKDICTYS', 'MYOLGZAUHCSX', 50], ['CHNVVCCZDPMH', 'HWLTUIEGLYVF', 24], ['OTKWBBGJSNPA', 'QBGIVIBVWJMY', 66], ['QTBOBWNEWWFN', 'JWSSSABAZKUH', 27], ['FTZBRTFCSFDW', 'QZPPBZVFKGND', 22], ['FTZFMYEXLUSI', 'XXZOEGEEWMUV', 4], ['XFLWCIAHWDCS', 'RHLFOMQHJGGT', 56], ['ONMSFTVWORGY', 'QUZXHQBVNHPD', 34], ['YZNELIDKXOKZ', 'QQGNUMCCVVHX', 51], ['HILZQSLFQLOW', 'EHUKYRQBKXMM', 81], ['UZISCTZBQYJZ', 'LUIEUOCGBHQS', 7], ['CWOSNKCMWGWG', 'XZINXKTIQMHT', 89], ['LLAMJWCBKQLZ', 'LDWVFXHIHOBQ', 9], ['GCRWLKALQVIV', 'WDUBOLURXDZU', 61], ['FEOCEWYGSVMD', 'YTWRLUKXMTMI', 79], ['JJRBJLLDKQDY', 'CYQHREFHOMUY', 90], ['EPTNQCGMILWR', 'ROBKYNKBRGXC', 57], ['SVJUAEUEWBPH', 'SCNXWJTHOBDS', 11], ['SFYELCAPXORD', 'JDLWNTAFDKIZ', 81], ['BUIYPSSYTGPL', 'GBICJNPCGAOZ', 18], ['YDZYQEMSQYFT', 'GTPIDZSFVBQW', 15], ['OFLDJCONONTM', 'HHONUZLAVETD', 18], ['RZCPGDJPWWUC', 'HEHYNTNSMPUI', 44], ['YNKZPLEROAEA', 'KBWRJMTHXXXP', 20], ['SQXVDDSWXKBL', 'XXJHUURDHFRU', 34], ['IXHKUDZRRHQA', 'HWJKXQVHGDKS', 68], ['FAIGFYMXSVZS', 'MSJGYIWHDRIQ', 79], ['RJPVHDDGHHMR', 'SQRYJJGONAVD', 79], ['MWHNSSVDCSEW', 'CUQKAYHEKWMA', 79], ['TUFKJNHDXNRX', 'EOSTNXSFCHCP', 46], ['GMBZEFVYMBSR', 'XPENZFUZNKAA', 56], ['PPVCPIVDIIDM', 'ZUTZETIFWQXG', 67], ['HESHVGPDLWMR', 'FACCACTUGVTL', 5], ['TGXYJLAZJUGH', 'UAXDMQSEQMTA', 49], ['AYJJLCHXWVXX', 'OYCSGZZXWPTK', 39]]

        result = [[['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100], ['AEEEFNPTVWXY', 'DEFGIJJMSSVW', 99], ['AEFLLLOUUZZZ', 'EIJKLMMMOPSV', 99], ['DFKLLORTUUUZ', 'HHIIJJJPRUWZ', 99], ['EFFHJKKKMNQZ', 'BEGGINPQVVYZ', 98], ['AAEHKKNORVWZ', 'AADKMNOSTUYZ', 97], ['ADFILQTUUWYZ', 'ACEGIJQQRTXZ', 97], ['BBBCFILOOQSV', 'CDDDDFIJKPZZ', 97]], [['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100]]]
        
        self.assertEqual(analyze(results, 26, 100), result)

    def test_46(self):
        results = [['ENQDPRQCDGDC', 'OAHFHJMQDMNK', 14], ['IOIHNOFMBKDC', 'FFJBMKOGLNCM', 56],
                    ['QARKJGHQCCML', 'QBRLNNQNGAJP', 69], ['HOQPACDCKAQA', 'CEALGJBPINPK', 56],
                    ['OCGFKPJOCGDD', 'EREFDMNKGPRC', 60], ['ROFMGDDFRDKE', 'BAORMIJBJQQI', 60],
                    ['RINJLINLGJMB', 'OBLDPNJFFCAF', 42], ['HHCAGBEFFMNI', 'IHJCOJKHDIPM', 24],
                    ['ELQRCQGRPIRG', 'GRKQMQEKBQLA', 26], ['BCLBFGCBLJBL', 'FCMRLQRNDGBJ', 82],
                    ['HRJLFMFPIIAL', 'BAFJGEFQJBQC', 73], ['PRFCCDRHINCJ', 'KNMKDJENOHER', 0],
                    ['ALELOKOHEHEM', 'OEPACQLRDRQA', 44], ['JMEABDMNMILB', 'ARGIDJQHNPFQ', 22],
                    ['KRIOJEMQCEMI', 'OBACEORJRJBR', 35], ['ENOLNADNDCDM', 'GRELKMLIJBDK', 3],
                    ['QKKONBPGJMRP', 'HCOIGPJBHAJN', 57], ['GLNBKRKGCBHN', 'PFIIRJDGHRBB', 71],
                    ['PJHNRRDOFOBI', 'HBCFFILPEBBJ', 85], ['FAGBCJCHFRAD', 'HCHFNHQFRMIF', 2],
                    ['ONORMENEMRRQ', 'EENKBIJQKMKI', 17], ['ROMNJANBIDRE', 'AJGGRIIJFMCE', 90],
                    ['IPPJNKKEPLKL', 'RNHDQIJJIEAF', 59], ['LJQRPNFPDODK', 'AKGBFPRDJBPQ', 7],
                    ['POCJCRNJAHQP', 'BPBDMRDNQEHC', 6], ['FGRFRPFPJMQC', 'RPIRHOJCMKIQ', 92],
                    ['EDLQMJLEPDEI', 'CQNRMMOBHEER', 16]]

        result = [[['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100], ['CFFFHHHIMNQR', 'AABCCDFFGHJR', 98],
                ['BDEGIJKKLLMR', 'ACDDDELMNNNO', 97], ['BBCDDEHMNPQR', 'ACCHJJNOPPQR', 94],
                ['ABBDFGJKPPQR', 'DDFJKLNOPPQR', 93], ['CFFFGJMPPQRR', 'CHIIJKMOPQRR', 92],
                ['ABDEIJMNNORR', 'ACEFGGIIJJMR', 90], ['ADFHHJKMMNOQ', 'CCDDDEGNPQQR', 86],
                ['BDFHIJNOOPRR', 'BBBCEFFHIJLP', 85], ['BCEEHMMNOQRR', 'DDEEEIJLLMPQ', 84]], [['CCCDFHIJNPRR', 'DEEHJKKMNNOR', 0]]]
        
        self.assertEqual(analyze(results, 26, -1), result)
        
    def test_47(self):
        results = [['ENQDPRQCDGDC', 'OAHFHJMQDMNK', 14], ['IOIHNOFMBKDC', 'FFJBMKOGLNCM', 56],
                    ['QARKJGHQCCML', 'QBRLNNQNGAJP', 69], ['HOQPACDCKAQA', 'CEALGJBPINPK', 56],
                    ['OCGFKPJOCGDD', 'EREFDMNKGPRC', 60], ['ROFMGDDFRDKE', 'BAORMIJBJQQI', 60],
                    ['RINJLINLGJMB', 'OBLDPNJFFCAF', 42], ['HHCAGBEFFMNI', 'IHJCOJKHDIPM', 24],
                    ['ELQRCQGRPIRG', 'GRKQMQEKBQLA', 26], ['BCLBFGCBLJBL', 'FCMRLQRNDGBJ', 82],
                    ['HRJLFMFPIIAL', 'BAFJGEFQJBQC', 73], ['PRFCCDRHINCJ', 'KNMKDJENOHER', 0],
                    ['ALELOKOHEHEM', 'OEPACQLRDRQA', 44], ['JMEABDMNMILB', 'ARGIDJQHNPFQ', 22],
                    ['KRIOJEMQCEMI', 'OBACEORJRJBR', 35], ['ENOLNADNDCDM', 'GRELKMLIJBDK', 3],
                    ['QKKONBPGJMRP', 'HCOIGPJBHAJN', 57], ['GLNBKRKGCBHN', 'PFIIRJDGHRBB', 71],
                    ['PJHNRRDOFOBI', 'HBCFFILPEBBJ', 85], ['FAGBCJCHFRAD', 'HCHFNHQFRMIF', 2],
                    ['ONORMENEMRRQ', 'EENKBIJQKMKI', 17], ['ROMNJANBIDRE', 'AJGGRIIJFMCE', 90],
                    ['IPPJNKKEPLKL', 'RNHDQIJJIEAF', 59], ['LJQRPNFPDODK', 'AKGBFPRDJBPQ', 7],
                    ['POCJCRNJAHQP', 'BPBDMRDNQEHC', 6], ['FGRFRPFPJMQC', 'RPIRHOJCMKIQ', 92],
                    ['EDLQMJLEPDEI', 'CQNRMMOBHEER', 16]]

        result = [[['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100], ['CFFFHHHIMNQR', 'AABCCDFFGHJR', 98],
                ['BDEGIJKKLLMR', 'ACDDDELMNNNO', 97], ['BBCDDEHMNPQR', 'ACCHJJNOPPQR', 94],
                ['ABBDFGJKPPQR', 'DDFJKLNOPPQR', 93], ['CFFFGJMPPQRR', 'CHIIJKMOPQRR', 92],
                ['ABDEIJMNNORR', 'ACEFGGIIJJMR', 90], ['ADFHHJKMMNOQ', 'CCDDDEGNPQQR', 86],
                ['BDFHIJNOOPRR', 'BBBCEFFHIJLP', 85], ['BCEEHMMNOQRR', 'DDEEEIJLLMPQ', 84]], [['CCCDFHIJNPRR', 'DEEHJKKMNNOR', 0]]]
        
        self.assertEqual(analyze(results, 26, 0), result)
        
    def test_48(self):
        results = [['ENQDPRQCDGDC', 'OAHFHJMQDMNK', 14], ['IOIHNOFMBKDC', 'FFJBMKOGLNCM', 56],
                    ['QARKJGHQCCML', 'QBRLNNQNGAJP', 69], ['HOQPACDCKAQA', 'CEALGJBPINPK', 56],
                    ['OCGFKPJOCGDD', 'EREFDMNKGPRC', 60], ['ROFMGDDFRDKE', 'BAORMIJBJQQI', 60],
                    ['RINJLINLGJMB', 'OBLDPNJFFCAF', 42], ['HHCAGBEFFMNI', 'IHJCOJKHDIPM', 24],
                    ['ELQRCQGRPIRG', 'GRKQMQEKBQLA', 26], ['BCLBFGCBLJBL', 'FCMRLQRNDGBJ', 82],
                    ['HRJLFMFPIIAL', 'BAFJGEFQJBQC', 73], ['PRFCCDRHINCJ', 'KNMKDJENOHER', 0],
                    ['ALELOKOHEHEM', 'OEPACQLRDRQA', 44], ['JMEABDMNMILB', 'ARGIDJQHNPFQ', 22],
                    ['KRIOJEMQCEMI', 'OBACEORJRJBR', 35], ['ENOLNADNDCDM', 'GRELKMLIJBDK', 3],
                    ['QKKONBPGJMRP', 'HCOIGPJBHAJN', 57], ['GLNBKRKGCBHN', 'PFIIRJDGHRBB', 71],
                    ['PJHNRRDOFOBI', 'HBCFFILPEBBJ', 85], ['FAGBCJCHFRAD', 'HCHFNHQFRMIF', 2],
                    ['ONORMENEMRRQ', 'EENKBIJQKMKI', 17], ['ROMNJANBIDRE', 'AJGGRIIJFMCE', 90],
                    ['IPPJNKKEPLKL', 'RNHDQIJJIEAF', 59], ['LJQRPNFPDODK', 'AKGBFPRDJBPQ', 7],
                    ['POCJCRNJAHQP', 'BPBDMRDNQEHC', 6], ['FGRFRPFPJMQC', 'RPIRHOJCMKIQ', 92],
                    ['EDLQMJLEPDEI', 'CQNRMMOBHEER', 16]]

        result = [[['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100], ['CFFFHHHIMNQR', 'AABCCDFFGHJR', 98],
                ['BDEGIJKKLLMR', 'ACDDDELMNNNO', 97], ['BBCDDEHMNPQR', 'ACCHJJNOPPQR', 94],
                ['ABBDFGJKPPQR', 'DDFJKLNOPPQR', 93], ['CFFFGJMPPQRR', 'CHIIJKMOPQRR', 92],
                ['ABDEIJMNNORR', 'ACEFGGIIJJMR', 90], ['ADFHHJKMMNOQ', 'CCDDDEGNPQQR', 86],
                ['BDFHIJNOOPRR', 'BBBCEFFHIJLP', 85], ['BCEEHMMNOQRR', 'DDEEEIJLLMPQ', 84]], [['ACCHJJNOPPQR', 'BBCDDEHMNPQR', 6]]]
        
        self.assertEqual(analyze(results, 26, 6), result)
        
    def test_49(self):
        results = [['ENQDPRQCDGDC', 'OAHFHJMQDMNK', 14], ['IOIHNOFMBKDC', 'FFJBMKOGLNCM', 56],
                    ['QARKJGHQCCML', 'QBRLNNQNGAJP', 69], ['HOQPACDCKAQA', 'CEALGJBPINPK', 56],
                    ['OCGFKPJOCGDD', 'EREFDMNKGPRC', 60], ['ROFMGDDFRDKE', 'BAORMIJBJQQI', 60],
                    ['RINJLINLGJMB', 'OBLDPNJFFCAF', 42], ['HHCAGBEFFMNI', 'IHJCOJKHDIPM', 24],
                    ['ELQRCQGRPIRG', 'GRKQMQEKBQLA', 26], ['BCLBFGCBLJBL', 'FCMRLQRNDGBJ', 82],
                    ['HRJLFMFPIIAL', 'BAFJGEFQJBQC', 73], ['PRFCCDRHINCJ', 'KNMKDJENOHER', 0],
                    ['ALELOKOHEHEM', 'OEPACQLRDRQA', 44], ['JMEABDMNMILB', 'ARGIDJQHNPFQ', 22],
                    ['KRIOJEMQCEMI', 'OBACEORJRJBR', 35], ['ENOLNADNDCDM', 'GRELKMLIJBDK', 3],
                    ['QKKONBPGJMRP', 'HCOIGPJBHAJN', 57], ['GLNBKRKGCBHN', 'PFIIRJDGHRBB', 71],
                    ['PJHNRRDOFOBI', 'HBCFFILPEBBJ', 85], ['FAGBCJCHFRAD', 'HCHFNHQFRMIF', 2],
                    ['ONORMENEMRRQ', 'EENKBIJQKMKI', 17], ['ROMNJANBIDRE', 'AJGGRIIJFMCE', 90],
                    ['IPPJNKKEPLKL', 'RNHDQIJJIEAF', 59], ['LJQRPNFPDODK', 'AKGBFPRDJBPQ', 7],
                    ['POCJCRNJAHQP', 'BPBDMRDNQEHC', 6], ['FGRFRPFPJMQC', 'RPIRHOJCMKIQ', 92],
                    ['EDLQMJLEPDEI', 'CQNRMMOBHEER', 16]]

        result = [[['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100], ['CFFFHHHIMNQR', 'AABCCDFFGHJR', 98],
                ['BDEGIJKKLLMR', 'ACDDDELMNNNO', 97], ['BBCDDEHMNPQR', 'ACCHJJNOPPQR', 94],
                ['ABBDFGJKPPQR', 'DDFJKLNOPPQR', 93], ['CFFFGJMPPQRR', 'CHIIJKMOPQRR', 92],
                ['ABDEIJMNNORR', 'ACEFGGIIJJMR', 90], ['ADFHHJKMMNOQ', 'CCDDDEGNPQQR', 86],
                ['BDFHIJNOOPRR', 'BBBCEFFHIJLP', 85], ['BCEEHMMNOQRR', 'DDEEEIJLLMPQ', 84]], [['AAACCDHKOPQQ', 'ABCEGIJKLNPP', 56], ['AACDELOPQQRR', 'AEEEHHKLLMOO', 56], ['BCDFHIIKMNOO', 'BCFFGJKLMMNO', 56]]]
        
        self.assertEqual(analyze(results, 26, 49), result)    
        
    def test_50(self):
        results = [['ENQDPRQCDGDC', 'OAHFHJMQDMNK', 14], ['IOIHNOFMBKDC', 'FFJBMKOGLNCM', 56],
                    ['QARKJGHQCCML', 'QBRLNNQNGAJP', 69], ['HOQPACDCKAQA', 'CEALGJBPINPK', 56],
                    ['OCGFKPJOCGDD', 'EREFDMNKGPRC', 60], ['ROFMGDDFRDKE', 'BAORMIJBJQQI', 60],
                    ['RINJLINLGJMB', 'OBLDPNJFFCAF', 42], ['HHCAGBEFFMNI', 'IHJCOJKHDIPM', 24],
                    ['ELQRCQGRPIRG', 'GRKQMQEKBQLA', 26], ['BCLBFGCBLJBL', 'FCMRLQRNDGBJ', 82],
                    ['HRJLFMFPIIAL', 'BAFJGEFQJBQC', 73], ['PRFCCDRHINCJ', 'KNMKDJENOHER', 0],
                    ['ALELOKOHEHEM', 'OEPACQLRDRQA', 44], ['JMEABDMNMILB', 'ARGIDJQHNPFQ', 22],
                    ['KRIOJEMQCEMI', 'OBACEORJRJBR', 35], ['ENOLNADNDCDM', 'GRELKMLIJBDK', 3],
                    ['QKKONBPGJMRP', 'HCOIGPJBHAJN', 57], ['GLNBKRKGCBHN', 'PFIIRJDGHRBB', 71],
                    ['PJHNRRDOFOBI', 'HBCFFILPEBBJ', 85], ['FAGBCJCHFRAD', 'HCHFNHQFRMIF', 2],
                    ['ONORMENEMRRQ', 'EENKBIJQKMKI', 17], ['ROMNJANBIDRE', 'AJGGRIIJFMCE', 90],
                    ['IPPJNKKEPLKL', 'RNHDQIJJIEAF', 59], ['LJQRPNFPDODK', 'AKGBFPRDJBPQ', 7],
                    ['POCJCRNJAHQP', 'BPBDMRDNQEHC', 6], ['FGRFRPFPJMQC', 'RPIRHOJCMKIQ', 92],
                    ['EDLQMJLEPDEI', 'CQNRMMOBHEER', 16]]

        result = [[['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100], ['CFFFHHHIMNQR', 'AABCCDFFGHJR', 98],
                ['BDEGIJKKLLMR', 'ACDDDELMNNNO', 97], ['BBCDDEHMNPQR', 'ACCHJJNOPPQR', 94],
                ['ABBDFGJKPPQR', 'DDFJKLNOPPQR', 93], ['CFFFGJMPPQRR', 'CHIIJKMOPQRR', 92],
                ['ABDEIJMNNORR', 'ACEFGGIIJJMR', 90], ['ADFHHJKMMNOQ', 'CCDDDEGNPQQR', 86],
                ['BDFHIJNOOPRR', 'BBBCEFFHIJLP', 85], ['BCEEHMMNOQRR', 'DDEEEIJLLMPQ', 84]], [['AAACCDHKOPQQ', 'ABCEGIJKLNPP', 56], ['AACDELOPQQRR', 'AEEEHHKLLMOO', 56], ['BCDFHIIKMNOO', 'BCFFGJKLMMNO', 56]]]
        
        self.assertEqual(analyze(results, 26, 52), result)
        
    def test_50(self):
        results = [['ENQDPRQCDGDC', 'OAHFHJMQDMNK', 14], ['IOIHNOFMBKDC', 'FFJBMKOGLNCM', 56],
                    ['QARKJGHQCCML', 'QBRLNNQNGAJP', 69], ['HOQPACDCKAQA', 'CEALGJBPINPK', 56],
                    ['OCGFKPJOCGDD', 'EREFDMNKGPRC', 60], ['ROFMGDDFRDKE', 'BAORMIJBJQQI', 60],
                    ['RINJLINLGJMB', 'OBLDPNJFFCAF', 42], ['HHCAGBEFFMNI', 'IHJCOJKHDIPM', 24],
                    ['ELQRCQGRPIRG', 'GRKQMQEKBQLA', 26], ['BCLBFGCBLJBL', 'FCMRLQRNDGBJ', 82],
                    ['HRJLFMFPIIAL', 'BAFJGEFQJBQC', 73], ['PRFCCDRHINCJ', 'KNMKDJENOHER', 0],
                    ['ALELOKOHEHEM', 'OEPACQLRDRQA', 44], ['JMEABDMNMILB', 'ARGIDJQHNPFQ', 22],
                    ['KRIOJEMQCEMI', 'OBACEORJRJBR', 35], ['ENOLNADNDCDM', 'GRELKMLIJBDK', 3],
                    ['QKKONBPGJMRP', 'HCOIGPJBHAJN', 57], ['GLNBKRKGCBHN', 'PFIIRJDGHRBB', 71],
                    ['PJHNRRDOFOBI', 'HBCFFILPEBBJ', 85], ['FAGBCJCHFRAD', 'HCHFNHQFRMIF', 2],
                    ['ONORMENEMRRQ', 'EENKBIJQKMKI', 17], ['ROMNJANBIDRE', 'AJGGRIIJFMCE', 90],
                    ['IPPJNKKEPLKL', 'RNHDQIJJIEAF', 59], ['LJQRPNFPDODK', 'AKGBFPRDJBPQ', 7],
                    ['POCJCRNJAHQP', 'BPBDMRDNQEHC', 6], ['FGRFRPFPJMQC', 'RPIRHOJCMKIQ', 92],
                    ['EDLQMJLEPDEI', 'CQNRMMOBHEER', 16]]

        result = [[['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100], ['CFFFHHHIMNQR', 'AABCCDFFGHJR', 98],
                ['BDEGIJKKLLMR', 'ACDDDELMNNNO', 97], ['BBCDDEHMNPQR', 'ACCHJJNOPPQR', 94],
                ['ABBDFGJKPPQR', 'DDFJKLNOPPQR', 93], ['CFFFGJMPPQRR', 'CHIIJKMOPQRR', 92],
                ['ABDEIJMNNORR', 'ACEFGGIIJJMR', 90], ['ADFHHJKMMNOQ', 'CCDDDEGNPQQR', 86],
                ['BDFHIJNOOPRR', 'BBBCEFFHIJLP', 85], ['BCEEHMMNOQRR', 'DDEEEIJLLMPQ', 84]], [['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100]]]
        
        self.assertEqual(analyze(results, 26, 100), result)
        
    def test_50(self):
        results = [['ENQDPRQCDGDC', 'OAHFHJMQDMNK', 14], ['IOIHNOFMBKDC', 'FFJBMKOGLNCM', 56],
                    ['QARKJGHQCCML', 'QBRLNNQNGAJP', 69], ['HOQPACDCKAQA', 'CEALGJBPINPK', 56],
                    ['OCGFKPJOCGDD', 'EREFDMNKGPRC', 60], ['ROFMGDDFRDKE', 'BAORMIJBJQQI', 60],
                    ['RINJLINLGJMB', 'OBLDPNJFFCAF', 42], ['HHCAGBEFFMNI', 'IHJCOJKHDIPM', 24],
                    ['ELQRCQGRPIRG', 'GRKQMQEKBQLA', 26], ['BCLBFGCBLJBL', 'FCMRLQRNDGBJ', 82],
                    ['HRJLFMFPIIAL', 'BAFJGEFQJBQC', 73], ['PRFCCDRHINCJ', 'KNMKDJENOHER', 0],
                    ['ALELOKOHEHEM', 'OEPACQLRDRQA', 44], ['JMEABDMNMILB', 'ARGIDJQHNPFQ', 22],
                    ['KRIOJEMQCEMI', 'OBACEORJRJBR', 35], ['ENOLNADNDCDM', 'GRELKMLIJBDK', 3],
                    ['QKKONBPGJMRP', 'HCOIGPJBHAJN', 57], ['GLNBKRKGCBHN', 'PFIIRJDGHRBB', 71],
                    ['PJHNRRDOFOBI', 'HBCFFILPEBBJ', 85], ['FAGBCJCHFRAD', 'HCHFNHQFRMIF', 2],
                    ['ONORMENEMRRQ', 'EENKBIJQKMKI', 17], ['ROMNJANBIDRE', 'AJGGRIIJFMCE', 90],
                    ['IPPJNKKEPLKL', 'RNHDQIJJIEAF', 59], ['LJQRPNFPDODK', 'AKGBFPRDJBPQ', 7],
                    ['POCJCRNJAHQP', 'BPBDMRDNQEHC', 6], ['FGRFRPFPJMQC', 'RPIRHOJCMKIQ', 92],
                    ['EDLQMJLEPDEI', 'CQNRMMOBHEER', 16]]

        result = [[['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100], ['CFFFHHHIMNQR', 'AABCCDFFGHJR', 98],
                ['BDEGIJKKLLMR', 'ACDDDELMNNNO', 97], ['BBCDDEHMNPQR', 'ACCHJJNOPPQR', 94],
                ['ABBDFGJKPPQR', 'DDFJKLNOPPQR', 93], ['CFFFGJMPPQRR', 'CHIIJKMOPQRR', 92],
                ['ABDEIJMNNORR', 'ACEFGGIIJJMR', 90], ['ADFHHJKMMNOQ', 'CCDDDEGNPQQR', 86],
                ['BDFHIJNOOPRR', 'BBBCEFFHIJLP', 85], ['BCEEHMMNOQRR', 'DDEEEIJLLMPQ', 84]], []]
        
        self.assertEqual(analyze(results, 26, 101), result)
        
        
if __name__ == '__main__':
    unittest.main()