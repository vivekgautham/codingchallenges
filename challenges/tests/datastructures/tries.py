import unittest
from challenges.src.datastructures import tries
import functools

class Test_Tries(unittest.TestCase):

    def test_TrieTree(self):
        t = tries.Trie()
        words = ['quick', 'brown', 'the', 'fox',]
        for word in words:
            t.insert(word)
        self.assertEqual(t.search("thequickbrownfox"), ['the', 'quick', 'brown', 'fox'] )
        self.assertEqual(t.search("thequickbrownfoxy"), [] )
        self.assertEqual(t.search("thesdquickbrodfwnfoxy"), [] )
        self.assertEqual(t.search("thequickbrown"), ['the', 'quick', 'brown'] )

    def test_typeahead(self):

        res = tries.typeaheadSearch([
            ["ADD","question","q1","0.5","What does Adam"],
            ["QUERY","3","Ada Ada"]
        ])
        self.assertEqual(res, [['q1']])

        res = tries.typeaheadSearch([
            ["ADD","user","u1","1.0","Adam D'Angelo"],
            ["ADD","user","u2","1.0","Adam Black"],
            ["ADD","topic","t1","0.8","Adam D'Angelo"],
            ["QUERY","3","Ada"]
        ])
        self.assertEqual(res, [['u2', 'u1', 't1']])


        res = tries.typeaheadSearch([
            ["ADD","user","u1","1.0","Adam D'Angelo"],
            ["ADD","user","u2","1.0","Adam Black"],
            ["ADD","topic","t1","0.8","Adam D'Angelo"],
            ["ADD","question","q1","0.5","What does Adam D'Angelo do at Quora?"],
            ["ADD","question","q2","0.5","How did Adam D'Angelo learn programming?"],
            ["QUERY","10","Adam"],
            ["QUERY","10","Adam D'A"],
            ["QUERY","10","Adam Cheever"],
            ["QUERY","10","LEARN how"],
            ["QUERY","1","lear H"],
            ["QUERY","0","lea"],
            ["DEL","u2"],
            ["QUERY","2","Adam"]
        ])
        self.assertEqual(res,
            [["u2","u1","t1","q2","q1"],
            ["u1","t1","q2","q1"],
            [],
            ["q2"],
            ["q2"],
            [],
            ["u1","t1"]]
        )

        res = tries.typeaheadSearch(
            [["ADD","user","z","1.0","Adam   D'Angelo"],
            ["ADD","user","y","1.0","Adam   Black"],
            ["ADD","topic","p","0.8","Adam    D'Angelo"],
            ["ADD","question","q1","0.5","What   does Adam   D'Angelo do at Quora?"],
            ["ADD","question","q2","0.5","How did Adam D'Angelo learn programming?"],
            ["QUERY","10","Adam"],
            ["QUERY","10","Adam D'A"],
            ["QUERY","10","Adam Cheever"],
            ["QUERY","10","LEARN how"],
            ["QUERY","1","lear H"],
            ["QUERY","0","lea"],
            ["DEL","z"],
            ["QUERY","2","Adam"],
            ["DEL","y"],
            ["DEL","p"],
            ["DEL","q2"],
            ["QUERY","10","w"],
            ["DEL","q1"],
            ["QUERY","10","Adam D'A"]]
        )
        self.assertEqual(res[0],
            ["y","z","p","q2","q1"],
        )
        self.assertEqual(res[1],
            ["z","p","q2","q1"],
        )
        self.assertEqual(res[2],
            [],
        )
        self.assertEqual(res[3:],
            [
                ["q2"],
                ["q2"],
                [],
                ["y","p"],
                ["q1"],
                []
            ]
        )

        self.assertEqual(
            tries.typeaheadSearch(
            [
                [
                "QUERY",
                "13",
                "THE PASSIONATE PILGRIM"
                ],
                [
                "ADD",
                "board",
                "b8dc94d",
                "13.17",
                "I."
                ],
                [
                "ADD",
                "user",
                "uf04924",
                "25.27",
                "WHEN"
                ],
                [
                "ADD",
                "question",
                "q48c0b6",
                "37.45",
                "my love   swears that   she is made of truth,"
                ],
                [
                "ADD",
                "user",
                "udd7536",
                "71.66",
                "I"
                ],
                [
                "ADD",
                "question",
                "q29311e",
                "8.66",
                "do believe her, though I know she lies,"
                ],
                [
                "ADD",
                "question",
                "qb25cb6",
                "47.88",
                "That she might think me some untutor'd youth,"
                ],
                [
                "ADD",
                "question",
                "q2a648a",
                "34.20",
                "Unskilful in the world's false forgeries."
                ],
                [
                "ADD",
                "question",
                "q56547d",
                "75.45",
                "Thus vainly thinking that she thinks me young,"
                ],
                [
                "ADD",
                "question",
                "q283205",
                "47.17",
                "Although I know my years be past the best,"
                ],
                [
                "DEL",
                "udd7536"
                ],
                [
                "ADD",
                "question",
                "qb0e402",
                "22.53",
                "smiling credit her false-speaking tongue,"
                ],
                [
                "ADD",
                "question",
                "q740222",
                "49.21",
                "Outfacing faults in love with love's ill rest."
                ],
                [
                "ADD",
                "question",
                "q8c6160",
                "1.64",
                "But wherefore says my love that she is young?"
                ],
                [
                "ADD",
                "question",
                "q02d1e7",
                "15.63",
                "And wherefore say not I that I am old?"
                ],
                [
                "ADD",
                "question",
                "qea5f80",
                "64.15",
                "O, love's best habit is a soothing tongue,"
                ],
                [
                "ADD",
                "question",
                "q1e5307",
                "79.78",
                "And age, in love, loves not to have years told."
                ],
                [
                "ADD",
                "question",
                "q56a218",
                "61.44",
                "Therefore I'll lie with love, and love with me,"
                ],
                [
                "ADD",
                "question",
                "qa7532e",
                "30.40",
                "Since that our faults in love thus smother'd be."
                ],
                [
                "ADD",
                "board",
                "bd01124",
                "12.38",
                "II."
                ],
                [
                "ADD",
                "question",
                "q6a387a",
                "80.05",
                "Two loves I have, of comfort and despair,"
                ],
                [
                "ADD",
                "question",
                "q31c9b5",
                "45.36",
                "That like two spirits do suggest me still;"
                ],
                [
                "ADD",
                "question",
                "q925916",
                "38.21",
                "My better angel is  a man right fair,"
                ],
                [
                "ADD",
                "question",
                "q3173a1",
                "10.55",
                "My worser spirit a woman colour'd ill."
                ],
                [
                "QUERY",
                "8",
                "To win me"
                ],
                [
                "ADD",
                "question",
                "qeab7b5",
                "1.77",
                "Tempteth my better angel from my side,"
                ],
                [
                "ADD",
                "question",
                "q21d91b",
                "47.80",
                "And would corrupt my saint to be a devil,"
                ],
                [
                "ADD",
                "question",
                "q792840",
                "70.06",
                "Wooing his purity with her fair pride."
                ],
                [
                "ADD",
                "question",
                "q5c70fa",
                "22.42",
                "And whether that my angel be turn'd fiend,"
                ],
                [
                "ADD",
                "question",
                "q7fdfa7",
                "71.46",
                "Suspect I may, yet not directly tell:"
                ],
                [
                "ADD",
                "question",
                "q46c506",
                "21.58",
                "For being both to me, both to each friend,"
                ],
                [
                "ADD",
                "user",
                "udd7536",
                "59.33",
                "I"
                ],
                [
                "ADD",
                "question",
                "q8761cb",
                "39.57",
                "guess one angel in another's hell;"
                ],
                [
                "ADD",
                "question",
                "q8f9b64",
                "42.08",
                "The truth I shall not know, but live in doubt,"
                ],
                [
                "ADD",
                "question",
                "q199e49",
                "56.43",
                "Till my bad angel fire my good one out."
                ],
                [
                "ADD",
                "board",
                "bcd3a76",
                "65.87",
                "III."
                ],
                [
                "ADD",
                "question",
                "qe8fda7",
                "40.30",
                "Did not the heavenly rhetoric of thine eye,"
                ],
                [
                "ADD",
                "question",
                "qf3c626",
                "90.39",
                "'Gainst whom the world could not hold argument,"
                ],
                [
                "ADD",
                "question",
                "q8cd2b0",
                "62.18",
                "Persuade my heart to this false perjury?"
                ],
                [
                "ADD",
                "question",
                "q99f2e6",
                "2.70",
                "Vows for thee broke deserve not punishment."
                ],
                [
                "ADD",
                "user",
                "u7fc562",
                "29.05",
                "A"
                ],
                [
                "ADD",
                "question",
                "q5c9762",
                "97.75",
                "woman I forswore; but I will prove,"
                ],
                [
                "ADD",
                "question",
                "q264669",
                "76.70",
                "Thou being a goddess, I forswore not thee:"
                ],
                [
                "ADD",
                "question",
                "qd69552",
                "33.71",
                "My vow was earthly, thou a heavenly love;"
                ],
                [
                "ADD",
                "question",
                "q1e8036",
                "48.07",
                "Thy grace being gain'd cures all disgrace in me."
                ],
                [
                "ADD",
                "question",
                "q2e72a2",
                "76.73",
                "My vow was breath, and breath a vapour is;"
                ],
                [
                "ADD",
                "question",
                "q0de296",
                "45.82",
                "Then, thou fair sun, that on this earth doth shine,"
                ],
                [
                "ADD",
                "question",
                "q401fd2",
                "62.35",
                "Exhale this vapour vow; in thee it is:"
                ],
                [
                "ADD",
                "question",
                "qf5f9fb",
                "86.68",
                "If broken, then it is no fault of mine."
                ],
                [
                "QUERY",
                "6",
                "If by me"
                ],
                [
                "ADD",
                "question",
                "qc90b40",
                "29.76",
                "To break an oath, to win a paradise?"
                ],
                [
                "ADD",
                "board",
                "b040e3d",
                "90.32",
                "IV."
                ],
                [
                "QUERY",
                "5",
                "Swe Cyt sit"
                ],
                [
                "ADD",
                "question",
                "qb80390",
                "50.14",
                "With young Adonis, lovely, fresh, and green,"
                ],
                [
                "ADD",
                "question",
                "q4fa905",
                "68.59",
                "Did court the lad with many a lovely look,"
                ],
                [
                "ADD",
                "question",
                "qcaf58b",
                "95.65",
                "Such looks as none could look but beauty's queen."
                ],
                [
                "ADD",
                "question",
                "q6a0d2d",
                "92.82",
                "She told him stories to delight his ear;"
                ],
                [
                "ADD",
                "question",
                "qdd2eb2",
                "61.48",
                "She showed him favors to allure his eye;"
                ],
                [
                "ADD",
                "question",
                "q7c0eee",
                "13.83",
                "To win his heart, she touch'd him here and there,--"
                ],
                [
                "ADD",
                "question",
                "q6a45ff",
                "69.06",
                "Touches so soft still conquer chastity."
                ],
                [
                "ADD",
                "question",
                "q0cbdb2",
                "19.23",
                "But whether unripe years did want conceit,"
                ],
                [
                "ADD",
                "question",
                "q3ad7f4",
                "3.06",
                "Or he refused to take her figured proffer,"
                ],
                [
                "ADD",
                "question",
                "qcbb3c9",
                "15.01",
                "The tender nibbler would not touch the bait,"
                ],
                [
                "ADD",
                "question",
                "qa312cd",
                "8.74",
                "But smile and jest at every gentle offer:"
                ],
                [
                "ADD",
                "question",
                "qe199c2",
                "91.00",
                "Then fell she on her back, fair queen, and toward:"
                ],
                [
                "ADD",
                "question",
                "q2b5526",
                "8.62",
                "He rose and ran away; ah, fool too froward!"
                ],
                [
                "ADD",
                "board",
                "b2a8f4d",
                "70.56",
                "V."
                ],
                [
                "ADD",
                "question",
                "q668664",
                "52.43",
                "If love make me forsworn, how shall I swear to love?"
                ],
                [
                "ADD",
                "user",
                "uf18621",
                "21.72",
                "O"
                ],
                [
                "ADD",
                "question",
                "q625234",
                "67.24",
                "never faith could hold, if not to beauty vow'd:"
                ],
                [
                "ADD",
                "question",
                "q5c5fb7",
                "49.17",
                "Though to myself forsworn, to thee I'll constant prove;"
                ],
                [
                "ADD",
                "question",
                "q37f99c",
                "2.79",
                "Those thoughts, to me like oaks, to thee like osiers bow'd."
                ],
                [
                "ADD",
                "question",
                "q9ac294",
                "56.02",
                "Study his bias leaves, and makes his book thine eyes,"
                ],
                [
                "ADD",
                "question",
                "q45cadc",
                "58.34",
                "Where all those pleasures live that art can comprehend."
                ],
                [
                "ADD",
                "question",
                "q2ff30f",
                "55.39",
                "If knowledge be the mark, to know thee shall suffice;"
                ],
                [
                "ADD",
                "question",
                "q239eca",
                "10.53",
                "Well learned is that tongue that well can thee commend;"
                ],
                [
                "ADD",
                "question",
                "qb20759",
                "43.72",
                "All ignorant that soul that sees thee without wonder;"
                ],
                [
                "ADD",
                "question",
                "qeebf4b",
                "42.03",
                "Which is to me some praise, that I thy parts admire:"
                ]
            ]),
            [[], [], [], []]

        )


if __name__ == '__main__':
    unittest.main()