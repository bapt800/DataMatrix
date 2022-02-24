import reedsolo

class DataMatrix:
    def __init__(self) -> None:
        self.matrix = [[0 for x in range(10)] for y in range(10)]
        self.lst_codeWord = []
        self.numberOfBlockUsed = 0
        
        self.topologie = (
                            (   (0, 8), (0, 9), (1, 8), (1, 9), (3, 0), (2, 8), (2, 9), (4, 0)  ),
                            (   (0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)  ),
                            (   (8, 0), (8, 1), (9, 0), (9, 1), (9, 2), (0, 2), (0, 3), (0, 4)  ),
                            (   (9, 3), (9, 4), (0, 5), (0, 6), (0, 7), (1, 5), (1, 6), (1, 7)  ),
                            (   (1, 3), (1, 4), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)  ),
                            (   (3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3)  ),
                            (   (3, 9), (5, 0), (4, 9), (6, 0), (6, 1), (5, 9), (6, 0), (7, 0)  ), 
                            (   (6, 2), (6, 3), (7, 2), (7, 3), (7, 4), (8, 2), (8, 3), (8, 4)  ), 
                            (   (4, 4), (4, 5), (5, 4), (5, 5), (5, 6), (6, 4), (6, 5), (6, 6)  ),
                            (   (2, 6), (2, 7), (3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8)  ),
                            (   (5, 7), (5, 8), (6, 7), (6, 8), (6, 9), (7, 7), (7, 8), (7, 9)  ),
                            (   (7, 5), (7, 6), (8, 5), (8, 6), (8, 7), (9, 5), (9, 6), (9, 7)  )
                        )


    def set_block(self, block_id, codeWord:int):
        assert self.numberOfBlockUsed < 5
        #wrong for corrector code #assert codeWord >= 130, "wrong codeWorld for number: 00-99"
        #wrong for corrector code #assert codeWord <= 229, "wrong codeWorld for number: 00-99"
        bin_data = bin(codeWord)
        bin_data = "0b11"
        while len(bin_data) != 10:
            bin_data = bin_data[:2] + '0' + bin_data[2:]

        for i in range(8):
            self.matrix[self.topologie[block_id][i][0]][self.topologie[block_id][i][1]] = int(bin_data[i+2])
        self.numberOfBlockUsed +=1
        self.lst_codeWord.append(codeWord)
    
    def add_remplisage(self):
        def calcCodeWord_Corrector(nbCodeWord_Used):
            PsAlea = ((149 * nbCodeWord_Used) % 253) + 1
            CW = (129 + PsAlea) % 254
            return CW

        assert self.numberOfBlockUsed <= 5
        if self.numberOfBlockUsed == 5:
            return

        self.set_block(self.numberOfBlockUsed, 129) #first does not use calc fx
        for i in range(self.numberOfBlockUsed, 5):
            CodeWord_fill = calcCodeWord_Corrector(self.numberOfBlockUsed +i )
            self.set_block(i, CodeWord_fill)

    def add_redSolomon(self):
        assert self.numberOfBlockUsed == 5
        rsc = reedsolo.RSCodec(7)
        print(self.lst_codeWord)
        print(rsc.encode(self.lst_codeWord))
        for i in range(12):
            print(int(rsc.encode(self.lst_codeWord))[i])

    


DM = DataMatrix()

print(DM.matrix)
DM.set_block(1, 229)
DM.add_remplisage()
print("---")
DM.add_redSolomon()
print("---")
print(DM.matrix)
print(DM.numberOfBlockUsed)