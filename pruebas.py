import Operacionesconvectoresymatrices

import unittest

class PruebasFunciones(unittest.TestCase):
    
    def test1(self):
        self.assertEqual([(22, -2), (7, -4),(10.2,-8.1),(0,-7)], Operacionesconvectoresymatrices.sumav([(6, -4), (7, 3),(4.2,-8.1),(0,-3)],[(16, 2), (0, -7),(6,0),(0,-4)]))
    
    def test2(self):
        self.assertEqual([(-6, 4), (-7, -3),(-4.2,8.1),(0,3)],Operacionesconvectoresymatrices.inverso([(6, -4), (7, 3),(4.2,-8.1),(0,-3)]))
    
    def test3(self): 
        self.assertEqual([(12, 21), (0, 0),(13,13),(12,8)],Operacionesconvectoresymatrices.escalarv((3,2),[(6, 3), (0, 0),(5,1),(4,0)]))
    
    def test4(self):
        self.assertEqual([[(8, 2),(2,-1)],[(1,0),(8,7)]],Operacionesconvectoresymatrices.sumam([[(3,2),(0,0)],
                                [(1,0),(4,2)]],
                               [[(5,0),(2,-1)],
                                [(0,0),(4,5)]]))
    def test5(self):
        self.assertEqual([[(2, -1), (7, -4)], [(2, -11), (-7, -9)]],Operacionesconvectoresymatrices.inversam([[(-2, 1), (-7, 4)],
                                [(-2, 11), (7, 9)]]))

    def test6(self):
        self.assertEqual([[(-2,1),(7,4)],[(-2,11),(7,9)]],Operacionesconvectoresymatrices.escalarm((1,2),[[(0,1),(3,-2)],[(4,3),(5,-1)]]))

    def test7(self):
        self.assertEqual([[(-2,1),(-2,11)],
                          [(7,4),(7,9)]],Operacionesconvectoresymatrices.trans([[(-2,1),(7,4)],
                                [(-2,11),(7,9)]]))
    def test8(self):        
        self.assertEqual([[(-8,-1),(-2,-11)],
                          [(3,4),(4,9)]],Operacionesconvectoresymatrices.conjugada([[(-8,1),(-2,11)],
                          [(3,-4),(4,-9)]]))
    def test9(self):        
        self.assertEqual([[(-8,-1),(3,4)],
                          [(-2,-11),(4,9)]],Operacionesconvectoresymatrices.adjunta([[(-8,1),(-2,11)],
                                  [(3,-4),(4,-9)]]))
    def test10(self):
        self.assertEqual(4,Operacionesconvectoresymatrices.norma([[(0, 1), (0, 1)],[(0, 1), (0, 1)]]))
    
    def test11(self):
        
        self.assertEqual([[(5, 0)], [(-6, 0)]],Operacionesconvectoresymatrices.accion([[(-2,0),(7,0)],
                               [(-9,0),(3,0)]],[[(1,0)],[(1,0)]]))
    def test12(self):
        
        self.assertEqual(190.24457942343588,Operacionesconvectoresymatrices.distancia([[(3,2),(0,0)],[(9,0),(4,2)],[(3,0),(2,-1)],[(0,0),(4,5)]],
                               [[(9,1),(14,2)],[(12,0),(3,1)],[(2,7),(2,4)],[(4,1),(1,3)]]))
    def test13(self):        
        self.assertEqual("The matrix is a unitary matrix",Operacionesconvectoresymatrices.unitaria([[(1/2,1/2),(1/2,-1/2)],
                                  [(1/2,-1/2),(1/2,1/2)]]))
    def test14(self):        
        self.assertEqual("The matrix is not a unitary matrix",Operacionesconvectoresymatrices.unitaria([[(3/2,1/2),(1/2,-1/2)],
                                  [(1/2,-1/2),(7/2,1/2)]]))
        

                                                
    def test15(self):        
        self.assertEqual("The matrix is hermitian",Operacionesconvectoresymatrices.hermitian([[(7,0),(6,5)],
                                  [(6,-5),(-3,0)]]))
    def test16(self):        
        self.assertEqual([[(-1, 0), (-2, 0), (-2, 0), (-4, 0)], [(-3, 0), (-4, 0), (-6, 0), (-8, 0)],
                   [(-3, 0), (-6, 0), (-4, 0), (-8, 0)], [(-9, 0), (-12, 0), (-12, 0), (-16, 0)]],Operacionesconvectoresymatrices.tensor([[(1,0),(2,0)],[(3,0),(4,0)]],
                                [[(-1,0),(-2,0)],[(-3,0),(-4,0)]]))                     
        
      
        

        


if __name__ == '__main__':
    unittest.main()
