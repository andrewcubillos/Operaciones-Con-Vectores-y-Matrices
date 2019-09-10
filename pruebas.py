from Operacionesconvectoresymatrices import *
from numeros complejos import*

import unittest

class PruebasFunciones(unittest.TestCase):
    def test(self):
        self.assertEqual(sumav([(6, -4), (7, 3),(4.2,-8.1),(0,-3)],[(16, 2), (0, -7),(6,0),(0,-4)]),[(22, -2), (7, -4),(10.2,-8.1),(0,-7)])

        self.assertEqual(inverso([(6, -4), (7, 3),(4.2,-8.1),(0,-3)]),[(-6, 4), (-7, -3),(-4.2,8.1),(0,3)])

        self.assertEqual(escalarv((3,2),[(6, 3), (0, 0),(5,1),(4,0)]),[(12, 21), (0, 0),(13,13),(12,8)])

        self.assertEqual(sumam([[(3,2),(0,0)],
                                [(1,0),(4,2)]],
                               [[(5,0),(2,-1)],
                                [(0,0),(4,5)]]), [[(8, 2),(2,-1)],[(1,0),(8,7)]])

        self.assertEqual(inversam([[(-2, 1), (7, 4)],
                                [(-2, 11), (7, 9)]]),
                         [[(2, -1), (-7, -4)],
                          [(2, -11), (-7,-9)]])


        self.assertEqual(escalarm((1,2),[[(0,1),(3,-2)],[(4,3),(5,-1)]]),[[(-2,1),(7,4)],[(-2,11),(7,9)]])

        self.assertEqual(trans([[(-2,1),(7,4)],
                                [(-2,11),(7,9)]]),
                         [[(-2,1),(-2,11)],
                          [(7,4),(7,9)]])
        
        self.assertEqual(conjugada([[(-8,1),(-2,11)],
                          [(3,-4),(4,-9)]]),
                         [[(-8,-1),(-2,-11)],
                          [(3,4),(4,9)]])
        
        self.assertEqual(adjunta([[(-8,1),(-2,11)],
                                  [(3,-4),(4,-9)]]),
                         [[(-8,-1),(3,4)],
                          [(-2,-11),(4,9)]])
        self.assertEqual(norma([[(0, 1), (0, 1)],[(0, 1), (0, 1)]]),4)
        
        self.assertEqual(accion([[(-2,0),(7,0)],
                               [(-9,0),(3,0)]],[[(1,0)],[(1,0)]]),[[(5, 0)], [(-6, 0)]])
        
        self.assertEqual(distancia([[(3,2),(0,0)],[(9,0),(4,2)],[(3,0),(2,-1)],[(0,0),(4,5)]],
                               [[(9,1),(14,2)],[(12,0),(3,1)],[(2,7),(2,4)],[(4,1),(1,3)]]), 190.24457942343588)
        
        self.assertEqual(unitaria([[(1/2,1/2),(1/2,-1/2)],
                                  [(1/2,-1/2),(1/2,1/2)]]),"The matrix is a unitary matrix")
        self.assertEqual(unitaria([[(3/2,1/2),(1/2,-1/2)],
                                  [(1/2,-1/2),(7/2,1/2)]]),"The matrix is not a unitary matrix")
        

                                                
        
        self.assertEqual(hermitian([[(7,0),(6,5)],
                                  [(6,-5),(-3,0)]]),"The matrix is hermitian")
        
        self.assertEqual(tensor([[(1,0),(2,0)],[(3,0),(4,0)]],
                                [[(-1,0),(-2,0)],[(-3,0),(-4,0)]]),
                                 [[(-1, 0), (-2, 0), (-2, 0), (-4, 0)], [(-3, 0), (-4, 0), (-6, 0), (-8, 0)],
                   [(-3, 0), (-6, 0), (-4, 0), (-8, 0)], [(-9, 0), (-12, 0), (-12, 0), (-16, 0)]])
        

       
                
        
      
        

        



                                                
        
       
                
        
      
        

        


if __name__ == '__main__':
    unittest.main()
