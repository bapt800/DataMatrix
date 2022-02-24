from DataMatrix import DataMatrix

def test_DataMatrix_init():
    DMatrix = DataMatrix()
    assert DMatrix.matrix == [[0 for x in range(8)] for y in range(8)]

