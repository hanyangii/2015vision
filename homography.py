import math
import numpy

def homographyMatrix(*param):
    dof = param[0]
    length = len(dof)
    print length
   
#Translation
   if length == 2:
       dx = dof[0]
       dy = dof[1]
       H = numpy.matrix(((1,0,dx),
                        (0,1,dy),
                        (0,0,1)))
       return H

#Euclidean
   elif length == 3:
        dx = dof[0]
        dy = dof[1]
        theta = math.radians(dof[2])
        H=numpy.matrix(((math.cos(theta), -math.sin(theta), dx),
                        (math.sin(theta), math.cos(theta), dy),
                        (0,0,1)))
        return H
       
#Similarity
   elif length == 4:
        dx=dof[0]
        dy=dof[1]
        theta=math.radians(dof[2])
        scale=dof[3]
        
        H = numpy.matrix(((scale*math.cos(theta), -scale*math.sin(theta), dx),
                           (scale*math.sin(theta), scale*math.cos(theta), dy),
                           (0,0,1)))
        return H

#Affine
    elif length = 6:
        a00=dof[0]
        a10=dof[1]
        a01=dof[2]
        a11=dof[3]
        a02=dof[4]
        a12=dof[5]

        H = numpy.matrix(((a00, a01, a02),
                          (a10, a11, a12),
                          (0,0,1)))
        return H

#Projective
   elif length == 9:
        H00=dof[0]
        H10=dof[1]
        H20=dof[2]
        H01=dof[3]
        H11=dof[4]
        H21=dof[5]
        H02=dof[6]
        H12=dof[7]
        H22=dof[8]

        H=numpy.matrix(((H00, H01, H02),
                        (H10, H11, H12),
                        (H20, H21, H22)))
        return H

   else:
       print 'wrong number of parameter' 
