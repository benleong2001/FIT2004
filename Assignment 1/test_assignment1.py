import unittest
from assignment1 import *

from tester_base import TesterBase


class TestAssignment1(TesterBase):

    def test_analyze(self):
        given_input = [['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
                       ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
                       ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
                       ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
                       ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
                       ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
                       ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]
        given_output = [['ABB', 'AAB', 70], ['ABB', 'BBB', 68],
                        ['AAB', 'BBB', 67], ['AAB', 'AAB', 65],
                        ['AAB', 'AAA', 64], ['ABB', 'ABB', 64],
                        ['AAA', 'AAA', 62], ['AAB', 'AAA', 58],
                        ['ABB', 'ABB', 58], ['AAB', 'ABB', 57]]
        scores = [64, 63, 71, 0]
        given_matches = [[['AAB', 'AAA', 64], ['ABB', 'ABB', 64]],
                         [['AAB', 'AAA', 64], ['ABB', 'ABB', 64]],
                         [],
                         [['AAB', 'ABB', 30]]]
        for score, match in zip(scores, given_matches):
            try:
                top10, matches = analyze(given_input, 2, score)
            except Exception:
                self.verificationErrors.append(
                    "analyze() function could not be called.")
                return

            try:
                self.assertEqual(
                    top10, given_output, ''.join(["Incorrect top10matches value returned by analyze() function: Expected ", str(given_output), ", got ", str(top10)]))
            except AssertionError as e:
                self.verificationErrors.append(e)
                return

            try:
                self.assertEqual(
                    matches, match, ''.join(["Incorrect searchedmatches value returned by analyze() function: Expected ", str(match), ", got ", str(matches)]))
            except AssertionError as e:
                self.verificationErrors.append(e)

    def test_analyze_self(self):
        self_input = [['EAE', 'BCA', 85], ['EEE', 'BDB', 17], ['EAD', 'ECD', 21],
                      ['ECA', 'CDE', 13], ['CDA', 'ABA', 76], ['BEA', 'CEC', 79],
                      ['EAE', 'CED', 8], ['CBE', 'CEA', 68], ['CDA', 'CEA', 58],
                      ['ACE', 'DEE', 24], ['DDC', 'DCA', 61], ['CDE', 'BDE', 67],
                      ['DED', 'EDD', 83], ['ABC', 'CAB', 54], ['AAB', 'BDB', 15],
                      ['BBE', 'EAD', 28], ['ACD', 'DCD', 50], ['DEB', 'CAA', 21],
                      ['EBE', 'AAC', 24], ['EBD', 'BCD', 48]]

        self_output = [['CDE', 'AEE', 92], ['CDE', 'ACE', 87], ['AEE', 'ABC', 85],
                       ['BBD', 'AAB', 85], ['BBD', 'EEE', 83], ['DDE', 'DDE', 83],
                       ['AAC', 'BDE', 79], ['ABE', 'CCE', 79], ['CDE', 'ADE', 79],
                       ['AAC', 'BEE', 76]]

        scores = [0, 8, 92, 93, 79, 76, 21, 24]
        matches = [[['AEE', 'CDE', 8]],
                   [['AEE', 'CDE', 8]],
                   [['CDE', 'AEE', 92]],
                   [],
                   [['AAC', 'BDE', 79], ['ABE', 'CCE', 79], ['CDE', 'ADE', 79]],
                   [['AAC', 'BEE', 76], ['ACD', 'AAB', 76], ['DEE', 'ACE', 76]],
                   [['ADE', 'CDE', 21], ['BDE', 'AAC', 21], ['CCE', 'ABE', 21]],
                   [['AAB', 'ACD', 24], ['ACE', 'DEE', 24], ['BEE', 'AAC', 24]]]
        for score, match in zip(scores, matches):
            try:
                top10, matches = analyze(self_input, 5, score)
            except Exception:
                self.verificationErrors.append(
                    "analyze() function could not be invoked")
                return

            try:
                self.assertEqual(
                    top10, self_output, ''.join(["Incorrect top10matches value returned by analyze() function: Expected ", str(top10), ", got ", str(self_output)]))
            except AssertionError as e:
                self.verificationErrors.append(e)
                return

            try:
                self.assertEqual(matches, match, ''.join(
                    ["Incorrect searchedmatches value returned by analyze() function: Expected ", str(match), ", got ", str(matches)]))
            except AssertionError as e:
                self.verificationErrors.append(e)

    def test_varying_input(self):
        input_score = [-1, 0, 6, 49, 52, 100, 101]
        output_searched_lists = [[[['CCCDFHIJNPRR', 'DEEHJKKMNNOR', 0]], [['BBB', 'AAA', 0]], [['BBB', 'AAA', 0]], [['BBB', 'AAA', 0]], [['AAA', 'AAA', 0]], [['AAA', 'CCC', 0], ['AAB', 'ABC', 0]]],
                                 [[['CCCDFHIJNPRR', 'DEEHJKKMNNOR', 0]], [['BBB', 'AAA', 0]], [['BBB', 'AAA', 0]], [['BBB', 'AAA', 0]], [['AAA', 'AAA', 0]], [['AAA', 'CCC', 0], ['AAB', 'ABC', 0]]],
                                 [[['ACCHJJNOPPQR', 'BBCDDEHMNPQR', 6]], [['AAA', 'BBB', 100]], [['AAA', 'BBB', 100]], [['AAA', 'BBB', 100]], [['ABB', 'AAA', 6]], [['BBB', 'ACC', 7]]],
                                 [[['AAACCDHKOPQQ', 'ABCEGIJKLNPP', 56], ['AACDELOPQQRR', 'AEEEHHKLLMOO', 56], ['BCDFHIIKMNOO', 'BCFFGJKLMMNO', 56]], [['AAA', 'BBB', 100]], [['AAA', 'BBB', 100]], [['AAA', 'BBB', 100]], [['AAB', 'ABB', 49], ['ABB', 'ABB', 49]], [['AAB', 'ABB', 49], ['ABB', 'ABB', 49]]],
                                 [[['AAACCDHKOPQQ', 'ABCEGIJKLNPP', 56], ['AACDELOPQQRR', 'AEEEHHKLLMOO', 56], ['BCDFHIIKMNOO', 'BCFFGJKLMMNO', 56]], [['AAA', 'BBB', 100]], [['AAA', 'BBB', 100]], [['AAA', 'BBB', 100]], [['AAB', 'ABB', 52], ['ABB', 'AAA', 52]], [['AAB', 'ABB', 52], ['ABB', 'AAA', 52], ['ABB', 'AAB', 52], ['ABB', 'ABB', 52]]],
                                 [[['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100]], [['AAA', 'BBB', 100]], [['AAA', 'BBB', 100]], [['AAA', 'BBB', 100]], [['AAA', 'AAA', 100]], [['ABC', 'AAB', 100], ['CCC', 'AAA', 100]]],
                                 [[], [], [], [], [], []]]

        input_results = [[['ENQDPRQCDGDC', 'OAHFHJMQDMNK', 14], ['IOIHNOFMBKDC', 'FFJBMKOGLNCM', 56],
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
                          ['EDLQMJLEPDEI', 'CQNRMMOBHEER', 16]],
                          
                          [['AAA', 'BBB', 100]], 
                          
                          [['AAA', 'BBB', 100], ['AAA', 'BBB', 100], ['AAA', 'BBB', 100], ['AAA', 'BBB', 100], 
                          ['AAA', 'BBB', 100], ['AAA', 'BBB', 100], ['AAA', 'BBB', 100], ['AAA', 'BBB', 100], 
                          ['AAA', 'BBB', 100], ['AAA', 'BBB', 100], ['AAA', 'BBB', 100], ['AAA', 'BBB', 100]],
                          
                          [['AAA', 'BBB', 100], ['BBB', 'AAA', 0], ['AAA', 'BBB', 100], ['BBB', 'AAA', 0], 
                          ['AAA', 'BBB', 100], ['BBB', 'AAA', 0], ['AAA', 'BBB', 100], ['BBB', 'AAA', 0], 
                          ['AAA', 'BBB', 100], ['BBB', 'AAA', 0], ['AAA', 'BBB', 100], ['BBB', 'AAA', 0], 
                          ['AAA', 'BBB', 100], ['BBB', 'AAA', 0]],
                          
                          [['BBB', 'BBB', 37], ['BBB', 'BBA', 38], ['BBB', 'BAB', 39], ['BBB', 'BAA', 40],
                          ['BBB', 'ABB', 41], ['BBB', 'ABA', 42], ['BBB', 'AAB', 43], ['BBB', 'AAA', 44],
                          ['BBA', 'BBB', 45], ['BBA', 'BBA', 46], ['BBA', 'BAB', 47], ['BBA', 'BAA', 48],
                          ['BBA', 'ABB', 49], ['BBA', 'ABA', 50], ['BBA', 'AAB', 51], ['BBA', 'AAA', 52],
                          ['BAB', 'BBB', 53], ['BAB', 'BBA', 54], ['BAB', 'BAB', 55], ['BAB', 'BAA', 56],
                          ['BAB', 'ABB', 57], ['BAB', 'ABA', 58], ['BAB', 'AAB', 59], ['BAB', 'AAA', 60],
                          ['BAA', 'BBB', 61], ['BAA', 'BBA', 62], ['BAA', 'BAB', 63], ['BAA', 'BAA', 64],
                          ['BAA', 'ABB', 65], ['BAA', 'ABA', 66], ['BAA', 'AAB', 67], ['BAA', 'AAA', 68],
                          ['ABB', 'BBB', 69], ['ABB', 'BBA', 70], ['ABB', 'BAB', 71], ['ABB', 'BAA', 72],
                          ['ABB', 'ABB', 73], ['ABB', 'ABA', 74], ['ABB', 'AAB', 75], ['ABB', 'AAA', 76],
                          ['ABA', 'BBB', 77], ['ABA', 'BBA', 78], ['ABA', 'BAB', 79], ['ABA', 'BAA', 80],
                          ['ABA', 'ABB', 81], ['ABA', 'ABA', 82], ['ABA', 'AAB', 83], ['ABA', 'AAA', 84],
                          ['AAB', 'BBB', 85], ['AAB', 'BBA', 86], ['AAB', 'BAB', 87], ['AAB', 'BAA', 88],
                          ['AAB', 'ABB', 89], ['AAB', 'ABA', 90], ['AAB', 'AAB', 91], ['AAB', 'AAA', 92],
                          ['AAA', 'BBB', 93], ['AAA', 'BBA', 94], ['AAA', 'BAB', 95], ['AAA', 'BAA', 96],
                          ['AAA', 'ABB', 97], ['AAA', 'ABA', 98], ['AAA', 'AAB', 99], ['AAA', 'AAA', 100]],
                          
                          [['CCC', 'AAA', 100], ['CCA', 'AAB', 99], ['BCA', 'ABA', 100], ['BAC', 'ABB', 97],
                          ['ABA', 'BAA', 96], ['AAA', 'BAB', 95], ['CBB', 'BBA', 96], ['CAC', 'BBB', 93],
                          ['BBB', 'AAA', 92], ['ACC', 'AAB', 91], ['ACA', 'ABA', 92], ['AAC', 'ABB', 89],
                          ['BAB', 'BAA', 88], ['CAA', 'BAB', 87], ['ABC', 'BBA', 88], ['BAA', 'BBB', 85],
                          ['CAB', 'AAA', 84], ['AAB', 'AAB', 83], ['ABB', 'ABA', 84], ['CBA', 'ABB', 81],
                          ['ACB', 'BAA', 80], ['BBA', 'BAB', 79], ['BCC', 'BBA', 80], ['CCB', 'BBB', 77],
                          ['CBC', 'AAA', 76], ['BBC', 'AAB', 75], ['BCB', 'ABA', 76], ['ABB', 'ABB', 73],
                          ['ABB', 'BAA', 72], ['ABB', 'BAB', 71], ['ABB', 'BBA', 72], ['ABB', 'BBB', 69],
                          ['BAA', 'AAA', 68], ['BAA', 'AAB', 67], ['BAA', 'ABA', 68], ['BAA', 'ABB', 65],
                          ['BAA', 'BAA', 64], ['BAA', 'BAB', 63], ['BAA', 'BBA', 64], ['BAA', 'BBB', 61],
                          ['BAB', 'AAA', 60], ['BAB', 'AAB', 59], ['BAB', 'ABA', 60], ['BAB', 'ABB', 57],
                          ['BAB', 'BAA', 56], ['BAB', 'BAB', 55], ['BAB', 'BBA', 56], ['BAB', 'BBB', 53],
                          ['BBA', 'AAA', 52], ['BBA', 'AAB', 51], ['BBA', 'ABA', 52], ['BBA', 'ABB', 49],
                          ['BBA', 'BAA', 48], ['BBA', 'BAB', 47], ['BBA', 'BBA', 48], ['BBA', 'BBB', 45],
                          ['BBB', 'AAA', 44], ['BBB', 'AAB', 43], ['BBB', 'ABA', 44], ['BBB', 'ABB', 41],
                          ['BBB', 'BAA', 40], ['BBB', 'BAB', 39], ['BBB', 'BBA', 40], ['BBB', 'BBB', 37]]]

        output_top10 = [[['DEEHJKKMNNOR', 'CCCDFHIJNPRR', 100], ['CFFFHHHIMNQR', 'AABCCDFFGHJR', 98],
                         ['BDEGIJKKLLMR', 'ACDDDELMNNNO', 97], ['BBCDDEHMNPQR', 'ACCHJJNOPPQR', 94],
                         ['ABBDFGJKPPQR', 'DDFJKLNOPPQR', 93], ['CFFFGJMPPQRR', 'CHIIJKMOPQRR', 92],
                         ['ABDEIJMNNORR', 'ACEFGGIIJJMR', 90], ['ADFHHJKMMNOQ', 'CCDDDEGNPQQR', 86],
                         ['BDFHIJNOOPRR', 'BBBCEFFHIJLP', 85], ['BCEEHMMNOQRR', 'DDEEEIJLLMPQ', 84]],
                         
                         [['AAA', 'BBB', 100], ['BBB', 'AAA', 0]],
                         
                         [['AAA', 'BBB', 100], ['BBB', 'AAA', 0]],
                         
                         [['AAA', 'BBB', 100], ['BBB', 'AAA', 0]],
                         
                         [['AAA', 'AAA', 100], ['AAA', 'AAB', 99], ['AAA', 'AAB', 98], ['AAA', 'ABB', 97], ['AAA', 'AAB', 96],
                         ['AAA', 'ABB', 95], ['AAA', 'ABB', 94], ['AAA', 'BBB', 93], ['AAB', 'AAA', 92], ['AAB', 'AAB', 91]],
                         
                         [['ABC', 'AAB', 100], ['CCC', 'AAA', 100], ['ACC', 'AAB', 99], ['ABC', 'ABB', 97], ['AAB', 'AAB', 96],
                         ['BBC', 'ABB', 96], ['AAA', 'ABB', 95], ['ACC', 'BBB', 93], ['AAC', 'AAB', 92], ['BBB', 'AAA', 92]]]
        ROSTER = 26

        for score, output_searched in zip(input_score, output_searched_lists):
            for results, top10, searched in zip(input_results, output_top10, output_searched):
                try:
                    test_top10, test_searched = analyze(results, ROSTER, score)
                except Exception as e:
                    self.verificationErrors.append(
                        "analyze() function could not be invoked")
                    return

                try:
                    self.assertEqual(
                        test_top10, top10, ''.join(["Incorrect top10matches value returned by analyze() function: Expected ", str(top10), ", got ", str(test_top10)]))
                except AssertionError as e:
                    self.verificationErrors.append(e)
                    return

                try:
                    self.assertEqual(test_searched, searched, ''.join(
                        ["Incorrect searchedmatches value returned by analyze() function: Expected ", str(searched), ", got ", str(test_searched)]))
                except AssertionError as e:
                    self.verificationErrors.append(e)

    def test_large_large_input(self):
        test_input = \
[['ZVJUKWHPNIQO', 'BRJCVKEMTRKU', 63], ['YIQJXUCATBIY', 'GOEBKTNEQOXU', 39], ['MHUVYBQSAQLC', 'NTNKUQYWYMIV', 58], ['YTVHOGSGFHQK', 'KLDMPPXWRVXK', 39], ['QYJZIZLVZBJR', 'HHRFSLDRCYBR', 66], 
['NABGULQKKPSC', 'MYARMIMWUPQI', 33], ['MQEFHYWEQEQF', 'SKWTRINZKNHZ', 56], ['CFVLWYEPIHTD', 'VNVMOTETFNZS', 97], ['LUYFGOTQDNUW', 'LNOTZYAMBJDY', 15], ['AXLIHDJFQCND', 'SKAHGGPLJQDW', 26], 
['XBAAGNTXAIKR', 'THCSSZBZUENU', 77], ['CHRKLIGSILMJ', 'DAIZUYKLLWRF', 48], ['SOXUJJGBOMOL', 'GMPUWAUQISEV', 74], ['BPYNVMYYQQRC', 'ALOAEDBOCYKS', 76], ['NFLVFKOJSKRO', 'LXOJVBXVZOZK', 16], 
['PPVCXTPBMAEL', 'ZHFMTHBQFHXS', 76], ['ZKGHDFGCWFRG', 'SUTCSDSIFJTK', 88], ['OYVFIGWMZOWI', 'YGECHBKNYUWR', 44], ['KNXDGJJMKKPA', 'NGWWWPFNVXQM', 74], ['GABAUOHHKISI', 'WQCTSYPTQOAO', 46], 
['MWYGNZAZUGKW', 'HICKBOFGUBBU', 81], ['IPLPYFHHDKCQ', 'YILGAMWIXWLS', 29], ['FKYXDSJIWQWX', 'XGOSDDUZJRAX', 8], ['PTICQYGEBHIH', 'WNXOHQMVOFSQ', 51], ['SVTGRKABFLVT', 'YQDMWUHWPTQW', 24], 
['IRMMHZESILHY', 'HISSLSKXZQYI', 51], ['HLPQTTWPZQHH', 'LNWBQTBBXFYR', 47], ['BZMCBVIQMTRD', 'RXOFFOLYCNCW', 94], ['MHVWDCDUYNDG', 'PPUZPAUKVECW', 47], ['NCKGDMIOUCFA', 'AUEKROBRPTOS', 59], 
['WNBNPIVCHGMR', 'ENLHLBAAYOJY', 93], ['WMKTQJWKKFDX', 'IIFOLFTGDCBP', 78], ['OIWAFYULUVBA', 'PPXMNMDOHQJY', 29], ['BGPZBTDUEVLY', 'BJZACXREPIEP', 79], ['QZHDRHLREVZF', 'YTQKJWOMDSBK', 0], 
['YFHFNWUMQTXO', 'JUIIRSDRKZVG', 64], ['YTBJVGNBIANK', 'ZZWGRLMLTFQK', 6], ['FJZKABDMBXQR', 'XWHMHSEWPVUI', 9], ['RLTMZFUMVPFD', 'SAPFUDVUXMWN', 12], ['RBFMNUDAFXQT', 'RSFCBRKAAXTK', 60], 
['DFDZJAYUBNIY', 'QAKYJQNDVSFJ', 0], ['AIUDHAIJMOUZ', 'NVEFIMYYMGYK', 19], ['JKNOADVQUTZY', 'AMDZPGUVRXAO', 14], ['RWZGJXAGRZIB', 'FHXYNYLTPCDJ', 21], ['RIMHNHUDCHYE', 'YVFOYMXOMPWL', 70], 
['OTDPYQXTRZPY', 'LGECGEVJRRCB', 11], ['NACUFYQRJKBG', 'XVWKPSNJJFIM', 95], ['FDTBYTDUSOGQ', 'ZGKXDRSFIWLI', 32], ['BBFPVZINOPQH', 'DIJULBSCJMGR', 40], ['PBTBHRWXXADT', 'NRNIHRQDAHWD', 68], 
['LUVBIWYQDHUM', 'OMZKEPTSFFFT', 72], ['UBATNOWFHMNP', 'GNGHHBDMOMSS', 43], ['QAZVAHCKMBTT', 'KWIIUHIWYRLM', 45], ['AKJVIHICULQT', 'OUOMMNQYMQVL', 55], ['GTEKJMWYQTEG', 'HKYVMPNPNTOX', 3], 
['BXYSZCOUZAYK', 'RXGQIBOPRALN', 17], ['VZPSHAYQBAYJ', 'DAZENTPOGGLP', 91], ['EIPVUJZPSSWW', 'LLCAEBHPCIFM', 18], ['YHOBYPDCVDRF', 'IZDKIUXPZYAF', 90], ['OTPWEYCKGWCF', 'ZPRLOMKQEFIH', 52], 
['OSPAVMUOOHCC', 'CYKDYDZNFBSY', 51], ['RWQSGDJSXABZ', 'PRYRYLWEVLPA', 13], ['YTDIZCYNYDMH', 'JRVZAPAJJAJR', 32], ['CDPZWKHBUJHN', 'VWLROBUEHZGZ', 67], ['KBWEVADGOVBJ', 'LJDEZUFSAXUX', 38], 
['IFRNHGUUCCVP', 'UQWVTEUMTRXJ', 55], ['NIXPFMTBOTQD', 'JHGONFJBUBRS', 19], ['TDVPBBEYIRUT', 'CJBVVHEKSMPN', 56], ['PKGUXCSPOJIY', 'RRZPXELGRUOY', 34], ['OCIQLOBFSBBV', 'ZDZDCDDKFJPI', 97], 
['ARZKETUFBBSJ', 'LPACWUGWHHXR', 14], ['VMCCGGFFCNHL', 'KDQKZCXEZXKV', 48], ['AFMZATESMICM', 'YRBBLDBRKIBG', 20], ['EXCIFGHIIIYW', 'TLATBFPWSUOY', 64], ['XMNYYPFSVXTV', 'TQUCEWLXSXPF', 36], 
['JOWOIHWLSBSU', 'OFPCBACEAFLZ', 91], ['XGJNWDAZNQBS', 'JLACETXZZFGC', 48], ['BOANPTJMQYSX', 'VHIZOYILVBQO', 74], ['VGYBNQECUPEO', 'RABRJTMZGBFZ', 40], ['OAYGMXISJXWN', 'FUXYIJEZIAOK', 81], 
['KDQXAPPLQLYH', 'AHNKYNEAGJAE', 5], ['EFXJEEAWXKFM', 'XMQLCIMRECNC', 53], ['TQRAWTGOWJAD', 'LEREHCJKZWOW', 37], ['PDMDWVNCRSET', 'PFORZIONAEGN', 86], ['EJSLEVABTAOW', 'TRERGQLWOTFV', 49], 
['JDSKXIVTLQZS', 'VSEUXFTKEUVE', 63], ['ZWCUCUFPOUFR', 'CXLUZQMJINCL', 65], ['JHYRUBTEHPED', 'RUWQCOFYAFUT', 91], ['MJFHURPYVOBI', 'ABYZRFGISGHP', 7], ['HYEWEUDNRVES', 'YXPIPIEMLPFK', 34], 
['FOTWRBBNMNAO', 'SRIPDFOAVPWN', 24], ['QUBPNNZYXDTC', 'EDWMRLJJSPWW', 51], ['ALFULLUZZOEZ', 'JSMOKLVIEMPM', 99], ['VGENYRDSSZAT', 'ZGWDOBDQZPEJ', 60], ['EQSRFRDPPHHX', 'FMRZAIKGCIRC', 20], 
['ZTQJIKNXWALY', 'ORFLBEOXGQJP', 40], ['ZJRPZWYURGHL', 'JLNQTCDOUXTR', 12], ['TIOLRGSUORMX', 'CVLUSNOWXISR', 84], ['JIDEXUNBJCGP', 'UOCAHXYEPOGG', 92], ['OLALVLCSFSOE', 'YZTLJJQOXLFY', 27], 
['PSEEIUELNNDT', 'JNHFOVHHTCUX', 93], ['XDZOGZVXUJTC', 'QGSCUBNUVVFT', 88], ['WYIMCWRCTCWH', 'AWIPZLCCEBCO', 26], ['MUYMPOAIIAWF', 'VUCVZMFXRNJD', 63], ['DRYASDRMEQIB', 'DVMVOQLZBRDN', 80], 
['XULOEINLHWCP', 'PAPQYCJROHQJ', 86], ['FTMOXXOFFHGL', 'ZFLTESOYUFJO', 16], ['USDEKGIOUXQM', 'YNCMEJTXOGUM', 49], ['RFSMPQGIMUEL', 'QIKNHJAOGIRS', 30], ['YIUQGDTHJNXD', 'JJILUWKIGDJT', 47], 
['IZUBECJNGOZB', 'JRZKKKOQZNXM', 64], ['AVKNGKGRHMPU', 'EKHFXQZJSOVG', 30], ['KOIEPBAUZYZB', 'XIDDPKYZVCHC', 82], ['QDZKPZWTCIHE', 'ILSCHPEGGFQT', 83], ['NNSEHTVORIKF', 'YPJIWWXHQIXE', 28], 
['JUQFMHNKTOXL', 'UQILUJDHRYVC', 25], ['LHZZWWIYJOQX', 'ZTXEQXPLZIIY', 82], ['MLHOCNBGZFPN', 'WSUKNZZVULEY', 75], ['IPRIJBWJNDLA', 'DLQPCMJGQOOJ', 38], ['WOKUNBQGBMZA', 'XQFWTTFUORFB', 43], 
['UGMWZVZAVVBS', 'WZVWEZXFFKXP', 12], ['MLDFTBNIOGYD', 'QQFSLOOOXKSN', 88], ['XCQKBAWZRKOF', 'IGBVSIXJHVEX', 44], ['QSEUPFOGOYSE', 'JQTDLAUVFLFA', 35], ['ZXDNYLCQPKKT', 'EOCNQEVWESMJ', 87], 
['YJFEXXCSRXCS', 'MXJKZBRWOWKF', 59], ['GDXQIVFTCCKO', 'EUZLCEOCBOWR', 20], ['NDSAEWFLAFXH', 'NJMSNTZVVGVQ', 75], ['UGLAJTODYOUO', 'DHOHAEBOCRZD', 91], ['XEXVTTIHKROW', 'LWGJMWICFYGF', 91], 
['JYDUTEPDRNCC', 'BQIQZRDVMPRU', 89], ['DRNTIKRELSHE', 'QRSYTIGRAINQ', 75], ['MALRDSBKORZG', 'QFVKPCFGVTPA', 26], ['PETLEOFDBZWH', 'FTRRUKQSCEOS', 27], ['VKNRYELHCUAG', 'PEVMRPGIOJOK', 20], 
['MZHLEZOJTUWQ', 'CIPFVXTRXAPH', 43], ['PJJKWPRCOEKI', 'XADTFXXHEKRI', 80], ['RHWURHROGOWY', 'XHQIVCBMNYVS', 96], ['XRANUHKYWXYE', 'TYYGMFWXUVCW', 80], ['TZHLYSADSXYR', 'YCKSMCXEDZJT', 56], 
['JWUGJCUYPMDY', 'OQRTKBPEEYZV', 44], ['HXEMIAWIWRFG', 'DXURSCEZQWEG', 75], ['ZXVCXJRCRYEW', 'DEEXOKUAQBCS', 79], ['DAGEKGVKUBSS', 'DORQRHMCFALM', 27], ['AOWNHNHVPAEV', 'PLORKAPBSHBO', 29], 
['OASCAWUDMPYU', 'CAYMUKJZZNHI', 17], ['INSNPQZRIVNF', 'HGIMUAABFQLL', 96], ['QXQZATGRXNRO', 'SNOVHLHPWHHI', 17], ['WQSCSAQFHZMC', 'XUYEPZEGYKVM', 85], ['VAZKGFMJLHVA', 'AFFPZQARTBXY', 25], 
['EXZKVFDJPSNW', 'TMODETZRFHSZ', 39], ['DKBAVHDSHYGP', 'LODBCMPVGWCO', 55], ['YSAYBCTQTJTI', 'AOTLCUDEQADK', 44], ['INLTVBNZFXRJ', 'RPOTFECPDQDD', 61], ['AHILJJIDTIDB', 'MHCQPHMCSSOZ', 77], 
['XUUDZKURKMKP', 'BMUATKHQUCCZ', 94], ['ATHVASPCLCNM', 'QZSGVKCRJCCM', 83], ['WMSEQIOLXAFF', 'LVKHUNSKZFLI', 34], ['OOPCXYPNPJGP', 'YWUMMTSSDDJO', 83], ['KAZZTFDIAZLV', 'UFBKUMAVSFDT', 64], 
['IADDKCJCLNVY', 'GDZHQZRZPHMG', 61], ['KEIDIFMUNPKU', 'DAZXEGUMLBRH', 54], ['IRZIQMFIQQTS', 'JYNGYRESTLDN', 33], ['VNDOEZQPAMPR', 'XUWVJPJRBZGT', 87], ['DKHUAKBFXVHW', 'PHZYCBWZLMQN', 91], 
['KBFXTXXTEZTJ', 'PFBUIZZZASSP', 24], ['QPPWLGBHWOZJ', 'YYBFQZOFUREF', 41], ['WJKOZGBFREDI', 'XCNZYKNTIKJX', 12], ['JBYKRECCKOTQ', 'TTADHSPCHGIC', 61], ['YZDCTAHATJIM', 'TLOMOPFGGGTL', 56], 
['QBKFDHRHREEC', 'FKGZFTZMKUHD', 20], ['PHCPBWKJCZSY', 'HTCKFHMBRISG', 54], ['VJUYETWQNZTU', 'ABOMMEYJJPDH', 29], ['BGRUTYSNBFMO', 'KSMYQWZNPKYF', 40], ['YVQQYQCUCPQF', 'PRXEJXRZBOXF', 22], 
['EZNKHWKAORVA', 'DOSMAUKTZANY', 97], ['JZKSPKZTSPHQ', 'SMPTXRCXKTUU', 92], ['EMDLPRWYDRFF', 'RHRTJNNHKUFY', 62], ['BDXGAKKBNIKP', 'LTSKARDJKEXM', 27], ['AQKDGWNWKQLI', 'FHGUSFDCCFRF', 60], 
['BKHUYGIWOOWK', 'HQOIGDLMNRMP', 70], ['XPUXMXPYCMAE', 'OTDYUKQESXMJ', 84], ['PVPBFDSSJJIW', 'NGQUFBJRSGDS', 23], ['KQWMRVTKVDKD', 'CREYZUNQGRDP', 14], ['MEBCNCWHFVLR', 'SQCFMQFOYBBG', 96], 
['VQMQHHBGCSPK', 'FBIPFKRACFZA', 62], ['RKTEZERYVOCV', 'MOGMHRDSVHHW', 66], ['NSOTWGHPXPZS', 'JXQOWYKVIUTU', 44], ['NEEQAVOGSPXL', 'DQSAKMCMCLXK', 47], ['GSTVFRZOTGZU', 'RNVZWJLJNUKX', 21], 
['RPALLVBJTXTP', 'ESTPLPLVZMZX', 62], ['ZDMWXVOFOQFU', 'XGBFTMXMZWWX', 12], ['QRISGPZADVPZ', 'ISIJEGJKVVEM', 64], ['LXUCXORRWWJF', 'BNUGSBZLJWUN', 24], ['PQNPFSNQFEZL', 'VOAMJAZQYVLM', 64], 
['XDPCTAJFYGOF', 'ALDCHSWOHEBO', 71], ['TYVLIQODJMWJ', 'RELFFIYRIYAO', 66], ['EXVXEONOPKCY', 'COPRUNMWCXIV', 0], ['EENOUAXSMYUW', 'EVFNDLFJTDXU', 40], ['DTZMYGMAREYS', 'GLCLSZUVLBAF', 37], 
['QGGPIZEVBVNY', 'KNFKEJQMHZKF', 2], ['QZCAINSSYWGH', 'MOMJLYDDGAWU', 47], ['PDYWQMRVTLAS', 'TJGGNJVQJRHY', 64], ['EVDLZUWFWRSJ', 'WDUFNRLEOFCO', 62], ['OMOCWGWYDFRF', 'PKUAMTMHMTUS', 26], 
['XHCFQWRXSABR', 'DIAQJWBGMXXA', 64], ['FWNFPYZXSKIC', 'TGVVVQAQLAFR', 14], ['YUYQBIHFIUPH', 'RCJZQCANMNUW', 41], ['CZHFAJJMFTRK', 'OEDRIRAEOQIO', 90], ['XFJBNEJMILXP', 'PPLOCJPZFUPO', 85], 
['ONJPZZWCJZMN', 'EROACCLBTFRT', 55], ['BWSPJPUXIDPJ', 'UIRFUUZCIKFS', 74], ['VNWNOCNHLKKZ', 'IXPCFZFWOYXK', 93], ['PMGSDDSTWWLF', 'FAELUNYMJBSQ', 44], ['VRKNNQCCNFZJ', 'RSIJMRLTVPPE', 42], 
['RYVJGEQJXYGN', 'QJWXNJNBLZYM', 79], ['WLEOAQHSIOOD', 'LEWJRPLLGUST', 68], ['VBTQXEPWPQRH', 'JCDGHAWUHMXM', 22], ['FWCDQIBPTNVT', 'AMMYXKCLVEDK', 42], ['PRYIUYGUOOJW', 'KVRKUMLTSIVK', 65], 
['DTIXJVKCMSUO', 'ATOHXUZTQJVC', 44], ['AEHMIBTJALBY', 'BTPOPXBLCUQG', 83], ['UUULFVDLTOTQ', 'KJAAJBPNDYWO', 21], ['SUSAWWEQCTZO', 'GSDQVWBAHESZ', 56], ['EEKFAHRPAJWV', 'MWCPISRXTUXQ', 92], 
['PJGGGANUJUUS', 'VHPCHCKOJLZM', 82], ['LPALKRMGZHNV', 'UVOFJMHGHDZW', 77], ['DGWINEOBFQEY', 'RXWNSTZDULIK', 95], ['XKRWJFWRKJLK', 'SWOARSWGNYOD', 9], ['JGAZTICEQXRQ', 'AZUFYWQLDUTI', 3], 
['GOJQESZSQOTL', 'BVKUZVMZOWNW', 80], ['YRWIGZHBEOXU', 'JGCURNPNQYUL', 37], ['VUXKHVIDSSHM', 'ZCBVRHAEYBYO', 37], ['RFTCNHTLJPTQ', 'FRPOUKZSPFML', 42], ['CQSUDPPCXZBS', 'EGQKQTYHQLPU', 61], 
['ZKAIWRMITYDK', 'YBPMZNUTTRSB', 41], ['VLKVYMAJJXNW', 'QXXNYZENZBSI', 12], ['XAJVPBEMJKIE', 'WNUOESCDBOFH', 46], ['MOPXQDNCQLJN', 'EFGPOOEIUYWI', 76], ['CDZAYGSUGLSF', 'RJNONOJLGWTE', 23], 
['SVDVVNUEGFZO', 'JKTKAYKCZEJV', 59], ['BPVZEYAYTCND', 'VSSTIKPKJGWA', 88], ['UIJWHIRZJJPH', 'FDZROLKLUUTU', 1], ['JEJWUUDSRDYB', 'WLOYXLSMWWWP', 82], ['XJKLUFLNJHMB', 'SEJHHADSFCAV', 35], 
['TNAUMQXVAIKG', 'NJHHECVUFSXP', 5], ['TEXQZHMRIBJJ', 'LTIKLHFCIYDG', 70], ['IFWDVELUZJPT', 'TKMJDTHNUUMV', 16], ['JSWSVFIMEGJD', 'NEVAWFETYEPX', 1], ['TYETFFHVMSRH', 'ZNPUIMFMJFOQ', 96], 
['CYESZGQGULJX', 'OLYURDBNRLZN', 10], ['QQSEBLMUDMMY', 'AIFQGZSPVHFS', 87], ['AKIVOQRVWWHC', 'MGUAFANTFGXO', 96], ['UJYXUCKMLSPE', 'CVSZAWBZGJOE', 73], ['FFYLWNJUWAOG', 'LQFOEYORIGIX', 94], 
['YTBRHSVOAFAN', 'OKSGIBWGINWG', 47], ['LBYBYNEZFSWC', 'RYWUXXXUDKFV', 71], ['NVQIRYUAMRPA', 'UMBBRXSEFLFJ', 76], ['YGMKAAXWEGDO', 'MGWBEVNKLNDU', 60], ['PJSXEWSUTMWY', 'GQLXDDDJSTZX', 14], 
['PXEWJFZNYFZD', 'OFGIYIPCNZOV', 88], ['XMNNWJFKDNNY', 'OHWWGGUEMLEL', 86], ['YCTAFKDICTYS', 'MYOLGZAUHCSX', 50], ['CHNVVCCZDPMH', 'HWLTUIEGLYVF', 24], ['OTKWBBGJSNPA', 'QBGIVIBVWJMY', 66], 
['QTBOBWNEWWFN', 'JWSSSABAZKUH', 27], ['FTZBRTFCSFDW', 'QZPPBZVFKGND', 22], ['FTZFMYEXLUSI', 'XXZOEGEEWMUV', 4], ['XFLWCIAHWDCS', 'RHLFOMQHJGGT', 56], ['ONMSFTVWORGY', 'QUZXHQBVNHPD', 34], 
['YZNELIDKXOKZ', 'QQGNUMCCVVHX', 51], ['HILZQSLFQLOW', 'EHUKYRQBKXMM', 81], ['UZISCTZBQYJZ', 'LUIEUOCGBHQS', 7], ['CWOSNKCMWGWG', 'XZINXKTIQMHT', 89], ['LLAMJWCBKQLZ', 'LDWVFXHIHOBQ', 9], 
['GCRWLKALQVIV', 'WDUBOLURXDZU', 61], ['FEOCEWYGSVMD', 'YTWRLUKXMTMI', 79], ['JJRBJLLDKQDY', 'CYQHREFHOMUY', 90], ['EPTNQCGMILWR', 'ROBKYNKBRGXC', 57], ['SVJUAEUEWBPH', 'SCNXWJTHOBDS', 11], 
['SFYELCAPXORD', 'JDLWNTAFDKIZ', 81], ['BUIYPSSYTGPL', 'GBICJNPCGAOZ', 18], ['YDZYQEMSQYFT', 'GTPIDZSFVBQW', 15], ['OFLDJCONONTM', 'HHONUZLAVETD', 18], ['RZCPGDJPWWUC', 'HEHYNTNSMPUI', 44], 
['YNKZPLEROAEA', 'KBWRJMTHXXXP', 20], ['SQXVDDSWXKBL', 'XXJHUURDHFRU', 34], ['IXHKUDZRRHQA', 'HWJKXQVHGDKS', 68], ['FAIGFYMXSVZS', 'MSJGYIWHDRIQ', 79], ['RJPVHDDGHHMR', 'SQRYJJGONAVD', 79], 
['MWHNSSVDCSEW', 'CUQKAYHEKWMA', 79], ['TUFKJNHDXNRX', 'EOSTNXSFCHCP', 46], ['GMBZEFVYMBSR', 'XPENZFUZNKAA', 56], ['PPVCPIVDIIDM', 'ZUTZETIFWQXG', 67], ['HESHVGPDLWMR', 'FACCACTUGVTL', 5], 
['TGXYJLAZJUGH', 'UAXDMQSEQMTA', 49], ['AYJJLCHXWVXX', 'OYCSGZZXWPTK', 39]]
    
        test_top10 = \
        [['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100], 
        ['AEEEFNPTVWXY', 'DEFGIJJMSSVW', 99], ['AEFLLLOUUZZZ', 'EIJKLMMMOPSV', 99], ['DFKLLORTUUUZ', 'HHIIJJJPRUWZ', 99], 
        ['EFFHJKKKMNQZ', 'BEGGINPQVVYZ', 98], ['AAEHKKNORVWZ', 'AADKMNOSTUYZ', 97], ['ADFILQTUUWYZ', 'ACEGIJQQRTXZ', 97], 
        ['BBBCFILOOQSV', 'CDDDDFIJKPZZ', 97]]

        roster = 26
        score = 69
        test_searchedmatches = [['AGHIIJKNOQRS', 'EFGILMMPQRSU', 70], ['BEHIJJMQRTXZ', 'CDFGHIIKLLTY', 70], ['BGHIKKOOUWWY', 'DGHILMMNOPQR', 70], ['CDEHHHIMNRUY', 'FLMMOOPVWXYY', 70], ['EFGHJKOQSVXZ', 'AGGHKKMNPRUV', 70]]
        score = 100 - 69
        test_searchedmatches = [['ADDHHINNQRRW', 'ABBDHPRTTWXX', 32], ['BDDFGOQSTTUY', 'DFGIIKLRSWXZ', 32], ['CDDHIMNTYYYZ', 'AAAJJJJPRRVZ', 32], ['DGHHJKKQSVWX', 'ADHHIKQRRUXZ', 32], ['EGJLLLPRSTUW', 'ADEHILOOOQSW', 32]]
        score = 69*2
        test_searchedmatches = []
        score = 69 / 3
        test_searchedmatches = [['ACDFGGLSSUYZ', 'EGJJLNNOORTW', 23], ['BCEHNSSTUUZZ', 'AAABGIKNRTXX', 23], ['BDFIJJPPSSVW', 'BDFGGJNQRSSU', 23], ['CCHHMMOPQSSZ', 'ABDDHIIIJJLT', 23], ['DFGHHJMOUVWZ', 'AGHKLLMNPRVZ', 23]]
        score = 69 * 0
        test_searchedmatches = [['ABDDFIJNUYYZ', 'ADFJJKNQQSVY', 0], ['CEEKNOOPVXXY', 'CCIMNOPRUVWX', 0], ['DEFHHLQRRVZZ', 'BDJKKMOQSTWY', 0]]
        score = 69 + 31
        test_searchedmatches = [['ADFJJKNQQSVY', 'ABDDFIJNUYYZ', 100], ['BDJKKMOQSTWY', 'DEFHHLQRRVZZ', 100], ['CCIMNOPRUVWX', 'CEEKNOOPVXXY', 100]]
        try: 
            top10, searchedmatches = analyze(test_input, roster, score)
        except Exception as e:
            self.verificationErrors.append(''.join(["analyze() function could not be invoked: ", str(e)]))
            return

        try:
            self.assertEqual(top10, test_top10, "".join(["Incorrect top10matches value return: Expected ", str(test_top10), ", got ", str(top10)]))       
        except AssertionError as e:
            self.verificationErrors.append(e)
            return

        try:
            self.assertEqual(searchedmatches, test_searchedmatches, "".join(["Incorrect searchedmatches value returned: Expected ", str(test_searchedmatches), ", got ", str(searchedmatches)]))
        except AssertionError as e:
            self.verificationErrors.append(e)
            return


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignment1)
    unittest.TextTestRunner(verbosity=0).run(suite)
