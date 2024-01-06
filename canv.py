#!/usr/bin/python3
import threading
from gi.repository import GObject
#import struct
import time
import gi
gi.require_version('PangoCairo', '1.0')
gi.require_version('Gtk', '3.0')
#import cairo
#
from gi.repository import GLib
from gi.repository import Gio,Gtk, Gdk, cairo, Pango, PangoCairo

#from gi.repository import GObject
import cairo
import  gtk
import locale
import os
import sys
import math
sys.path.append('venv/lib/python3.6/site-packages')
import numpy as np
from numpy import arange
import ctypes
class numbering(object):
    def __init__(self,X1,Y1):
        int: X1
        int: Y1
        self.X1 = X1
        self.Y1 = Y1
from  array import *
#from typing import NamedTuple
class Coords(object):
    def __init__(self,X1,Y1,X2,Y2,StartNode,EndNode):
        float: X1
        float: Y1
        float: X2
        float: Y2
        str: StartNode
        str: EndNode
        self.X1 = X1
        self.Y1 = Y1
        self.X2 = X2
        self.Y2 = Y2
        self.StartNode=StartNode
        self.EndNode = EndNode
class UniqueNode(object):
    def __init__(self,StartNode,EndNode,angle,X,Y):
        str:StartNode
        str:EndNode
        float: angle
        float: X
        float: Y
        self.StartNode=StartNode
        self.EndNode = EndNode
        self.angle=angle
        self.X=X
        self.Y=Y
class Node(object):
    def __init__(self,  name ,  X,  Y):
        str :name
        float :X
        float :Y
        self.name = name
        self.X = X
        self.Y = Y
class  Beam(object):
    def __init__(self,name,StartNode,EndNode,xl,yl,Elasticity,Inertia,Area,H,at,N1,Q1,M1,N2,Q2,M2,regflag):
        name      : str
        StartNode : str
        EndNode   : str
        xl :float
        yl :float
        Elasticity : float
        Inertia: float
        Area : float
        H: float
        at: float
        N1: float
        Q1: float
        M1: float
        N2: float
        Q2: float
        M2: float
        regflag: int
        #MS: bool
        #ME: bool
        self.name=name
        self.StartNode=StartNode
        self.EndNode = EndNode
        self.xl=xl
        self.yl = yl
        self.Elasticity=Elasticity
        self.Inertia=Inertia
        self.Area=Area
        self.H=H
        self.at = at
        self.N1 = N1
        self.Q1 = Q1
        self.M1 = M1
        self.N2 = N2
        self.Q2 = Q2
        self.M2 = M2
        self.regflag=regflag
        # regflag xxxx   binary
        #         ||||
        #         ||||
        #         ||||- RMS 0 false 1 true
        #         ||||- RMES 0 false 1 true
        #         ||- DDS 0 false 1 true
        #         | - DDE 1 false 1 true
        #  RMS Release Moments Start Node
        #  RME Release Moments End Node
        #  DDS Dependent displacement and angle on endnode from Startnode
        #  DDE Dependent displacement and angle on startnode from Endnode
class  Beamunit(object):
    def __init__(self,name,N1,Q1,M1,N2,Q2,M2):
        name      : str
        N1: float
        Q1: float
        M1: float
        N2: float
        Q2: float
        M2: float
        self.name=name
        self.N1 = N1
        self.Q1 = Q1
        self.M1 = M1
        self.N2 = N2
        self.Q2 = Q2
        self.M2 = M2
class Graph(object):
    def __init__(self,name,X1,Y1,X2,Y2):
        name:str
        X1: float
        Y1: float
        X2: float
        Y2: float
        self.name=name
        self.X1=X1
        self.Y1 = Y1
        self.X2 = X2
        self.Y2 = Y2


class DynamicArray(object):

    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''
    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds !')

        return self.A[k]  # Retrieve from the array at index k


    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)

        self.A[self.n] = ele  # Set self.n index to element
        self.n += 1

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """

        B = self.make_array(new_cap)  # New bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]
        self.A = B  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity
    def _copyitem(self,ind):
        C=self.make_array(self.n+1)
        self.n += 1
        self.capacity = self.n

        for k in range(0,ind+1):
            C[k]=self.A[k]
        for k in range(ind+1,len(C)):
            if (k==ind+1):
                #By Value
                C[k] = Node(self.A[k-1].name,self.A[k-1].X,self.A[k-1].Y)
            else:
                C[k]=self.A[k-1]
        self.A=C


    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()

    def removeAt(self, index):
        """
        This function deletes item from a specified index..
        """

        if self.n == 0:
            print("Array is empty deletion not Possible")
            return

        if index < 0 or index >= self.n:
            return IndexError("Index out of bound....deletion not possible")
        B = self.make_array(self.n-1)
        c=0
        for k in range(self.n):  # Reference all existing values
            if k!=index:
                B[c] = self.A[k]
                c+=1
        self.n -= 1
        self.capacity = self.n
        self.A=B
# def OnDraw(w, cr):
#    p=w.get_allocation()
#    a1=1
#    a2=2
#    b1=3
#    b2=4
#    x = np.array([[a1, a2], [b1, b2]])
#    a=np.array([[2],[3]])
#    y = np.linalg.solve(x,a)
#    print(x)
#    print(y)
    #np.dot(x, y)
#    print("height: "+str(p.height))
#    cr.set_source_rgb(1, 1, 0)
#    cr.arc(320,240,100, 0, 1.5*math.pi)
#    cr.stroke_preserve()

#    cr.set_source_rgb(0, 0, 0)
#    cr.stroke()

   # cr.arc(280,210,20, 0, 2*math.pi)
   # cr.arc(360,210,20, 0, 2*math.pi)
   # cr.fill()
#   cr.set_source_rgb(3, 0, 0)
#    cr.set_line_width(10)
#    cr.set_line_cap(cairo.LINE_CAP_SQUARE)
   # cr.arc(320, 240, 60, math.pi/4, math.pi*3/4)
    #cr.stroke()
#    cr.set_line_width(1)
#    for i in range(int(0),int(p.width)):
        #cr.move_to(int(i),int((i*i)/((p.height))))
#        cr.move_to(int(i), p.height)
#        cr.line_to(int(i)+1,1+int((i*i)/((p.height))))
#        cr.stroke()
 #       cr.fill()

#    cr.move_to(0,int(p.height/4))
#    cr.line_to(p.width/2,int(p.height/4))

#    cr.stroke()
#    cr.set_line_width(2)
#    cr.set_source_rgb(1, 0, 0)

    #cr.move_to (220,30)
    #cr.line_to(219,29)
#    cr.stroke()
class Switcher(object):
    def indirect(self, file):
         method_name = MyWindow.lastcommand  # 'number_' + str(i)
         method = getattr(self, method_name, lambda: 'Invalid')
         return method(file)

    def BEAM(self,file):

        beams = DynamicArray()
        beamunit=DynamicArray()
        #MyWindow.karray=np.zeros((3*len(localnodes),3*len(localnodes)))
        # MyWindow.results=np.zeros(3*len(localnodes))
        # MyWindow.fixedresults=np.zeros(3*len(localnodes))

        MyWindow.line="r"
        while MyWindow.line:
            MyWindow.line=file.readline()
            if (MyWindow.line[0:4].upper() == "Node".upper()):
                return "Duplicate Node command in line " + str(MyWindow.cnt)
            MyWindow.cnt+=1
            if (MyWindow.line[0:4].upper()!="Beam".upper() and MyWindow.line[0:8].upper()!="Material".upper() and MyWindow.line[0:5].upper() != "Loads".upper() and MyWindow.line[0:11].upper()!="Beam fixing".upper() and MyWindow.line[0:11].upper()!="Node fixing".upper()):
                if (len(MyWindow.line) > 0 and MyWindow.line[0:1] != "#" and MyWindow.line[0:1] != "\n"):
                    linesplit = MyWindow.line.split((" "))
                    k = 0
                    st = ""
                    for st in linesplit:
                        flag = False
                        if (st != "\n"):
                            if ((st != " ") and (k == 0) and (not flag)):
                                if st[-1]=="\n":
                                    return "Beam not  defined in line "+str(MyWindow.cnt)
                                beamname = st
                                omoiarabd = False
                                if (len(beams)>1):
                                    for e in range(0,len(beams)):
                                        if (beamname==beams[e].name):
                                            omoiarabd=True
                                            break
                                if omoiarabd:
                                    return "Duplicate beam name in Line "+str(MyWindow.cnt)
                                flag = True
                                k += 1
                            if ((st != " ") and (k == 1) and (not flag)):
                                startnode = st
                                k += 1
                                flag = True
                        #If I have brackets, we have angle
                            if ((st != " ") and (k == 2) and (not flag)):
                                if(st[0]=="("):
                                    if  (st[-2]==")"):
                                        angle=float(st.strip("(").strip(")")[0:-2])
                                        endnode=startnode
                                        startnode=endnode+"SPRING"
                                        flag=False
                                        for u in range(len(MyWindow.localnodes)):
                                            if (MyWindow.localnodes[u].name==startnode):
                                                flag=True
                                                break
                                        #Case not met node not found
                                        if not flag:
                                            MyWindow.fullNode = Node(startnode, "", "")
                                            MyWindow.fullNode.X = str(angle)
                                            MyWindow.fullNode.X.strip()
                                            MyWindow.localnodes.append(MyWindow.fullNode)
                                        else:
                                            for u in range(len(MyWindow.localnodes)):
                                                if (MyWindow.localnodes[u].name == startnode):
                                                    #Put in reverse order
                                                    MyWindow.localnodes[u].X=MyWindow.localnodes[u].X+" "+str(angle)
                                                    break
                                elif (st[-1] == "\n"):
                                   endnode = st[0:-1]
                                else:
                                   endnode =  float(st)
                                if startnode.strip()==endnode.strip() and not (startnode.__contains__("SPRING")):
                                    return "Same startnode and endnode in beamnum "+beamname+" in line "+str(MyWindow.cnt)
                                k += 1
                                #See the angle
                                if(len(beams)>0):
                                    symptosh=False
                                    for e in range(len(beams)):
                                        if not beams[e].StartNode.__contains__("SPRING"):
                                            if ((startnode.strip()==beams[e].StartNode and (endnode.strip()==beams[e].EndNode)) or
                                            (startnode.strip() == beams[e].EndNode and (endnode.strip() == beams[e].StartNode))):
                                                symptosh=True
                                                break
                                            if ((startnode.strip() == beams[e].StartNode and (
                                                  endnode.strip() == beams[e].EndNode)) or
                                                  (startnode.strip() == beams[e].EndNode and (
                                                      endnode.strip() == beams[e].StartNode))):
                                                    symptosh = True
                                                    break
                                        else:
                                           if ((startnode.strip()==beams[e].StartNode) and (endnode.strip()==beams[e].EndNode) and (angle==beams[e].xl)):
                                                    symptosh= True
                                                    break
                                    if symptosh:
                                        return "Duplicate beam  "+beams[k].name+ " in line "+str(MyWindow.cnt)
                                #fullNode = Node(namnode, Xnode, Ynode)
                                snode=MyWindow.findobject(self,startnode,MyWindow.nodes)
                                enode = MyWindow.findobject(self, endnode, MyWindow.nodes)
                                if not startnode.__contains__("SPRING"):
                                    x=MyWindow.nodes[enode].X-MyWindow.nodes[snode].X
                                    y=MyWindow.nodes[enode].Y-MyWindow.nodes[snode].Y
                                    beam = Beam(beamname, startnode, endnode,x,y,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3)

                                else:
                                    #ιδεατή ράβδος (ελαστική στήριξη)
                                    beam = Beam(beamname, startnode, endnode,angle, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                0.0, 0.0, 0.0, 0.0,3)
                                # MyWindow.karray=np.zeros((3*len(localnodes),3*len(localnodes)))
                                # MyWindow.results=np.zeros(3*len(localnodes))
                                # MyWindow.fixedresults=np.zeros(3*len(localnodes))

                                beams.append(beam)
                        if (k > 2):
                            break
                        if ((st != "\n") and (k == 0)):
                            if (k <= 2):
                                return "Error in Line " + str(MyWindow.cnt) + " too few arguments"

                        elif (st == "\n" and (k <= 2)):
                            return "Error in Line " + str(MyWindow.cnt) + " too few arguments"

            else:
              if  len(beams)>=1:
                MyWindow.lastcommand = MyWindow.line[0:-1]

                return beams
              else:
                return "Error no beams defined"

        return None


    def NODE(self,file):
        MyWindow.line="r"
        while MyWindow.line:
            MyWindow.line=file.readline()
            MyWindow.cnt+=1
            if (MyWindow.line[0:4].upper()!="Beam".upper() and MyWindow.line[0:8].upper()!="Material".upper() and MyWindow.line[0:5].upper() != "Loads".upper() and MyWindow.line[0:11].upper()!="Beam fixing".upper() and MyWindow.line[0:11].upper()!="Node fixing".upper()):
                if (len(MyWindow.line) > 0 and MyWindow.line[0:1] != "#" and MyWindow.line[0:1] != "\n"):
                    linesplit = MyWindow.line.split((" "))
                    k = 0
                    st = ""
                    for st in linesplit:
                        flag = False
                        if (st != "\n"):
                            if ((st != " ") and (k == 0) and (not flag)):
                                namnode = str(st)

                                flag = True
                                k += 1
                            if ((st != " ") and (k == 1) and (not flag)):
                                try:
                                    Xnode = float(st)
                                except ValueError:
                                    return "Node X value must be a number in Line: "+str(MyWindow.cnt)
                                k += 1
                                flag = True
                                if len(MyWindow.localnodes)>0:
                                    for u in range(len(MyWindow.localnodes)):
                                        if (MyWindow.localnodes[u].name[-6:].upper()=="SPRING"):
                                            return "Reserved word SPRING used in Node "+MyWindow.localnodes[u].name.strip("SPRING")+" in Line: " + str(MyWindow.cnt-1)
                                        if (namnode==MyWindow.localnodes[u].name):
                                            return "Duplicate Node name in Line: "+str(MyWindow.cnt)
                            if ((st != " ") and (k == 2) and (not flag)):
                                try:
                                    if (st[-1] == "\n"):
                                        Ynode = float(st[0:-1])
                                    else:
                                        Ynode = float(st)
                                except ValueError:
                                    return "Node Y value must be a number in Line: " + str(MyWindow.cnt)
                                k += 1
                                MyWindow.fullNode = Node(namnode, Xnode, Ynode)
                                MyWindow.localnodes.append(MyWindow.fullNode)

                            flag = True
                        if (k > 2):
                            break
                        if ((st != "\n") and (k == 0)):
                            if (k <= 2):
                                print("Error in Line " + str(MyWindow.cnt) + " too few arguments")
                                exit()
                        elif (st == "\n" and (k <= 2)):
                            print("Error in Line " + str(MyWindow.cnt) + " too few arguments")
                            exit()
            else:
              MyWindow.lastcommand=MyWindow.line[0:-1]
              if len(MyWindow.localnodes)>1:
                  #Initialize stiffness matrix and its results which will be populated and solved
                  # 3 are the degrees of freedom per node
                  #MyWindow.karray=np.zeros((3*len(localnodes),3*len(localnodes)))
                  #MyWindow.results=np.zeros(3*len(localnodes))
                  #MyWindow.fixedresults=np.zeros(3*len(localnodes))
                  #MyWindow.karray[r][c]=1.
                  return MyWindow.localnodes
              else:
                  if len(MyWindow.localnodes) == 1:
                      return "Not enough nodes!\nDefine at least 2 Nodes"
                  else:
                      return "No nodes found!\nDefine at least 2 Nodes"
    def Irect(self,b,h):
        return 1/12*b*pow(h,3.0)
    def Arect(self,b,h):
        return b*h

    def kspringcomputations(self, k):
        startNodeIndex = 0
        endNodeIndex = 1
        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 0] = k

        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1] = 0
        # symmetric
        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 0] = 0

        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2] = 0
        # symmetric
        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 0] = \
            MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
        # 2nd line
        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = 0
        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = 0
        # symmetric
        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
        # 3rd line
        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = 0

        # Top Right and Lower Left bands
        # 1 line
        MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0] = - k
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 0] = \
            MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0]

        MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 1] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 0] = \
            MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 1]

        MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 2] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 0] = \
            MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 2]

        # 2nd line
        MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 0] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 1] = \
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 0]

        MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = 0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = \
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]

        MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = 0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]

        MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 0] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 2] = \
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 0]

        MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = 0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = \
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]

        MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = \
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2]

        # Lower Right sub matrix
        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0] = k

        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 0] = \
            MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]

        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 0] = \
            MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
        ###
        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = 0

        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = 0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = \
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]

        ####

        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 0
        return
    #def kbeamcomputations(self,El,I,A,lbeam,m1,m2):
    def kbeamcomputations(self, El, I, A, lbeam, regflag,beams):#),neighboringbeams):
        #n1 q1 m1
        #n2 q2 m2 1 for fixed and 0 for released
        regflag=3
        startNodeIndex = 0
        endNodeIndex = 1
        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 0] = El * A / lbeam
        #if neighboringbeams != None:
        #    for nei in range(0,len(neighboringbeams)):
        #        if  (MyWindow.beams[MyWindow.findobject(MyWindow, neighboringbeams[nei], MyWindow.beams)].regflag & 4) == 4 and \
        #                MyWindow.beams[MyWindow.findobject(MyWindow, beams, MyWindow.beams)].StartNode == MyWindow.beams[
        #                    MyWindow.findobject(MyWindow, neighboringbeams[nei], MyWindow.beams)].EndNode:
        #MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 0] = 0.0


        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1] = 0
        # symmetric
        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 0] = 0

        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2] = 0
        # symmetric
        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 0] = \
            MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
        # 2nd line
        if regflag & 3 ==3: #m1==1 and m2==1:
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = 12 * El * I / math.pow(lbeam, 3.0)
            #if neighboringbeams != None:
            #    for nei in range(0,len(neighboringbeams)):
            #        if (MyWindow.beams[MyWindow.findobject(MyWindow,neighboringbeams[nei],MyWindow.beams)].regflag & 4)==4 and \
            #            MyWindow.beams[MyWindow.findobject(MyWindow,beams,MyWindow.beams)].StartNode==MyWindow.beams[MyWindow.findobject(MyWindow,neighboringbeams[nei],MyWindow.beams)].EndNode:
            #MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = 0.0
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = 6 * El * I / math.pow(lbeam, 2.0)
        # symmetric
            MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
        elif regflag & 2==2:#m1==0 and m2==1:
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = 3 * El * I / math.pow(lbeam, 3.0)
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = 0.0
        # symmetric
            MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
        elif regflag & 1==1: #m1==1 and m2==0:
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = 3 * El * I / math.pow(lbeam, 3.0)
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = 3 * El * I / math.pow(lbeam, 2.0)
            # symmetric
            MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
                MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
        elif regflag & 252 ==0 :
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = 0.0
            MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = 0.0
            # symmetric
            MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
                MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
        # 3rd line
        if regflag & 3 ==3: #m1==1 and m2==1:m1 == 1 and m2 == 1:
            MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = (El / lbeam) * 4 * I
            #if neighboringbeams != None:
            #    for nei in range(0,len(neighboringbeams)):
            #        if (MyWindow.beams[MyWindow.findobject(MyWindow, neighboringbeams[nei], MyWindow.beams)].regflag & 4) == 4 and \
            #                MyWindow.beams[MyWindow.findobject(MyWindow, beams, MyWindow.beams)].StartNode == MyWindow.beams[
            #                    MyWindow.findobject(MyWindow, neighboringbeams[nei], MyWindow.beams)].EndNode:
            #MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = 0.0


        elif regflag & 2==2:#m1 == 0 and m2 == 1:
            MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = 0.0
        elif regflag & 1==1:#m1 == 1 and m2 == 0:
            MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = 3*El*I/lbeam
        elif regflag & 252 == 0:
            MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = 0.0

        # Top Right and Lower Left bands
        # 1 line
        MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0] = - El * A / lbeam
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 0] = \
            MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0]

        MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 1] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 0] = \
            MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 1]

        MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 2] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 0] = \
            MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 2]

        # 2nd line
        MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 0] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 1] = \
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 0]
        if regflag & 3 ==3:#m1==1 and m2==1:
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = -12.0 * El * I / math.pow(lbeam, 3.0)
        # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = \
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
        elif regflag & 2 ==2: #m1==0 and m2==1:
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = -3.0 * El * I / math.pow(lbeam, 3.0)
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
        elif regflag & 1 == 1:#m1 == 1 and m2 == 0:
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = -3.0 * El * I / math.pow(lbeam, 3.0)
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
        elif regflag & 252 == 0:
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 1] = \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
        if regflag & 3 ==3: #m1 == 1 and m2 == 1:
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = 6 * El * I / math.pow(lbeam, 2.0)
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
        elif regflag & 2 ==2: #m1==0 and m2==1:
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = 3 * El * I / math.pow(lbeam, 2.0)
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
        elif regflag & 1 ==1:#m1 == 1 and m2 == 0:
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
        elif regflag & 252 ==0:
            MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1] = \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
        MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 0] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 2] = \
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
        if regflag & 3 ==3: #m1 == 1 and m2 == 1:
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = -6 * El * I / math.pow(lbeam, 2.0)
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
        elif regflag & 2 ==2: #m1==0 and m2==1:
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
        elif regflag & 1 ==1:#m1 == 1 and m2 == 0:
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = -3 * El * I / math.pow(lbeam, 2.0)
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
        elif regflag & 252 ==0:
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2] = \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
        if regflag & 3 ==3: #m1 == 1 and m2 == 1:
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 2 * El * I / lbeam
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
        elif regflag & 2 ==2: #m1==0 and m2==1:#
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
        elif regflag & 1 == 1: #m1 == 1 and m2 == 0:
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
        elif regflag & 252 ==0:
            MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2] = \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
        # Lower Right sub matrix
        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0] = El * A / lbeam
        #if neighboringbeams != None:
        #    for nei in range(0,len(neighboringbeams)):
        #        if (MyWindow.beams[MyWindow.findobject(MyWindow, neighboringbeams[nei], MyWindow.beams)].regflag & 8 == 8) and \
        #                MyWindow.beams[MyWindow.findobject(MyWindow, beams, MyWindow.beams)].EndNode == MyWindow.beams[
        #                    MyWindow.findobject(MyWindow, neighboringbeams[nei], MyWindow.beams)].StartNode:
        #MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0] = 0.0
        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 0] = \
            MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]

        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2] = 0.0
        # symmetric
        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 0] = \
            MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
        ###
        if regflag & 3 ==3: #m1 == 1 and m2 == 1:#
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = 12.0 * El * I / math.pow(lbeam, 3.0)
            #if neighboringbeams != None:
            #    for nei in range(0,len(neighboringbeams)):
            #        if  (MyWindow.beams[MyWindow.findobject(MyWindow, neighboringbeams[nei], MyWindow.beams)].regflag & 8 == 8 and \
            #                MyWindow.beams[MyWindow.findobject(MyWindow, beams, MyWindow.beams)].EndNode == MyWindow.beams[
            #                    MyWindow.findobject(MyWindow, neighboringbeams[nei], MyWindow.beams)].StartNode):
            #MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = 0.0

        elif regflag & 2 ==2:#m1==0 and m2==1:
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = 3.0 * El * I / math.pow(lbeam, 3.0)
        elif regflag & 1 ==1:#m1==1 and m2==0:
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = 3.0 * El * I / math.pow(lbeam, 3.0)
        elif regflag & 252 ==0:
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1] = 0.0
        if regflag & 3 ==3: #m1 == 1 and m2 == 1:#
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = -6.0 * El * I / math.pow(lbeam, 2.0)
        # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = \
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
        elif regflag & 2 == 2: #m1==0 and m2==1:
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = -3.0 * El * I / math.pow(lbeam, 2.0)
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = \
                MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
        elif regflag & 1 == 1:#m1==1 and m2==0:
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = \
                MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
        elif regflag & 252 ==0:
            MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2] = 0.0
            # symmetric
            MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1] = \
                MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
        ####
        if regflag & 3 ==3: # m1 == 1 and m2 == 1:
            MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 4 * El * I / lbeam
            #if neighboringbeams != None:
            #    for nei in range(0,len(neighboringbeams)):
            #        if (MyWindow.beams[MyWindow.findobject(MyWindow,neighboringbeams[nei], MyWindow.beams)].regflag & 8 == 8) and \
            #                MyWindow.beams[MyWindow.findobject(MyWindow, beams, MyWindow.beams)].EndNode == MyWindow.beams[
            #                    MyWindow.findobject(MyWindow, neighboringbeams[nei], MyWindow.beams)].StartNode:
            #MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 0.0


        elif regflag & 2 ==2:# m1==0 and m2 == 1:
            MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 3 * El * I / lbeam
        elif regflag & 1 ==1: #m1==1 and m2==0:
            MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2] =0.0
        elif regflag & 252 ==0:
            MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2] = 0.0
        return
    def MATERIAL(self, file):
        foundNodes=DynamicArray()

        MyWindow.line = "r"
        materialname=""
        while MyWindow.line:
            MyWindow.line = file.readline()
            if (MyWindow.line[0:4].upper() == "Node".upper() and (MyWindow.line[0:11].upper() != "Node fixing".upper() )):
                return "Duplicate Node command in line " + str(MyWindow.cnt)
            if (MyWindow.line[0:4].upper() == "Beam".upper()) and (MyWindow.line[0:16].upper()!="Beam Dist Loads:".upper() and MyWindow.line[0:11].upper() != "Beam fixing".upper()):
                return "Duplicate Beam command in line " + str(MyWindow.cnt)
            MyWindow.cnt += 1
            if (MyWindow.line[0:4].upper() != "Beam".upper() and MyWindow.line[0:8].upper() != "Material".upper() and MyWindow.line[0:5].upper() != "Loads".upper() and MyWindow.line[0:11].upper() != "Node fixing".upper()    and MyWindow.line[0:11].upper() != "Beam fixing".upper()):
                if (len(MyWindow.line) > 0 and MyWindow.line[0:1] != "#" and MyWindow.line[0:1] != "\n"):
                    linesplit = MyWindow.line.split((" "))
                    if linesplit[0:-1]==[]:
                        materialname=""
                    if len(materialname)==0:
                        #Parsing beam name
                        El=0
                        b=0
                        h=0
                        if linesplit[0]=="\n":
                            st=linesplit[0][0:-1]
                            found=False
                            for e in MyWindow.beams:
                                if (st == MyWindow.beams[e].name):
                                    found = True
                                    break
                            if not found:
                               return "Material beam defined in Material \nbut not defined beam name in Line " + str(MyWindow.cnt)
                        else:
                             if linesplit[0][-1]=="\n":
                                 materialname = linesplit[0][0:-1]
                             else:
                                 materialname = linesplit[0]
                             if len(foundNodes) > 0:
                                 found=False

                                 for e in range(len(foundNodes)):
                                     if foundNodes[e] ==materialname:
                                            return "Duplicate material name in Line " + str(MyWindow.cnt)


                    else:
                        #Parsing Materials
                        st = ""
                        cod=""
                        k = 0
                        #parse Material line
                        for st in linesplit:
                            flag = False
                            if (st != "\n"):
                                if ((st != "\n") and (k == 0) and (not flag)):
                                    if st[-1]=="\n":
                                       cod=st[0:-1]
                                    else:
                                       cod = st

                                    #for e in range(len(MyWindow.beams)):
                                    #    if MyWindow.beams[e].name==materialname:
                                    #        found+=1
                                    #if found>1:
                                    #    return "Duplicate material definition in Line "+str(MyWindow.cnt)
                                    #elif found==0:
                                    #    return "Beam material defined but no beam were defined in beams in Line " + str(MyWindow.cnt)


                                if ((cod.upper()=="E" or cod.upper()=="Ε") and (k == 1) and (not (flag))):
                                    try:
                                        if st[-1]=="\n":
                                            El=float(st[0:-1])*1.0e6
                                        else:
                                            El=float(st)*1.0e6
                                    except ValueError:
                                        return "Elasticity must be a positive nonzero number in Line "+str(MyWindow.cnt)
                                    if El<=0:
                                        return "Elasticity must be a positive nonzero number in Line "+str(MyWindow.cnt)
                                    flag = True
                                if (cod.upper() == "B" or cod.upper()=="Β") and (k == 1) and (flag==False):
                                    try:
                                        if st[-1] == "\n":
                                            b = float(st[0:-1])
                                        else:
                                            b = float(st)
                                    except ValueError:
                                        return "Width(b) must be a positive nonzero number in Line "+str(MyWindow.cnt)
                                    if b <= 0:
                                        return "Width(b) must be a positive nonzero number in Line " + str(MyWindow.cnt)
                                    flag = True
                                if (cod.upper() == "H" or cod.upper()=="Η") and (k == 1) and (flag==False):
                                    try:
                                        if st[-1] == "\n":
                                            h = float(st[0:-1])
                                        else:
                                            h = float(st)
                                    except ValueError:
                                        return "Height (h) must be a positive nonzero number in Line " + str(MyWindow.cnt)
                                    if h <= 0:
                                        return "Height (h) must be a positive nonzero number in Line " + str(MyWindow.cnt)
                                    if El>0 and b>0 and h>0:
                                        # (self, name, StartNode, EndNote, xl, yl, Elasticity, Inertia, Area):
                                        beamindex = MyWindow.findobject(self, materialname, MyWindow.beams)
                                        if MyWindow.beams[beamindex].StartNode.find("SPRING") >-1:
                                            return "You defined beam elasticity instead of spring elasticity in Line "+str(MyWindow.cnt)

                                        foundNodes.append(materialname)
                                        #(self, name, StartNode, EndNote, xl, yl, Elasticity, Inertia, Area):
                                        MyWindow.beams[beamindex].Elasticity=El
                                        MyWindow.beams[beamindex].Inertia=self.Irect(b,h)
                                        MyWindow.beams[beamindex].Area = self.Arect(b, h)
                                        MyWindow.beams[beamindex].h = h
                                        #materialname=""
                                        flag = True
                                if (cod.upper() == "Κ" or cod.upper() == "K") and (k == 1) and (flag == False):
                                    try:
                                        if st[-1] == "\n":
                                            kk = float(st[0:-1])*1000.0
                                        else:
                                            kk = float(st)*1000.0
                                    except ValueError:
                                        return "Elasticity constant (k) must be a positive nonzero number in Line " + str(
                                            MyWindow.cnt)

                                    if kk <= 0:
                                        return "Elasticity constant must be a positive nonzero number in Line " + str(
                                            MyWindow.cnt)
                                    if kk > 0:
                                        # (self, name, StartNode, EndNote, xl, yl, Elasticity, Inertia, Area):
                                        beamindex = MyWindow.findobject(self, materialname, MyWindow.beams)
                                       # if MyWindow.beams[beamindex].Endnode=="":
                                        if MyWindow.beams[beamindex].StartNode.find("SPRING") ==-1:
                                            return "You defined spring elasticity instead of beam in Line " + str(MyWindow.cnt)

                                        foundNodes.append(materialname)
                                        # (self, name, StartNode, EndNote, xl, yl, Elasticity, Inertia, Area):
                                        MyWindow.beams[beamindex].Elasticity = kk
                                        #else:
                                         #   return "Elastic support not defined in Line "+str(MyWindow.cnt)
                                        # materialname=""
                                        flag = True
                                if (cod.upper() == "AT" or cod.upper() == "ΑΤ" ) and (k == 1) and (flag == False):
                                    try:
                                        if st[-1] == "\n":
                                            at = float(st[0:-1])
                                        else:
                                            at = float(st)
                                    except ValueError:
                                        return "Temperature constant must be a positive number in Line " + str(MyWindow.cnt)
                                    if at < 0:
                                        return "Temperature constant must be a positive number in Line " + str(MyWindow.cnt)
                                    else:
                                        # (self, name, StartNode, EndNote, xl, yl, Elasticity, Inertia, Area):
                                        beamindex = MyWindow.findobject(self, materialname, MyWindow.beams)
                                        MyWindow.beams[beamindex].at = at
                            k+=1


            #gg = np.array(MyWindow.karray - MyWindow.karray.T)

            else:
                break

        flag = True
        sfy= 0
        sfx = 0
        while flag:
            flag = False
            foundbeams = DynamicArray()
            for e in range(0,len(MyWindow.beams)):
                stnode1 = MyWindow.beams[e].StartNode
                if MyWindow.beams[e].StartNode.find("SPRING") > -1:
                    sfy = math.cos((MyWindow.beams[e].xl * math.pi / 180)) * MyWindow.beams[e].Elasticity
                    sfx = math.sin((MyWindow.beams[e].xl * math.pi / 180)) * MyWindow.beams[e].Elasticity
                flag = False
                for f in range(0,len(MyWindow.beams)):
                    if e != f:
                        stnode2 = MyWindow.beams[f].StartNode
                        if MyWindow.beams[e].StartNode.find("SPRING") > -1 and stnode1 == stnode2:
                            sfy += math.cos((MyWindow.beams[f].xl * math.pi / 180)) * MyWindow.beams[f].Elasticity
                            sfx += math.sin((MyWindow.beams[f].xl * math.pi / 180)) * MyWindow.beams[f].Elasticity
                            # Add springs
                            foundbeams.append(f)

                if len(foundbeams)>0:
                    co=len(foundbeams)-1
                    while co>=0:
                        MyWindow.beams.removeAt(foundbeams[len(foundbeams)-1])
                        co-=1
                    ang=math.atan2(sfy,sfx)*180.0/math.pi
                    norm=math.sqrt(sfx*sfx+sfy*sfy)
                    MyWindow.beams[e].xl=ang
                    MyWindow.beams[e].Elasticity=norm
                    flag=True
                    break
        for e in range(0, len(MyWindow.beams)):
            if MyWindow.beams[e].StartNode.find("SPRING") == -1:
                if (MyWindow.beams[e].Elasticity == 0 or MyWindow.beams[e].Inertia == 0 or MyWindow.beams[e].Area == 0):
                    return "No beam material defined\nYou must define all beams"
            else:
                if (MyWindow.beams[e].Elasticity == 0):
                    return "No elasticity defined\nYou must define elasticity on node"



        # Fixing SPRING nodes
        # X=0



        return MyWindow.beams
        return None

    def addglobalstiffnessmatrixcompact(self):
        for e in range(0, len(MyWindow.beams)):
            #if MyWindow.nodes[MyWindow.perm.index(MyWindow.findobject(MyWindow, MyWindow.beams[e].StartNode, MyWindow.nodes))].name.find("SPRING")==-1:
            if MyWindow.beams[e].StartNode.find("SPRING") == -1:
                neighboringbeams = DynamicArray()
                beamname = MyWindow.beams[e].name
                # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
                beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                beamstartnode = MyWindow.beams[beamnameindex].StartNode
                startNodeIndex1 = MyWindow.perm.index(MyWindow.findobject(self, beamstartnode, MyWindow.nodes))

                beamendnode = MyWindow.beams[beamnameindex].EndNode
                endNodeIndex1 = MyWindow.perm.index(MyWindow.findobject(self, beamendnode, MyWindow.nodes))
                El = MyWindow.beams[beamnameindex].Elasticity
                lbeam = math.sqrt(
                    math.pow(MyWindow.beams[beamnameindex].xl, 2.0) + math.pow(MyWindow.beams[beamnameindex].yl,
                                                                               2.0))
                A = MyWindow.beams[beamnameindex].Area
                xl = MyWindow.beams[beamnameindex].xl
                yl = MyWindow.beams[beamnameindex].yl
                c = xl / lbeam
                s = yl / lbeam
                transf = np.zeros((6, 6))
                transf[0][0] = c
                transf[0][1] = s
                transf[1][0] = -s
                transf[1][1] = c
                transf[2][2] = 1.0
                transf[3][3] = c
                transf[3][4] = s
                transf[4][3] = -s
                transf[4][4] = c
                transf[5][5] = 1.0
                I = MyWindow.beams[beamnameindex].Inertia
                MyWindow.kbeam = np.zeros((6, 6))
                Switcher.kbeamcomputations(self, El, I, A, lbeam, MyWindow.beams[beamnameindex].regflag,beamname)#,neighboringbeams)
                MyWindow.kbeam = np.dot(transf.T, np.dot(MyWindow.kbeam, transf))



                ########################################################################################################################
                # 1st line
                startNodeIndex = 0
                endNodeIndex = 1
                if endNodeIndex1>startNodeIndex1:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                    # MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                    #   MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]
                    # symmetric
                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 2)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                    # MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
                    # symmetric
                    # 3MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 0]
                    # 2nd line

                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 3)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]

                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 2)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]

                    # 3rd line
                    # MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]

                    # MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                    #   MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]
                    # symmetric
                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 2)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]

                    # MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
                    # symmetric
                    # 3MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 0]
                    # 2nd line

                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 3)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]

                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]

                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 2)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]

                    # 3rd line
                    # MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                # Top Right and Low Left bands
                # 1 line
                # MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 0] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 0]
                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1))] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1))] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                # MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 0]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1))] += MyWindow.kbeam[startNodeIndex * 3 + 0][
                        endNodeIndex * 3 + 1]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1))] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                # if (endNodeIndex1 > startNodeIndex1):
                #    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1*3+1]-1-3*(endNodeIndex1-startNodeIndex1)) ] += MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                # else:
                #    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1*3 + 1]-1-3*(startNodeIndex1-endNodeIndex1))] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]

                # MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                # MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                #   MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 0]
                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) - 2)] += MyWindow.kbeam[startNodeIndex * 3 + 0][
                        endNodeIndex * 3 + 2]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) - 2)] += MyWindow.kbeam[endNodeIndex * 3 + 0][
                        startNodeIndex * 3 + 2]

                # 2nd line
                # MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                #   MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 0]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) + 1)] += MyWindow.kbeam[startNodeIndex * 3 + 1][
                        endNodeIndex * 3 + 0]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) + 1)] += MyWindow.kbeam[endNodeIndex * 3 + 1][
                        startNodeIndex * 3 + 0]

                # MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1))] += MyWindow.kbeam[startNodeIndex * 3 + 1][
                        endNodeIndex * 3 + 1]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1))] += MyWindow.kbeam[endNodeIndex * 3 + 1][
                        startNodeIndex * 3 + 1]

                #               MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                #                   MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                # symmetric
                #               MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                #                   MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2]

                # MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                #     MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) + 2)] += MyWindow.kbeam[startNodeIndex * 3 + 2][
                        endNodeIndex * 3 + 0]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) + 2)] += MyWindow.kbeam[endNodeIndex * 3 + 2][
                        startNodeIndex * 3 + 0]

                # MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                #   MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                #   MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) + 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) + 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1]

                # MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1))] += MyWindow.kbeam[startNodeIndex * 3 + 2][
                        endNodeIndex * 3 + 2]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1))] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2]

                # Lower Right sub matrix
                if endNodeIndex1>startNodeIndex1:
                # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]

                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 2)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                    ###
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 3)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]

                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1]

                    ####
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 2)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                else:
                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 2)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                    ###
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 3)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]

                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1]

                    ####
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 2)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
            else:
                beamname = MyWindow.beams[e].name
                # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
                beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                beamstartnode = MyWindow.beams[beamnameindex].StartNode
                startNodeIndex1 = MyWindow.perm.index(MyWindow.findobject(self, beamstartnode, MyWindow.nodes))
                beamendnode = MyWindow.beams[beamnameindex].EndNode
                endNodeIndex1 = MyWindow.perm.index(MyWindow.findobject(self, beamendnode, MyWindow.nodes))
                # Κόμβος αρχής  ράβδου μητρώο ακαμψίας
                # d1,x
                # (self, name, StartNode, EndNode, xl, yl, Elasticity, Inertia, Area):
                # Κόμβος αρχής μητρώο ακαμψίας
                El = MyWindow.beams[beamnameindex].Elasticity
                # beam = Beam(beamname, startnode, "", angle, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                #           0.0, 0.0, 0.0, 0.0)

                # xl = MyWindow.beams[beamnameindex].xl
                # yl = MyWindow.beams[beamnameindex].yl
                c = math.cos(MyWindow.beams[e].xl * math.pi / 180.0)
                s = math.sin(MyWindow.beams[e].xl * math.pi / 180.0)
                transf = np.zeros((6, 6))
                transf[0][0] = c
                transf[0][1] = s
                transf[1][0] = -s
                transf[1][1] = c
                transf[2][2] = 1.0
                transf[3][3] = c
                transf[3][4] = s
                transf[4][3] = -s
                transf[4][4] = c
                transf[5][5] = 1.0
                # I = MyWindow.beams[beamnameindex].Inertia
                MyWindow.kbeam = np.zeros((6, 6))

                Switcher.kspringcomputations(self,El)
                MyWindow.kbeam = np.dot(transf.T, np.dot(MyWindow.kbeam, transf))

                ########################################################################################################################
                # 1st line
                startNodeIndex = 0
                endNodeIndex = 1
                if endNodeIndex1 > startNodeIndex1:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                    # MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                    #   MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]
                    # symmetric
                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 2)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                    # MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
                    # symmetric
                    # 3MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 0]
                    # 2nd line

                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 3)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]

                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 2)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]

                    # 3rd line
                    # MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]

                    # MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                    #   MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]
                    # symmetric
                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 2)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]

                    # MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
                    # symmetric
                    # 3MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 0]
                    # 2nd line

                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 3)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]

                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]

                    # MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 2)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]

                    # 3rd line
                    # MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                # Top Right and Low Left bands
                # 1 line
                # MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 0] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 0]
                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1))] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1))] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                # MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 0]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1))] += MyWindow.kbeam[startNodeIndex * 3 + 0][
                        endNodeIndex * 3 + 1]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1))] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                # if (endNodeIndex1 > startNodeIndex1):
                #    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1*3+1]-1-3*(endNodeIndex1-startNodeIndex1)) ] += MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                # else:
                #    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1*3 + 1]-1-3*(startNodeIndex1-endNodeIndex1))] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]

                # MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                # MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                #   MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 0]
                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) - 2)] += MyWindow.kbeam[startNodeIndex * 3 + 0][
                        endNodeIndex * 3 + 2]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) - 2)] += MyWindow.kbeam[endNodeIndex * 3 + 0][
                        startNodeIndex * 3 + 2]

                # 2nd line
                # MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                #   MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 0]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) + 1)] += MyWindow.kbeam[startNodeIndex * 3 + 1][
                        endNodeIndex * 3 + 0]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) + 1)] += MyWindow.kbeam[endNodeIndex * 3 + 1][
                        startNodeIndex * 3 + 0]

                # MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1))] += MyWindow.kbeam[startNodeIndex * 3 + 1][
                        endNodeIndex * 3 + 1]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1))] += MyWindow.kbeam[endNodeIndex * 3 + 1][
                        startNodeIndex * 3 + 1]

                #               MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                #                   MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                # symmetric
                #               MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                #                   MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2]

                # MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                #     MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) + 2)] += MyWindow.kbeam[startNodeIndex * 3 + 2][
                        endNodeIndex * 3 + 0]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) + 2)] += MyWindow.kbeam[endNodeIndex * 3 + 2][
                        startNodeIndex * 3 + 0]

                # MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                #   MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                #   MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1) + 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1) + 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1]

                # MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                #    MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                # symmetric
                # MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                #    MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2]

                if (endNodeIndex1 > startNodeIndex1):
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1 - 3 * (
                            endNodeIndex1 - startNodeIndex1))] += MyWindow.kbeam[startNodeIndex * 3 + 2][
                        endNodeIndex * 3 + 2]
                else:
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1 - 3 * (
                            startNodeIndex1 - endNodeIndex1))] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2]

                # Lower Right sub matrix
                if endNodeIndex1 > startNodeIndex1:
                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 1] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]

                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 2)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                    ###
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 3)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]

                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 2] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1]

                    ####
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 2)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[endNodeIndex1 * 3 + 3] - 1)] += \
                        MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                else:
                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 1] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 0]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 2)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                    ###
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 3)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]

                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 2] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                    # symmetric
                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                    #    MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1]

                    ####
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 2)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1]

                    # MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                    #   MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                    MyWindow.uarray[int(MyWindow.firstindexcolumns[startNodeIndex1 * 3 + 3] - 1)] += \
                        MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
                if (MyWindow.nodes[MyWindow.perm[startNodeIndex1]].name.find("SPRING")>-1):
                    try:
                        p = MyWindow.displacementsindex.index(MyWindow.perm[startNodeIndex1] * 3)
                    except ValueError:
                        MyWindow.displacementsindex.append(MyWindow.perm[startNodeIndex1]* 3)
                        MyWindow.displacements.append(0.0)
                    try:
                        p = MyWindow.displacementsindex.index(MyWindow.perm[startNodeIndex1]* 3 + 1)
                    except ValueError:
                        MyWindow.displacementsindex.append(MyWindow.perm[startNodeIndex1] * 3 + 1)
                        MyWindow.displacements.append(0.0)
                    try:
                        p = MyWindow.displacementsindex.index(MyWindow.perm[startNodeIndex1] * 3 + 2)
                    except ValueError:
                        MyWindow.displacementsindex.append(MyWindow.perm[startNodeIndex1] * 3 + 2)
                        MyWindow.displacements.append(0.0)
                else:
                    try:
                        p = MyWindow.displacementsindex.index(MyWindow.perm[endNodeIndex1] * 3)
                    except ValueError:
                        MyWindow.displacementsindex.append(MyWindow.perm[endNodeIndex1] * 3)
                        MyWindow.displacements.append(0.0)
                    try:
                        p = MyWindow.displacementsindex.index(MyWindow.perm[endNodeIndex1] * 3 + 1)
                    except ValueError:
                        MyWindow.displacementsindex.append(MyWindow.perm[endNodeIndex1] * 3 + 1)
                        MyWindow.displacements.append(0.0)
                    try:
                        p = MyWindow.displacementsindex.index(MyWindow.perm[endNodeIndex1] * 3 + 2)
                    except ValueError:
                        MyWindow.displacementsindex.append(MyWindow.perm[endNodeIndex1] * 3 + 2)
                        MyWindow.displacements.append(0.0)
    def addglobalstiffnessmatrix(self):
        for e in range(0, len(MyWindow.beams)):
            if MyWindow.beams[e].StartNode.find("SPRING") == -1:
                neighboringbeams = DynamicArray()
                beamname = MyWindow.beams[e].name
                # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
                beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                beamstartnode = MyWindow.beams[beamnameindex].StartNode
                startNodeIndex1 = MyWindow.perm.index(MyWindow.findobject(self, beamstartnode, MyWindow.nodes))
                beamendnode = MyWindow.beams[beamnameindex].EndNode
                endNodeIndex1 = MyWindow.perm.index(MyWindow.findobject(self, beamendnode, MyWindow.nodes))
                El = MyWindow.beams[beamnameindex].Elasticity
                lbeam = math.sqrt(
                    math.pow(MyWindow.beams[beamnameindex].xl, 2.0) + math.pow(MyWindow.beams[beamnameindex].yl,
                                                                               2.0))
                A = MyWindow.beams[beamnameindex].Area
                xl = MyWindow.beams[beamnameindex].xl
                yl = MyWindow.beams[beamnameindex].yl
                c = xl / lbeam
                s = yl / lbeam
                transf = np.zeros((6, 6))
                transf[0][0] = c
                transf[0][1] = s
                transf[1][0] = -s
                transf[1][1] = c
                transf[2][2] = 1.0
                transf[3][3] = c
                transf[3][4] = s
                transf[4][3] = -s
                transf[4][4] = c
                transf[5][5] = 1.0
                I = MyWindow.beams[beamnameindex].Inertia
                MyWindow.kbeam = np.zeros((6, 6))
                Switcher.kbeamcomputations(self, El, I, A, lbeam, MyWindow.beams[beamnameindex].regflag,beamname)#,neighboringbeams)
                MyWindow.kbeam = np.dot(transf.T, np.dot(MyWindow.kbeam, transf))
                startNodeIndex = 0
                endNodeIndex = 1
                ########################################################################################################################
                # 1st line
                MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 0]

                MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 0]
                # 2nd line
                MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]
                MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1]
                # 3rd line
                MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
                # Top Right and Low Left bands
                # 1 line
                MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 0]

                MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 0]

                # 2nd line
                MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 0]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1]

                MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 2]

                MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2]

                MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2]

                # Lower Right sub matrix
                MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]

                MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 0]

                MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                ###
                MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]

                MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1]

                ####

                MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
            else:
                beamname = MyWindow.beams[e].name
                # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
                beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                beamstartnode = MyWindow.beams[beamnameindex].StartNode
                startNodeIndex1 =MyWindow.perm.index( MyWindow.findobject(self, beamstartnode, MyWindow.nodes))
                beamendnode = MyWindow.beams[beamnameindex].EndNode
                endNodeIndex1 = MyWindow.perm.index(MyWindow.findobject(self, beamendnode, MyWindow.nodes))
                # Κόμβος αρχής  ράβδου μητρώο ακαμψίας
                # d1,x
                # (self, name, StartNode, EndNode, xl, yl, Elasticity, Inertia, Area):
                # Κόμβος αρχής μητρώο ακαμψίας
                El = MyWindow.beams[beamnameindex].Elasticity
                # beam = Beam(beamname, startnode, "", angle, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                #           0.0, 0.0, 0.0, 0.0)

                # xl = MyWindow.beams[beamnameindex].xl
                # yl = MyWindow.beams[beamnameindex].yl
                c = math.cos(MyWindow.beams[e].xl * math.pi / 180.0)
                s = math.sin(MyWindow.beams[e].xl * math.pi / 180.0)
                transf = np.zeros((6, 6))
                transf[0][0] = c
                transf[0][1] = s
                transf[1][0] = -s
                transf[1][1] = c
                transf[2][2] = 1.0
                transf[3][3] = c
                transf[3][4] = s
                transf[4][3] = -s
                transf[4][4] = c
                transf[5][5] = 1.0
                # I = MyWindow.beams[beamnameindex].Inertia
                MyWindow.kbeam = np.zeros((6, 6))
                # 1st line
                Switcher.kspringcomputations(self,El)
                # self.kspringomputations(0.0)
                ########################################################################################################################
                # Global from Local coordinate system
                # [k]=([T]T)*[k']*[T] where [T]T transposed matrix transformation matrix
                # MyWindow.kbeam = np.dot(MyWindow.kbeam, transf)
                # MyWindow.kbeam = np.dot(transf.T,MyWindow.kbeam)
                MyWindow.kbeam = np.dot(transf.T, np.dot(MyWindow.kbeam, transf))
                startNodeIndex = 0
                endNodeIndex = 1
                ########################################################################################################################
                # 1st line
                MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 0]

                MyWindow.karray[startNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 0][startNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 0]
                # 2nd line
                MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 1]
                MyWindow.karray[startNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 1][startNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 1]
                # 3rd line
                MyWindow.karray[startNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 2][startNodeIndex * 3 + 2]
                # Top Right and Low Left bands
                # 1 line
                MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 0]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 0]

                MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 0]

                MyWindow.karray[startNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 0]

                # 2nd line
                MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 0]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 1]

                MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 1]

                MyWindow.karray[startNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 1]

                MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 0][startNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 0][startNodeIndex * 3 + 2]

                MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 1][startNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 1][startNodeIndex * 3 + 2]

                MyWindow.karray[startNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[startNodeIndex * 3 + 2][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][startNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 2][startNodeIndex * 3 + 2]

                # Lower Right sub matrix
                MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 0]

                MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 1]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 0]

                MyWindow.karray[endNodeIndex1 * 3 + 0][endNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 0][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 0] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 0]
                ###
                MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 1]

                MyWindow.karray[endNodeIndex1 * 3 + 1][endNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 1][endNodeIndex * 3 + 2]
                # symmetric
                MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 1] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 1]

                ####

                MyWindow.karray[endNodeIndex1 * 3 + 2][endNodeIndex1 * 3 + 2] += \
                    MyWindow.kbeam[endNodeIndex * 3 + 2][endNodeIndex * 3 + 2]

                try:
                    p = MyWindow.displacementsindex.index(MyWindow.perm[startNodeIndex1] * 3)
                except ValueError:
                    MyWindow.displacementsindex.append(MyWindow.perm[startNodeIndex1] * 3)
                    MyWindow.displacements.append(0.0)
                try:
                    p = MyWindow.displacementsindex.index(MyWindow.perm[startNodeIndex1] * 3 + 1)
                except ValueError:
                    MyWindow.displacementsindex.append(MyWindow.perm[startNodeIndex1] * 3 + 1)
                    MyWindow.displacements.append(0.0)
                try:
                    p = MyWindow.displacementsindex.index(MyWindow.perm[startNodeIndex1] * 3 + 2)
                except ValueError:
                    MyWindow.displacementsindex.append(MyWindow.perm[startNodeIndex1] * 3 + 2)
                    MyWindow.displacements.append(0.0)
    def inputnode(self,nodenam,x,y,M):
        nodenameindex = MyWindow.findobject(self, nodenam, MyWindow.nodes)
        if y==None:
            y = 0.0
        if x == None:
            x = 0.0
        if M == None:
            M = 0.0
        #Θα τα δούμε αργότερα για εξωτ. φορτίσεις υπό γωνία
        c=1
        s=0
        transf = np.zeros((6, 6))
        transf[0][0] = c
        transf[0][1] = s
        transf[1][0] = -s
        transf[1][1] = c
        transf[2][2] = 1.0

        transf[3][3] = c
        transf[3][4] = s
        transf[4][3] = -s
        transf[4][4] = c
        transf[5][5] = 1.0
        #mat = transf.dot(localf.T)
        element = np.zeros(3 * len(MyWindow.nodes))
        element[nodenameindex * 3 + 0] = x
        element[nodenameindex * 3 + 1] = y
        element[nodenameindex * 3 + 2] = M
        MyWindow.results = np.add(MyWindow.results, element)

    def inputbeam(self,beamnam,x,y1,y2):
        #Trapezoidal uniform load
        beamnameindex = MyWindow.findobject(self, beamnam, MyWindow.beams)
        beamstartnode = MyWindow.beams[beamnameindex].StartNode
        startNodeIndex = MyWindow.findobject(self, beamstartnode, MyWindow.nodes)
        beamendnode = MyWindow.beams[beamnameindex].EndNode
        endNodeIndex =MyWindow.findobject(self, beamendnode, MyWindow.nodes)
        xl = MyWindow.beams[beamnameindex].xl
        yl = MyWindow.beams[beamnameindex].yl

        lbeam = math.sqrt(math.pow(xl, 2.0) + math.pow(yl,2.0))
        A = MyWindow.beams[beamnameindex].Area
        c = xl / lbeam
        s = yl / lbeam

        if x!=None:
            N1 = -0.5*x * lbeam
            N2 = -0.5*x * lbeam

        else:
            N1=0
            N2=0
        if y1 != None or y2!=None:
                if y1==None:
                    y1=y2
                if y2==None:
                    y2=y1
                M1=((3*y1+2*y2)*math.pow(lbeam,2)/60)
                M2 =-((2*y1+3*y2)*math.pow(lbeam,2)/60)
                Q1=((7*y1+3*y2)*lbeam/20)
                Q2=((3*y1+7*y2)*lbeam / 20)
                #M1 =1 / 12.0 * y * math.pow(lbeam, 2.0)
                #M2 = -M1
                #Q1 = 0.5 * y * lbeam
                #Q2 = Q1
        else:
            Q1=0
            M1=0
            Q2=0
            M2=0
        transf = np.zeros((6, 6))
        transf[0][0] = c
        transf[0][1] = s
        transf[1][0] = -s
        transf[1][1] = c
        transf[2][2] = 1.0

        transf[3][3] = c
        transf[3][4] = s
        transf[4][3] = -s
        transf[4][4] = c
        transf[5][5] = 1.0
        localf = np.zeros((6))
        localf[0] = N1
        localf[1] = Q1
        localf[2] = M1
        localf[3] = N2
        localf[4] = Q2
        localf[5] = M2
        MyWindow.beams[beamnameindex].N1 += N1
        MyWindow.beams[beamnameindex].Q1 += Q1
        MyWindow.beams[beamnameindex].M1 += M1
        MyWindow.beams[beamnameindex].N2 += N2
        MyWindow.beams[beamnameindex].Q2 += Q2
        MyWindow.beams[beamnameindex].M2 += M2

        #Forces with transposed tranformation matrix
        mat = np.dot(transf.T,localf)
        element = np.zeros(3 * len(MyWindow.nodes))
        element[startNodeIndex * 3 + 0] = mat[0]
        element[startNodeIndex * 3 + 1] = mat[1]
        element[startNodeIndex * 3 + 2] = mat[2]
        element[endNodeIndex * 3 + 0] = mat[3]
        element[endNodeIndex * 3 + 1] = mat[4]
        element[endNodeIndex * 3 + 2] = mat[5]
        MyWindow.fixedresults = np.add(MyWindow.fixedresults, element)
    def inputtemperature(self,beamnam,Te,Ti,Tr):

        beamnameindex = MyWindow.findobject(self, beamnam, MyWindow.beams)
        beamstartnode = MyWindow.beams[beamnameindex].StartNode
        startNodeIndex =MyWindow.findobject(self, beamstartnode, MyWindow.nodes)
        beamendnode = MyWindow.beams[beamnameindex].EndNode
        endNodeIndex = MyWindow.findobject(self, beamendnode, MyWindow.nodes)
        at=MyWindow.beams[beamnameindex].at

        if at==0 or Te==None or Ti==None:
            return
        h = MyWindow.beams[beamnameindex].h
        lbeam = math.sqrt(
            math.pow(MyWindow.beams[beamnameindex].xl, 2.0) + math.pow(
                MyWindow.beams[beamnameindex].yl,
                2.0))
        A = MyWindow.beams[beamnameindex].Area
        I = MyWindow.beams[beamnameindex].Inertia
        El = MyWindow.beams[beamnameindex].Elasticity/1000000

        xl = MyWindow.beams[beamnameindex].xl
        yl = MyWindow.beams[beamnameindex].yl
        c = xl / lbeam
        s = yl / lbeam
        if Tr!=None:
            N1 = at*El*A*((Te+Ti)*0.5-Tr)
            N2 = -N1
        else:
            N1=0
            N2=0
        Q1 = 0


        Q2 = Q1
        M1 = -El * I * at * (Te - Ti) / h
        M2 = -M1
        transf = np.zeros((6, 6))
        MyWindow.beams[beamnameindex].N1 += N1
        MyWindow.beams[beamnameindex].Q1 += Q1
        MyWindow.beams[beamnameindex].M1 += M1
        MyWindow.beams[beamnameindex].N2 += N2
        MyWindow.beams[beamnameindex].Q2 += Q2
        MyWindow.beams[beamnameindex].M2 += M2
        transf[0][0] = c
        transf[0][1] = s
        transf[1][0] = -s
        transf[1][1] = c
        transf[2][2] = 1.0

        transf[3][3] = c
        transf[3][4] = s
        transf[4][3] = -s
        transf[4][4] = c
        transf[5][5] = 1.0
        localf = np.zeros((6))
        localf[0] = N1
        localf[1] = Q1
        localf[2] = M1
        localf[3] = N2
        localf[4] = Q2
        localf[5] = M2

        mat = np.dot(transf.T,localf)
        element = np.zeros(3 * len(MyWindow.nodes))
        element[startNodeIndex * 3 + 0] = mat[0]
        element[startNodeIndex * 3 + 1] = mat[1]
        element[startNodeIndex * 3 + 2] = mat[2]
        element[endNodeIndex * 3 + 0] = mat[3]
        element[endNodeIndex * 3 + 1] = mat[4]
        element[endNodeIndex * 3 + 2] = mat[5]
        MyWindow.fixedresults = np.add(MyWindow.fixedresults, element)

    def LOADS(self, file):
        MyWindow.line = "r"
        cod = ""
        nodename = ""
        beamname = ""
        x1 = None
        y1 = None
        ti = None
        te = None
        tr = None
        M = None
        cas = 0
        while MyWindow.line:
            MyWindow.line = file.readline()
            if (MyWindow.line[0:4].upper() == "Node".upper() and (
                    MyWindow.line.upper()[0:15] != "Node Conc Loads".upper()) and (
                    MyWindow.line.upper()[0:11] != "Node Fixing".upper()) ):
                return "Duplicate Node command in line " + str(MyWindow.cnt)
            if (MyWindow.line[0:5].upper() == "Beam\n".upper()) and not (
                    MyWindow.line.upper()[0:15] == "Beam Dist Loads".upper()):
                return "Duplicate Beam command in line " + str(MyWindow.cnt)
            if (MyWindow.line[0:8].upper() == "Material".upper()):
                return "Duplicate Material command in line " + str(MyWindow.cnt)
            if (MyWindow.line[0:5].upper() == "Loads".upper()):
                return "Duplicate Loads command in line " + str(MyWindow.cnt)
            MyWindow.cnt += 1

            if (MyWindow.line[0:8].upper() != "Material".upper() and MyWindow.line[0:11].upper() != "Beam fixing".upper()and MyWindow.line[
                                                                                                            0:11].upper() != "Node fixing".upper()):
                if (len(MyWindow.line) > 0 and MyWindow.line[0:1] != "#" and MyWindow.line[0:1] != "\n"):
                    linesplit = MyWindow.line
                    if MyWindow.line.upper()[0:15] == "Beam Dist Loads".upper() or MyWindow.line.upper()[
                                                                                   0:15] == "Node Conc Loads".upper():
                        if cas > 0 and cmnd.upper()[0:15] == "Beam Dist Loads".upper():
                            # Σε περίπτωση τέλους ενότητας

                            x1 = None
                            y1 = None

                            beamname = ""
                            cod = ""
                        if linesplit[-1] == "\n":
                            cmnd = linesplit[0:-1]
                        else:
                            cmnd = linesplit

                        cas = 0
                    elif cmnd.upper()[0:15] == "Beam Dist Loads".upper() and cas == 0 and beamname == "":
                        ti = None
                        te = None
                        tr = None

                        if linesplit[-1] == "\n" and beamname == "":
                            beamname = linesplit[0:-1]
                        else:
                            beamname = linesplit
                            found = False
                            for e in range(len(MyWindow.beams)):
                                if MyWindow.beams[e].name == beamname:
                                    found = True
                                    break
                            if not (found):
                                return "Beam not defined in beams. Error in Line " + str(MyWindow.cnt)

                    elif (cmnd.upper()[0:15] == "Node Conc Loads".upper() and cas == 0 and nodename == ""):
                        if linesplit[-1] == "\n":
                            nodename = linesplit[0:-1]
                        else:
                            nodename = linesplit
                        found = False
                        for e in range(len(MyWindow.nodes)):
                            if MyWindow.nodes[e].name == nodename:
                                found = True
                                break
                        if not (found):
                            return "Node not defined in node conc loads. Error in Line " + str(MyWindow.cnt)
                    elif len(cod) == 0:
                        if linesplit[-1] == "\n":
                            nam = linesplit[0:-1]
                        else:
                            nam = linesplit
                        if (
                                nam.upper() == "X" or nam.upper() == "Χ" or nam.upper() == "Y" or nam.upper() == "Υ" or nam.upper() == "M" or nam.upper() == "Μ" or nam.upper() == "TE".upper() or nam.upper() == "ΤΕ".upper()
                                or nam.upper() == "TI".upper() or nam.upper() == "ΤΙ".upper() or nam.upper() == "TR" or nam.upper() == "ΤR"):
                            cod = nam
                        else:
                            cod = ""
                            cas = 0
                            if cmnd.upper()[0:9] == "Node Conc".upper():
                                if linesplit[-1] == "\n":
                                    nodename = linesplit[0:-1]
                                else:
                                    nodename = linesplit
                                found = False
                                for e in range(len(MyWindow.nodes)):
                                    if MyWindow.nodes[e].name == nodename:
                                        found = True
                                        break
                                if not (found):
                                    return "Node not defined in node conc loads. Error in Line " + str(MyWindow.cnt)
                            elif cmnd.upper()[0:9] == "Beam Dist".upper():
                                if beamname != "":
                                    beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
                                    if beamname != "" and MyWindow.beams[beamnameindex].at > 0 and (
                                            te == None and ti != None) or (ti != None and ti == None):
                                        return "Internal or external temperatures not defined in line " + str(
                                            MyWindow.cnt)
                                    else:
                                        if beamname != "":
                                            self.inputtemperature(beamname.strip(), te, ti, tr)
                                            ti = None
                                            te = None
                                            tr = None
                                if linesplit[-1] == "\n":
                                    beamname = linesplit[0:-1]
                                else:
                                    beamname = linesplit
                                found = False
                                for e in range(len(MyWindow.beams)):
                                    if MyWindow.beams[e].name == beamname:
                                        found = True
                                        break
                                if not (found):
                                    return "Beam not defined in beams. Error in Line " + str(MyWindow.cnt)
                    elif len(cod) > 0:
                        if cod.upper() == "X" or cod.upper() == "Χ":
                            cas += 1
                            try:
                                if linesplit[-1] == "\n":
                                    x1 = float(linesplit[0:-1])*1000.0
                                else:
                                    x1 = float(linesplit)*1000.0
                            except ValueError:
                                return "Load X must be a number in Line " + str(MyWindow.cnt)

                            if cmnd.upper()[0:4] == "Node".upper():
                                self.inputnode(nodename.strip(), x1, y1, M)
                            elif cmnd.upper()[0:4] == "Beam".upper():
                                beamnameindex = MyWindow.findobject(self, beamname.strip(), MyWindow.beams)
                                beamstartnode = MyWindow.beams[beamnameindex].StartNode
                                if beamstartnode.__contains__("SPRING"):
                                    return "Beam Distribution loads applied on spring"
                                self.inputbeam(beamname.strip(), x1, y1,y2)
                            cod = ""
                            x1 = None
                        elif cod.upper() == "Y" or cod.upper() == "Υ":
                            cas += 1
                            try:
                                if linesplit[-1] == "\n":
                                    if len(linesplit.split(" "))==2:
                                        y1=float(linesplit.split(" ")[0])*1000.0
                                        y2 = float(linesplit.split(" ")[1])*1000.0
                                    else:
                                        y1 = float(linesplit.split(" ")[0])*1000.0
                                        y2=y1
                                else:
                                    y1 = float(linesplit)*1000.0
                            except ValueError:
                                return "Load Y must be a number in Line " + str(MyWindow.cnt)
                            if cmnd.upper()[0:4] == "Node".upper():
                                self.inputnode(nodename, x1, y1, M)
                            elif cmnd.upper()[0:4] == "Beam".upper():
                                beamnameindex = MyWindow.findobject(self, beamname.strip(), MyWindow.beams)
                                beamstartnode = MyWindow.beams[beamnameindex].StartNode
                                if beamstartnode.__contains__("SPRING"):
                                    return "Beam Distribution loads applied on spring"
                                self.inputbeam(beamname.strip(), x1, y1,y2)
                            cod = ""
                            y1 = None
                        elif cod.upper() == "M" or cod.upper() == "Μ":
                            cas += 1
                            try:
                                if linesplit[-1] == "\n":
                                    M = float(linesplit[0:-1])*1000.0
                                else:
                                    M = float(linesplit)*1000.0
                            except ValueError:
                                return "Moment M must be a number in Line " + str(MyWindow.cnt)
                            if cmnd.upper()[0:4] == "Node".upper():
                                self.inputnode(nodename.strip(), x1, y1, M)
                            elif cmnd.upper()[0:4] == "Beam".upper():
                                beamnameindex = MyWindow.findobject(self, beamname.strip(), MyWindow.beams)
                                beamstartnode = MyWindow.beams[beamnameindex].StartNode
                                if beamstartnode.__contains__("SPRING"):
                                    return "Beam Distribution loads applied on spring"
                                self.inputbeam(beamname.strip(), x1, y1,y2)
                            cod = ""
                            M = None
                        elif cod.upper() == "TE" or cod.upper() == "ΤΕ":
                            cas += 1
                            try:
                                if linesplit[-1] == "\n":
                                    te = float(linesplit[0:-1])
                                else:
                                    te = float(linesplit)
                            except ValueError:
                                return "Temperature difference must be a number in Line " + str(MyWindow.cnt)
                            if cmnd.upper()[0:4] == "Node".upper():
                                return "Temperature must be defined in beam loads"
                            # elif cmnd.upper()[0:4] == "Beam".upper():
                            # if te != None and ti != None:
                            #    self.inputtemperature(beamname,te,ti,tr)

                            cod = ""

                        elif cod.upper() == "TI" or cod.upper() == "ΤΙ":
                            cas += 1
                            try:
                                if linesplit[-1] == "\n":
                                    ti = float(linesplit[0:-1])
                                else:
                                    ti = float(linesplit)
                            except ValueError:
                                return "Temperature difference must be a number in Line " + str(MyWindow.cnt)
                            if cmnd.upper()[0:4] == "Node".upper():
                                return "Temperature must be defined in beam loads"
                            # elif cmnd.upper()[0:4] == "Beam".upper():
                            # if te!=None and ti!=None:
                            #    self.inputtemperature(beamname,te,ti,tr)

                            cod = ""

                        elif cod.upper() == "TR" or cod.upper() == "ΤR":
                            cas += 1
                            try:
                                if linesplit[-1] == "\n":
                                    tr = float(linesplit[0:-1])
                                else:
                                    tr = float(linesplit)
                            except ValueError:
                                return "Temperature difference must be a number in Line " + str(MyWindow.cnt)
                            if cmnd.upper()[0:4] == "Node".upper():
                                return "Temperature must be defined in beam loads"
                            # elif cmnd.upper()[0:4] == "Beam".upper():
                            # if te!=None and ti!=None:
                            #    self.inputtemperature(beamname,te,ti,tr)

                            cod = ""

                        else:
                            if cmnd.upper()[0:9] == "Node Conc".upper():
                                nodename = cod
                                found = False
                                for e in range(len(MyWindow.nodes)):
                                    if MyWindow.nodes[e].name == nodename:
                                        found = True
                                        break
                                if not (found):
                                    return "Node not defined in nodes. Error in Line " + str(MyWindow.cnt)
                            if cmnd.upper()[0:4] == "Beam".upper():
                                beamname = cod
                                found = False
                                for e in range(len(MyWindow.beams)):
                                    if MyWindow.beams[e].name == beamname:
                                        found = True
                                        break
                                if not (found):
                                    return "Beam not defined in beams. Error in Line " + str(MyWindow.cnt)
                            cod = ""
                            x1 = None
                            y1 = None
                            M = None
                            cas = 0
                    elif ((cmnd.upper()[0:15] == "Beam Dist Loads".upper() or
                           (MyWindow.line.upper()[0:15] == "Beam Dist Loads".upper()) or
                           (MyWindow.line.upper()[0:-1] == "\n".upper() and cmnd.upper()[
                                                                            0:15] == "Beam Dist Loads".upper()) or
                           (beamname != "")) and cas > 0):
                        if x1 == None and y1 == None:
                            return "No Beam Dist Loads defined"
                        else:
                            x1 = None
                            y1 = None
                            beamname = ""
                            if cas > 0:
                                if linesplit[-1] == "\n":
                                    beamname = linesplit[0:-1]
                                else:
                                    beamname = linesplit
                                    found = False
                                    for e in range(len(MyWindow.beams)):
                                        if MyWindow.beams[e].name == beamname:
                                            found = True
                                            break
                                    if not (found):
                                        return "Beam not defined in beams. Error in Line " + str(MyWindow.cnt)
                                cas = 0
                                cod = ""
                    elif (((MyWindow.line.upper()[0:15] == "Node Conc Loads".upper() or (
                            cmnd.upper()[0:15] == "Node Conc Loads".upper()) or
                            (MyWindow.line.upper()[0:-1] == "\n".upper() and cmnd.upper()[
                                                                             0:15] == "Node Conc Loads".upper()) or
                            ((nodename != "")))) and cas > 0):
                        if x1 == None and y1 == None and M == None:
                            return "No Concentrated Loads defined"
                        else:

                            x1 = None
                            y1 = None
                            M = None
                            if cas > 0:
                                if linesplit[-1] == "\n":
                                    nam = linesplit[0:-1]
                                else:
                                    nam = linesplit
                                if (
                                        nam.upper() == "X" or nam.upper() == "Χ" or nam.upper() == "Y" or nam.upper() == "Υ" or nam.upper() == "M" or nam.upper() == "Μ" or nam.upper() == "TE" or nam.upper() == "ΤΕ"
                                        or nam.upper() == "ΤΙ" or nam.upper() == "ΤΙ" or nam.upper() == "ΤR" or nam.upper() == "ΤR"):
                                    cod = nam
                                else:
                                    nodename = nam
                                    found = False
                                    for e in range(len(MyWindow.nodes)):
                                        if MyWindow.nodes[e].name == nodename:
                                            found = True
                                            break
                                    if not (found):
                                        return "Node not defined in nodes. Error in Line " + str(MyWindow.cnt)
                                    cas = 0
                                    cod = ""
                    else:
                        if x1 == None and y1 == None:
                            return "Beam " + beamname + " was given but not forces given in Line " + str(MyWindow.cnt)


        else:
            return MyWindow.results
        return None
    def BEAMFIXING(self, file):
        foundbeams = DynamicArray()

        MyWindow.line = "r"
        beamname=""
        k=0
        while MyWindow.line:
            MyWindow.line = file.readline()
            #if (MyWindow.line[0:4].upper() == "Node".upper()):
            #    return "Duplicate Node command in line " + str(MyWindow.cnt)
            if (MyWindow.line[0:4].upper() == "Beam".upper()):
                return "Duplicate Beam command in line " + str(MyWindow.cnt)
            MyWindow.cnt += 1
            if (MyWindow.line[0:4].upper() != "Beam".upper() and MyWindow.line[
                                                                 0:8].upper() != "Material".upper() and MyWindow.line[
                                                                                                        0:5].upper() != "Loads".upper() and MyWindow.line[
                                                                                                                                            0:11].upper() != "Beam fixing".upper() and MyWindow.line[
                                                                                                                                            0:11].upper() != "Node fixing".upper() ):
                if (len(MyWindow.line) > 0 and MyWindow.line[0:1] != "#" and MyWindow.line[0:1] != "\n"):
                    linesplit = MyWindow.line.split((" "))
                    if k>0 and (linesplit[0].upper()!="RMS\n" and linesplit[0].upper()!="RME\n"):
                        beamname=""
                        k=0

                    if len(beamname) == 0:
                        # Parsing beam name
                        if linesplit[0] == "\n":
                            st = linesplit[0][0:-1]
                            found = False
                            for e in MyWindow.beams:
                                if (st == MyWindow.beams[e].name):
                                    found = True
                                    break
                            if not found:
                                return "Beam not found in Beam fixing in Line " + str(MyWindow.cnt)
                        else:
                            if linesplit[0][-1] == "\n":
                                beamname = linesplit[0][0:-1]
                            else:
                                beamname = linesplit[0]
                            if len(foundbeams) > 0:
                                found = False
                                for e in range(len(foundbeams)):
                                    if foundbeams[e] == MyWindow.beams[e].name:
                                        return "Duplicate beam  in beam fixing in Line " + str(MyWindow.cnt)
                                    foundbeams.append(MyWindow.beams[e].name)

                    else:
                        # Parsing Materials
                        st = ""
                        cod = ""
                        k = 0
                        # parse Material line
                        for st in linesplit:
                            flag = False
                            if (st != "\n"):
                                if ((st != "\n") and (k == 0) and (not flag)):
                                    if st[-1] == "\n":
                                        cod = st[0:-1]
                                    else:
                                        cod = st
                                    k+=1

                                #RMS Release moments start node
                                if ((cod.upper() == "RMS")  and (k == 1) and (not (flag))):
                                    beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                                    MyWindow.beams[beamnameindex].regflag=(MyWindow.beams[beamnameindex].regflag & 254)
                                else:
                                    beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                                    MyWindow.beams[beamnameindex].regflag= MyWindow.beams[beamnameindex].regflag | 1
                                # RMS Release moments end node
                                if ((cod.upper() == "RME") and (k == 1) and (not flag )):
                                    beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                                    MyWindow.beams[beamnameindex].regflag = (MyWindow.beams[beamnameindex].regflag & (253))
                                else:
                                    beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                                    MyWindow.beams[beamnameindex].regflag = MyWindow.beams[beamnameindex].regflag | 2
                                # DDS Dependent displacement from startnode at end node
                                #
                                #if (cod.upper() == "DDS") and (k == 1) and (flag == False):
                                 #   beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                                 #   if len(MyWindow.dependendnodes)>0:
                                 #       for ee in range(0, len(MyWindow.dependendnodes)):
                                 #           if MyWindow.dependendnodes[ee] == MyWindow.beams[beamnameindex].EndNode:
                                 #               return "Duplicate dependend Endnode " + MyWindow.dependendnodes[ee] + " on beam " + MyWindow.beams[
                                 #                          beamnameindex].name + " in Line " + str(MyWindow.cnt)
                                 #   MyWindow.dependendnodes.append(MyWindow.beams[beamnameindex].EndNode)
                                 #   MyWindow.beams[beamnameindex].regflag = (MyWindow.beams[beamnameindex].regflag | (4))
                                #else:
                                #    beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                                #    startnode=MyWindow.beams[beamnameindex].EndNode
                                #    MyWindow.beams[beamnameindex].regflag = MyWindow.beams[
                                #                                                beamnameindex].regflag & 251
                                # DDE Dependent displacement from endnode at startnode
                                #if (cod.upper() == "DDE") and (k == 1) and (flag == False):
                                #    beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
                                 #   if len(MyWindow.dependendnodes) > 0:
                                #        for ee in range(0, len(MyWindow.dependendnodes)):
                                #            if MyWindow.dependendnodes[ee] == MyWindow.beams[beamnameindex].StartNode:
                                #                return "Duplicate dependend Startnode " + MyWindow.dependendnodes[ee] + " on beam " + \
                                #                       MyWindow.beams[beamnameindex].name + " in Line " + str(MyWindow.cnt)
                                #    MyWindow.beams[beamnameindex].regflag = (
                                #                MyWindow.beams[beamnameindex].regflag | (8))
                                #    MyWindow.dependendnodes.append(MyWindow.beams[beamnameindex].StartNode)
                                #else:
                                #    beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)

                                #    MyWindow.beams[beamnameindex].regflag = MyWindow.beams[
                                #                                                beamnameindex].regflag & 247

                                    #flag = True
                            flag=False


            else:
                oo = 0
                for k in range(0,len(MyWindow.beams)):
                    # StartNode

                    if MyWindow.beams[k].regflag & 3==2:
                        nodename=MyWindow.beams[k].StartNode
                        nodenameindex = MyWindow.findobject(self, nodename, MyWindow.nodes)
                        MyWindow.nodes._copyitem(nodenameindex)
                        MyWindow.nodes[nodenameindex+1].name=MyWindow.nodes[nodenameindex].name+"_{:02d}".format(oo)
                        MyWindow.beams[k].StartNode=MyWindow.nodes[nodenameindex+1].name
                        oo+=1
                        continue
                    if MyWindow.beams[k].regflag & 3==1:
                        nodename=MyWindow.beams[k].EndNode
                        nodenameindex = MyWindow.findobject(self, nodename, MyWindow.nodes)
                        MyWindow.nodes._copyitem(nodenameindex)
                        MyWindow.nodes[nodenameindex].name=MyWindow.nodes[nodenameindex].name+"_{:02d}".format(oo)
                        MyWindow.beams[k].EndNode=MyWindow.nodes[nodenameindex].name
                        oo+=1

                #MyWindow.nodes._copyitem(2)
                MyWindow.karray = np.zeros((3 * len(MyWindow.nodes), 3 * len(MyWindow.nodes)))
                MyWindow.results = np.zeros(3 * len(MyWindow.nodes))
                MyWindow.fixedresults = np.zeros(3 * len(MyWindow.nodes))
                MyWindow.perm = Switcher.mc_kee(self, MyWindow.beams)

                MyWindow.rowlengths = np.zeros(3 * len(MyWindow.nodes))
                MyWindow.firstindexcolumns = np.zeros(1 + 3 * len(MyWindow.nodes))
                MyWindow.bandcolumnlength = np.zeros((len(MyWindow.beams), 3))
                for j in range(len(MyWindow.beams)):
                    i1 = MyWindow.perm.index(MyWindow.findobject(MyWindow, MyWindow.beams[j].StartNode, MyWindow.nodes))
                    i2 = MyWindow.perm.index(MyWindow.findobject(MyWindow, MyWindow.beams[j].EndNode, MyWindow.nodes))
                    #i1 =MyWindow.findobject(MyWindow, MyWindow.beams[j].StartNode, MyWindow.nodes)
                    #i2 = MyWindow.findobject(MyWindow, MyWindow.beams[j].EndNode, MyWindow.nodes)

                    if i1 > i2:
                        temp = i1
                        i1 = i2
                        i2 = temp
                    MyWindow.bandcolumnlength[j][0] = int(j)
                    MyWindow.bandcolumnlength[j][1] = int(i1)
                    MyWindow.bandcolumnlength[j][2] = int(i2)
                    if MyWindow.rowlengths[i1 * 3] == 0:
                        MyWindow.rowlengths[i1 * 3] = int(1)
                        MyWindow.rowlengths[i1 * 3 + 1] = int(2)
                        MyWindow.rowlengths[i1 * 3 + 2] = int(3)
                    if (i2 - i1) * 3 + 1 > MyWindow.rowlengths[i2 * 3]:
                        MyWindow.rowlengths[i2 * 3] = int((i2 - i1) * 3 + 1)
                        MyWindow.rowlengths[i2 * 3 + 1] = int((i2 - i1) * 3 + 2)
                        MyWindow.rowlengths[i2 * 3 + 2] = int((i2 - i1) * 3 + 3)

                    # print (str(j)+"     "+str(i1)+"      "+str(i2))
                    # +" ="+str(i2-i1))
                s1 = 0
                MyWindow.bandcolumnlength = MyWindow.bandcolumnlength[MyWindow.bandcolumnlength[:, 2].argsort()]
                MyWindow.bandcolumnlength = MyWindow.bandcolumnlength[
                    MyWindow.bandcolumnlength[:, 1].argsort(kind='mergesort')]
                #print("{0:4d} {1:4d}".format(int(0), int(MyWindow.firstindexcolumns[0])))
                MyWindow.firstindexcolumns[0] = 0
                for j in range(1, 3 * len(MyWindow.localnodes) + 1):
                    s1 += MyWindow.rowlengths[j - 1]
                    MyWindow.firstindexcolumns[j] = s1
                #    print ("{0:5d} {1:4d} {2:4d}".format (int(j),int(MyWindow.rowlengths[j-1]),int(s1)))

                MyWindow.resp = np.zeros(3 * len(MyWindow.nodes))
                # print ("{0:4d}".format(int(np.sum(MyWindow.rowlengths))))
                MyWindow.totalsum = int(np.sum(MyWindow.rowlengths))
                MyWindow.uarray = np.zeros(MyWindow.totalsum)
                MyWindow.larray = np.zeros(MyWindow.totalsum)
                MyWindow.totalsum = int(np.sum(MyWindow.rowlengths))

                Switcher.addglobalstiffnessmatrixcompact(self)
                #Switcher.addglobalstiffnessmatrix(self)
                return MyWindow.nodes
        MyWindow.karray = np.zeros((3 * len(MyWindow.nodes), 3 * len(MyWindow.nodes)))
        MyWindow.results = np.zeros(3 * len(MyWindow.nodes))
        MyWindow.fixedresults = np.zeros(3 * len(MyWindow.nodes))
        MyWindow.perm = Switcher.mc_kee(self, MyWindow.beams)
        MyWindow.rowlengths = np.zeros(3 * len(MyWindow.nodes))
        MyWindow.firstindexcolumns = np.zeros(1 + 3 * len(MyWindow.nodes))
        MyWindow.bandcolumnlength = np.zeros((len(MyWindow.beams), 3))
        for j in range(len(MyWindow.beams)):
            i1 = MyWindow.perm.index(MyWindow.findobject(MyWindow, MyWindow.beams[j].StartNode, MyWindow.nodes))
            i2 = MyWindow.perm.index(MyWindow.findobject(MyWindow, MyWindow.beams[j].EndNode, MyWindow.nodes))
            if i1 > i2:
                temp = i1
                i1 = i2
                i2 = temp
            MyWindow.bandcolumnlength[j][0] = int(j)
            MyWindow.bandcolumnlength[j][1] = int(i1)
            MyWindow.bandcolumnlength[j][2] = int(i2)
            if MyWindow.rowlengths[i1 * 3] == 0:
                MyWindow.rowlengths[i1 * 3] = int(1)
                MyWindow.rowlengths[i1 * 3 + 1] = int(2)
                MyWindow.rowlengths[i1 * 3 + 2] = int(3)
            if (i2 - i1) * 3 + 1 > MyWindow.rowlengths[i2 * 3]:
                MyWindow.rowlengths[i2 * 3] = int((i2 - i1) * 3 + 1)
                MyWindow.rowlengths[i2 * 3 + 1] = int((i2 - i1) * 3 + 2)
                MyWindow.rowlengths[i2 * 3 + 2] = int((i2 - i1) * 3 + 3)

            # print (str(j)+"     "+str(i1)+"      "+str(i2))
            # +" ="+str(i2-i1))
        s1 = 0
        MyWindow.bandcolumnlength = MyWindow.bandcolumnlength[MyWindow.bandcolumnlength[:, 2].argsort()]
        MyWindow.bandcolumnlength = MyWindow.bandcolumnlength[
            MyWindow.bandcolumnlength[:, 1].argsort(kind='mergesort')]
        # print("{0:4d} {1:4d}".format(int(0), int(MyWindow.firstindexcolumns[0])))
        MyWindow.firstindexcolumns[0] = 0
        for j in range(1, 3 * len(MyWindow.localnodes) + 1):
            s1 += MyWindow.rowlengths[j - 1]
            MyWindow.firstindexcolumns[j] = s1
        #    print ("{0:5d} {1:4d} {2:4d}".format (int(j),int(MyWindow.rowlengths[j-1]),int(s1)))

        MyWindow.resp = np.zeros(3 * len(MyWindow.nodes))
        # print ("{0:4d}".format(int(np.sum(MyWindow.rowlengths))))
        MyWindow.totalsum = int(np.sum(MyWindow.rowlengths))
        MyWindow.uarray = np.zeros(MyWindow.totalsum)
        MyWindow.larray = np.zeros(MyWindow.totalsum)
        MyWindow.totalsum = int(np.sum(MyWindow.rowlengths))

        Switcher.addglobalstiffnessmatrixcompact(self)
        #Switcher.addglobalstiffnessmatrix(self)
        return MyWindow.nodes

    def NODEFIXING(self, file):
        foundNodes = DynamicArray()
        MyWindow.line = "r"
        nodename=""
        X=None
        Y=None
        T=None

        while MyWindow.line:
            MyWindow.line = file.readline()
            if (MyWindow.line[0:4].upper() == "Node".upper()):
                return "Duplicate Node command in line " + str(MyWindow.cnt)
            if (MyWindow.line[0:4].upper() == "Beam".upper() and MyWindow.line[0:11].upper() != "Beam fixing".upper()):
                return "Duplicate Beam command in line " + str(MyWindow.cnt)
            MyWindow.cnt += 1
            if (MyWindow.line[0:4].upper() != "Beam".upper() and MyWindow.line[
                                                                 0:8].upper() != "Material".upper() and MyWindow.line[
                                                                                                        0:5].upper() != "Loads".upper() and MyWindow.line[
                                                                                                                                            0:11].upper() != "Beam fixing".upper() and MyWindow.line[
                                                                                                                                            0:11].upper() != "Node fixing".upper()):
                if (len(MyWindow.line) > 0 and MyWindow.line[0:1] != "#" and MyWindow.line[0:1] != "\n"):
                    linesplit = MyWindow.line.split((" "))
                    if (linesplit[0:-1]==[] and len(nodename)>0):
                        if X==None and Y==None and T==None:
                            return "Node defined but no displacements defined in line "+str(MyWindow.cnt)
                        nodenameindex=MyWindow.findobject(self,nodename,MyWindow.nodes)
                        if X!=None:
                            MyWindow.displacementsindex.append(nodenameindex*3)
                            MyWindow.displacements.append(X/1000.0)
                        if Y!=None:
                            MyWindow.displacementsindex.append(nodenameindex*3+1)
                            MyWindow.displacements.append(Y/1000.0)
                        if T!=None:
                            MyWindow.displacementsindex.append(nodenameindex*3+2)
                            MyWindow.displacements.append(T/1000.0)
                        X = None
                        Y = None
                        T = None
                        nodename=""
                    if len(nodename) == 0:
                        # Parsing beam name
                        if linesplit[0] == "\n":
                            st = linesplit[0][0:-1]
                            found = False
                            for e in MyWindow.nodes:
                                if (st == MyWindow.nodes[e].name):
                                    found = True
                                    break
                            if not found:
                                return "Node not found in Node fixing in Line " + str(MyWindow.cnt)
                        else:
                            if linesplit[0][-1] == "\n":
                                nodename = linesplit[0][0:-1]
                            else:
                                nodename = linesplit[0]
                            if len(foundNodes) > 0:
                                found = False
                                for e in range(len(foundNodes)):
                                    if foundNodes[e] == nodename:
                                        return "Duplicate material name in Line " + str(MyWindow.cnt)
                            foundNodes.append(nodename)
                    else:
                        # Parsing Materials
                        st = ""
                        cod = ""
                        k = 0
                        # parse Material line
                        for st in linesplit:
                            flag = False
                            if (st != "\n"):
                                if ((st != "\n") and (k == 0) and (not flag)):
                                    if st[-1] == "\n":
                                        cod = st[0:-1]
                                    else:
                                        cod = st
                                    k+=1
                                    flag = True
                                if ((cod.upper() == "X" or cod.upper() == "Χ") and (k == 1) and (not (flag))):
                                    try:
                                        if st[-1] == "\n":
                                            X = float(st[0:-1])
                                        else:
                                            X = float(st)
                                    except ValueError:
                                        return "Displacement X must be a number in Line " + str(MyWindow.cnt)
                                    flag = True
                                if (cod.upper() == "Y" or cod.upper() == "Υ") and (k == 1) and (flag == False):
                                    try:
                                        if st[-1] == "\n":
                                            Y = float(st[0:-1])
                                        else:
                                            Y = float(st)
                                    except ValueError:
                                        return "Displacement Y must be a number in Line " + str(MyWindow.cnt)
                                    flag = True
                                if (cod.upper() == "T" or cod.upper() == "Τ") and (k == 1) and (flag == False):
                                    try:
                                        if st[-1] == "\n":
                                            T = float(st[0:-1])
                                        else:
                                            T = float(st)
                                    except ValueError:
                                        return "Rotation T must be a number in Line " + str(MyWindow.cnt)
            else:
                if (MyWindow.line[0:5].upper() == "Loads".upper() or MyWindow.line[0:11].upper() == "Beam fixing".upper() and len(nodename) > 0):
                    #if (MyWindow.line[0:5].upper() == "Loads".upper()) and len(nodename)==0 and len(MyWindow.displacementsindex)==0:
                    #    Switcher.addglobalstiffnessmatrix(self)

                    if MyWindow.line[0:5].upper() == "Loads".upper() and X == None and Y == None and T == None and len(MyWindow.displacementsindex)==0:
                        return MyWindow.nodes
                    if len(nodename)>0:
                        nodenameindex = MyWindow.findobject(self, nodename, MyWindow.nodes)
                        if X != None:
                            MyWindow.displacementsindex.append(nodenameindex * 3)
                            MyWindow.displacements.append(X/1000.0)
                        if Y != None:
                            MyWindow.displacementsindex.append(nodenameindex * 3 + 1)
                            MyWindow.displacements.append(Y/1000.0)
                        if T != None:
                            MyWindow.displacementsindex.append(nodenameindex * 3 + 2)
                            MyWindow.displacements.append(T/1000.0)

                    MyWindow.lastcommand = MyWindow.line[0:-1]
                    if (len(MyWindow.displacementsindex) < 3):
                        return MyWindow.nodes
                        #return "Not enough equilibrium equations\nFixes must be at least 3"



                return MyWindow.nodes

        return MyWindow.nodes

    def mc_kee(self,beams):
        #pl=[]
        #mm = DynamicArray()
        #t#hesis={}
        consequetive=[]

        indexes=[]
        max1=0
        for ii in range(0,len(beams)):
            Startn = MyWindow.findobject(MyWindow, beams[ii].StartNode, MyWindow.nodes)
            Endn = MyWindow.findobject(MyWindow, beams[ii].EndNode, MyWindow.nodes)
            uu=numbering(Startn,Endn)
            indexes.append(Startn)
            indexes.append(Endn)
            if math.fabs(Endn-Startn)>max1:
                u1=ii
                max1=math.fabs(Endn-Startn)
        rank=1
        i = 0
        ind2=-1
        ind3=0
        ind4=0
        sign=1
        ex1=False
        while len(consequetive)<int((len(MyWindow.results))/3):
        #while len(consequetive)<=((len(indexes)*0.5-1))*(0.5*(len(indexes)))*0.5:
                values = np.array(indexes)
                ind5=0

                if ind2==-1:
                    while True:
                        i = 0
                        while ind5<len(values):
                            if indexes[ind5]==-1:
                                ind5 += 1
                                continue
                            i=len( np.where(values == indexes[ind5])[0])

                            if i<=rank:
                                startindex = np.where(values == indexes[ind5])[0][0]

                                if len(consequetive)>0:
                                    try:
                                        #Check if it's on the list
                                        ind1 = consequetive.index(indexes[ind5])
                                        currentind=ind5
                                        if i<rank:
                                            break
                                        indexes[ind5]=-1
                                    except ValueError:
                                        currentind = 0
                                        break
                                        pass
                                else:
                                    currentind = 0
                                    break
                            ind5 += 1
                        if ind5<len(values):
                            break
                        else:
                            ind5=0
                            rank+=1

                if (i==rank  and len(consequetive)==0):
                    consequetive.append(indexes[ind5])
                    indexes[ind5]=-1
                    ind2=-2
                    if (ind5%2==0):
                        consequetive.append(indexes[ind5+1])
                        indexes[ind5+1] = -1
                        ind5+=1
                        sign=1
                    else:
                        consequetive.append(indexes[ind5 - 1])
                        indexes[ind5 - 1]= -1
                        ind5 -= 1
                        sign=-1
                    currentind=ind5
                elif (len(consequetive)>0):
                    try:
                        ind1=-1
                        #Find match to the last element of the list
                        if currentind==0:
                            ind1=ind5
                            consequetive.append(indexes[ind5])

                        ind1=indexes.index(consequetive[-1],currentind)

                        try:
                            ind2 = consequetive.index(indexes[ind1])
                            indexes[ind1]=-1
                        except ValueError:
                            pass
                        if (ind1 % 2 == 0):
                            nextelement=ind1+1
                        else:
                            nextelement=ind1-1
                        try:
                            indexes[ind1] = -1
                            element1=indexes[nextelement]
                            if currentind!=0:
                                ind2=-2
                            else:
                                ind2=-1
                            #Find if element is in the added list
                            ind2=consequetive.index(element1)
                            ind2=-1
                               # indexes[ind2]=-1
                            #Found stop iteration
                        except ValueError:
                            #if it's not in the list add it and add -1 to the list
                            if element1>-1:
                                consequetive.append(element1)
                            indexes[nextelement]=-1

                        if ind2!=-2:
                            o=1
                    except ValueError:

                        ind2=-1


        consequetive.reverse()
        #max2=0
        #for ii in range(0, len(beams)):
        #    Startn = consequetive[MyWindow.findobject(MyWindow, beams[ii].StartNode, MyWindow.nodes)]
        #    Endn =  consequetive[MyWindow.findobject(MyWindow, beams[ii].EndNode, MyWindow.nodes)]
        #    if math.fabs(Endn - Startn) > max2:
        #        u2=ii
        #        max2 = math.fabs(Endn - Startn)
        #consequetive = []
        #for k in range(len(MyWindow.nodes)):
            #consequetive.append(k)
        return consequetive
    def Croutold(self,a,b):
        #a=np.array(
         #  [[  7344400000,	0,	-11016600000,	3672200000,	0,      0],
         #   [   0,	   44066400000,	0,	0,-22033200000,0],
         #   [-11016600000,	0,	44066400000,	0,	0,11016600000],
         #   [3672200000,	0,	0,	14688800000,	0,3672200000],
         #   [0,	-22033200000,	0,	0,	22033200000,0],
         #   [0,	0,	11016600000,	3672200000,	0,		7344400000]])
        #print(a)
        #b=np.array([-2500,	0,	-30000,	0,	0,	2500])
        m, n = a.shape
        if (m != n):
            print("Crout cannot be used.")  # Ensure that the number of equations is equal to the number of unknowns
        else:
            l = np.zeros((n, n))
            u = np.zeros((n, n))
            s1 = 0
            s2 = 0
           # a=[]
            for i in range(n):
                l[i][0] = a[i][0]
                u[i][i] = 1
            for j in range(1, n):
                u[0][j] = a[0][j] / l[0][0]
            for k in range(1, n):
                for i in range(k, n):
                    for r in range(k): s1 += l[i][r] * u[r][k]
                    l[i][k] = a[i][k] - s1
                    s1 = 0  # Initialize s1 after each summation=0
                for j in range(k + 1, n):
                    for r in range(k): s2 += l[k][r] * u[r][j]
                    u[k][j] = (a[k][j] - s2) / l[k][k]
                    s2 = 0  # Initialize s2 after each summation=0
            #
            print (l)
            print (u)
            y = np.zeros(n)
            s3 = 0
            y[0] = b[0] / l[0][0]  # First calculate the first x solution
            for k in range(1, n):
                for r in range(k):
                    s3 += l[k][r] * y[r]
                y[k] = (b[k] - s3) / l[k][k]
                s3 = 0

                # Back generation to solve
            x = np.zeros(n)
            s4 = 0
            x[n - 1] = y[n - 1]
            for k in range(n - 2, -1, -1):
                for r in range(k + 1, n):
                    s4 += u[k][r] * x[r]
                x[k] = y[k] - s4
                s4 = 0

            return x

        #if __name__ == '__main__':  # When the module is run directly, the following code blocks will be run. When the module is imported, the code blocks will not be run.

    def Crout(self, matrix, rightPart):

        #cout = 0
        #m, n = matrix.shape
        #if (m != n):
        #    raise Exception("Not equal matrix dimensions")
        #else:
        #rightPart=[1,0,0,1]
        #rightPart = [1,2,2,0,0,1]
        y=np.zeros(len(rightPart))
        x = np.zeros(len(rightPart))
        renum=[]
        for k in range(0,len(rightPart)):
            try:
                ind=MyWindow.displacementsindex.index(k)

            except ValueError:
                renum.append(k)
        l=np.zeros(len(matrix))
        u = np.zeros(len(matrix))
        #renum=[0,3,4,5]
        n=len(rightPart)
        k1=[]

        ############################## L U factorization Crout method #################################
        for e in range(0,n):
            try:
                f=renum.index(e)
                plithos0=MyWindow.firstindexcolumns[int(1 + e)] -   MyWindow.firstindexcolumns[int(e)]
                currentindex = int(e - plithos0 + 1)
                if e>0:
                    l[int(MyWindow.firstindexcolumns[int(e)]+plithos0-1)]=matrix[int(MyWindow.firstindexcolumns[int(e)]+plithos0-1)]
                    k1.append(l[int(MyWindow.firstindexcolumns[int(e)]+plithos0-1)])
                    u[int(MyWindow.firstindexcolumns[int(e)]+plithos0-1)]=1.0
                else:
                    l[int(MyWindow.firstindexcolumns[0])] = matrix[0]
                    k1.append(l[int(MyWindow.firstindexcolumns[0])])
                    u[int(MyWindow.firstindexcolumns[0]) ] = 1.0
                break
            except ValueError:
                pass

        for i in range(e+1,n):

            if int((i / n * 100)) % 10 == 0:
                GLib.idle_add(prog, i / n)
            elif i == n - 1:
                GLib.idle_add(prog, 1.0)
            if MyWindow.solveexit:
                GLib.idle_add(destroywindow)
                return
            try:
                    f = renum.index(i)
                    plithos0 = int(MyWindow.firstindexcolumns[int(1 + i)] - MyWindow.firstindexcolumns[int(i)])
                    currentindex =int( i -plithos0+1)
                    for j in range(currentindex,currentindex+plithos0):
                        try:
                            f=renum.index(j)
                        except ValueError:
                            continue
                        plithos1 = int(MyWindow.firstindexcolumns[int(1 + j)] - MyWindow.firstindexcolumns[int(j)])
                        currentindex1 = int(j - plithos1 + 1)
                        s3 = 0
                        try:
                            #f = renum.index(j)
                            for g in range(currentindex,j):
                               try:

                                 if (currentindex-currentindex1 + j - g - 1<0):
                                     continue

                                 s3 += l[int(MyWindow.firstindexcolumns[int(i)] + j - g - 1)] * u[int(MyWindow.firstindexcolumns[int(j)]+currentindex-currentindex1 + j - g - 1)]

                               except ValueError:
                                   pass
                            l[int(MyWindow.firstindexcolumns[int(i)]+j-currentindex)] = matrix[int(MyWindow.firstindexcolumns[int(i)]+j-currentindex)] - s3

                        except ValueError:
                            pass
                        if i==j:
                            try:
                                f = renum.index(i)
                                k1.append(l[int(MyWindow.firstindexcolumns[int(i)] + j - currentindex)])
                                u[int(MyWindow.firstindexcolumns[int(i)] + j - currentindex)] = 1.0
                            except ValueError:
                                pass
                        else:
                            s3 = 0
                            try:

                                for g in range(currentindex,j):
                                    try:
                                        if int(currentindex-currentindex1+j-g-1<0):
                                            continue
                                        s3 += l[int(MyWindow.firstindexcolumns[int(j)] +currentindex-currentindex1+j-g-1)] *  u[int(MyWindow.firstindexcolumns[int(i)] +j-g-1)]
                                    except ValueError:
                                        pass
                                dokj=j
                                try:
                                    f = renum.index(dokj)
                                    while dokj>=0:
                                        try:
                                            f = renum.index(dokj)
                                            plithos1 = int(MyWindow.firstindexcolumns[int(1 + dokj)] - MyWindow.firstindexcolumns[int(dokj)])
                                            currentindex1 = int(dokj - plithos1 + 1)
                                            u[int(MyWindow.firstindexcolumns[int(i)]+dokj-currentindex)] = (matrix[int(MyWindow.firstindexcolumns[int(i)]+dokj-currentindex)]-s3)/l[int(MyWindow.firstindexcolumns[int(dokj)] +plithos1-1)]
                                            break
                                        except ValueError:
                                            pass
                                        dokj-=1
                                except ValueError:
                                    pass
                                #####l
                            except ValueError:
                                pass
                        #except ValueError:
                         #   pass
            except ValueError:
                pass
        #f = open("/home/lefteris/Downloads/rightpart.txt", "w")
        #for cc in range(0, 159):
        #    f.write("{0:.6f}".format(rightPart[cc]))
        #    f.write("\n")
        #f.close()
        #for cc in range(0, 2775):
        #    f.write("{0:.6f}".format(l[cc]))
        #    f.write(" {0:.6f}".format(u[cc]))
        #    f.write("\n")

        #f.close()
        #for i in range(0, n):
         #   w=""
         #   if i==155:
         #       w=""
         #   plithos0 = int(MyWindow.firstindexcolumns[int(1 + i)] - MyWindow.firstindexcolumns[int(i)])
         #   currentindex = int(i - plithos0 + 1)
         #   for j in range(0, n):
         #       plithos1 = int(MyWindow.firstindexcolumns[int(1 + j)] - MyWindow.firstindexcolumns[int(j)])
         #       currentindex1 = int(j - plithos1 + 1)
         #       if i==j:
         #           w+=str(u[int(MyWindow.firstindexcolumns[int(i)] + plithos0 - 1)]) + " "
         #       elif i>=currentindex1 and i<j:
         #           w+=str(u[int(MyWindow.firstindexcolumns[int(j)] + i - currentindex1)]) + " "

         #       elif j>=currentindex and i>j:
                    #w+=str(u[int(MyWindow.firstindexcolumns[int(i)] + j - currentindex)]) + " "
          #          w += "0.00 "
           #     else:
            #        w+="0.00 "

           # print(w)

        k1=np.sort(k1)
        y[int(renum[0])]=rightPart[int(renum[0])]/l[int(MyWindow.firstindexcolumns[e+1])-1]
        for i in range(1,len(rightPart)):

            s3=0
            try:
                f=renum.index(i)
                plithos0 = int(MyWindow.firstindexcolumns[int(1 + i)] - MyWindow.firstindexcolumns[int(i)])
                currentindex = int(i - plithos0 + 1)
                for j in range(currentindex,currentindex+plithos0-1):
                    try:
                        f=renum.index(j)
                        s3+=l[int(MyWindow.firstindexcolumns[int(i)]+j-currentindex)]*y[int(j)]
                    except ValueError:
                        pass
                y[int(i)] = (rightPart[int(i)] - s3) / l[int(MyWindow.firstindexcolumns[int(i)]+plithos0-1)]
            except ValueError:
                pass

            #s3 = 0
        #y[0] = rightPart[0] / l[0][0]  # First calculate the first x solution
        #for k in range(1, len(renum)):
        #    for r in range(k):
        #        s3 += l[k][r] * y[r]
        #    y[k] = (rightPart[k] - s3) / l[k][k]
        #    s3 = 0
        #f = open("/home/lefteris/Downloads/ypart.txt", "w")
        #for cc in range(0, 159):
        #    f.write("{0:.6e}".format(y[cc]))
        #    f.write("\n")
        #f.close()
        # for cc in range(0, 2775):
        #    f.write("{0:.6f}".format(l[cc]))
        #    f.write(" {0:.6f}".format(u[cc]))
        #    f.write("\n")

        # f.close()
            # Back generation to solve
        #x = np.zeros(len(renum))
        x[int(renum[-1])] = y[int(renum[-1])]
        for i in range(len(rightPart)-2,-1,-1):
            s3 = 0
            try:
                f = renum.index(i)
                if i==renum[-1]:
                    continue

                plithos0 = int(MyWindow.firstindexcolumns[int(1 + i)] - MyWindow.firstindexcolumns[int(i)])
                currentindex = int(i - plithos0 + 1)
                for j in range(len(rightPart)-1,i,-1):
                    try:
                        f=renum.index(j)
                        plithos1 = int(MyWindow.firstindexcolumns[int(1 + j)] - MyWindow.firstindexcolumns[int(j)])
                        currentindex1 = int(j - plithos1 + 1)
                        if currentindex1<=i:
                            s3 += u[int(MyWindow.firstindexcolumns[int(j)] +i-currentindex1)] * x[int(j)]
                    except ValueError:
                        pass
                x[int(i)] = y[int(i)] - s3
            except ValueError:
                pass
        #s4 = 0
        #x[n - 1] = y[n - 1]
        #for k in range(n - 2, -1, -1):
        #    for r in range(k + 1, n):
        #        s4 += u[k][r] * x[r]
        #    x[k] = y[k] - s4
        #    s4 = 0
        # Put
        #f = open("/home/lefteris/Downloads/xpart.txt", "w")
        #for cc in range(0, 159):
         #   f.write("{0:.6e}".format(x[cc]))
         #   f.write("\n")
        #f.close()
        # for cc in range(0, 2775):
        #    f.write("{0:.6f}".format(l[cc]))
        #    f.write(" {0:.6f}".format(u[cc]))
        #    f.write("\n")

        # f.close()
        for i in range(0,len(MyWindow.displacementsindex)):
            x[MyWindow.displacementsindex[i]]=MyWindow.displacements[i]
        return x
    def resultforces(self):
        forces=[]
        for j in range(0,len(MyWindow.results)):
            s3=0.0
            plithos0 = int(MyWindow.firstindexcolumns[int(1 + j)] - MyWindow.firstindexcolumns[int(j)])
            currentindex = int(j - plithos0 + 1)
            for i in range(0,len(MyWindow.results)):

                    #renum.index(j)
                plithos0 = int(MyWindow.firstindexcolumns[int(1 + i)] - MyWindow.firstindexcolumns[int(i)])
                currentindex1 = int(i - plithos0 + 1)
                if (i<=j and j>=currentindex1 and i>=currentindex):
                   s3+=MyWindow.alldisplacements[i]*MyWindow.uarray[int(MyWindow.firstindexcolumns[j]+i-currentindex)]
                elif (i>j and j>=currentindex1 and i>=currentindex):
                   s3 += MyWindow.alldisplacements[i] * MyWindow.uarray[int(MyWindow.firstindexcolumns[i] + j-currentindex1)]
            #s3 -= MyWindow.results[j]
            s3=s3-MyWindow.fixedresults[j] - MyWindow.newresults[j]
            forces.append(s3)

        return  forces

class MyWindow(Gtk.Window):
    cos=[]
    solveexit=False
    lastcommand = ""
    mouseX=0.0
    mouseY = 0.0
    maxN = 0
    maxQ = 0
    maxM = 0
    filename = ""
    line=""
    cnt = 0
    stafilenam=""
    localnodes = DynamicArray()
    dependendnodes = DynamicArray()
    nodes = DynamicArray()
    beams = DynamicArray()
    beamunit=DynamicArray()
   # fullnode=DynamicArray()
    whol=""
    handler_id=0
    current_page=0
    stopfile=0
    displacementsindex =[]
    displacements=[]
    textbuffer=Gtk.TextBuffer()
    notebook = Gtk.Notebook()
    button=Gtk.MenuItem
    textview = Gtk.TextView()
    layout2 = Gtk.DrawingArea()
    layout3 = Gtk.DrawingArea()
    layout4 = Gtk.DrawingArea()
    layout1 = Gtk.Layout()
    layout5 = Gtk.DrawingArea()
    layout6 = Gtk.DrawingArea()
    layout7 = Gtk.DrawingArea()
    layout = Gtk.Layout()
    scrolledwindow = Gtk.ScrolledWindow()
    copytoclipboard=Gtk.MenuItem()
    cleartext=Gtk.Button()
    solveframe=Gtk.Button()
    print = Gtk.MenuItem()
    about = Gtk.MenuItem()
    resultstopdf=Gtk.MenuItem()
    textresultmenu=Gtk.MenuItem()
    printtopdf = Gtk.MenuItem()
    num_lines = 0
    ratio=0.0
    w = 608
    h = 340
    scale=50.0
    font=9.0
    windowtitle="Solve flat frame"
    def __init__(self):
        #print(struct.calcsize("P")*8)
        Gtk.Window.__init__(self)
        #Switcher.Croutold(MyWindow,[],[])
        MyWindow.textresultmenu = builder.get_object("mnuFilePrintResults")
        MyWindow.textresultmenu.set_sensitive(False)
        MyWindow.textresultmenu.connect("activate", self.on_print_results)
        MyWindow.resultstopdf = builder.get_object("mnuExportResultsTopdf")
        MyWindow.resultstopdf.connect("activate", self.on_print_results)
        MyWindow.resultstopdf.set_sensitive(False)
        MyWindow.titl=builder.get_object("window1")
        MyWindow.button = builder.get_object("mnuFileOpen")
        MyWindow.button.connect("activate", self.on_file_clicked)
        #MyWindow.copytoclipboard = builder.get_object("mnuCopytoclipboard")
        window.set_size_request(640,480)
        MyWindow.titl.set_title(MyWindow.windowtitle)

        exit = builder.get_object("mnuFileQuit")
        exit.connect("activate", Gtk.main_quit)
        MyWindow.layout = builder.get_object("layout")
        MyWindow.cleartext = builder.get_object("cleartext")
        MyWindow.solveframe=builder.get_object("solveframe")
        MyWindow.solveframe.set_sensitive(False)
        MyWindow.solveframe.connect("clicked", self.on_solve_clicked)
        #MyWindow.button.connect("clicked", self.on_file_clicked)
        MyWindow.cleartext.connect("clicked", self.on_cleartext_clicked)
        #MyWindow.printing = builder.get_object("printing")
        #MyWindow.printing.connect("clicked", self.on_print_clicked)
        #MyWindow.printing.set_sensitive(False)
        MyWindow.printing = builder.get_object("mnuFilePrint")
        MyWindow.printing.set_sensitive(False)
        MyWindow.printing.connect("activate", self.on_print_clicked)
        MyWindow.cleartext.set_sensitive(False)
        MyWindow.printtopdf = builder.get_object("mnuPrinttopdf")
        window.set_size_request(640,480)
        exit = builder.get_object("mnuFileQuit")
        exit.connect("activate", Gtk.main_quit)
        MyWindow.about = builder.get_object("mnuAboutMenu")
        MyWindow.about.connect("activate", self.about_dialog)

        MyWindow.copytoclipboard = builder.get_object("mnuCopytoclipboard")
        MyWindow.copytoclipboard.connect("activate",self.on_copyclipboard_clicked)
        MyWindow.layout = builder.get_object("layout")
        MyWindow.cleartext = builder.get_object("cleartext")
        #MyWindow.button.connect("clicked", self.on_file_clicked)
        MyWindow.cleartext.connect("clicked", self.on_cleartext_clicked)
        #MyWindow.printing = builder.get_object("printing")
        #MyWindow.printing.connect("clicked", self.on_print_clicked)
        #MyWindow.printing.set_sensitive(False)
        MyWindow.printing = builder.get_object("mnuFilePrint")
        MyWindow.printing.set_sensitive(False)
        MyWindow.printing.connect("activate", self.on_print_clicked)
        MyWindow.cleartext.set_sensitive(False)
        MyWindow.printtopdf = builder.get_object("mnuPrinttopdf")
        MyWindow.printtopdf.connect("activate", self.on_print_to_pdf)
        MyWindow.printtopdf.set_sensitive(False)
        MyWindow.cleartext.set_sensitive(False)
        MyWindow.copytoclipboard.set_sensitive(False)

        MyWindow.layout.put(MyWindow.notebook, 10, 70)
        #layout.add(notebook)


        MyWindow.scrolledwindow.set_size_request(MyWindow.w,MyWindow.h)

        MyWindow.textbuffer = MyWindow.textview.get_buffer()
        MyWindow.textview.set_editable(False)
        MyWindow.layout1.add(MyWindow.scrolledwindow)
        MyWindow.textview.show()
        MyWindow.scrolledwindow.add(MyWindow.textview)
        #scrollbar.add(textview)
        MyWindow.layout1.set_size_request(MyWindow.w, MyWindow.h)
        MyWindow.layout1.show()


        #MyWindow.layout2.set_size_request(MyWindow.w*1.3, MyWindow.h)
        MyWindow.notebook.show()
        MyWindow.scrolledwindow.show()
        #MyWindow.notebook.show()

        MyWindow.copytoclipboard.connect("activate", self.on_copyclipboard_clicked)
        #MyWindow.handler_id=MyWindow.layout2.connect("draw",self.OnDrawlM)
        #MyWindow.layout2.disconnect(MyWindow.handler_id)

        MyWindow.layout2.show()
        MyWindow.layout3.show()
        #MyWindow.layout4.set_size_request(MyWindow.w,MyWindow.h)
        MyWindow.layout4.show()
        #window.connect("configure-event",self.resf)
        #window.connect("window-state-event",self.k1)
        MyWindow.layout5.show()
        MyWindow.layout6.show()
        MyWindow.layout7.show()
        window.connect("size-allocate", self.allocate_size)
        MyWindow.notebook.connect("button-release-event", self.on_tab_selected)
        #window.connect("configure-event", self.conf)

        window.show_all()
    def about_dialog(self,widget):
        #dialog1 = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
        #                            Gtk.ButtonsType.YES_NO, "Are you sure ?")

        dialog = Gtk.MessageDialog(
            self,
            0,
            Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK,
            "Solve Static Frames\n     Version 2.00",
        )
        dialog.format_secondary_text(
            "GNU 2020 Lefteris Leontopoulos."
        )
        res=dialog.run()


        dialog.destroy()


    def on_print_results(self,widget):
        ps = Gtk.PaperSize.new_custom("cc", "cc", 210, 297, Gtk.Unit.MM)
        st = Gtk.PrintSettings()
        s = Gtk.PageSetup()
        s.set_paper_size(ps)
        #s.set_bottom_margin(4.3, Gtk.Unit.MM)
        s.set_bottom_margin(4.3, Gtk.Unit.MM)
        s.set_left_margin(4.3, Gtk.Unit.MM)
        s.set_right_margin(4.3, Gtk.Unit.MM)
        s.set_top_margin(4.3, Gtk.Unit.MM)
        s.set_orientation(Gtk.PageOrientation.PORTRAIT)
        print_op = Gtk.PrintOperation()
        #print_op.set_n_pages(2)
        #

        #print_op.set_n_pages(1)
        print_op.set_default_page_setup(s)
        print_op.connect("begin_print", self.createpages)
        print_op.connect("draw_page", self.drawpage4)
        if widget.get_label()[0:6]=="Export":
            dialog = Gtk.FileChooserDialog("Save PDF file", self, Gtk.FileChooserAction.SAVE,
                                           (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE,
                                            Gtk.ResponseType.OK))
            dialog.set_do_overwrite_confirmation(True)
            filter1 = Gtk.FileFilter()
            filter2 = Gtk.FileFilter()
            filter1.set_name("PDF files")
            filter1.add_pattern("*.pdf")
            filter2.set_name("All files")
            filter2.add_pattern("*")
            dialog.add_filter(filter1)
            dialog.add_filter(filter2)
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                if (dialog.get_filename != ""):
                    filenam = dialog.get_filename()
                    print_op.set_export_filename(filenam)
                    res = print_op.run(Gtk.PrintOperationAction.EXPORT, None)
                    dialog.destroy()
                else:
                    dialog.destroy()
            else:
                dialog.destroy()
        else:
            res = print_op.run(Gtk.PrintOperationAction.PRINT_DIALOG, None)


    def on_tab_selected(self,widget,cr):
        MyWindow.current_page=widget.get_current_page()

    def allocate_size(self,widget,cr):
        width=widget.get_allocation().width
        height = widget.get_allocation().height

        MyWindow.scrolledwindow.set_size_request(width+MyWindow.w-640, height+MyWindow.h-480)
        MyWindow.layout1.set_size_request(width+MyWindow.w-640, height+MyWindow.h-480)
        MyWindow.layout2.set_size_request(width + MyWindow.w - 640, height + MyWindow.h - 480)
        if self==window:
            try:
                self.layout.move(MyWindow.cleartext, width - 122, 13)
                self.layout.move(MyWindow.solveframe,width - 232, 13)
            except AttributeError:
                pass
    #def toolt(widget,x,y,keyboard_mode,tooltip):
    def toolt(*args):
        fl=False
        x=args[len(args)-4]
        y=args[len(args)-3]

        tooltip=args[len(args)-1]
        for e in range(0,len(MyWindow.Graph)):
            if ((not math.isnan(MyWindow.Graph[e].X1)) and (not math.isnan(MyWindow.Graph[e].X2)) and (not math.isnan(MyWindow.Graph[e].Y1)) and (not math.isnan(MyWindow.Graph[e].Y2))):
                if x>=int(MyWindow.Graph[e].X1) and x<=int(MyWindow.Graph[e].X2) and y>=int(MyWindow.Graph[e].Y1 ) and y<=int(MyWindow.Graph[e].Y2):
                    #startNodeIndex = MyWindow.findobject(MyWindow, MyWindow.Graph[e].name, MyWindow.nodes)
                    nodeindex = MyWindow.findobject(MyWindow, MyWindow.Graph[e].name, MyWindow.nodes)

                    if (nodeindex>-1):
                       try:
                        txtN = "<span foreground='#ff0000'>DX= {:.6f}mm</span>"
                        txtQ = "<span foreground='#009000'>DY= {:.6f}mm</span>"
                        txtM = "<span foreground='#0000ff'>Dt= {:.6f}mrad</span>"

                        if not(MyWindow.alldisplacements is None):
                            metak= (txtN.format(1000.0 * MyWindow.alldisplacements[MyWindow.perm.index(nodeindex) * 3 + 0]) + " " + txtQ.format(
                                1000.0 * MyWindow.alldisplacements[MyWindow.perm.index(nodeindex) * 3 + 1]) + " " + txtM.format(1000.0 * MyWindow.alldisplacements[MyWindow.perm.index(nodeindex) * 3 + 2]))
                        else:
                            metak=""
                        nam1=MyWindow.Graph[e].name
                        if "_" in nam1[-3:]:
                            nam1=nam1[-3:]
                       except TypeError as error:
                        metak = ""

                       tooltip.set_markup("<b>"+nam1+" <span foreground='#ff0000'>("+str(MyWindow.nodes[nodeindex].X)+ "</span>,<span foreground='#ff0000'>"+str(MyWindow.nodes[nodeindex].Y)+")</span>\n"+metak+"</b>")
                    else:
                        nam1 = MyWindow.Graph[e].name
                        if "_" in nam1[-3:]:
                            nam1=nam1[-3:]
                        tooltip.set_markup("<b>"+nam1+"</b>")
                    fl=True
                    break
        return fl

    #def mousemove(widget,cr):
        #MyWindow.mouseX=cr.x
        #MyWindow.mouseY = cr.y
        #widget.queue_draw()


    def createframe(widget,cr):

        coor=MyWindow.create_frame_beam(widget,cr)
        sig = "Frame Design"
        p = widget.get_allocation()
        wndh = p.height
        wndp = p.width
        cr.set_source_rgb(0.2, 0.0, 0.0)
        cr.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
        cr.move_to((p.width - dx) / 2, 20)
        cr.show_text(sig)
        # guiobj.create_frame_beam(widget, cr)
        #guiobj.create_frame_beam(widget, cr)
        p = widget.get_allocation()
        wndh = p.height
        wndp = p.width
    def create_frame_beam(widget,cr):
        MyWindow.Graph=DynamicArray()
        maxx = -9e99
        maxy = -9e99
        minx = 9e99
        miny = 9e99
        widget.set_property("has-tooltip",True)
        #widget.connect("motion-notify-event", MyWindow.mousemove)
        widget.connect("query-tooltip",MyWindow.toolt)
        #widget.connect("query-tooltip", MyWindow.toolt)
        p = widget.get_allocation()
        wndh=p.height
        wndp=p.width
        cr.move_to(20, 20)
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.set_font_size(MyWindow.font * 1.3)
        #cr.show_text("X:" + str(MyWindow.mouseX) + ",Y:" + str(MyWindow.mouseY))

        for k in range(0,len(MyWindow.nodes)):

            if MyWindow.nodes[k].name.find("SPRING") > -1:
                continue
            if MyWindow.nodes[k].X > maxx:
                maxx = MyWindow.nodes[k].X
            if MyWindow.nodes[k].X < minx:
                minx = MyWindow.nodes[k].X
            if MyWindow.nodes[k].Y > maxy:
                maxy = MyWindow.nodes[k].Y
            if MyWindow.nodes[k].Y < miny:
                miny = MyWindow.nodes[k].Y
        Dx = maxx - minx
        Dy = maxy - miny
        if Dy==0:
            Dy=Dx
            miny=minx
            maxy=maxx

        #cr.set_line_width(1)
        wx = widget.get_allocation().width*420/MyWindow.w
        wy = widget.get_allocation().height*240/MyWindow.h
        try:
            MyWindow.ratio = min(0.5,Dy / Dx,1.0)

        except ZeroDivisionError as error:
            MyWindow.ratio  = 1.0

        originx = 0
        originy = 0

        coords=DynamicArray()
        for k in range(0,len(MyWindow.beams)):
            beamname = MyWindow.beams[k].name
            # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
            beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
            beamstartnode = MyWindow.beams[beamnameindex].StartNode
            if beamstartnode.find("SPRING") > -1:
                continue
            startNodeIndex =MyWindow.findobject(MyWindow, beamstartnode, MyWindow.nodes)
            beamendnode = MyWindow.beams[beamnameindex].EndNode
            endNodeIndex = MyWindow.findobject(MyWindow, beamendnode, MyWindow.nodes)
            xl = MyWindow.beams[beamnameindex].xl
            yl = MyWindow.beams[beamnameindex].yl
            c = xl / math.sqrt(xl * xl + yl * yl)
            s = yl / math.sqrt(xl * xl + yl * yl)
            if Dx>0:
                x1 = originx + wx * ((MyWindow.nodes[startNodeIndex].X-minx) / Dx)
                y1 = originy - wy*MyWindow.ratio * ((MyWindow.nodes[startNodeIndex].Y-miny) / Dy)
                x2 = originx + wx * ((MyWindow.nodes[endNodeIndex].X-minx) / Dx)
                y2 = originy - wy*MyWindow.ratio * ((MyWindow.nodes[endNodeIndex].Y-miny) / Dy)
            else:
                MyWindow.ratio=1.0
                x1 = originx
                y1 = originy - wy * MyWindow.ratio * ((MyWindow.nodes[startNodeIndex].Y-miny) / Dy)
                x2 = originx
                y2 = originy - wy * MyWindow.ratio * ((MyWindow.nodes[endNodeIndex].Y-miny) / Dy)
            w=Coords(x1,y1,x2,y2,beamstartnode,beamendnode)
            coords.append(w)

        xmax = -9e99
        ymax = -9e99
        xmin = 9e99
        ymin = 9e99
        for k in range(0,len(MyWindow.beams)):
            beamname = MyWindow.beams[k].name
            # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
            beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
            beamstartnode = MyWindow.beams[beamnameindex].StartNode
            if beamstartnode.find("SPRING") > -1:
                continue
            startNodeIndex = MyWindow.findobject(MyWindow, beamstartnode, MyWindow.nodes)
            beamendnode = MyWindow.beams[beamnameindex].EndNode
            endNodeIndex = MyWindow.findobject(MyWindow, beamendnode, MyWindow.nodes)
            xl = MyWindow.beams[beamnameindex].xl
            yl = MyWindow.beams[beamnameindex].yl
            c = xl / math.sqrt(xl * xl + yl * yl)
            s = yl / math.sqrt(xl * xl + yl * yl)
            x1a=coords[k].X1+MyWindow.scale*(wndh/wndp)*c
            x1k = coords[k].X1 - MyWindow.scale*(wndh/wndp) * c
            x2a=coords[k].X2 + MyWindow.scale*(wndh/wndp) * c
            x2k=coords[k].X2-MyWindow.scale*(wndh/wndp) * c
            y1a = coords[k].Y1 + MyWindow.scale*(wndh/wndp) * s*MyWindow.ratio
            y1k = coords[k].Y1 - MyWindow.scale*(wndh/wndp) * s*MyWindow.ratio
            y2a = coords[k].Y2 + MyWindow.scale*(wndh/wndp) * s*MyWindow.ratio
            y2k = coords[k].Y2 - MyWindow.scale*(wndh/wndp) * s*MyWindow.ratio
            xmax=max(xmax,x1a,x1k,x2a,x2k)
            xmin = min(xmin,x1a, x1k, x2a, x2k)
            ymax = max(ymax,y1a, y1k, y2a, y2k)
            ymin = min(ymin,y1a, y1k, y2a, y2k)
        wid=xmax-xmin
        hei=ymax-ymin
        if hei<wndh/16:
            hei+=wndh/2
            originy = (wndh - hei)
        if wid==0:
            originy = wndh -hei/16
        else:
            originy = wndh - hei
        originx=(wndp-wid)/2

        e=0
        for k in range(0,len(MyWindow.beams)):
            beamname = MyWindow.beams[k].name
            # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
            beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
            beamstartnode = MyWindow.beams[beamnameindex].StartNode
            if beamstartnode.find("SPRING") > -1:
                continue
            startNodeIndex = MyWindow.findobject(MyWindow, beamstartnode, MyWindow.nodes)
            beamendnode = MyWindow.beams[beamnameindex].EndNode
            endNodeIndex = MyWindow.findobject(MyWindow, beamendnode, MyWindow.nodes)
            xl = MyWindow.beams[beamnameindex].xl
            yl = MyWindow.beams[beamnameindex].yl
            c = xl / math.sqrt(xl * xl + yl * yl)
            s = yl / math.sqrt(xl * xl + yl * yl)
            coords[e].X1+=originx
            coords[e].X2 += originx
            coords[e].Y1 += originy
            coords[e].Y2 += originy
            coords[e].StartNode=beamstartnode
            coords[e].EndNode = beamendnode
            cr.set_line_width(5)
            cr.set_source_rgb(0, 0, 0)
            cr.move_to(coords[e].X1, coords[e].Y1)
            c1 = (coords[e].X2 - coords[e].X1) / math.sqrt(
                math.pow((coords[e].X2 - coords[e].X1), 2.0) + math.pow((coords[e].Y2 - coords[e].Y1), 2.0))
            s1 = (coords[e].Y2 - coords[e].Y1) / math.sqrt(
                math.pow((coords[e].X2 - coords[e].X1), 2.0) + math.pow((coords[e].Y2 - coords[e].Y1), 2.0))

            #w=Coords(x1,y1,x2,y2)
            #coords.append(w)
            cr.line_to(coords[e].X2, coords[e].Y2)
            cr.stroke()
            cr.set_line_width(1)
            cr.set_source_rgb(1, 0, 0)
            cr.move_to(coords[e].X1 + 5 * s1, coords[e].Y1 - 5 * c1)
            cr.line_to(coords[e].X1 - 5 * s1, coords[e].Y1 + 5 * c1)
            cr.stroke()
            sig =MyWindow.beams[e].StartNode
            if "_" in sig[-3:]:
                sig=sig[:-3]
            cr.save()
            cr.set_font_size(MyWindow.font)
            (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
            cr.move_to(coords[e].X1 - 5 * s1, coords[e].Y1 - 5 * c1)
            cr.rotate(math.atan2(s1,c1))
            #cr.move_to(0, 0)
            cr.set_font_size(MyWindow.font)
            p1=cr.text_extents(sig)

            stx=coords[e].X1- 5 * c1
            sty=coords[e].Y1- 5 * s1
            enx=coords[e].X1- 5 * c1+p1.width*c1-p1.height*s1
            eny=coords[e].Y1- 5 * s1-p1.width*s1-p1.height*c1


            if enx<stx:
                temp=enx
                enx=stx
                stx=temp
            if eny < sty:
                temp = eny
                eny = sty
                sty = temp
            MyWindow.Graph.append(Graph(sig, stx,sty ,enx,eny))
            cr.show_text(sig)

            cr.restore()


            e+=1

        for k in range(0,len(MyWindow.beams)):
            beamname = MyWindow.beams[k].name
            # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
            beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
            beamstartnode = MyWindow.beams[beamnameindex].StartNode
            if beamstartnode.find("SPRING") > -1:
                continue
            startNodeIndex = MyWindow.findobject(MyWindow, beamstartnode, MyWindow.nodes)
            beamendnode = MyWindow.beams[beamnameindex].EndNode
            endNodeIndex = MyWindow.findobject(MyWindow, beamendnode, MyWindow.nodes)
            xl = MyWindow.beams[beamnameindex].xl
            yl = MyWindow.beams[beamnameindex].yl
            c = xl / math.sqrt(xl * xl + yl * yl)
            s = yl / math.sqrt(xl * xl + yl * yl)
            x1a=coords[k].X1+MyWindow.scale*(wndh/wndp)*c
            x1k = coords[k].X1 - MyWindow.scale*(wndh/wndp) * c
            x2a=coords[k].X2 + MyWindow.scale*(wndh/wndp) * c
            x2k=coords[k].X2-MyWindow.scale*(wndh/wndp) * c
            y1a = coords[k].Y1 + MyWindow.scale*(wndh/wndp) * s*MyWindow.ratio
            y1k = coords[k].Y1 - MyWindow.scale*(wndh/wndp) * s*MyWindow.ratio
            y2a = coords[k].Y2 + MyWindow.scale*(wndh/wndp) * s*MyWindow.ratio
            y2k = coords[k].Y2 - MyWindow.scale*(wndh/wndp) * s*MyWindow.ratio
            xmax=max(xmax,x1a,x1k,x2a,x2k)
            xmin = min(xmin,x1a, x1k, x2a, x2k)
            ymax = max(ymax,y1a, y1k, y2a, y2k)
            ymin = min(ymin,y1a, y1k, y2a, y2k)
        wid=xmax-xmin
        hei=ymax-ymin
        if hei<wndh/16:
            hei+=wndh/2
            originy = (wndh - hei)
        if wid==0:
            originy = wndh -hei/16
        else:
            originy = wndh - hei
        originx=(wndp-wid)/2

        e=0
        MyWindow.cos=[]

        for k in range(0,len(MyWindow.beams)):
            beamname = MyWindow.beams[k].name
            # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
            beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
            beamstartnode =MyWindow.beams[beamnameindex].StartNode

            if (beamstartnode.find("SPRING") > -1):
              continue
            beamendnode = MyWindow.beams[beamnameindex].EndNode
            if "_" in beamstartnode[-3:]:
                beamstartnode = beamstartnode[:-3]
            if "_" in beamendnode[-3:]:
                beamendnode = beamendnode[:-3]

            MyWindow.cos.append(beamstartnode)
            MyWindow.cos.append(beamendnode)
        e=0
        for k in range(0,len(MyWindow.beams)):
            beamname = MyWindow.beams[k].name
            # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
            beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
            beamstartnode = MyWindow.beams[beamnameindex].StartNode
            if beamstartnode.find("SPRING") > -1:
                continue
            endnodeflag=True
            beamendnode = MyWindow.beams[beamnameindex].EndNode
            for l in range(0,len(MyWindow.cos)):
                if "_" in beamendnode[-3:]:
                    beamendnode = beamendnode[:-3]
                if ((l%2==0) and (MyWindow.cos[l]==beamendnode)):
                    endnodeflag=False
                    break
            if (endnodeflag):
                c1 = (coords[e].X2 - coords[e].X1) / math.sqrt(
                    math.pow((coords[e].X2 - coords[e].X1), 2.0) + math.pow((coords[e].Y2 - coords[e].Y1), 2.0))
                s1 = (coords[e].Y2 - coords[e].Y1) / math.sqrt(
                    math.pow((coords[e].X2 - coords[e].X1), 2.0) + math.pow((coords[e].Y2 - coords[e].Y1), 2.0))

                cr.set_line_width(1)
                cr.set_source_rgb(1, 0, 0)
                cr.move_to(coords[e].X2 - 5 * s1, coords[e].Y2 + 5 * c1)
                cr.line_to(coords[e].X2 + 5 * s1, coords[e].Y2 - 5 * c1)
                cr.stroke()
                sig = MyWindow.beams[e].EndNode
                if "_" in sig[-3:]:
                    sig = sig[:-3]

                cr.save()
                cr.set_font_size(MyWindow.font)
                (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                cr.move_to(coords[e].X2 - 5 * s1, coords[e].Y2 - 5 * c1)
                cr.rotate(math.atan2((s1), (c1)))
                # cr.move_to(0, 0)
                cr.set_font_size(MyWindow.font)
                p1 = cr.text_extents(sig)
                stx = coords[e].X2 - 5 * s1
                sty = coords[e].Y2 - 5 * c1
                enx = coords[e].X2 - 5 * s1 + p1.width * c1 - p1.height * s1
                eny = coords[e].Y2 - 5 * c1 - p1.width * s1 - p1.height * c1
                if enx < stx:
                    temp = enx
                    enx = stx
                    stx = temp
                if eny < sty:
                    temp = eny
                    eny = sty
                    sty = temp
                MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
                cr.show_text(sig)
                cr.restore()
            e+=1
        return coords
    def forcedown(self,cr,x,y,ang,txt):
        cr.save()
        #cr.translate(x,y+24+int(12 * math.cos(math.pi / 3)))
        cr.translate(x, y)
        cr.rotate(ang)
        cr.set_source_rgb(0, 0.8, 0)
        cr.move_to(0,0)
        cr.line_to(0, +20+12 * math.sin(math.pi / 3))
        cr.stroke()
        cr.set_source_rgb(0, 0, 0.4)
        cr.move_to(0,+20+12 * math.sin(math.pi / 3))
        cr.line_to(int(0-12*math.cos(math.pi/3)), 20)
        #cr.line_to(int(0),12 * math.sin(math.pi / 3))
        cr.line_to(int(0 + 12 * math.cos(math.pi / 3)),  20)
        cr.line_to(0,  +20+12 * math.sin(math.pi / 3))
        cr.fill()
        cr.restore()
        cr.save()
        cr.translate(x,y)
        p1 = cr.text_extents(txt)
        cr.rotate(ang + math.pi / 2)
        cr.move_to(+22+12 * math.sin(math.pi / 3),p1.height/2)
        cr.set_font_size(MyWindow.font)

        if (ang>0 and ang<=math.pi/2 or (ang>-math.pi/2 and ang<=0)):
            cr.move_to(+22 + 12 * math.sin(math.pi / 3) + p1.width, -p1.height / 2)
            cr.rotate(math.pi)
        cr.show_text(txt)

        cr.restore()
        stx=  x+(20+12 * math.sin(math.pi / 3))*math.cos(ang+math.pi/2)-p1.height/2*math.sin(ang+math.pi/2)
        sty = y +(20+12 * math.sin(math.pi / 3))*math.sin(ang+math.pi/2)-p1.height/2*math.cos(ang+math.pi/2)
        enx = x+(20+12 * math.sin(math.pi / 3)+p1.width)*math.cos(ang+math.pi/2)+p1.height/2*math.sin(ang+math.pi/2)
        eny = y+(20+12 * math.sin(math.pi / 3)+p1.width)*math.sin(ang+math.pi/2)+p1.height/2*math.cos(ang+math.pi/2)
        if enx < stx:
            temp = enx
            enx = stx
            stx = temp
        if eny < sty:
            temp = eny
            eny = sty
            sty = temp

        MyWindow.Graph.append(Graph(txt, stx,sty ,enx,eny))

    def forceup(self,cr,x,y,ang,txt):
        cr.save()
        #cr.translate(x,y+24+int(12 * math.cos(math.pi / 3)))
        cr.translate(x, y)
        cr.rotate(ang)
        cr.set_source_rgb(0, 0.8, 0)
        cr.move_to(0,0)
        cr.line_to(0, +20+12 * math.sin(math.pi / 3))
        cr.stroke()
        cr.set_source_rgb(0, 0, 0.4)
        cr.move_to(0,0)
        cr.line_to(int(0-12*math.cos(math.pi/3)), 12 * math.sin(math.pi / 3))
        #cr.line_to(int(0),12 * math.sin(math.pi / 3))
        cr.line_to(int(0 + 12 * math.cos(math.pi / 3)),  12 * math.sin(math.pi / 3))
        cr.line_to(0, 0)
        cr.fill()
        cr.restore()
        cr.save()
        cr.translate(x,y)
        p1 = cr.text_extents(txt)
        cr.rotate(ang-math.pi/2)
        cr.move_to(-22-12 * math.sin(math.pi / 3)-p1.width,p1.height/2)
        cr.set_font_size(MyWindow.font)

        if ((ang>math.pi/2 and ang<=math.pi) or (ang>-math.pi and ang<=-math.pi/2)):
            cr.move_to(-22 - 12 * math.sin(math.pi / 3) , -p1.height / 2)
            cr.rotate(math.pi)
        cr.show_text(txt)

        cr.restore()
        stx=  x+(22+12 * math.sin(math.pi / 3))*math.cos(ang+math.pi/2 )-p1.height/2*math.sin(ang+math.pi/2 )
        sty = y +(22+12 * math.sin(math.pi / 3))*math.sin(ang+math.pi/2 )-p1.height/2*math.cos(ang+math.pi/2 )
        enx = x+(22+12 * math.sin(math.pi / 3)+p1.width)*math.cos(ang+math.pi/2)+p1.height/2*math.sin(ang+math.pi/2)
        eny = y+(22+12 * math.sin(math.pi / 3)+p1.width)*math.sin(ang+math.pi/2 )+p1.height/2*math.cos(ang+math.pi/2 )
        if enx < stx:
            temp = enx
            enx = stx
            stx = temp
        if eny < sty:
            temp = eny
            eny = sty
            sty = temp

        MyWindow.Graph.append(Graph(txt, stx,sty ,enx,eny))
    def OnDrawlReactions( widget, cr):
        #MyWindow.create_frame_beam(widget, cr)
        p = widget.get_allocation()
        wndh = p.height
        wndp = p.width
        coor = MyWindow.create_frame_beam(widget, cr)
        sig = "Reactions in Kilonewtons"
        cr.set_source_rgb(0.2, 0.0, 0)
        cr.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
        cr.move_to((p.width - dx) / 2, 20)
        cr.show_text(sig)
        uniquecoords = DynamicArray()
        e=0

        for k in range(0, len(MyWindow.beams)):
            beamstartnode = MyWindow.beams[k].StartNode
            beamendnode = MyWindow.beams[k].EndNode
            if MyWindow.beams[k].StartNode.find("SPRING") > -1:

                flag1=False
                flag2=False
                for ee in range(len(coor)):
                    if coor[ee].StartNode==beamendnode:
                        flag1=True
                    if coor[ee].EndNode==beamendnode:
                        flag2=True
                    if flag1 or flag2: break
                if flag1:
                    x1 = coor[ee].X1
                    y1 = coor[ee].Y1
                    flag=False
                    for e1 in range(0, len(uniquecoords)):
                        if uniquecoords[e1].X==x1 and uniquecoords[e1].Y==y1:
                            flag=True
                            break
                    if not flag:
                        uniquecoords.append(UniqueNode(MyWindow.beams[k].StartNode,MyWindow.beams[k].EndNode,MyWindow.beams[k].xl,x1,y1))
                if flag2:
                    x2 = coor[ee].X2
                    y2 = coor[ee].Y2
                    flag = False
                    for e1 in range(0, len(uniquecoords)):
                        if uniquecoords[e1].X == x2 and uniquecoords[e1].Y == y2:
                            flag = True
                            break
                    if not flag:
                        uniquecoords.append(UniqueNode(MyWindow.beams[k].StartNode,MyWindow.beams[k].EndNode,MyWindow.beams[k].xl, x2, y2))
        txtQ = "{:.2f}"
        txtN = "{:.2f}"
        for ee in range(0,len(uniquecoords)):
            try:
                k1= MyWindow.displacementsindex.index(3*MyWindow.findobject(MyWindow,uniquecoords[ee].StartNode,MyWindow.nodes)+1)
                tripl=np.zeros((3))
                tripl[0]=0
                tripl[1] = MyWindow.externalforces[MyWindow.displacementsindex[k1] ]
                #tripl[2] = MyWindow.externalforces[MyWindow.displacementsindex[k1] + 1]
                #if math.fabs(tripl[1])>=1e-3:
                if tripl[1] > 0.0:
                    MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y, 0.0,txtQ.format(math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]]/1000.0)))
                else:
                    MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y, math.pi, txtQ.format(
                        math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
            except ValueError:
                try:
                    k1 = MyWindow.displacementsindex.index(
                        3 * MyWindow.findobject(MyWindow, uniquecoords[ee].EndNode, MyWindow.nodes)+1 )
                    tripl = np.zeros((3))
                    #tripl[0] = MyWindow.externalforces[MyWindow.displacementsindex[k1] - 1]
                    tripl[0]=0
                    tripl[1] = MyWindow.externalforces[MyWindow.displacementsindex[k1]]
                   # if math.fabs(tripl[1]) >= 1e-3:
                    if tripl[1]>0.0:
                        MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y,
                                         math.pi/2.0, txtQ.format(
                                math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
                    else:
                        MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y,
                                         -math.pi / 2.0, txtQ.format(
                                math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
                except ValueError:
                    pass
        for ee in range(0, len(uniquecoords)):
                try:
                    k1 = MyWindow.displacementsindex.index(
                        3 * MyWindow.findobject(MyWindow, uniquecoords[ee].StartNode, MyWindow.nodes) )
                    tripl = np.zeros((3))
                    tripl[1] = 0
                    tripl[0] = MyWindow.externalforces[MyWindow.displacementsindex[k1]]
                    #if math.fabs(tripl[0]) >= 1e-3:
                    #if tripl[0]<0.0:
                      #  MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y,
                     #                    math.pi/2.0, txtN.format(
                     #           math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
                    #else:
                      #  MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y,
                      #                   -math.pi / 2.0, txtN.format(
                      #          math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
                        # tripl[2] = MyWindow.externalforces[MyWindow.displacementsindex[k1] + 1]
                except ValueError:
                    pass
        #           try:
                       # k1 = MyWindow.displacementsindex.index(
                      #      3 * MyWindow.findobject(MyWindow, uniquecoords[ee].EndNode, MyWindow.nodes) )
                      #  tripl = np.zeros((3))
                     #   tripl[1]=0
                     #   tripl[0] = MyWindow.externalforces[MyWindow.displacementsindex[k1]]
                       # if math.fabs(tripl[0]) >= 1e-3:
                     #   if tripl[0]<0.0:
                      #      MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y,
                     #                        0.0, txtN.format(
                     #               math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
                        #else:
                     #       MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y,
                     #                        math.pi, txtN.format(
                      #              math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
                        # tripl[2] = MyWindow.externalforces[MyWindow.displacementsindex[k1] + 1]
                #except ValueError:
                 #       pass
        uniquecoords=[]
        for k in range(0,len(MyWindow.displacementsindex)):
            nodename = MyWindow.nodes[int(MyWindow.displacementsindex[k]/3)]
            if (nodename.name.find("SPRING")>-1):
                continue
            else:
                nodeindex = MyWindow.findobject(MyWindow, nodename.name, MyWindow.nodes)
                if ((MyWindow.displacementsindex[k] ==nodeindex* 3) or (MyWindow.displacementsindex[k] ==nodeindex* 3+1)) :
                    for e in range(0, len(MyWindow.beams)):
                        if MyWindow.beams[e].StartNode.find("SPRING") == -1:
                            flag1 = False
                            flag2 = False
                            for ee in range(len(coor)):
                                if coor[ee].StartNode == nodename.name:
                                    flag1 = True
                                if coor[ee].EndNode == nodename.name:
                                    flag2 = True
                                if flag1 or flag2: break
                            if flag1:
                                x1 = coor[ee].X1
                                y1 = coor[ee].Y1
                                flag = False
                                for e1 in range(0, len(uniquecoords)):
                                    if uniquecoords[e1].X == x1 and uniquecoords[e1].Y == y1:
                                        flag = True
                                        break
                                if  not flag:
                                    uniquecoords.append(
                                        UniqueNode(coor[ee].StartNode, coor[ee].EndNode,
                                                   math.atan2(MyWindow.beams[e].yl,MyWindow.beams[e].xl), x1, y1))
                            if flag2:
                                x2 = coor[ee].X2
                                y2 = coor[ee].Y2
                                flag = False
                                for e1 in range(0, len(uniquecoords)):
                                    if uniquecoords[e1].X == x2 and uniquecoords[e1].Y == y2:
                                        flag = True
                                        break
                                if not flag:
                                    uniquecoords.append(
                                        UniqueNode(coor[ee].StartNode, coor[ee].EndNode,
                                                   math.atan2(MyWindow.beams[e].yl,MyWindow.beams[e].xl), x2, y2))
        for ee in range(0,len(uniquecoords)):
            try:
                k1= MyWindow.displacementsindex.index(3*MyWindow.findobject(MyWindow,uniquecoords[ee].StartNode,MyWindow.nodes))
                tripl=np.zeros((3))
                tripl[0]=0
                tripl[1] = MyWindow.externalforces[MyWindow.displacementsindex[k1] ]
                #tripl[2] = MyWindow.externalforces[MyWindow.displacementsindex[k1] + 1]
                #if math.fabs(tripl[1])>=1e-3:
                if tripl[1] > 0.0:
                    MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y, 0.0,txtQ.format(math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]]/1000.0)))
                else:
                    MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y, math.pi, txtQ.format(
                        math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
            except ValueError:
                try:
                    k1 = MyWindow.displacementsindex.index(
                        3 * MyWindow.findobject(MyWindow, uniquecoords[ee].EndNode, MyWindow.nodes) )
                    tripl = np.zeros((3))
                    #tripl[0] = MyWindow.externalforces[MyWindow.displacementsindex[k1] - 1]
                    tripl[0]=0
                    tripl[1] = MyWindow.externalforces[MyWindow.displacementsindex[k1]]
                   # if math.fabs(tripl[1]) >= 1e-3:
                    if tripl[1]>0.0:
                        MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y,
                                         math.pi/2.0, txtQ.format(
                                math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
                    else:
                        MyWindow.forceup(MyWindow, cr, uniquecoords[ee].X, uniquecoords[ee].Y,
                                         -math.pi / 2.0, txtQ.format(
                                math.fabs(MyWindow.externalforces[MyWindow.displacementsindex[k1]] / 1000.0)))
                except ValueError:
                    pass




    def OnDrawlLoads( widget, cr):
       # MyWindow.create_frame_beam(widget, cr)
        p = widget.get_allocation()
        wndh = p.height
        wndp = p.width
        coor = MyWindow.create_frame_beam(widget, cr)
        sig = "Loads in Kilonewtons"
        cr.set_source_rgb(0.2, 0.0, 0)
        cr.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
        cr.move_to((p.width - dx) / 2, 20)
        cr.show_text(sig)
        #MyWindow.forceup(MyWindow,cr,12)

    #            cr.move_to(x1 + 0 * s, y1 + 0 * c)

 #           cr.line_to(x1 - MyWindow.beamunit[e].M1 * MyWindow.scale*(wndp/wndh) * s,
          #             y1 + MyWindow.beamunit[e].M1 * MyWindow.scale*(wndp/wndh) * c)
 #           cr.stroke()
  #          cr.move_to(x2 + 0 * s, y2 + 0 * c)
  #          cr.line_to(x2 - MyWindow.beamunit[e].M2 * MyWindow.scale*(wndp/wndh) * s,
  #                     y2 + MyWindow.beamunit[e].M2 * MyWindow.scale*(wndp/wndh) * c)
  #          cr.stroke()
  #          cr.move_to(x1 - MyWindow.beamunit[e].M1 * MyWindow.scale*(wndp/wndh) * s,
  #                     y1 + MyWindow.beamunit[e].M1 * MyWindow.scale*(wndp/wndh) * c)
  #          cr.line_to(x2 - MyWindow.beamunit[e].M2 * MyWindow.scale*(wndp/wndh) * s,
  #                     y2 + MyWindow.beamunit[e].M2 * MyWindow.scale*(wndp/wndh) * c)
  #          cr.stroke()
  #          cr.save()

    def OnDrawDisplacements( widget, cr):
        #MyWindow.create_frame_beam(widget, cr)
        p = widget.get_allocation()
        wndh = p.height
        wndp = p.width
        coor = MyWindow.create_frame_beam(widget, cr)
        sig = "Displacements in mm (local beam)"
        cr.set_source_rgb(0.2, 0.0, 0)
        cr.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
        cr.move_to((p.width - dx) / 2, 20)
        cr.show_text(sig)
        for a in range(0, len(MyWindow.nodes)):
            if MyWindow.nodes[a].name.find("SPRING") > -1:
                continue
            ind = 0
            findindex = []
            while True:
                try:
                    ind = MyWindow.cos.index(MyWindow.nodes[a].name, ind, len(MyWindow.cos))
                    findindex.append(ind)
                    ind += 1
                except ValueError as error:
                    break
            if ((len(findindex) == 1)):


                beamname = MyWindow.beams[int(findindex[0]/2)].name
                # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
                beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
                beamstartnode = MyWindow.beams[beamnameindex].StartNode
                if beamstartnode.find("SPRING") > -1:
                    continue
                xl = MyWindow.beams[beamnameindex].xl
                yl = MyWindow.beams[beamnameindex].yl
                localdisplacements = np.zeros(6)
                globaldisplacements = np.zeros(6)
                transf = np.zeros((6, 6))

                lbeam = math.sqrt(xl * xl + yl * yl)
                c = xl / lbeam
                s = yl / lbeam
                transf[0][0] = c
                transf[0][1] = s
                transf[1][0] = -s
                transf[1][1] = c
                transf[2][2] = 1.0
                transf[3][3] = c
                transf[3][4] = s
                transf[4][3] = -s
                transf[4][4] = c
                transf[5][5] = 1.0

                nodeindex = MyWindow.findobject(MyWindow, MyWindow.nodes[a].name, MyWindow.nodes)
                cr.set_source_rgb(0.0, 0.2, 0)

                x1 = coor[beamnameindex].X1
                x2 = coor[beamnameindex].X2
                y1 = coor[beamnameindex].Y1
                y2 = coor[beamnameindex].Y2
                c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                stn = MyWindow.findobject(MyWindow, coor[beamnameindex].StartNode, MyWindow.nodes)
                enn = MyWindow.findobject(MyWindow, coor[beamnameindex].EndNode, MyWindow.nodes)
                globaldisplacements[0] = MyWindow.alldisplacements[MyWindow.perm.index(stn) * 3]
                globaldisplacements[1] = MyWindow.alldisplacements[MyWindow.perm.index(stn) * 3 + 1]
                globaldisplacements[2] = MyWindow.alldisplacements[MyWindow.perm.index(stn) * 3 + 2]
                globaldisplacements[3] = MyWindow.alldisplacements[MyWindow.perm.index(enn) * 3]
                globaldisplacements[4] = MyWindow.alldisplacements[MyWindow.perm.index(enn) * 3 + 1]
                globaldisplacements[5] = MyWindow.alldisplacements[MyWindow.perm.index(enn) * 3 + 2]
                localdisplacements = np.dot(transf, globaldisplacements)
                if MyWindow.beams[beamnameindex].StartNode == MyWindow.nodes[a].name:
                    M1 = localdisplacements[1] * 1000
                    txtDispl = "{:.3f}"
                    sig = txtDispl.format(M1)
                    cr.set_font_size(MyWindow.font)
                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                    cr.save()
                    cr.translate(x1, y1)
                    cr.rotate(math.atan2((y2 - y1), (x2 - x1)) + math.pi / 2)
                    cr.move_to(6, 0)
                    cr.set_font_size(MyWindow.font)

                    cr.show_text(sig)
                    cr.restore()
                    p1 = cr.text_extents(sig)
                    c1 = math.cos(math.pi / 2 + math.atan2(y2 - y1, x2 - x1))
                    s1 = math.sin(math.pi / 2 + math.atan2(y2 - y1, x2 - x1))
                    stx = x1 + 6 * c1 + p1.width * c1
                    sty = y1 + 6 * s1 - p1.height * c1
                    enx = x1 + 6 * c1 + p1.height * s1
                    eny = y1 + 6 * s1 + p1.width * s1
                    if enx < stx:
                        temp = enx
                        enx = stx
                        stx = temp
                    if eny < sty:
                        temp = eny
                        eny = sty
                        sty = temp
                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
            if MyWindow.beams[beamnameindex].EndNode == MyWindow.nodes[a].name:
                    M2 = localdisplacements[4] * 1000
                    txtDispl = "{:.3f}"
                    sig = txtDispl.format(M1)
                    cr.set_font_size(MyWindow.font)
                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                    cr.save()
                    cr.translate(x2, y2)
                    cr.rotate(math.atan2((y2 - y1), (x2 - x1)) + math.pi / 2)
                    cr.move_to(6, 0)
                    cr.set_font_size(MyWindow.font)

                    cr.show_text(sig)
                    cr.restore()
                    p1 = cr.text_extents(sig)
                    c1 = math.cos(math.pi / 2 + math.atan2(y2 - y1, x2 - x1))
                    s1 = math.sin(math.pi / 2 + math.atan2(y2 - y1, x2 - x1))
                    stx = x2 + 6 * c1 + p1.width * c1
                    sty = y2 + 6 * s1 - p1.height * c1
                    enx = x2 + 6 * c1 + p1.height * s1
                    eny = y2 + 6 * s1 + p1.width * s1
                    if enx < stx:
                        temp = enx
                        enx = stx
                        stx = temp
                    if eny < sty:
                        temp = eny
                        eny = sty
                        sty = temp
                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
            else:
                indd = []
                beamname = MyWindow.beams[int(findindex[0] / 2)].name
                # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
                beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
                beamstartnode = MyWindow.beams[beamnameindex].StartNode
                if beamstartnode.find("SPRING") > -1:
                    continue
                xl = MyWindow.beams[beamnameindex].xl
                yl = MyWindow.beams[beamnameindex].yl
                localdisplacements = np.zeros(6)
                globaldisplacements = np.zeros(6)
                transf = np.zeros((6, 6))

                lbeam = math.sqrt(xl * xl + yl * yl)
                c = xl / lbeam
                s = yl / lbeam
                transf[0][0] = c
                transf[0][1] = s
                transf[1][0] = -s
                transf[1][1] = c
                transf[2][2] = 1.0
                transf[3][3] = c
                transf[3][4] = s
                transf[4][3] = -s
                transf[4][4] = c
                transf[5][5] = 1.0

                nodeindex = MyWindow.findobject(MyWindow, MyWindow.nodes[a].name, MyWindow.nodes)
                cr.set_source_rgb(0.0, 0.2, 0)

                x1 = coor[beamnameindex].X1
                x2 = coor[beamnameindex].X2
                y1 = coor[beamnameindex].Y1
                y2 = coor[beamnameindex].Y2
                c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                stn = MyWindow.findobject(MyWindow, coor[beamnameindex].StartNode, MyWindow.nodes)
                enn = MyWindow.findobject(MyWindow, coor[beamnameindex].EndNode, MyWindow.nodes)
                globaldisplacements[0] = MyWindow.alldisplacements[MyWindow.perm.index(stn) * 3]
                globaldisplacements[1] = MyWindow.alldisplacements[MyWindow.perm.index(stn) * 3 + 1]
                globaldisplacements[2] = MyWindow.alldisplacements[MyWindow.perm.index(stn) * 3 + 2]
                globaldisplacements[3] = MyWindow.alldisplacements[MyWindow.perm.index(enn) * 3]
                globaldisplacements[4] = MyWindow.alldisplacements[MyWindow.perm.index(enn) * 3 + 1]
                globaldisplacements[5] = MyWindow.alldisplacements[MyWindow.perm.index(enn) * 3 + 2]
                localdisplacements = np.dot(transf, globaldisplacements)
                if MyWindow.beams[beamnameindex].StartNode == MyWindow.nodes[a].name:
                    M1 = localdisplacements[1] * 1000
                    txtDispl = "{:.3f}"
                    sig = txtDispl.format(M1)
                    cr.set_font_size(MyWindow.font)
                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                    cr.save()
                    cr.translate(x1, y1)
                    cr.rotate(math.atan2((y2 - y1), (x2 - x1)) + math.pi / 2)
                    cr.move_to(6, 0)
                    cr.set_font_size(MyWindow.font)

                    cr.show_text(sig)
                    cr.restore()
                    p1 = cr.text_extents(sig)
                    c1 = math.cos(math.pi / 2 + math.atan2(y2 - y1, x2 - x1))
                    s1 = math.sin(math.pi / 2 + math.atan2(y2 - y1, x2 - x1))
                    stx = x1 + 6 * c1 + p1.width * c1
                    sty = y1 + 6 * s1 - p1.height * c1
                    enx = x1 + 6 * c1 + p1.height * s1
                    eny = y1 + 6 * s1 + p1.width * s1
                    if enx < stx:
                        temp = enx
                        enx = stx
                        stx = temp
                    if eny < sty:
                        temp = eny
                        eny = sty
                        sty = temp
                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))

            if MyWindow.beams[beamnameindex].EndNode == MyWindow.nodes[a].name:
                M2 = localdisplacements[4] * 1000
                txtDispl = "{:.3f}"
                sig = txtDispl.format(M2)
                cr.set_font_size(MyWindow.font)
                (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                cr.save()
                cr.translate(x2, y2)
                cr.rotate(math.atan2((y2 - y1), (x2 - x1)) + math.pi / 2)
                cr.move_to(6, 0)
                cr.set_font_size(MyWindow.font)

                cr.show_text(sig)
                cr.restore()
                p1 = cr.text_extents(sig)
                c1 = math.cos(math.pi / 2 + math.atan2(y2 - y1, x2 - x1))
                s1 = math.sin(math.pi / 2 + math.atan2(y2 - y1, x2 - x1))
                stx = x2 + 6 * c1 + p1.width * c1
                sty = y2 + 6 * s1 - p1.height * c1
                enx = x2 + 6 * c1 + p1.height * s1
                eny = y2 + 6 * s1 + p1.width * s1
                if enx < stx:
                    temp = enx
                    enx = stx
                    stx = temp
                if eny < sty:
                    temp = eny
                    eny = sty
                    sty = temp
                MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))


    def OnDrawlM( widget, cr):
    #def OnDrawlM(guiobj, widget, cr):
        #guiobj.create_frame_beam(widget, cr)
        #MyWindow.create_frame_beam(widget, cr)
        p = widget.get_allocation()
        wndh = p.height
        wndp = p.width
        #coor = guiobj.create_frame_beam(widget, cr)

        coor = MyWindow.create_frame_beam(widget, cr)

        cr.set_line_width(1)
        sig = "Beam Moments in Kilonewton meters"
        cr.set_source_rgb(0.2, 0.0, 0)
        cr.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
        cr.move_to((p.width - dx) / 2, 20)
        cr.show_text(sig)


        fl = True
        for e in range(0, len(MyWindow.beamunit)):
            if (math.fabs(MyWindow.beamunit[e].M1) > 1e-5 or math.fabs(MyWindow.beamunit[e].M2) >1e-5):
                fl = False
                break
        if fl: return

        for a in range(0, len(MyWindow.nodes)):
            if MyWindow.nodes[a].name.find("SPRING") > -1:
                continue
            ind = 0
            findindex = []
            while True:
                try:
                    nam1 = MyWindow.nodes[a].name
                    if "_" in nam1[-3:]:
                        nam1 = nam1[:-3]

                    ind = MyWindow.cos.index(nam1, ind, len(MyWindow.cos))
                    # ind = MyWindow.cos.index(MyWindow.nodes[a].name, ind, len(MyWindow.cos))
                    findindex.append(ind)
                    ind += 1
                except ValueError as error:
                    break
            if ((len(findindex) == 1)):
                nodeindex = MyWindow.findobject(MyWindow, MyWindow.nodes[a].name, MyWindow.nodes)
                cr.set_source_rgb(0.0, 0.2, 0)
                beamindex = int(findindex[0] / 2)
                x1 = coor[int(findindex[0] / 2)].X1
                y1 = coor[int(findindex[0] / 2)].Y1
                x2 = coor[int(findindex[0] / 2)].X2
                y2 = coor[int(findindex[0] / 2)].Y2
                # gon = math.ataQ2(MyWindow.beams[int(findindex[l] / 2)].yl, MyWindow.beams[int(findindex[l] / 2)].xl)
                c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))

                # x1 = coor[beamindex].X1
                # x2 = coor[beamindex].X2
                # y1 = coor[beamindex].Y1
                # y2 = coor[beamindex].Y2
                # gon = math.ataQ2(MyWindow.beams[int(findindex[0] / 2)].xl, MyWindow.beams[int(findindex[0] / 2)].yl)

                M1x = -MyWindow.beamunit[int(findindex[0] / 2)].M1 * MyWindow.scale * (wndp / wndh) * s
                M1y = - MyWindow.beamunit[int(findindex[0] / 2)].M1 * MyWindow.scale * (wndp / wndh) * c
                M2x = - MyWindow.beamunit[int(findindex[0] / 2)].M2 * MyWindow.scale * (wndp / wndh) * s
                M2y = -MyWindow.beamunit[int(findindex[0] / 2)].M2 * MyWindow.scale * (wndp / wndh) * c
                #           y2 + MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh) * c)

                txtM = "{:.2f}"
                if MyWindow.beams[beamindex].StartNode == MyWindow.nodes[a].name:
                    cr.move_to(x1 + 0 * s, y1 + 0 * c)


                    a1x = MyWindow.beamunit[beamindex].M1 * MyWindow.scale * (wndp / wndh) * s
                    a1y = MyWindow.beamunit[beamindex].M1 * MyWindow.scale * (wndp / wndh) * c

                    cr.line_to(x1 - MyWindow.beamunit[beamindex].M1 * MyWindow.scale * (wndp / wndh) * s,
                               y1 + MyWindow.beamunit[beamindex].M1 * MyWindow.scale * (wndp / wndh) * c)


                    cr.stroke()
                    cr.save()
                    M1 = MyWindow.beamunit[beamindex].M1 * MyWindow.maxM
                    sig = txtM.format(M1 / 1000.0)
                    cr.set_font_size(MyWindow.font)
                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                    p1 = cr.text_extents(sig)
                    gon = math.atan2(-c, s)

                    c = math.cos(gon)
                    s = math.sin(gon)

                    cr.translate(x1 - MyWindow.beamunit[beamindex].M1 * MyWindow.scale * (wndp / wndh) * c,
                                 y1 - MyWindow.beamunit[beamindex].M1 * MyWindow.scale * (wndp / wndh) * s)

                    cr.move_to(0, 0)
                    cr.rotate(gon)
                    # gon = math.ataM2(M1y, M1x)
                    # c = math.cos(gon)
                    # s = math.sin(gon)

                    cr.set_font_size(MyWindow.font)
                    cr.show_text(sig)

                    stx = x1 - a1x
                    sty = y1 + a1y
                    enx = stx + p1.width * c + p1.height * s
                    eny = sty - p1.height * c + p1.width * s

                    cr.restore()

                if MyWindow.beams[beamindex].EndNode == MyWindow.nodes[a].name:
                    cr.move_to(x2 + 0 * s, y2 + 0 * c)
                    cr.line_to(x2 - MyWindow.beamunit[beamindex].M2 * MyWindow.scale * (wndp / wndh) * s,
                               y2 + MyWindow.beamunit[beamindex].M2 * MyWindow.scale * (wndp / wndh) * c)

                    cr.stroke()

                    cr.set_font_size(MyWindow.font)
                    p1 = cr.text_extents(sig)
                    cr.save()
                    a2x = + MyWindow.beamunit[beamindex].M2 * MyWindow.scale * (wndp / wndh) * s
                    a2y =  MyWindow.beamunit[beamindex].M2 * MyWindow.scale * (wndp / wndh) * c
                    M2 = MyWindow.beamunit[beamindex].M2 * MyWindow.maxM
                    sig = txtM.format(M2 / 1000.0)

                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)

                    cr.translate(x2 - MyWindow.beamunit[beamindex].M2 * MyWindow.scale * (wndp / wndh) * s,
                                 y2 + MyWindow.beamunit[beamindex].M2 * MyWindow.scale * (wndp / wndh) * c)

                    cr.rotate(math.atan2(c,s))
                    gon = math.atan2(c,s)
                    c = math.cos(gon)
                    s = math.sin(gon)
                    cr.move_to(0, 0)
                    cr.set_font_size(MyWindow.font)
                    cr.show_text(sig)
                    stx = x2 - a2x
                    sty = y2 + a2y

                    enx = stx + p1.width * c + p1.height * s
                    eny = sty + p1.width * s + p1.height * c

                    cr.restore()
                if enx < stx:
                    temp = enx
                    enx = stx
                    stx = temp
                if eny < sty:
                    temp = eny
                    eny = sty
                    sty = temp

                #cr.move_to(stx, sty)
                #cr.line_to(enx, eny)
                #cr.stroke()
                MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
            else:
                indd = []
                for l in range(0, len(findindex)):
                    x1 = coor[int(findindex[l] / 2)].X1
                    y1 = coor[int(findindex[l] / 2)].Y1
                    x2 = coor[int(findindex[l] / 2)].X2
                    y2 = coor[int(findindex[l] / 2)].Y2
                    # gon = math.ataM2(MyWindow.beams[int(findindex[l] / 2)].yl, MyWindow.beams[int(findindex[l] / 2)].xl)
                    c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                    s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                    gon = math.atan2(s, c)
                    M1x = MyWindow.beamunit[int(findindex[l] / 2)].M1 * MyWindow.scale * (wndp / wndh) * s
                    M1y =  MyWindow.beamunit[int(findindex[l] / 2)].M1 * MyWindow.scale * (wndp / wndh) * c
                    M2x =  MyWindow.beamunit[int(findindex[l] / 2)].M2 * MyWindow.scale * (wndp / wndh) * s
                    M2y = MyWindow.beamunit[int(findindex[l] / 2)].M2 * MyWindow.scale * (wndp / wndh) * c
                    #           y2 + MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh) * c)

                    if (findindex[l] % 2 == 0):
                        indd.append(['S', x1, y1, M1x, M1y, gon])
                    else:
                        indd.append(['E', x2, y2, M2x, M2y, gon])
                # indd=sorted(indd,key=lambda x:x[5])
                l1 = 0
                cou = 0
                indtodelete = []
                while l1 < len(indd):
                    x1 = coor[int(findindex[l1] / 2)].X1
                    y1 = coor[int(findindex[l1] / 2)].Y1
                    x2 = coor[int(findindex[l1] / 2)].X2
                    y2 = coor[int(findindex[l1] / 2)].Y2

                    lM = math.pow(math.pow(indd[l1][3], 2.0) + math.pow(indd[l1][4], 2.0), 0.5)

                    maxelement = l1
                    cr.save()
                    txtM = "{:.2f}"
                    if (indd[maxelement][0] == "S"):
                        M1 = MyWindow.beamunit[int(findindex[maxelement] / 2)].M1 * MyWindow.maxM
                        sig = txtM.format(M1 / 1000.0)
                        c1 = (indd[maxelement][3]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        s1 = (indd[maxelement][4]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        stx = indd[maxelement][1] - indd[maxelement][3]
                        sty = indd[maxelement][2] + indd[maxelement][4]
                        p1 = cr.text_extents(sig)
                        enx = stx + p1.width * c1 + p1.height * s1
                        eny = sty - p1.height * c1 + p1.width * s1
                    else:
                        M2 = MyWindow.beamunit[int(findindex[maxelement] / 2)].M2 * MyWindow.maxM
                        sig = txtM.format(M2 / 1000.0)
                        p1 = cr.text_extents(sig)
                        c1 = (indd[maxelement][3]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        s1 = (indd[maxelement][4]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        stx = indd[maxelement][1] - indd[maxelement][3]
                        sty = indd[maxelement][2] + indd[maxelement][4]
                        enx = stx + p1.width * c1 + p1.height * s1
                        eny = sty - p1.height * c1 + p1.width * s1
                    if enx < stx:
                        temp = enx
                        enx = stx
                        stx = temp
                    if eny < sty:
                        temp = eny
                        eny = sty
                        sty = temp

                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                    cr.translate(indd[maxelement][1] - indd[maxelement][3],
                                 indd[maxelement][2] + indd[maxelement][4])
                    cr.set_font_size(MyWindow.font)

                    #cr.rotate(math.atan2(indd[maxelement][4], indd[maxelement][3]))
                    cr.move_to(0, 0)
                    #cr.rotate(math.atan2(s1,c1))
                    cr.rotate(math.atan2(indd[maxelement][4],indd[maxelement][3]))
                    cr.set_font_size(MyWindow.font)
                    cr.show_text(sig)

                    cr.restore()
                    #cr.move_to(stx, sty)
                    #cr.line_to(enx, eny)
                    #cr.stroke()


                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))

                    l2 = l1 + 1
                    gon = indd[l1][5]
                    indtodelete.append(l1)

                    while l2 < len(indd):
                        x1 = coor[int(findindex[l2] / 2)].X1
                        y1 = coor[int(findindex[l2] / 2)].Y1
                        x2 = coor[int(findindex[l2] / 2)].X2
                        y2 = coor[int(findindex[l2] / 2)].Y2
                        if math.fabs(indd[l2][5] - gon) < 1e-5:
                            indtodelete.append(l2)
                            if math.fabs((math.pow(math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0),
                                                   0.5) - lM)) > 0.1:
                                cr.save()
                                txtM = "{:.2f}"
                                if (indd[l2][0] == "S"):
                                    M1 = MyWindow.beamunit[int(findindex[l2] / 2)].M1 * MyWindow.maxM
                                    sig = txtM.format(M1 / 1000.0)
                                else:
                                    M2 = MyWindow.beamunit[int(findindex[l2] / 2)].M2 * MyWindow.maxM
                                    sig = txtM.format(M2 / 1000.0)
                                (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                                p1 = cr.text_extents(sig)
                                cr.translate(indd[l2][1] - indd[l2][3],
                                             indd[l2][2] + indd[l2][4])
                                # cr.translate(x1 - MyWindow.beamunit[e].M1 * MyWindow.scale*(wndp/wndh) * s,
                                #             y1 + MyWindow.beamunit[e].M1 * MyWindow.scale*(wndp/wndh) * c)
                                cr.set_font_size(MyWindow.font)
                                cr.rotate(math.atan2(indd[l2][4], indd[l2][3]))
                                cr.move_to(0, 0)
                                cr.set_font_size(MyWindow.font)
                                cr.show_text(sig)
                                cr.restore()
                                if (indd[l2][0] == "S"):
                                    c1 = -(indd[l2][3]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    s1 = (indd[l2][4]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    stx = indd[l2][1] - indd[l2][3]
                                    sty = indd[l2][2] + indd[l2][4]
                                    enx = stx + p1.width * c1 + p1.height * s1
                                    eny = sty - p1.height * c1 + p1.width * s1
                                    if enx < stx:
                                        temp = enx
                                        enx = stx
                                        stx = temp
                                    if eny < sty:
                                        temp = eny
                                        eny = sty
                                        sty = temp


                                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))

                                else:

                                    c1 = (indd[l2][3]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    s1 = (indd[l2][4]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    stx = indd[l2][1] - indd[l2][3]
                                    sty = indd[l2][2] + indd[l2][4]
                                    enx = stx + p1.width * c1 + p1.height * s1
                                    eny = sty - p1.height * c1 + p1.width * s1
                                    if enx < stx:
                                        temp = enx
                                        enx = stx
                                        stx = temp
                                    if eny < sty:
                                        temp = eny
                                        eny = sty
                                        sty = temp
                                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))


                            if ((math.pow(math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0), 0.5) - lM) > 0.1):
                                maxelement = l2
                                lM = math.pow(math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0),
                                              0.5)
                        l2 += 1
                    x1 = coor[int(findindex[maxelement] / 2)].X1
                    x2 = coor[int(findindex[maxelement] / 2)].X2
                    y1 = coor[int(findindex[maxelement] / 2)].Y1
                    y2 = coor[int(findindex[maxelement] / 2)].Y2
                    c = (indd[maxelement][3]) / math.sqrt(
                        math.pow((indd[maxelement][3]), 2.0) + math.pow((indd[maxelement][4]), 2.0))
                    s = (indd[maxelement][4]) / math.sqrt(
                        math.pow((indd[maxelement][3]), 2.0) + math.pow((indd[maxelement][4]), 2.0))
                    if indd[maxelement][0] == "S":
                        cr.move_to(x1, y1)
                        cr.line_to(x1 - indd[maxelement][3], y1 + indd[maxelement][4])
                    else:
                        cr.move_to(x2, y2)
                        cr.line_to(x2 - indd[maxelement][3], y2 + indd[maxelement][4])
                    cr.stroke()

                    maxeleold = maxelement
                    if (len(indd) == 2):
                        if maxelement == 1:
                            maxelement = 0
                        else:
                            maxelement = 1

                        # case of opposite direction
                        if ((indd[maxeleold][4] * indd[maxelement][4] <= 0) and (
                                indd[maxeleold][3] * indd[maxelement][3] <= 0)):
                            if indd[maxeleold][0] == "S":
                                cr.move_to(x1, y1)
                                cr.line_to(x1 - indd[maxelement][3], y1 + indd[maxelement][4])
                            else:
                                cr.move_to(x2, y2)
                                cr.line_to(x2 - indd[maxelement][3], y2 + indd[maxelement][4])
                            cr.stroke()
                    l3 = len(indtodelete) - 1
                    while l3 >= 0:
                        if (len(indd) > 0):
                            indd.pop(indtodelete[l3])
                            findindex.pop(indtodelete[l3])
                        if (len(indtodelete) > 0):
                            indtodelete.pop(l3)
                        l3 -= 1
                        l1 -= 1
                    if len(indd) == 0:
                        break
                    l1 += 1

        for e in range(0, len(coor)):
            cr.set_source_rgb(0.0, 0.2, 0)
            x1 = coor[e].X1
            x2 = coor[e].X2
            y1 = coor[e].Y1
            y2 = coor[e].Y2
            c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            cr.move_to(x1 - MyWindow.beamunit[e].M1 * MyWindow.scale * (wndp / wndh) * s,
                       y1 + MyWindow.beamunit[e].M1 * MyWindow.scale * (wndp / wndh) * c)
            cr.line_to(x2 - MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh) * s,
                       y2 + MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh) * c)
            cr.stroke()

    def OnDrawlQ(widget, cr):
        coor = MyWindow.create_frame_beam(widget, cr)
        cr.set_line_width(1)
        p = widget.get_allocation()
        wndh = p.height
        wndp = p.width
        sig = "Shear forces in Kilonewtons"
        cr.set_source_rgb(0.2, 0.0, 0)
        cr.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
        cr.move_to((p.width - dx) / 2, 20)
        cr.show_text(sig)
        for a in range(0, len(MyWindow.nodes)):
            if MyWindow.nodes[a].name.find("SPRING") > -1:
                continue
            ind = 0
            findindex = []
            while True:
                try:
                    nam1 = MyWindow.nodes[a].name
                    if "_" in nam1[-3:]:
                        nam1 = nam1[:-3]

                    ind = MyWindow.cos.index(nam1, ind, len(MyWindow.cos))
                    #ind = MyWindow.cos.index(MyWindow.nodes[a].name, ind, len(MyWindow.cos))
                    findindex.append(ind)
                    ind += 1
                except ValueError as error:
                    break
            if ((len(findindex) == 1)):
                nodeindex = MyWindow.findobject(MyWindow, MyWindow.nodes[a].name, MyWindow.nodes)
                cr.set_source_rgb(0.0, 0.2, 0)
                beamindex = int(findindex[0] / 2)
                x1 = coor[int(findindex[0] / 2)].X1
                y1 = coor[int(findindex[0] / 2)].Y1
                x2 = coor[int(findindex[0] / 2)].X2
                y2 = coor[int(findindex[0] / 2)].Y2
                # gon = math.ataQ2(MyWindow.beams[int(findindex[l] / 2)].yl, MyWindow.beams[int(findindex[l] / 2)].xl)
                c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))

                #x1 = coor[beamindex].X1
                #x2 = coor[beamindex].X2
                #y1 = coor[beamindex].Y1
                #y2 = coor[beamindex].Y2
                #gon = math.ataQ2(MyWindow.beams[int(findindex[0] / 2)].xl, MyWindow.beams[int(findindex[0] / 2)].yl)
                gon =math.atan2(s,c)
                c = math.cos(gon)
                s = math.sin(gon)

                Q1x = -MyWindow.beamunit[int(findindex[0] / 2)].Q1 * MyWindow.scale * (wndp / wndh) * s
                Q1y =-  MyWindow.beamunit[int(findindex[0] / 2)].Q1 * MyWindow.scale * (wndp / wndh) * c
                Q2x = - MyWindow.beamunit[int(findindex[0] / 2)].Q2 * MyWindow.scale * (wndp / wndh) * s
                Q2y = -MyWindow.beamunit[int(findindex[0] / 2)].Q2 * MyWindow.scale * (wndp / wndh) * c
                #           y2 + MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh) * c)

                txtQ = "{:.2f}"
                if MyWindow.beams[beamindex].StartNode == MyWindow.nodes[a].name:
                    cr.move_to(x1 + 0 * s, y1 + 0 * c)
                    cr.line_to(x1 + MyWindow.beamunit[beamindex].Q1 * MyWindow.scale * (wndp / wndh) * s,
                               y1 - MyWindow.beamunit[beamindex].Q1 * MyWindow.scale * (wndp / wndh) * c)
                    a1x = MyWindow.beamunit[beamindex].Q1 * MyWindow.scale * (wndp / wndh) * s
                    a1y = - MyWindow.beamunit[beamindex].Q1 * MyWindow.scale * (wndp / wndh) * c
                    cr.stroke()
                    cr.save()
                    Q1 = MyWindow.beamunit[beamindex].Q1 * MyWindow.maxQ
                    sig = txtQ.format(Q1 / 1000.0)
                    cr.set_font_size(MyWindow.font)
                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                    p1 = cr.text_extents(sig)
                    cr.translate(x1 + MyWindow.beamunit[beamindex].Q1 * MyWindow.scale * (wndp / wndh) * s,
                                 y1 - MyWindow.beamunit[beamindex].Q1 * MyWindow.scale * (wndp / wndh) * c)

                    gon = math.atan2(c,s)
                    c = math.cos(gon)
                    s = math.sin(gon)
                    cr.rotate(gon)
                    # gon = math.ataQ2(Q1y, Q1x)
                    # c = math.cos(gon)
                    # s = math.sin(gon)
                    cr.move_to(0, 0)
                    cr.set_font_size(MyWindow.font)
                    cr.show_text(sig)

                    stx = x1+a1x
                    sty = y1+a1y
                    enx = stx - p1.width * c + p1.height * s
                    eny = sty + p1.height * c + p1.width * s
                    cr.restore()
                    if enx < stx:
                        temp = enx
                        enx = stx
                        stx = temp
                    if eny < sty:
                        temp = eny
                        eny = sty
                        sty = temp

                    #cr.move_to(stx, sty)
                    #cr.line_to(enx, eny)
                    #cr.stroke()

                if MyWindow.beams[beamindex].EndNode == MyWindow.nodes[a].name:
                    cr.move_to(x2 + 0 * s, y2 + 0 * c)
                    cr.line_to(x2 + MyWindow.beamunit[beamindex].Q2 * MyWindow.scale * (wndp / wndh) * s,
                               y2 - MyWindow.beamunit[beamindex].Q2 * MyWindow.scale * (wndp / wndh) * c)

                    cr.stroke()

                    cr.set_font_size(MyWindow.font)
                    p1 = cr.text_extents(sig)
                    cr.save()
                    a2x =  + MyWindow.beamunit[beamindex].Q2 * MyWindow.scale * (wndp / wndh) * s
                    a2y =  -MyWindow.beamunit[beamindex].Q2 * MyWindow.scale * (wndp / wndh) * c
                    Q2 = MyWindow.beamunit[beamindex].Q2 * MyWindow.maxQ
                    sig = txtQ.format(Q2 / 1000.0)

                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)

                    cr.translate(x2 + MyWindow.beamunit[beamindex].Q2 * MyWindow.scale * (wndp / wndh) * s,
                                 y2 - MyWindow.beamunit[beamindex].Q2 * MyWindow.scale * (wndp / wndh) * c)

                    gon = math.atan2(c,s)
                    cr.rotate(gon)

                    c = math.cos(gon)
                    s = math.sin(gon)
                    cr.move_to(0, 0)
                    cr.set_font_size(MyWindow.font)
                    cr.show_text(sig)
                    stx = x2+a2x
                    sty = y2+a2y
                    enx = stx - p1.width * c + p1.height * s
                    eny = sty + p1.width * s + p1.height * c

                    cr.restore()

                if enx < stx:
                    temp = enx
                    enx = stx
                    stx = temp
                if eny < sty:
                    temp = eny
                    eny = sty
                    sty = temp

                #cr.move_to(stx, sty)
                #cr.line_to(enx, eny)
                #cr.stroke()
                MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
            else:
                indd = []
                for l in range(0, len(findindex)):
                    x1 = coor[int(findindex[l] / 2)].X1
                    y1 = coor[int(findindex[l] / 2)].Y1
                    x2 = coor[int(findindex[l] / 2)].X2
                    y2 = coor[int(findindex[l] / 2)].Y2
                    #gon = math.ataQ2(MyWindow.beams[int(findindex[l] / 2)].yl, MyWindow.beams[int(findindex[l] / 2)].xl)
                    c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                    s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                    gon=math.atan2(s,c)
                    Q1x =- MyWindow.beamunit[int(findindex[l] / 2)].Q1 * MyWindow.scale * (wndp / wndh) * s
                    Q1y = - MyWindow.beamunit[int(findindex[l] / 2)].Q1 * MyWindow.scale * (wndp / wndh) * c
                    Q2x = - MyWindow.beamunit[int(findindex[l] / 2)].Q2 * MyWindow.scale * (wndp / wndh) * s
                    Q2y =- MyWindow.beamunit[int(findindex[l] / 2)].Q2 * MyWindow.scale * (wndp / wndh) * c
                    #           y2 + MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh) * c)

                    if (findindex[l] % 2 == 0):
                        indd.append(['S', x1, y1, Q1x, Q1y, gon])
                    else:
                        indd.append(['E', x2, y2, Q2x, Q2y, gon])
                # indd=sorted(indd,key=lambda x:x[5])
                l1 = 0
                cou = 0
                indtodelete = []
                while l1 < len(indd):
                    x1 = coor[int(findindex[l1] / 2)].X1
                    y1 = coor[int(findindex[l1] / 2)].Y1
                    x2 = coor[int(findindex[l1] / 2)].X2
                    y2 = coor[int(findindex[l1] / 2)].Y2

                    lM = math.pow(math.pow(indd[l1][3], 2.0) + math.pow(indd[l1][4], 2.0), 0.5)

                    maxelement = l1
                    cr.save()
                    txtQ = "{:.2f}"
                    if (indd[maxelement][0] == "S"):
                        Q1 = MyWindow.beamunit[int(findindex[maxelement] / 2)].Q1 * MyWindow.maxQ
                        sig = txtQ.format(Q1 / 1000.0)
                        c1 = (indd[maxelement][3]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        s1 = (indd[maxelement][4] )/ math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        stx = indd[maxelement][1] - indd[maxelement][3]
                        sty = indd[maxelement][2] + indd[maxelement][4]
                        p1 = cr.text_extents(sig)

                    else:
                        Q2 = MyWindow.beamunit[int(findindex[maxelement] / 2)].Q2 * MyWindow.maxQ
                        sig = txtQ.format(Q2 / 1000.0)
                        p1 = cr.text_extents(sig)
                        c1 = (indd[maxelement][3]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        s1 = (indd[maxelement][4]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        stx = indd[maxelement][1] - indd[maxelement][3]
                        sty = indd[maxelement][2] + indd[maxelement][4]

                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                    cr.translate(indd[maxelement][1] - indd[maxelement][3],
                                 indd[maxelement][2] + indd[maxelement][4])
                    cr.set_font_size(MyWindow.font)
                    gon=math.atan2(+ indd[maxelement][4],+ indd[maxelement][3])
                    cr.rotate(gon)
                    enx = stx + p1.width * c1 + p1.height * s1
                    eny = sty- p1.height * c1 + p1.width * s1


                    if enx < stx:
                        temp = enx
                        enx = stx
                        stx = temp
                    if eny < sty:
                        temp = eny
                        eny = sty
                        sty = temp

                    cr.move_to(0, 0)
                    cr.set_font_size(MyWindow.font)
                    cr.show_text(sig)

                    cr.restore()
                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
                    #cr.move_to(stx, sty)
                    #cr.line_to(enx, eny)
                    #cr.stroke()

                    l2 = l1 + 1
                    gon = indd[l1][5]
                    indtodelete.append(l1)

                    while l2 < len(indd):
                        x1 = coor[int(findindex[l2] / 2)].X1
                        y1 = coor[int(findindex[l2] / 2)].Y1
                        x2 = coor[int(findindex[l2] / 2)].X2
                        y2 = coor[int(findindex[l2] / 2)].Y2
                        if math.fabs(indd[l2][5] - gon) < 1e-5:
                            indtodelete.append(l2)
                            if math.fabs((math.pow(math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0),
                                                   0.5) - lM)) > 0.1:
                                cr.save()
                                txtQ = "{:.2f}"
                                if (indd[l2][0] == "S"):
                                    Q1 = MyWindow.beamunit[int(findindex[l2] / 2)].Q1 * MyWindow.maxQ
                                    sig = txtQ.format(Q1 / 1000.0)
                                else:
                                    Q2 = MyWindow.beamunit[int(findindex[l2] / 2)].Q2 * MyWindow.maxQ
                                    sig = txtQ.format(Q2 / 1000.0)
                                (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                                p1 = cr.text_extents(sig)
                                cr.translate(indd[l2][1] + indd[l2][3],
                                             indd[l2][2] + indd[l2][4])
                                # cr.translate(x1 - MyWindow.beamunit[e].Q1 * MyWindow.scale*(wndp/wndh) * s,
                                #             y1 + MyWindow.beamunit[e].Q1 * MyWindow.scale*(wndp/wndh) * c)
                                cr.set_font_size(MyWindow.font)
                                cr.rotate(math.atan2(indd[l2][4], indd[l2][3]))
                                cr.move_to(0, 0)
                                cr.set_font_size(MyWindow.font)
                                cr.show_text(sig)
                                cr.restore()
                                if (indd[l2][0] == "S"):
                                    c1 = (indd[l2][3]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    s1 = (indd[l2][4]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    stx = indd[l2][1] + indd[l2][3]
                                    sty = indd[l2][2] + indd[l2][4]
                                    enx = stx + p1.width * c1 + p1.height * s1
                                    eny = sty - p1.height * c1 + p1.width * s1
                                    if enx < stx:
                                        temp = enx
                                        enx = stx
                                        stx = temp
                                    if eny < sty:
                                        temp = eny
                                        eny = sty
                                        sty = temp

                                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
                                else:
                                    c1 = (indd[l2][3]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    s1 = (indd[l2][4]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    stx = indd[l2][1] + indd[l2][3]
                                    sty = indd[l2][2] + indd[l2][4]
                                    enx = stx - p1.width * c1 - p1.height * s1
                                    eny = sty + p1.height * c1 - p1.width * s1
                                    if enx < stx:
                                        temp = enx
                                        enx = stx
                                        stx = temp
                                    if eny < sty:
                                        temp = eny
                                        eny = sty
                                        sty = temp

                                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
                                #cr.move_to(stx, sty)
                                #cr.line_to(enx,eny)
                                #cr.stroke()
                            if ((math.pow(math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0), 0.5) - lM) > 0.1):
                                maxelement = l2
                                lM = math.pow(math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0),
                                              0.5)
                        l2 += 1
                    x1 = coor[int(findindex[maxelement] / 2)].X1
                    x2 = coor[int(findindex[maxelement] / 2)].X2
                    y1 = coor[int(findindex[maxelement] / 2)].Y1
                    y2 = coor[int(findindex[maxelement] / 2)].Y2
                    c = (indd[maxelement][3]) / math.sqrt(
                        math.pow((indd[maxelement][3]), 2.0) + math.pow((indd[maxelement][4]), 2.0))
                    s = (indd[maxelement][4]) / math.sqrt(
                        math.pow((indd[maxelement][3]), 2.0) + math.pow((indd[maxelement][4]), 2.0))
                    if indd[maxelement][0] == "S":
                        cr.move_to(x1, y1)
                        cr.line_to(x1 - indd[maxelement][3], y1 + indd[maxelement][4])
                    else:
                        cr.move_to(x2, y2)
                        cr.line_to(x2 - indd[maxelement][3], y2 + indd[maxelement][4])
                    cr.stroke()
                    maxeleold = maxelement
                    if (len(indd)==2):
                        if maxelement==1:
                            maxelement = 0
                        else:
                            maxelement=1

                        #case of opposite direction
                        if ((indd[maxeleold][4]*indd[maxelement][4]<=0) and (indd[maxeleold][3]*indd[maxelement][3]<=0)):
                            if indd[maxeleold][0] == "S":
                                cr.move_to(x1, y1)
                                cr.line_to(x1 - indd[maxelement][3], y1 + indd[maxelement][4])
                            else:
                                cr.move_to(x2, y2)
                                cr.line_to(x2 - indd[maxelement][3], y2 + indd[maxelement][4])
                            cr.stroke()
                    l3 = len(indtodelete) - 1
                    while l3 >= 0:
                        if (len(indd) > 0):
                            indd.pop(indtodelete[l3])
                            findindex.pop(indtodelete[l3])
                        if (len(indtodelete) > 0):
                            indtodelete.pop(l3)
                        l3 -= 1
                        l1 -= 1
                    if len(indd) == 0:
                        break
                    l1 += 1

        for e in range(0, len(coor)):
            cr.set_source_rgb(0.0, 0.2, 0)
            x1 = coor[e].X1
            x2 = coor[e].X2
            y1 = coor[e].Y1
            y2 = coor[e].Y2
            c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            cr.move_to(x1 + MyWindow.beamunit[e].Q1 * MyWindow.scale * (wndp / wndh) * s,
                       y1 - MyWindow.beamunit[e].Q1 * MyWindow.scale * (wndp / wndh) * c)
            cr.line_to(x2 + MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh) * s,
                       y2 - MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh) * c)
            cr.stroke()

    def OnDrawlN( widget, cr):
        coor = MyWindow.create_frame_beam(widget, cr)
        cr.set_line_width(1)
        p=widget.get_allocation()
        wndh = p.height
        wndp = p.width
        sig = "Axial forces in Kilonewtons"
        cr.set_source_rgb(0.2, 0.0, 0)
        cr.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
        cr.move_to((p.width - dx) / 2, 20)
        cr.show_text(sig)
        if (math.fabs(MyWindow.maxN)<0.1):
            return
        for a in range(0, len(MyWindow.nodes)):
            if MyWindow.nodes[a].name.find("SPRING") > -1:
                continue
            ind = 0
            findindex = []
            while True:
                try:
                    nam1 = MyWindow.nodes[a].name
                    if "_" in nam1[-3:]:
                        nam1 = nam1[:-3]

                    ind = MyWindow.cos.index(nam1, ind, len(MyWindow.cos))
                    #ind = MyWindow.cos.index(MyWindow.nodes[a].name, ind, len(MyWindow.cos))
                    findindex.append(ind)
                    ind += 1
                except ValueError as error:
                    break
            if ((len(findindex) == 1)):
                nodeindex = MyWindow.findobject(MyWindow, MyWindow.nodes[a].name, MyWindow.nodes)
                cr.set_source_rgb(0.0, 0.2, 0)
                beamindex = int(findindex[0] / 2)
                x1 = coor[int(findindex[0] / 2)].X1
                y1 = coor[int(findindex[0] / 2)].Y1
                x2 = coor[int(findindex[0] / 2)].X2
                y2 = coor[int(findindex[0] / 2)].Y2
                # gon = math.atan2(MyWindow.beams[int(findindex[l] / 2)].yl, MyWindow.beams[int(findindex[l] / 2)].xl)
                c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))

                #x1 = coor[beamindex].X1
                #x2 = coor[beamindex].X2
                #y1 = coor[beamindex].Y1
                #y2 = coor[beamindex].Y2
                #gon = math.atan2(MyWindow.beams[int(findindex[0] / 2)].xl, MyWindow.beams[int(findindex[0] / 2)].yl)
                gon =math.atan2(s,c)
                c = math.cos(gon)
                s = math.sin(gon)

                N1x = -MyWindow.beamunit[int(findindex[0] / 2)].N1 * MyWindow.scale * (wndp / wndh) * s
                N1y = - MyWindow.beamunit[int(findindex[0] / 2)].N1 * MyWindow.scale * (wndp / wndh) * c
                N2x = - MyWindow.beamunit[int(findindex[0] / 2)].N2 * MyWindow.scale * (wndp / wndh) * s
                N2y = -MyWindow.beamunit[int(findindex[0] / 2)].N2 * MyWindow.scale * (wndp / wndh) * c
                #           y2 + MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh) * c)

                txtN = "{:.2f}"
                if MyWindow.beams[beamindex].StartNode == MyWindow.nodes[a].name:
                    cr.move_to(x1 + 0 * s, y1 + 0 * c)
                    cr.line_to(x1 + MyWindow.beamunit[beamindex].N1 * MyWindow.scale * (wndp / wndh) * s,
                               y1 - MyWindow.beamunit[beamindex].N1 * MyWindow.scale * (wndp / wndh) * c)
                    a1x =  + MyWindow.beamunit[beamindex].N1 * MyWindow.scale * (wndp / wndh) * s
                    a1y = - MyWindow.beamunit[beamindex].N1 * MyWindow.scale * (wndp / wndh) * c
                    cr.stroke()
                    cr.save()
                    N1 = MyWindow.beamunit[beamindex].N1 * MyWindow.maxN
                    sig = txtN.format(N1 / 1000.0)
                    cr.set_font_size(MyWindow.font)
                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                    p1 = cr.text_extents(sig)
                    cr.translate(x1 + MyWindow.beamunit[beamindex].N1 * MyWindow.scale * (wndp / wndh) * s,
                                 y1 - MyWindow.beamunit[beamindex].N1 * MyWindow.scale * (wndp / wndh) * c)

                    gon = math.atan2(c,s)
                    c = math.cos(gon)
                    s = math.sin(gon)

                    cr.rotate(gon)
                    # gon = math.atan2(N1y, N1x)
                    # c = math.cos(gon)
                    # s = math.sin(gon)
                    cr.move_to(0, 0)
                    cr.set_font_size(MyWindow.font)
                    cr.show_text(sig)

                    stx = x1+a1x
                    sty = y1+a1y
                    enx = stx + p1.width * c + p1.height * s
                    eny = sty - p1.height * c + p1.width * s
                    cr.restore()
                    if enx < stx:
                        temp = enx
                        enx = stx
                        stx = temp
                    if eny < sty:
                        temp = eny
                        eny = sty
                        sty = temp
                    #cr.move_to(stx,sty)
                    #cr.line_to(enx,eny)
                    #cr.stroke()
                if MyWindow.beams[beamindex].EndNode == MyWindow.nodes[a].name:

                    cr.move_to(x2 + 0 * s, y2 + 0 * c)
                    cr.line_to(x2 + MyWindow.beamunit[beamindex].N2 * MyWindow.scale * (wndp / wndh) * s,
                               y2 - MyWindow.beamunit[beamindex].N2 * MyWindow.scale * (wndp / wndh) * c)

                    cr.stroke()

                    cr.set_font_size(MyWindow.font)
                    p1 = cr.text_extents(sig)
                    cr.save()
                    a2x =  + MyWindow.beamunit[beamindex].N2 * MyWindow.scale * (wndp / wndh) * s
                    a2y =  - MyWindow.beamunit[beamindex].N2 * MyWindow.scale * (wndp / wndh) * c
                    N2 = MyWindow.beamunit[beamindex].N2 * MyWindow.maxN
                    sig = txtN.format(N2 / 1000.0)

                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)

                    cr.translate(x2 + MyWindow.beamunit[beamindex].N2 * MyWindow.scale * (wndp / wndh) * s,
                                 y2 - MyWindow.beamunit[beamindex].N2 * MyWindow.scale * (wndp / wndh) * c)

                    gon = math.atan2(c,s)
                    cr.rotate(gon)

                    c = math.cos(gon)
                    s = math.sin(gon)
                    cr.move_to(0, 0)
                    cr.set_font_size(MyWindow.font)
                    cr.show_text(sig)
                    stx = x2+a2x
                    sty = y2+a2y

                    # stx = x2 - MyWindow.beamunit[beamindex].N2 * MyWindow.scale * (wndp / wndh) * c
                    # sty = y2 - MyWindow.beamunit[beamindex].N2 * MyWindow.scale * (wndp / wndh) * s

                    enx = stx + p1.width * c+ p1.height * s
                    eny = sty - p1.height * c + p1.width * s

                    cr.restore()

                if enx < stx:
                    temp = enx
                    enx = stx
                    stx = temp
                if eny < sty:
                    temp = eny
                    eny = sty
                    sty = temp
                #cr.move_to(stx,sty)
                #cr.line_to(enx,eny)
                #cr.stroke()

                MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
            else:
                indd = []
                for l in range(0, len(findindex)):
                    x1 = coor[int(findindex[l] / 2)].X1
                    y1 = coor[int(findindex[l] / 2)].Y1
                    x2 = coor[int(findindex[l] / 2)].X2
                    y2 = coor[int(findindex[l] / 2)].Y2
                    #gon = math.atan2(MyWindow.beams[int(findindex[l] / 2)].yl, MyWindow.beams[int(findindex[l] / 2)].xl)
                    c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                    s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
                    gon=math.atan2(c,s)
                    N1x = -MyWindow.beamunit[int(findindex[l] / 2)].N1 * MyWindow.scale * (wndp / wndh) * s
                    N1y = - MyWindow.beamunit[int(findindex[l] / 2)].N1 * MyWindow.scale * (wndp / wndh) * c
                    N2x = - MyWindow.beamunit[int(findindex[l] / 2)].N2 * MyWindow.scale * (wndp / wndh) * s
                    N2y = -MyWindow.beamunit[int(findindex[l] / 2)].N2 * MyWindow.scale * (wndp / wndh) * c
                    #           y2 + MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh) * c)

                    if (findindex[l] % 2 == 0):
                        indd.append(['S', x1, y1, N1x, N1y, gon])
                    else:
                        indd.append(['E', x2, y2, N2x, N2y, gon])
                # indd=sorted(indd,key=lambda x:x[5])
                l1 = 0
                cou = 0
                indtodelete = []
                while l1 < len(indd):
                    x1 = coor[int(findindex[l1] / 2)].X1
                    y1 = coor[int(findindex[l1] / 2)].Y1
                    x2 = coor[int(findindex[l1] / 2)].X2
                    y2 = coor[int(findindex[l1] / 2)].Y2

                    lM = math.pow(math.pow(indd[l1][3], 2.0) + math.pow(indd[l1][4], 2.0), 0.5)
                    maxelement = l1
                    cr.save()
                    txtN = "{:.2f}"
                    if (indd[maxelement][0] == "S"):

                        N1 = MyWindow.beamunit[int(findindex[maxelement] / 2)].N1 * MyWindow.maxN
                        sig = txtN.format(N1 / 1000.0)
                        c1 = (indd[maxelement][3]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        s1 = (indd[maxelement][4]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        stx = indd[maxelement][1] - indd[maxelement][3]
                        sty = indd[maxelement][2] + indd[maxelement][4]
                        p1 = cr.text_extents(sig)
                        enx = stx + p1.width * c1 + p1.height * s1
                        eny = sty - p1.height * c1 + p1.width * s1
                        if enx < stx:
                            temp = enx
                            enx = stx
                            stx = temp
                        if eny < sty:
                            temp = eny
                            eny = sty
                            sty = temp
                        #cr.move_to(stx, sty)
                        #cr.line_to(enx, eny)
                        #cr.stroke()
                        gon = math.atan2(indd[l1][4], indd[l1][3])
                    else:

                        gon = math.atan2(indd[l1][4], indd[l1][3])
                        N2 = MyWindow.beamunit[int(findindex[maxelement] / 2)].N2 * MyWindow.maxN
                        sig = txtN.format(N2 / 1000.0)
                        p1 = cr.text_extents(sig)
                        c1 = (indd[maxelement][3]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        s1 = (indd[maxelement][4]) / math.sqrt(
                            math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0))
                        stx = indd[maxelement][1] - indd[maxelement][3]
                        sty = indd[maxelement][2] + indd[maxelement][4]
                        enx = stx + p1.width * c1 + p1.height * s1
                        eny = sty - p1.height * c1 + p1.width * s1

                    (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                    cr.translate(indd[maxelement][1] - indd[maxelement][3],
                                 indd[maxelement][2] + indd[maxelement][4])
                    cr.set_font_size(MyWindow.font)



                    #cr.rotate(math.atan2(indd[maxelement][4], indd[maxelement][3]))
                    cr.rotate(gon)
                    cr.move_to(0, 0)
                    cr.set_font_size(MyWindow.font)
                    cr.show_text(sig)

                    cr.restore()
                    if enx < stx:
                        temp = enx
                        enx = stx
                        stx = temp
                    if eny < sty:
                        temp = eny
                        eny = sty
                        sty = temp
                    #cr.move_to(stx,sty)
                    #cr.line_to(enx,eny)
                    #cr.stroke()
                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))

                    l2 = l1 + 1
                    gon = indd[l1][5]
                    indtodelete.append(l1)

                    while l2 < len(indd):
                        x1 = coor[int(findindex[l2] / 2)].X1
                        y1 = coor[int(findindex[l2] / 2)].Y1
                        x2 = coor[int(findindex[l2] / 2)].X2
                        y2 = coor[int(findindex[l2] / 2)].Y2

                        if math.fabs(indd[l2][5] - gon) < 1e-5:
                            indtodelete.append(l2)
                            if math.fabs((math.pow(math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0),
                                                   0.5) - lM)) > 0.1:
                                cr.save()
                                txtN = "{:.2f}"
                                if (indd[l2][0] == "S"):
                                    N1 = MyWindow.beamunit[int(findindex[l2] / 2)].N1 * MyWindow.maxN
                                    sig = txtN.format(N1 / 1000.0)
                                else:
                                    N2 = MyWindow.beamunit[int(findindex[l2] / 2)].N2 * MyWindow.maxN
                                    sig = txtN.format(N2 / 1000.0)
                                (x, y, wid, hei, dx, dy) = cr.text_extents(sig)
                                p1 = cr.text_extents(sig)
                                cr.translate(indd[l2][1] + indd[l2][3],
                                             indd[l2][2] + indd[l2][4])
                                # cr.translate(x1 - MyWindow.beamunit[e].N1 * MyWindow.scale*(wndp/wndh) * s,
                                #             y1 + MyWindow.beamunit[e].N1 * MyWindow.scale*(wndp/wndh) * c)
                                cr.set_font_size(MyWindow.font)
                                cr.rotate(math.atan2(indd[l2][4], indd[l2][3]))
                                cr.move_to(0, 0)
                                cr.set_font_size(MyWindow.font)
                                cr.show_text(sig)
                                cr.restore()
                                if (indd[l2][0] == "S"):
                                    c1 = (indd[l2][3]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    s1 = (indd[l2][4]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    stx = indd[l2][1] - indd[l2][3]
                                    sty = indd[l2][2] + indd[l2][4]
                                    enx = stx + p1.width * c1 + p1.height * s1
                                    eny = sty - p1.height * c1 + p1.width * s1
                                    if enx < stx:
                                        temp = enx
                                        enx = stx
                                        stx = temp
                                    if eny < sty:
                                        temp = eny
                                        eny = sty
                                        sty = temp
                                    #cr.move_to(stx, sty)
                                    #cr.line_to(enx, eny)
                                    #cr.stroke()
                                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))
                                else:
                                    c1 = (indd[l2][3]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    s1 = (indd[l2][4]) / math.sqrt(
                                        math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0))
                                    stx = indd[l2][1] - indd[l2][3]
                                    sty = indd[l2][2] + indd[l2][4]
                                    enx = stx + p1.width * c1 + p1.height * s1
                                    eny = sty - p1.height * c1 + p1.width * s1
                                    if enx < stx:
                                        temp = enx
                                        enx = stx
                                        stx = temp
                                    if eny < sty:
                                        temp = eny
                                        eny = sty
                                        sty = temp
                                    #cr.move_to(stx, sty)
                                    #cr.line_to(enx, eny)
                                    #cr.stroke()
                                    MyWindow.Graph.append(Graph(sig, stx, sty, enx, eny))

                            if ((math.pow(math.pow(indd[l2][3], 2.0) + math.pow(indd[l2][4], 2.0), 0.5) - lM) > 0.1):
                                maxelement = l2
                                lM = math.pow(math.pow(indd[maxelement][3], 2.0) + math.pow(indd[maxelement][4], 2.0),
                                              0.5)
                        l2 += 1
                    x1 = coor[int(findindex[maxelement] / 2)].X1
                    x2 = coor[int(findindex[maxelement] / 2)].X2
                    y1 = coor[int(findindex[maxelement] / 2)].Y1
                    y2 = coor[int(findindex[maxelement] / 2)].Y2
                    c = (indd[maxelement][3]) / math.sqrt(
                        math.pow((indd[maxelement][3]), 2.0) + math.pow((indd[maxelement][4]), 2.0))
                    s = (indd[maxelement][4]) / math.sqrt(
                        math.pow((indd[maxelement][3]), 2.0) + math.pow((indd[maxelement][4]), 2.0))
                    if indd[maxelement][0] == "S":
                        cr.move_to(x1, y1)
                        cr.line_to(x1 - indd[maxelement][3], y1 + indd[maxelement][4])
                    else:
                        cr.move_to(x2, y2)
                        cr.line_to(x2 - indd[maxelement][3], y2 + indd[maxelement][4])
                    cr.stroke()
                    maxeleold = maxelement
                    if (len(indd)==2):
                        if maxelement==1:
                            maxelement = 0
                        else:
                            maxelement=1

                        #case of opposite direction
                        if ((indd[maxeleold][4]*indd[maxelement][4]<=0) and (indd[maxeleold][3]*indd[maxelement][3]<=0)):
                            if indd[maxeleold][0] == "S":
                                cr.move_to(x1, y1)
                                cr.line_to(x1 - indd[maxelement][3], y1 + indd[maxelement][4])
                            else:
                                cr.move_to(x2, y2)
                                cr.line_to(x2 - indd[maxelement][3], y2 + indd[maxelement][4])
                            cr.stroke()
                    l3 = len(indtodelete) - 1
                    while l3 >= 0:
                        if (len(indd) > 0):
                            indd.pop(indtodelete[l3])
                            findindex.pop(indtodelete[l3])
                        if (len(indtodelete) > 0):
                            indtodelete.pop(l3)
                        l3 -= 1
                        l1 -= 1
                    if len(indd) == 0:
                        break
                    l1 += 1

        for e in range(0, len(coor)):
            cr.set_source_rgb(0.0, 0.2, 0)
            x1 = coor[e].X1
            x2 = coor[e].X2
            y1 = coor[e].Y1
            y2 = coor[e].Y2
            c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            cr.move_to(x1 + MyWindow.beamunit[e].N1 * MyWindow.scale * (wndp / wndh) * s,
                       y1 - MyWindow.beamunit[e].N1 * MyWindow.scale * (wndp / wndh) * c)
            cr.line_to(x2 + MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh) * s,
                       y2 - MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh) * c)
            cr.stroke()

        MyWindow.sc1 = MyWindow.scale

    def bg(self, op, cx):
        w = cx.get_width()
        h = cx.get_height()

    #      print ("page_height ", page_height)

    def draw_page1(self, operation, context, page_nr=None):
        ctx = context.get_cairo_context()
        w = context.get_width()
        h = context.get_height()
        # cx.select_font_face("Times", 0, 1)
        # ex = cx.text_extents("Instrucțiuni de utilizare:")[2]

        # if page_nr == 3:
        #   coords=None
        #   self.drawpage4(context)
        #   return

        # ww, hh = int(w / 4), int(h / 2)
        # ctx.move_to(0, 0)
        # ctx.line_to(w, h)
        # ctx.stroke()
        maxx = -9e99
        maxy = -9e99
        minx = 9e99
        miny = 9e99
        # p = widget.get_allocation()
        wndh = h
        wndp = w
        for k in range(len(MyWindow.nodes)):
            if MyWindow.nodes[k].name.find("SPRING") > -1:
                continue
            if MyWindow.nodes[k].X > maxx:
                maxx = MyWindow.nodes[k].X
            if MyWindow.nodes[k].X < minx:
                minx = MyWindow.nodes[k].X
            if MyWindow.nodes[k].Y > maxy:
                maxy = MyWindow.nodes[k].Y
            if MyWindow.nodes[k].Y < miny:
                miny = MyWindow.nodes[k].X
        Dx = maxx - minx
        Dy = maxy - miny
        try:
            MyWindow.ratio = max(0.5, Dy / Dx, 1.0)
        except ZeroDivisionError as error:
            MyWindow.ratio = 1.0

        # cr.set_line_width(1)
        wx = w * 0.75
        wy = h * 0.375
        originx = 0
        originy = 0
        e = 0
        coords = DynamicArray()
        for k in range(len(MyWindow.beams)):
            beamname = MyWindow.beams[k].name
            # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
            beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
            beamstartnode = MyWindow.beams[beamnameindex].StartNode
            if beamstartnode.find("SPRING") > -1:
                continue
            startNodeIndex = MyWindow.findobject(MyWindow, beamstartnode, MyWindow.nodes)
            beamendnode = MyWindow.beams[beamnameindex].EndNode
            endNodeIndex = MyWindow.findobject(MyWindow, beamendnode, MyWindow.nodes)
            xl = MyWindow.beams[beamnameindex].xl
            yl = MyWindow.beams[beamnameindex].yl
            c = xl / math.sqrt(xl * xl + yl * yl)
            s = yl / math.sqrt(xl * xl + yl * yl)
            if Dx > 0:
                x1 = originx + wx * (MyWindow.nodes[startNodeIndex].X / Dx)
                y1 = originy - wy * MyWindow.ratio * (MyWindow.nodes[startNodeIndex].Y / Dy)
                x2 = originx + wx * (MyWindow.nodes[endNodeIndex].X / Dx)
                y2 = originy - wy * MyWindow.ratio * (MyWindow.nodes[endNodeIndex].Y / Dy)
            else:
                MyWindow.ratio = 1.0
                x1 = originx
                y1 = originy - wy * MyWindow.ratio * (MyWindow.nodes[startNodeIndex].Y / Dy)
                x2 = originx
                y2 = originy - wy * MyWindow.ratio * (MyWindow.nodes[endNodeIndex].Y / Dy)

            w1 = Coords(x1, y1, x2, y2, beamstartnode, beamendnode)
            coords.append(w1)
            e += 1

        xmax = -9e99
        ymax = -9e99
        xmin = 9e99
        ymin = 9e99
        e = 0
        for k in range(len(MyWindow.beams)):
            beamname = MyWindow.beams[k].name
            # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
            beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
            beamstartnode = MyWindow.beams[beamnameindex].StartNode
            if beamstartnode.find("SPRING") > -1:
                continue
            startNodeIndex = MyWindow.findobject(MyWindow, beamstartnode, MyWindow.nodes)
            beamendnode = MyWindow.beams[beamnameindex].EndNode
            endNodeIndex = MyWindow.findobject(MyWindow, beamendnode, MyWindow.nodes)
            xl = MyWindow.beams[beamnameindex].xl
            yl = MyWindow.beams[beamnameindex].yl
            c = xl / math.sqrt(xl * xl + yl * yl)
            s = yl / math.sqrt(xl * xl + yl * yl)
            x1a = coords[e].X1 + MyWindow.scale * (wndp / wndh) * c
            x1k = coords[e].X1 - MyWindow.scale * (wndp / wndh) * c
            x2a = coords[e].X2 + MyWindow.scale * (wndp / wndh) * c
            x2k = coords[e].X2 - MyWindow.scale * (wndp / wndh) * c
            y1a = coords[e].Y1 + MyWindow.scale * (wndp / wndh) * s * MyWindow.ratio
            y1k = coords[e].Y1 - MyWindow.scale * (wndp / wndh) * s * MyWindow.ratio
            y2a = coords[e].Y2 + MyWindow.scale * (wndp / wndh) * s * MyWindow.ratio
            y2k = coords[e].Y2 - MyWindow.scale * (wndp / wndh) * s * MyWindow.ratio
            xmax = max(xmax, x1a, x1k, x2a, x2k)
            xmin = min(xmin, x1a, x1k, x2a, x2k)
            ymax = max(ymax, y1a, y1k, y2a, y2k)
            ymin = min(ymin, y1a, y1k, y2a, y2k)
            e += 1
        wid = xmax - xmin
        hei = ymax - ymin
        originx = (wndp - wid) / 2
        originy = (wndh - (wndh - hei) / 2)
        e = 0
        for k in range(len(MyWindow.beams)):
            beamname = MyWindow.beams[k].name
            # Ψάχνω στη ράβδο ποιους κόμβους ενώνει
            beamnameindex = MyWindow.findobject(MyWindow, beamname, MyWindow.beams)
            beamstartnode = MyWindow.beams[beamnameindex].StartNode
            if beamstartnode.find("SPRING") > -1:
                continue
            startNodeIndex = MyWindow.findobject(MyWindow, beamstartnode, MyWindow.nodes)
            beamendnode = MyWindow.beams[beamnameindex].EndNode
            endNodeIndex = MyWindow.findobject(MyWindow, beamendnode, MyWindow.nodes)
            xl = MyWindow.beams[beamnameindex].xl
            yl = MyWindow.beams[beamnameindex].yl
            c = xl / math.sqrt(xl * xl + yl * yl)
            s = yl / math.sqrt(xl * xl + yl * yl) * MyWindow.ratio
            coords[e].X1 += originx
            coords[e].X2 += originx
            coords[e].Y1 += originy
            coords[e].Y2 += originy
            ctx.set_line_width(2)
            ctx.set_source_rgb(0, 0, 0)
            ctx.move_to(coords[e].X1, coords[e].Y1)
            ctx.line_to(coords[e].X2, coords[e].Y2)
            ctx.stroke()
            ctx.set_line_width(1)
            ctx.set_source_rgb(1, 0, 0)
            ctx.move_to(coords[e].X1 - 5 * s, coords[e].Y1 - 5 * c)
            ctx.line_to(coords[e].X1 + 5 * s, coords[e].Y1 + 5 * c)

            ctx.stroke()
            sig = MyWindow.beams[e].StartNode
            ctx.save()
            ctx.set_font_size(MyWindow.font)
            (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
            ctx.move_to(coords[e].X1 - 5 * s, coords[e].Y1 - 5 * c)
            ctx.rotate(math.atan2((yl), (xl)))
            # cr.move_to(0, 0)
            ctx.set_font_size(MyWindow.font)
            ctx.show_text(sig)
            ctx.restore()

            e += 1
        e -= 1
        ctx.set_line_width(1)
        ctx.set_source_rgb(1, 0, 0)
        ctx.move_to(coords[e].X2 - 5 * MyWindow.ratio * s, coords[e].Y2 - 5 * c)
        ctx.line_to(coords[e].X2 + 5 * MyWindow.ratio * s, coords[e].Y2 + 5 * c)
        ctx.stroke()
        sig = MyWindow.beams[e].EndNode
        ctx.save()
        ctx.set_font_size(MyWindow.font)
        (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
        ctx.move_to(coords[e].X2 - 5 * s, coords[e].Y2 - 5 * c)
        ctx.rotate(math.atan2((yl), (xl)))
        # cr.move_to(0, 0)
        ctx.set_font_size(MyWindow.font)
        ctx.show_text(sig)
        ctx.restore()

        if page_nr == 0:
            self.drawpage1(ctx, coords, w, h)
        elif page_nr == 1:
            self.drawpage2(ctx, coords, w, h)
        elif page_nr == 2:
            self.drawpage3(ctx, coords, w, h)

    def drawpage1(self, ctx, coor, w, h):
        wndh = h
        wndp = w
        # coor = guiobj.create_frame_beam(widget, cr)
        sig = "Beam Moments in Kilonewton meters"
        ctx.set_source_rgb(0.2, 0.0, 0)
        ctx.select_font_face("Times", 0, 1)
        ctx.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
        ctx.move_to((wndp - dx) / 2, 20)
        ctx.show_text(sig)
        sc1 = MyWindow.scale
        scx1 = 0
        scy1 = 0
        scx2 = 0
        scy2 = 0
        for e in range(len(coor)):
            ctx.set_source_rgb(0.0, 0.2, 0)
            x1 = coor[e].X1
            x2 = coor[e].X2
            y1 = coor[e].Y1
            y2 = coor[e].Y2
            if x2 == x1 and y1 == y2:
                continue
            c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            try:
                scx1 = abs(-x1 / (MyWindow.beamunit[e].M1 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy1 = abs(+y1 / (MyWindow.beamunit[e].M1 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scx2 = abs((wndp - x1) / (MyWindow.beamunit[e].M1 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy2 = abs((y1 - wndh) / (MyWindow.beamunit[e].M1 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                MyWindow.scale = min(MyWindow.scale, scx1, scy1, scx2, scy2)
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            MyWindow.scale = min(MyWindow.scale, scx1, scy1, scx2, scy2)
            try:
                scx1 = abs(-x2 / (MyWindow.beamunit[e].M2 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy1 = abs(+y2 / (MyWindow.beamunit[e].M2 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scx2 = abs((wndp - x2) / (MyWindow.beamunit[e].M2 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy2 = abs((y2 - wndh) / (MyWindow.beamunit[e].M2 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1

            MyWindow.scale = min(MyWindow.scale, scx1, scy1, scx2, scy2)
        for e in range(len(coor)):
            ctx.set_source_rgb(0.0, 0.2, 0)
            x1 = coor[e].X1
            x2 = coor[e].X2
            y1 = coor[e].Y1
            y2 = coor[e].Y2
            if x2 == x1 and y1 == y2:
                continue
            c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            ctx.move_to(x1 + 0 * s, y1 + 0 * c)
            ctx.line_to(x1 - MyWindow.beamunit[e].M1 * MyWindow.scale * (wndp / wndh) * s,
                        y1 + MyWindow.beamunit[e].M1 * MyWindow.scale * (wndp / wndh) * c)
            ctx.stroke()
            ctx.move_to(x2 + 0 * s, y2 + 0 * c)
            ctx.line_to(x2 - MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh) * s,
                        y2 + MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh) * c)
            ctx.stroke()
            ctx.move_to(x1 - MyWindow.beamunit[e].M1 * MyWindow.scale * (wndp / wndh) * s,
                        y1 + MyWindow.beamunit[e].M1 * MyWindow.scale * (wndp / wndh) * c)
            ctx.line_to(x2 - MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh) * s,
                        y2 + MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh) * c)
            ctx.stroke()
            ctx.save()

            M1 = MyWindow.beamunit[e].M1 * MyWindow.maxM
            txtM = "{:.2f}"

            sig = txtM.format(M1 / 1000.0)
            ctx.set_font_size(MyWindow.font)
            (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
            ctx.translate(x1 - MyWindow.beamunit[e].M1 * MyWindow.scale * (wndp / wndh) * s,
                          y1 + MyWindow.beamunit[e].M1 * MyWindow.scale * (wndp / wndh) * c)
            ctx.rotate(math.atan2((y2 - y1), (x2 - x1)))
            ctx.move_to(0, 0)
            ctx.set_font_size(MyWindow.font)
            ctx.show_text(sig)
            ctx.restore()
            ctx.save()
            M2 = MyWindow.beamunit[e].M2 * MyWindow.maxM
            txtM = "{:.2f}"
            ctx.set_font_size(MyWindow.font)
            sig = txtM.format(M2 / 1000.0)
            (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
            ctx.translate(x2 - (MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh)) * s,
                          y2 + MyWindow.beamunit[e].M2 * MyWindow.scale * (wndp / wndh) * c)
            ctx.rotate(math.atan2((y2 - y1), x2 - x1))
            ctx.move_to(0, 0)
            ctx.set_font_size(MyWindow.font)
            ctx.show_text(sig)
            ctx.restore()
        MyWindow.sc1 = MyWindow.scale

    def drawpage2(self,ctx,coor,w,h):
        wndh = h
        wndp = w
        #coor = guiobj.create_frame_beam(widget, cr)
        sig = "Shear Forces in Kilonewtons"
        ctx.set_source_rgb(0.2, 0.0, 0)
        ctx.select_font_face("Times", 0, 1)
        ctx.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
        ctx.move_to((wndp - dx) / 2, 20)
        ctx.show_text(sig)
        sc1 = MyWindow.scale
        scx1 = 0
        scy1 = 0
        scx2 = 0
        scy2 = 0
        for e in range(len(coor)):
            ctx.set_source_rgb(0.0, 0.2, 0)
            x1 = coor[e].X1
            x2 = coor[e].X2
            y1 = coor[e].Y1
            y2 = coor[e].Y2
            if x2==x1 and y1==y2:
                continue
            c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            try:
                scx1 = abs(-x1 / (MyWindow.beamunit[e].Q1 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy1 = abs(+y1 / (MyWindow.beamunit[e].Q1 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scx2 = abs((wndp - x1) / (MyWindow.beamunit[e].Q1 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy2 = abs((y1 - wndh) / (MyWindow.beamunit[e].Q1 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                MyWindow.scale = min(MyWindow.scale, scx1, scy1, scx2, scy2)
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            MyWindow.scale = min(MyWindow.scale, scx1, scy1, scx2, scy2)
            try:
                scx1 = abs(-x2 / (MyWindow.beamunit[e].Q2 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy1 = abs(+y2 / (MyWindow.beamunit[e].Q2 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scx2 = abs((wndp - x2) / (MyWindow.beamunit[e].Q2 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy2 = abs((y2 - wndh) / (MyWindow.beamunit[e].Q2 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1

            MyWindow.scale = min(MyWindow.scale, scx1, scy1, scx2, scy2)
        for e in range(len(coor)):
            ctx.set_source_rgb(0.0, 0.2, 0)
            x1 = coor[e].X1
            x2 = coor[e].X2
            y1 = coor[e].Y1
            y2 = coor[e].Y2
            if x2 == x1 and y1 == y2:
                continue

            c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            ctx.move_to(x1 + 0 * s, y1 + 0 * c)
            ctx.line_to(x1 + MyWindow.beamunit[e].Q1 * MyWindow.scale * (wndp / wndh) * s,
                       y1 - MyWindow.beamunit[e].Q1 * MyWindow.scale * (wndp / wndh) * c)
            ctx.stroke()
            ctx.move_to(x2 + 0 * s, y2 + 0 * c)
            ctx.line_to(x2 + MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh) * s,
                       y2 - MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh) * c)
            ctx.stroke()
            ctx.move_to(x1 + MyWindow.beamunit[e].Q1 * MyWindow.scale * (wndp / wndh) * s,
                       y1 - MyWindow.beamunit[e].Q1 * MyWindow.scale * (wndp / wndh) * c)
            ctx.line_to(x2 + MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh) * s,
                       y2 - MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh) * c)
            ctx.stroke()
            ctx.save()

            Q1 = MyWindow.beamunit[e].Q1 * MyWindow.maxQ
            txtQ = "{:.2f}"

            sig = txtQ.format(Q1/1000.0)
            ctx.set_font_size(MyWindow.font)
            (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
            ctx.translate(x1 + MyWindow.beamunit[e].Q1 * MyWindow.scale * (wndp / wndh) * s,
                         y1 - MyWindow.beamunit[e].Q1 * MyWindow.scale * (wndp / wndh) * c)
            ctx.rotate(math.atan2((y2 - y1), (x2 - x1)))
            ctx.move_to(0, 0)
            ctx.set_font_size(MyWindow.font)
            ctx.show_text(sig)
            ctx.restore()
            ctx.save()
            Q2 = MyWindow.beamunit[e].Q2 * MyWindow.maxQ
            txtQ = "{:.2f}"
            ctx.set_font_size(MyWindow.font)
            sig = txtQ.format(Q2/1000.0)
            (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
            ctx.translate(x2 + (MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh)) * s,
                         y2 - MyWindow.beamunit[e].Q2 * MyWindow.scale * (wndp / wndh) * c)
            ctx.rotate(math.atan2((y2 - y1), x2 - x1))
            ctx.move_to(0, 0)
            ctx.set_font_size(MyWindow.font)
            ctx.show_text(sig)
            ctx.restore()
        MyWindow.sc1 = MyWindow.scale
    def drawpage3(self,ctx,coor,w,h):
        wndh = h
        wndp = w
        #coor = guiobj.create_frame_beam(widget, cr)
        sig = "Axial Forces in Kilonewtons"
        ctx.set_source_rgb(0.2, 0.0, 0)
        ctx.select_font_face("Times", 0, 1)
        ctx.set_font_size(MyWindow.font * 1.3)
        (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
        ctx.move_to((wndp - dx) / 2, 20)
        ctx.show_text(sig)
        sc1 = MyWindow.scale
        scx1 = 0
        scy1 = 0
        scx2 = 0
        scy2 = 0
        for e in range(len(coor)):
            ctx.set_source_rgb(0.0, 0.2, 0)
            x1 = coor[e].X1
            x2 = coor[e].X2
            y1 = coor[e].Y1
            y2 = coor[e].Y2
            if x2 == x1 and y1 == y2:
                continue
            c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            try:
                scx1 = abs(-x1 / (MyWindow.beamunit[e].N1 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy1 = abs(+y1 / (MyWindow.beamunit[e].N1 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scx2 = abs((wndp - x1) / (MyWindow.beamunit[e].N1 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy2 = abs((y1 - wndh) / (MyWindow.beamunit[e].N1 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                MyWindow.scale = min(MyWindow.scale, scx1, scy1, scx2, scy2)
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            MyWindow.scale = min(MyWindow.scale, scx1, scy1, scx2, scy2)
            try:
                scx1 = abs(-x2 / (MyWindow.beamunit[e].N2 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy1 = abs(+y2 / (MyWindow.beamunit[e].N2 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scx2 = abs((wndp - x2) / (MyWindow.beamunit[e].N2 * (wndp / wndh) * s))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1
            try:
                scy2 = abs((y2 - wndh) / (MyWindow.beamunit[e].N2 * (wndp / wndh) * c))
            except ZeroDivisionError as error:
                MyWindow.scale = sc1

            MyWindow.scale = min(MyWindow.scale, scx1, scy1, scx2, scy2)
        for e in range(len(coor)):
            ctx.set_source_rgb(0.0, 0.2, 0)
            x1 = coor[e].X1
            x2 = coor[e].X2
            y1 = coor[e].Y1
            y2 = coor[e].Y2
            if x2 == x1 and y1 == y2:
                continue

            c = (x2 - x1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            s = (y2 - y1) / math.sqrt(math.pow((x2 - x1), 2.0) + math.pow((y2 - y1), 2.0))
            ctx.move_to(x1 + 0 * s, y1 + 0 * c)
            ctx.line_to(x1 + MyWindow.beamunit[e].N1 * MyWindow.scale * (wndp / wndh) * s,
                       y1 - MyWindow.beamunit[e].N1 * MyWindow.scale * (wndp / wndh) * c)
            ctx.stroke()
            ctx.move_to(x2 + 0 * s, y2 + 0 * c)
            ctx.line_to(x2 + MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh) * s,
                       y2 - MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh) * c)
            ctx.stroke()
            ctx.move_to(x1 + MyWindow.beamunit[e].N1 * MyWindow.scale * (wndp / wndh) * s,
                       y1 - MyWindow.beamunit[e].N1 * MyWindow.scale * (wndp / wndh) * c)
            ctx.line_to(x2 + MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh) * s,
                       y2 - MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh) * c)
            ctx.stroke()
            ctx.save()

            N1 = MyWindow.beamunit[e].N1 * MyWindow.maxN
            txtN = "{:.2f}"

            sig = txtN.format(N1/1000.0)
            ctx.set_font_size(MyWindow.font)
            (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
            ctx.translate(x1 + MyWindow.beamunit[e].N1 * MyWindow.scale * (wndp / wndh) * s,
                         y1 - MyWindow.beamunit[e].N1 * MyWindow.scale * (wndp / wndh) * c)
            ctx.rotate(math.atan2((y2 - y1), (x2 - x1)))
            ctx.move_to(0, 0)
            ctx.set_font_size(MyWindow.font)
            ctx.show_text(sig)
            ctx.restore()
            ctx.save()
            N2 = MyWindow.beamunit[e].N2 * MyWindow.maxN
            txtN = "{:.2f}"
            ctx.set_font_size(MyWindow.font)
            sig = txtN.format(N2/1000.0)
            (x, y, wid, hei, dx, dy) = ctx.text_extents(sig)
            ctx.translate(x2 + (MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh)) * s,
                         y2 - MyWindow.beamunit[e].N2 * MyWindow.scale * (wndp / wndh) * c)
            ctx.rotate(math.atan2((y2 - y1), x2 - x1))
            ctx.move_to(0, 0)
            ctx.set_font_size(MyWindow.font)
            ctx.show_text(sig)
            ctx.restore()
        MyWindow.sc1 = MyWindow.scale


    def draw_page (self, operation, context, page_number):
        end = self.layout10.get_line_count()
        cr = context.get_cairo_context()
        cr.set_source_rgb(0, 0, 0)
        i = 0
        start = 0
        start_pos = 0
        iter = self.layout10.get_iter()
        while 1:
            if i >= start:
                line = iter.get_line()
                #print(line)
                _, logical_rect = iter.get_line_extents()
                # x_bearing, y_bearing, lwidth, lheight = logical_rect
                baseline = iter.get_baseline()
                if i == start:
                    start_pos = 12000 / 1024.0  # 1024.0 is float(pango.SCALE)
                cr.move_to(0 / 1024.0, baseline / 1024.0 - start_pos)
                PangoCairo.show_layout_line(cr, line)
            i += 1
            if not (i < end and iter.next_line()):
                break

    def createpages(self, op, context):
        page_height = 0
        ctx = context.get_cairo_context()
        w = context.get_width()
        h = context.get_height()
        self.layout = context.create_pango_layout()
        self.layout.set_width(int(w * Pango.SCALE))
        self.layout.set_height(int(h * Pango.SCALE))
        text = MyWindow.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), True)
        self.layout.set_font_description(Pango.FontDescription("Times 10"))
        self.layout.set_text(text, len(text))
        exts = self.layout.get_extents()

        MyWindow.num_lines = self.layout.get_line_count()
        if (MyWindow.textbuffer.get_line_count()==MyWindow.num_lines):
            op.set_n_pages(1)
        else:
            op.set_n_pages(1 + int(MyWindow.textbuffer.get_line_count() / MyWindow.num_lines))
    def drawpage4(self, operation, context, page_nr=None):
        w = context.get_width()
        h = context.get_height()

        ctx = context.get_cairo_context()
        textpage="Page "+str(1+page_nr)
        self.layoutheader = context.create_pango_layout()
        self.layoutheader.set_width(int(w * Pango.SCALE))
        self.layoutheader.set_height(int(h * Pango.SCALE))
        self.layoutheader.set_font_description(Pango.FontDescription("Times 10"))
        self.layoutheader.set_text(textpage, len(textpage))
        self.layoutfooter = context.create_pango_layout()
        self.layoutfooter.set_width(int(w * Pango.SCALE))
        self.layoutfooter.set_height(int(h * Pango.SCALE))
        self.layoutfooter.set_font_description(Pango.FontDescription("Times 10"))
        self.layoutfooter.set_text(MyWindow.stafilenam, len(MyWindow.stafilenam))

        text=MyWindow.textbuffer.get_text(self.textbuffer.get_iter_at_line((MyWindow.num_lines-2)*page_nr),self.textbuffer.get_iter_at_line((MyWindow.num_lines-2)*(page_nr+1)),True)

        self.layout = context.create_pango_layout()
        self.layout.set_width(int(w * Pango.SCALE))
        self.layout.set_height(int(h * Pango.SCALE))
        self.layout.set_font_description(Pango.FontDescription("Times 10"))
        self.layout.set_text(text, len(text))
        ctx.set_source_rgb(0, 0, 0)
        i = 0
        start = 0
        start_pos = 0
        end=self.layout.get_line_count()
        iter = self.layout.get_iter()
        while 1:
            if i >= start:
                line = iter.get_line_readonly()

                _, logical_rect = iter.get_line_extents()
#                x_bearing, y_bearing, lwidth, lheight = logical_rect
                baseline = iter.get_baseline()

                if i == start:
                    startheight=logical_rect.height
                    start_pos = 12000 / 1024.0  # 1024.0 is float(pango.SCALE)
                    iterheader=self.layoutheader.get_iter()
                    header_rect=iterheader.get_line_extents()
                    baselineheader = iterheader.get_baseline()
                    ctx.move_to(self.layout.get_width() / 2048 - header_rect.logical_rect.width / 2048 , baselineheader / 1024.0 - start_pos)
                    PangoCairo.show_layout_line(ctx, iterheader.get_line_readonly())
                    ctx.move_to(0 / 1024.0, startheight/1024+baseline / 1024.0 - start_pos)
                else:
                    ctx.move_to(0 / 1024.0, startheight/1024+baseline / 1024.0 - start_pos)
                #ctx.move_to(self.layout.get_width() / 2.0 - logical_rect.width / 2.0, baseline / 1024.0 - start_pos)
                #if i==start:


                PangoCairo.show_layout_line(ctx, line)


            i += 1
            if not (i < end and iter.next_line()):
                break

        iterfooter = self.layoutfooter.get_iter()
        footer_rect = iterfooter.get_line_extents()
        baselinefooter = iterfooter.get_baseline()
        ctx.move_to(self.layoutfooter.get_width() / 2048 - footer_rect.logical_rect.width / 2048,
                    h-baselinefooter/1024)
        PangoCairo.show_layout_line(ctx, iterfooter.get_line_readonly())


    def on_print_to_pdf(self,widget):
        #res = print_op.run(Gtk.PrintOperationAction.PRINT_DIALOG, None)
        #res = print_op.run(Gtk.PrintOperationAction.EXPORT, None)  # play with action, but for test export first; if it's ok, then action.PRINT
        dialog = Gtk.FileChooserDialog("Save PDF file", self, Gtk.FileChooserAction.SAVE,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
        dialog.set_do_overwrite_confirmation(True)
        filter1 = Gtk.FileFilter()
        filter2 = Gtk.FileFilter()
        filter1.set_name("PDF files")
        filter1.add_pattern("*.pdf")
        filter2.set_name("All files")
        filter2.add_pattern("*")
        dialog.add_filter(filter1)
        dialog.add_filter(filter2)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            if (dialog.get_filename != ""):
                filenam = dialog.get_filename()
                #if filenam[0:-4]!=".pdf":
                #    filenam+=".pdf"
                ps = Gtk.PaperSize.new_custom("cc", "cc", 210, 297, Gtk.Unit.MM)
                st = Gtk.PrintSettings()
                s = Gtk.PageSetup()
                s.set_paper_size(ps)
                s.set_bottom_margin(4.3, Gtk.Unit.MM)
                s.set_left_margin(4.3, Gtk.Unit.MM)
                s.set_right_margin(4.3, Gtk.Unit.MM)
                s.set_top_margin(4.3, Gtk.Unit.MM)
                s.set_orientation(Gtk.PageOrientation.LANDSCAPE)
                print_op = Gtk.PrintOperation()
                print_op.set_n_pages(3)
                print_op.set_default_page_setup(s)
                print_op.connect("begin_print", self.bg)
                print_op.connect("draw_page", self.draw_page1)
                print_op.set_export_filename(filenam)

                res = print_op.run(Gtk.PrintOperationAction.EXPORT, None)

                dialog.destroy()
            else:
                dialog.destroy()
        else:
                dialog.destroy()
        #pd.set_export_filename("test.pdf")
        #result = pd.run(Gtk.PrintOperationAction.EXPORT, None)  # play with action, but for test export first; if it's ok, then action.PRINT
        #print(result)  # handle errors etc.

    def on_print_clicked(self,widget):
        ps = Gtk.PaperSize.new_custom("cc", "cc", 210, 297, Gtk.Unit.MM)
        st = Gtk.PrintSettings()
        s = Gtk.PageSetup()
        s.set_paper_size(ps)
        s.set_bottom_margin(4.3, Gtk.Unit.MM)
        s.set_left_margin(4.3, Gtk.Unit.MM)
        s.set_right_margin(4.3, Gtk.Unit.MM)
        s.set_top_margin(4.3, Gtk.Unit.MM)
        s.set_orientation(Gtk.PageOrientation.LANDSCAPE)
        print_op = Gtk.PrintOperation()
        print_op.set_n_pages(3)
        print_op.set_default_page_setup(s)
        print_op.connect("begin_print", self.bg)
        print_op.connect("draw_page", self.draw_page1)
        res = print_op.run(Gtk.PrintOperationAction.PRINT_DIALOG, None)
        #print(res)

    def on_copyclipboard_clicked(self,widget):
        #print(MyWindow.textbuffer.get_text(self.textbuffer.get_start_iter(),self.textbuffer.get_end_iter(),True))
        clipboard = Gtk.Clipboard().get(Gdk.SELECTION_CLIPBOARD)
        text=MyWindow.textbuffer.get_text(self.textbuffer.get_start_iter(),self.textbuffer.get_end_iter(),False)
        clipboard.set_text(text, -1)

    def on_cleartext_clicked(self, widget):
        if MyWindow.notebook.get_n_pages() > 0:
            dialog1 = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
                                        Gtk.ButtonsType.YES_NO, "Are you sure ?")
            #dialog1.format_secondary_text("")

            #dialog1.move(1200,700)
            resp = dialog1.run()
            if resp == Gtk.ResponseType.YES:
                MyWindow.textbuffer.set_text("")
                self.initializevalues()

            dialog1.destroy()
    def initializevalues(self):
        MyWindow.stopfile=0
        MyWindow.uarray = []
        MyWindow.larray = []
        MyWindow.totalsum=0
        MyWindow.cos=[]
        MyWindow.cnt = 0
        MyWindow.titl.set_title(MyWindow.windowtitle)
        MyWindow.solveexit=False
        MyWindow.textbuffer.set_text("")
        MyWindow.filename = ""
        MyWindow.line = ""
        MyWindow.cnt = 0
        MyWindow.stafilenam = ""
        MyWindow.alldisplacements =None
        MyWindow.dependendnodes = DynamicArray()
        MyWindow.localnodes = DynamicArray()
        MyWindow.nodes = DynamicArray()
        MyWindow.beams = DynamicArray()
        MyWindow.beamunit = DynamicArray()
        MyWindow.Graph = DynamicArray()
        MyWindow.perm=[]
    #    aa = [[2, 1, 3], [1, 1, 1], [3, 2, 1]]
     #   res = [5, 6, 7]
     #   print(Switcher.SolveUsingLU(self,aa, res))

        MyWindow.current_page = 0
        MyWindow.displacementsindex = []
        MyWindow.displacements = []
        MyWindow.maxN = 0
        MyWindow.maxQ = 0
        MyWindow.maxM = 0
        MyWindow.ksubarray=None
        MyWindow.subresults = None
        MyWindow.fixedresults = None
        MyWindow.karray = None
        MyWindow.subdisplacements = None
        MyWindow.textresultmenu.set_sensitive(False)
        MyWindow.resultstopdf.set_sensitive(False)
        MyWindow.printing.set_sensitive(False)
        MyWindow.copytoclipboard.set_sensitive(False)
        MyWindow.cleartext.set_sensitive(False)
        MyWindow.printtopdf.set_sensitive(False)
        MyWindow.solveframe.set_sensitive(False)
        MyWindow.current_page = 0
        if MyWindow.notebook.get_n_pages() > 0:
            for p1 in range(MyWindow.notebook.get_n_pages()):
                MyWindow.notebook.remove_page(0)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Select Sta file", self, Gtk.FileChooserAction.OPEN,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,         Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        filter1=Gtk.FileFilter()
        filter2=Gtk.FileFilter()
        filter3=Gtk.FileFilter()
        filter1.set_name("Sta files")
        filter1.add_pattern("*.sta")
        filter2.set_name("All files")
        filter2.add_pattern("*")
        dialog.add_filter(filter1)
        dialog.add_filter(filter2)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            if (dialog.get_filename!=""):
                self.initializevalues()
                MyWindow.stafilenam=dialog.get_filename()
                #MyWindow.beamunit = DynamicArray()
                #MyWindow.maxM=0
                #MyWindow.maxQ = 0
                #MyWindow.maxN = 0

                MyWindow.create_node_beam(MyWindow,MyWindow.stafilenam)
#                app_main(MyWindow.stafilenam)

                dialog.destroy()

            else:
                self.filename=""
                self.labelf="No file selected!"
                dialog.destroy()
        else:
            print("Cancel")
            dialog.destroy()
            text = self.entry.get_text(self.textbuffer.get_start_iter(),self.textbuffer.get_end_iter(),True)
            if text.isnumeric() and len(text)>0 and int(text)>0 and len(self.filename)>0:
                self.button1.set_sensitive(True)
            else:
                self.button1.set_sensitive(False)

    def findobject(self,srch,object):
        flag=False
        for e in range(len(object)):
            if object[e].name==srch:
                flag=True
                break
        if flag:
            return e
        else:
            return -1
    def create_node_beam(self,filename):
            file = open(filename, "r")
            # GLib.idle_add(setnewtitle,window,MyWindow.windowtitle+": "+filename)

            # window.set_title(MyWindow.windowtitle+": "+filename)
            # window.set_title("Solve flat frame :"+filename)
            MyWindow.line = "#"
            s = Switcher()
            while MyWindow.line:
                MyWindow.cnt += 1
                MyWindow.line = file.readline()
                if (len(MyWindow.line) > 0 and MyWindow.line[0:1] != "#"):
                    if ((MyWindow.line[0:5].upper() == "Node:".upper()) or MyWindow.line[
                                                                           :-1].upper() == "Node".upper() or MyWindow.lastcommand.upper() == "Node".upper()):
                        MyWindow.lastcommand = "Node".upper()
                        MyWindow.nodes = s.indirect(file)
                        if (type(MyWindow.nodes) is str):
                            MyWindow.whol = "Error" + MyWindow.nodes
                            # return False
                            # self.initializevalues()
                            destroywindow()
                            #GLib.idle_add(destroywindow)
                            file.close()
                            return
                if ((MyWindow.line[0:5].upper() == "Beam:".upper()) or MyWindow.line[
                                                                       :-1].upper() == "Beam".upper() or MyWindow.lastcommand.upper() == "Beam".upper()):
                    MyWindow.lastcommand = "Beam".upper()
                    MyWindow.beams = s.indirect(file)
                    if (type(MyWindow.beams) is str):
                        MyWindow.whol = "Error" + MyWindow.beams
                        # self.initializevalues()
                        destroywindow()
                        #GLib.idle_add(destroywindow)
                        file.close()
                        return
                    break
                            # if ((MyWindow.line[0:9].upper() == "Material:".upper()) or MyWindow.line[
                            #                                               :-1].upper() == "Material:".upper() or MyWindow.lastcommand.upper() == "Material".upper()):

            file.close()
            MyWindow.cleartext.set_sensitive(True)
            MyWindow.label1 = Gtk.Label("Frame")
            MyWindow.firstpass=True
            #MyWindow.perm=Switcher.mc_kee(self,MyWindow.beams)
            #MyWindow.perm=list(range(len(MyWindow.nodes)))
            MyWindow.show_frame(MyWindow)
    def show_frame(self):
        MyWindow.solveframe.set_sensitive(True)
        if MyWindow.notebook.get_n_pages() > 0:
            for p1 in range(MyWindow.notebook.get_n_pages()):
                MyWindow.notebook.remove_page(-1)

        if MyWindow.firstpass:
            MyWindow.stopfile = MyWindow.cnt
            MyWindow.firstpass=False
        MyWindow.notebook.append_page(MyWindow.layout2, MyWindow.label1)
        MyWindow.notebook.set_current_page(0)
        if MyWindow.handler_id>0 and not MyWindow.solveexit:
            MyWindow.layout2.disconnect(MyWindow.handler_id)
        MyWindow.beamunit = DynamicArray()

        MyWindow.handler_id = MyWindow.layout2.connect("draw", MyWindow.createframe)
        MyWindow.layout2.set_size_request(MyWindow.w, MyWindow.h)
        MyWindow.layout2.queue_allocate()
        MyWindow.solveexit = False
        #MyWindow.layout2.show()

        sta = MyWindow.stafilenam
        stasplit = sta.split("/")
        MyWindow.titl.set_title(MyWindow.windowtitle + ": " + stasplit[len(stasplit) - 1])

    def on_solve_clicked(self, widget):
        MyWindow.solveframe.set_sensitive(False)
        MyWindow.layout2.disconnect(MyWindow.handler_id)
        MyWindow.handler_id=0
        app_main(MyWindow.stafilenam)


    def readfile(self,filename):
       file = open(filename, "r")
       #GLib.idle_add(setnewtitle,window,MyWindow.windowtitle+": "+filename)

       cou=0
       while  cou<MyWindow.stopfile-1:#((MyWindow.line[0:9] .upper()!= "Material:".upper()) and MyWindow.line[:-1].upper() != "Material".upper() ):
        MyWindow.line = file.readline()
        cou+=1
       MyWindow.cnt=MyWindow.stopfile
       #window.set_title(MyWindow.windowtitle+": "+filename)
       #window.set_title("Solve flat frame :"+filename)
       #MyWindow.line = "#"
       s = Switcher()
       while MyWindow.line:
           MyWindow.cnt+=1
           MyWindow.line = file.readline()
           if ((MyWindow.line[0:9].upper() == "Material:".upper()) or MyWindow.line[
                                                                :-1].upper() == "Material:".upper() or MyWindow.lastcommand.upper() == "Material".upper()):
               MyWindow.lastcommand = "Material".upper()
               MyWindow.material = s.indirect(file)
               if (type(MyWindow.material) is str):
                    MyWindow.whol = "Error" + MyWindow.material
                    # return False
                    #self.initializevalues()
                    GLib.idle_add(destroywindow)
                    file.close()
                    return
               fl1=False
           if (MyWindow.line[0:11].upper() == "Beam fixing".upper()):
                MyWindow.lastcommand = "Beamfixing".upper()
                MyWindow.beamfixing = s.indirect(file)

                if (type(MyWindow.beamfixing) is str):
                    MyWindow.whol = "Error" + MyWindow.beamfixing
                    # return False
                    #self.initializevalues()
                    GLib.idle_add(destroywindow)
                    file.close()
                    return

                fl1=True
           if (MyWindow.line[0:11].upper() == "Node fixing".upper()):
                    MyWindow.lastcommand = "Nodefixing".upper()
                    MyWindow.nodefixing = s.indirect(file)
                    if (type(MyWindow.nodefixing) is str):
                        MyWindow.whol = "Error" + MyWindow.nodefixing
                        # return False
                        #self.initializevalues()
                        GLib.idle_add(destroywindow)
                        file.close()
                        return
           if (MyWindow.line[0:11].upper() == "Beam fixing".upper() and not fl1):
                MyWindow.lastcommand = "Beamfixing".upper()
                MyWindow.beamfixing = s.indirect(file)

                if (type(MyWindow.beamfixing) is str):
                    MyWindow.whol = "Error" + MyWindow.beamfixing
                    # return False
                    #self.initializevalues()
                    GLib.idle_add(destroywindow)
                    file.close()
                    return

           if not fl1:
               MyWindow.karray = np.zeros((3 * len(MyWindow.nodes), 3 * len(MyWindow.nodes)))
               MyWindow.results = np.zeros(3 * len(MyWindow.nodes))
               MyWindow.fixedresults = np.zeros(3 * len(MyWindow.nodes))
               MyWindow.perm = Switcher.mc_kee(self, MyWindow.beams)
               MyWindow.rowlengths = np.zeros(3 * len(MyWindow.nodes))
               MyWindow.firstindexcolumns = np.zeros(1 + 3 * len(MyWindow.nodes))
               MyWindow.bandcolumnlength = np.zeros((len(MyWindow.beams), 3))
               for j in range(len(MyWindow.beams)):
                   i1 = MyWindow.perm.index(MyWindow.findobject(MyWindow, MyWindow.beams[j].StartNode, MyWindow.nodes))
                   i2 = MyWindow.perm.index(MyWindow.findobject(MyWindow, MyWindow.beams[j].EndNode, MyWindow.nodes))
                   if i1 > i2:
                       temp = i1
                       i1 = i2
                       i2 = temp
                   MyWindow.bandcolumnlength[j][0] = int(j)
                   MyWindow.bandcolumnlength[j][1] = int(i1)
                   MyWindow.bandcolumnlength[j][2] = int(i2)
                   if MyWindow.rowlengths[i1 * 3] == 0:
                       MyWindow.rowlengths[i1 * 3] = int(1)
                       MyWindow.rowlengths[i1 * 3 + 1] = int(2)
                       MyWindow.rowlengths[i1 * 3 + 2] = int(3)
                   if (i2 - i1) * 3 + 1 > MyWindow.rowlengths[i2 * 3]:
                       MyWindow.rowlengths[i2 * 3] = int((i2 - i1) * 3 + 1)
                       MyWindow.rowlengths[i2 * 3 + 1] = int((i2 - i1) * 3 + 2)
                       MyWindow.rowlengths[i2 * 3 + 2] = int((i2 - i1) * 3 + 3)

                   # print (str(j)+"     "+str(i1)+"      "+str(i2))
                   # +" ="+str(i2-i1))
               s1 = 0
               MyWindow.bandcolumnlength = MyWindow.bandcolumnlength[MyWindow.bandcolumnlength[:, 2].argsort()]
               MyWindow.bandcolumnlength = MyWindow.bandcolumnlength[
                   MyWindow.bandcolumnlength[:, 1].argsort(kind='mergesort')]
               # print("{0:4d} {1:4d}".format(int(0), int(MyWindow.firstindexcolumns[0])))
               MyWindow.firstindexcolumns[0] = 0
               for j in range(1, 3 * len(MyWindow.localnodes) + 1):
                   s1 += MyWindow.rowlengths[j - 1]
                   MyWindow.firstindexcolumns[j] = s1
               #    print ("{0:5d} {1:4d} {2:4d}".format (int(j),int(MyWindow.rowlengths[j-1]),int(s1)))

               MyWindow.resp = np.zeros(3 * len(MyWindow.nodes))
               # print ("{0:4d}".format(int(np.sum(MyWindow.rowlengths))))
               MyWindow.totalsum = int(np.sum(MyWindow.rowlengths))
               MyWindow.uarray = np.zeros(MyWindow.totalsum)
               MyWindow.larray = np.zeros(MyWindow.totalsum)
               MyWindow.totalsum = int(np.sum(MyWindow.rowlengths))
            #Switcher.addglobalstiffnessmatrix(self)
               Switcher.addglobalstiffnessmatrixcompact(self)
           if ((MyWindow.line[0:6].upper() == "Loads:".upper()) or MyWindow.line[
                                                               :-1].upper() == "Loads:".upper() or MyWindow.lastcommand.upper() == "Loads".upper()):
                    MyWindow.lastcommand = "Loads".upper()
                    MyWindow.loads = s.indirect(file)
                    if (type(MyWindow.loads) is str):
                        MyWindow.whol = "Error" + MyWindow.loads
                        # return False
                        #self.initializevalues()
                        GLib.idle_add(destroywindow)
                        file.close()
                        return


       file.close()
       wholestring=""
       #Creating reduced matrix and reduced matrix results, applying boundary conditions
       #Delete rows
       #MyWindow.ksubarray=[]

      # MyWindow.ksubarray=np.delete(MyWindow.karray,MyWindow.displacementsindex,0)
       # Delete columns
       #MyWindow.ksubarray = np.delete(MyWindow.ksubarray, MyWindow.displacementsindex, 1)
       #We have to subtract initial array columns that relate with the displacements from  reduced results matrix
       proslist=[]

           # Subtracting beam forces from nodes

       MyWindow.newresults=MyWindow.results
       MyWindow.results = np.add(MyWindow.fixedresults, MyWindow.results)
       for k in range(0,len(MyWindow.perm)):
           MyWindow.newresults[MyWindow.perm.index(k)*3]=MyWindow.results[k*3]
           MyWindow.newresults[MyWindow.perm.index(k) * 3+1] = MyWindow.results[k* 3+1]
           MyWindow.newresults[MyWindow.perm.index(k)* 3 + 2] = MyWindow.results[k* 3 + 2]
       MyWindow.results=MyWindow.newresults
       displacementsindex1=[]
       for k in MyWindow.displacementsindex:
           displacementsindex1.append(3*MyWindow.perm.index((int(k/3)))+k%3)
       MyWindow.displacementsindex=displacementsindex1
       for e in MyWindow.displacementsindex:
      #Subtracting all k eleaments from results
          #for ind in range(len(MyWindow.results)):
            #i1 instead e
          i1=e
          #i1=3*MyWindow.perm[int(e/3)]+(e%3)
          plithos=int(MyWindow.firstindexcolumns[i1+1]-MyWindow.firstindexcolumns[i1])
          for ind in range(0,plithos):
            #if e-plithos+ind+1!=MyWindow.displacementsindex.index(e):
                #MyWindow.results[ind]-=MyWindow.array[ind][e]*MyWindow.displacements[MyWindow.displacementsindex.index(e)]
             MyWindow.results[i1-plithos+ind+1] -= MyWindow.uarray[int(MyWindow.firstindexcolumns[i1]+ind)] * MyWindow.displacements[MyWindow.displacementsindex.index(i1)]
          for ind in range(i1+1,len(MyWindow.results)):
            plithos1 = int(MyWindow.firstindexcolumns[ind + 1] - MyWindow.firstindexcolumns[ind])
            offs=ind-i1
            if offs<=plithos1:
                MyWindow.results[ind] -= MyWindow.uarray[int(MyWindow.firstindexcolumns[ind+1]-1+i1-ind )] *    MyWindow.displacements[MyWindow.displacementsindex.index(i1)]
       MyWindow.alldisplacements = np.zeros(3 * len(MyWindow.nodes))
       #if ((MyWindow.ksubarray.shape[0]==0) and (MyWindow.ksubarray.shape[1]==0)):
       MyWindow.whol = ""
           # MyWindow.initializevalues(MyWindow)
           #MyWindow.subresults = np.delete(MyWindow.results, MyWindow.displacementsindex, 0)
       if (np.count_nonzero(MyWindow.results, axis=None)==0):
           MyWindow.whol = "Error" + "No loads defined"
           # return False
           #MyWindow.initializevalues(MyWindow)
           GLib.idle_add(destroywindow)
           return
       else:
           try:
               #f = open("/home/use47/Downloads/perm.txt", "w")
               #for cc1 in range(0, 18):

                #   for cc2 in range(0, 18):
                        #f.write("{:3d}".format(MyWindow.perm.index(int(cc/3))))
                 #        f.write("{:3f} ".format(MyWindow.karray[cc1,cc2]))
                  # f.write("\n")
               #f.close()
               MyWindow.alldisplacements = Switcher.Crout(self, MyWindow.uarray, MyWindow.results)
                #al1=np.zeros(len(MyWindow.alldisplacements))
                #for i in range(0,len(MyWindow.perm)):
                #    al1[MyWindow.perm.index(i)*3]=MyWindow.alldisplacements[3*i]
                #    al1[MyWindow.perm.index(i) * 3+1] = MyWindow.alldisplacements[1+3 *i]
                #    al1[MyWindow.perm.index(i) * 3 + 2] = MyWindow.alldisplacements[2 + 3 * i]
                #for g in range(0,len(MyWindow.alldisplacements)):
                #    MyWindow.alldisplacements[g]=al1[g]
                #MyWindow.subdisplacements = Switcher.SolveUsingLUfp(self, MyWindow.ksubarray, MyWindow.subresults)
           except Exception as e:
                MyWindow.alldisplacements = None
                MyWindow.whol = "Error" + " "+str(e)
           # return False
           #self.initializevalues()
                GLib.idle_add(destroywindow)
           #self.initializevalues(self)
                return
       if MyWindow.solveexit:
           MyWindow.whol = ""
           #MyWindow.initializevalues(MyWindow)
           GLib.idle_add(destroywindow)

           return




           #//MyWindow.results = MyWindow.subresults
           #if len(proslist)>0:
            #   MyWindow.subdisplacements=  np.zeros(len(MyWindow.subdisplacementsapom) + len(proslist))
             #  newind = 0
             #  newinde = 0
             #  for ind in range(len(MyWindow.subdisplacementsapom) + len(proslist)):
             #      try:
             #          MyWindow.subdisplacements[ind] = MyWindow.subdisplacements[proslist.index(ind)]
             #      except ValueError:
             #          MyWindow.subdisplacements[ind] = MyWindow.subdisplacementsapom[newinde]
             #          newinde += 1
           #else:
                #MyWindow.subdisplacements=[]


           #newinde=0
           #try:
           #    for ind in range(0,len(MyWindow.subdisplacements)+len(MyWindow.displacements)):
           #        try:
           #             MyWindow.alldisplacements[ind] = MyWindow.displacements[MyWindow.displacementsindex.index(ind)]

           #        except ValueError:
           #             MyWindow.alldisplacements[ind] = MyWindow.subdisplacements[newinde]
           #             newinde += 1
           #except TypeError:
           #    return


       #for o in range(0, len(MyWindow.perm), 3):
        #   temp=MyWindow.alldisplacements[int(o/3)]
        #   MyWindow.alldisplacements[o]=MyWindow.alldisplacements[MyWindow.perm.index(int(o/3))*3]
        #   MyWindow.alldisplacements[MyWindow.perm[int(o/3)] * 3]=temp
        ##   MyWindow.alldisplacements[o] = MyWindow.alldisplacements[MyWindow.perm.index(int(o/3)) * 3+1]
         #  MyWindow.alldisplacements[MyWindow.perm[int(o/3)] * 3+1] = temp
          # temp = MyWindow.alldisplacements[o*3 + 2]
          # MyWindow.alldisplacements[o] = MyWindow.alldisplacements[MyWindow.perm.index(int(o/3))* 3 + 2]
          # MyWindow.alldisplacements[MyWindow.perm.index(int(o/3))* 3 + 2] = temp

       wholestring+="Displacements\n"
       #print(MyWindow.alldisplacements)
       for nodes in range(len(MyWindow.nodes)):
        nam1=MyWindow.nodes[nodes].name
        if ("_" in nam1[-3:]):
            for k1 in range(0,len(MyWindow.beams)):
                if (nam1==MyWindow.beams[k1].StartNode or nam1==MyWindow.beams[k1].EndNode):
                    break
            nam1=nam1[:-3]

            nam1=nam1+ "     (Beam "+ MyWindow.beams[k1].name+")"
        wholestring+="Node "+str(nam1)+"\n"
        txtN = "DX=  {:.6f} millimeters"
        txtQ = "DY=  {:.6f} millimeters"
        txtM = "Dt=  {:.6f} milliradians"
        txtNodeX=" (X,Y)=({:.3f},"
        txtNodeY = "{:.3f})"
        wholestring+=(txtN.format(1000.0*MyWindow.alldisplacements[MyWindow.perm.index(nodes)*3+0]) + " " + txtQ.format(1000.0*MyWindow.alldisplacements[MyWindow.perm.index(nodes) * 3 + 1])+" "+txtM.format(1000.0*MyWindow.alldisplacements[MyWindow.perm.index(nodes) * 3 + 2]))
        if not MyWindow.nodes[nodes].name.__contains__("SPRING"):
                     wholestring+=txtNodeX.format(MyWindow.nodes[nodes].X)+txtNodeY.format(MyWindow.nodes[nodes].Y)+"\n"
        else:
                     wholestring +=  "\n"
       #Switcher.resultforces(MyWindow)
       #MyWindow.externalforces =np.dot(MyWindow.karray,MyWindow.alldisplacements)-MyWindow.fixedresults-MyWindow.newresults
       MyWindow.externalforces=Switcher.resultforces(MyWindow)
       for k in range(len(MyWindow.externalforces)):
           if math.fabs(MyWindow.externalforces[k])<0.01:
               MyWindow.externalforces[k]=0.0
       wholestring +="Forces\n"
       wholestring +="Counterclockwise notation\n"
       for nodes in range(len(MyWindow.nodes)):
           if ("_" in nam1[-3:]):
            for k1 in range(0, len(MyWindow.beams)):
                if (nam1 == MyWindow.beams[k1].StartNode or nam1 == MyWindow.beams[k1].EndNode):
                    break
            nam1 = nam1[:-3]
            nam1 = nam1 + "     (Beam " + MyWindow.beams[k1].name + ")"
            wholestring+="Node "+str(nam1)+"\n"
            txtN = "X=  {:.6f} kN"
            txtQ = "Y=  {:.6f} kN"
            txtM = "M=  {:.6f} kNm"
            #wholestring+=(txtN.format(MyWindow.externalforces[MyWindow.perm[nodes]*3+0]/1000.0) + " " + txtQ.format(MyWindow.externalforces[MyWindow.perm[nodes] * 3 + 1]/1000.0)+" "+txtM.format(MyWindow.externalforces[MyWindow.perm[nodes] * 3 + 2]/1000.0))+"\n"
            wholestring += (txtN.format(
                MyWindow.externalforces[MyWindow.perm.index(nodes) * 3 + 0] / 1000.0) + " " + txtQ.format(
                MyWindow.externalforces[MyWindow.perm.index(nodes) * 3 + 1] / 1000.0) + " " + txtM.format(
                MyWindow.externalforces[MyWindow.perm.index(nodes) * 3 + 2] / 1000.0)) + "\n"
            wholestring += ("--------------------------------------------------------------------------------------------------------------------------------------\n")
       MyWindow.kbeam=np.zeros((6,6))
       MyWindow.beamdisplacements=np.zeros(6)
       MyWindow.beamForces=DynamicArray()
       wholestring += "Free body notation\n"
       if len(MyWindow.beamunit)>0:
           MyWindow.beamunit=DynamicArray()
       for e in range(len(MyWindow.beams)):
           beamname = MyWindow.beams[e].name
           # Search at the beam which nodes connect
           beamnameindex = MyWindow.findobject(self, beamname, MyWindow.beams)
           beamstartnode = MyWindow.beams[beamnameindex].StartNode
           startNodeIndex1 = MyWindow.findobject(self, beamstartnode, MyWindow.nodes)
           beamendnode = MyWindow.beams[beamnameindex].EndNode
           endNodeIndex1 = MyWindow.findobject(self, beamendnode, MyWindow.nodes)
           if ("_" in beamendnode[-3:]):
            beamendnode = beamendnode[:-3]
           if ("_" in beamstartnode[-3:]):
            beamstartnodebeamstartnode = beamstartnode[:-3]
           transf = np.zeros((6, 6))
           if not beamstartnode.find("SPRING") > -1:
                El = MyWindow.beams[beamnameindex].Elasticity
                lbeam = math.sqrt(
                math.pow(MyWindow.beams[beamnameindex].xl, 2.0) + math.pow(MyWindow.beams[beamnameindex].yl,2.0))
                A = MyWindow.beams[beamnameindex].Area
                xl = MyWindow.beams[beamnameindex].xl
                yl = MyWindow.beams[beamnameindex].yl
                c = xl / lbeam
                s = yl / lbeam
                I = MyWindow.beams[beamnameindex].Inertia
                transf[0][0] = c
                transf[0][1] = s
                transf[1][0] = -s
                transf[1][1] = c
                transf[2][2] = 1.0
                transf[3][3] = c
                transf[3][4] = s
                transf[4][3] = -s
                transf[4][4] = c
                transf[5][5] = 1.0
                Switcher.kbeamcomputations(self, El, I, A, lbeam, MyWindow.beams[beamnameindex].regflag, beamname)
           else:
               k = MyWindow.beams[beamnameindex].Elasticity
               xl = MyWindow.beams[beamnameindex].xl
               c = math.cos(xl* math.pi/180)
               s = math.sin(xl* math.pi/180)
               transf[0][0] = c
               transf[0][1] = s
               transf[1][0] = -s
               transf[1][1] = c
               transf[2][2] = 1.0
               transf[3][3] = c
               transf[3][4] = s
               transf[4][3] = -s
               transf[4][4] = c
               transf[5][5] = 1.0
               Switcher.kspringcomputations(self, k)
           startNodeIndex = 0
           endNodeIndex = 1
           #MyWindow.k = np.delete(MyWindow.karray, MyWindow.displacementsindex, 0)

           MyWindow.beamdisplacements[0] = MyWindow.alldisplacements[3*MyWindow.perm.index(startNodeIndex1)]
           MyWindow.beamdisplacements[1] = MyWindow.alldisplacements[3*MyWindow.perm.index(startNodeIndex1)+ 1]
           MyWindow.beamdisplacements[2] = MyWindow.alldisplacements[3*MyWindow.perm.index(startNodeIndex1) + 2]
           MyWindow.beamdisplacements[3] = MyWindow.alldisplacements[3*MyWindow.perm.index(endNodeIndex1)]
           MyWindow.beamdisplacements[4] = MyWindow.alldisplacements[3*MyWindow.perm.index(endNodeIndex1) + 1]
           MyWindow.beamdisplacements[5] = MyWindow.alldisplacements[3*MyWindow.perm.index(endNodeIndex1) + 2]

           MyWindow.beamdisplacements = np.dot(transf, MyWindow.beamdisplacements)

           MyWindow.beamfixedlocalforces=np.zeros(6)

           MyWindow.beamfixedlocalforces[0] = MyWindow.beams[e].N1
           MyWindow.beamfixedlocalforces[1] = MyWindow.beams[e].Q1
           MyWindow.beamfixedlocalforces[2] = MyWindow.beams[e].M1
           MyWindow.beamfixedlocalforces[3] = MyWindow.beams[e].N2
           MyWindow.beamfixedlocalforces[4] = MyWindow.beams[e].Q2
           MyWindow.beamfixedlocalforces[5] = MyWindow.beams[e].M2

           #MyWindow.beamfixedlocalforces = np.dot(transf, MyWindow.beamfixedlocalforces)
           #Make beam stiffness matrix
           MyWindow.localforces = np.zeros(6)
           MyWindow.localforces = np.subtract(np.dot(MyWindow.kbeam, MyWindow.beamdisplacements),MyWindow.beamfixedlocalforces)
           #MyWindow.beamForces.append(MyWindow.localforces)
           wholestring+= ("Beam :" +beamname + " connects nodes "+beamstartnode+ " and "+beamendnode)+"\n"
           wholestring+= ("Beam forces\n")
           #with np.printoptions(precision=3, suppress=True):
           # print(MyWindow.localforces)
           #print("Node " + str(MyWindow.nodes[startNodeIndex1].name))
           if ("_" in MyWindow.nodes[startNodeIndex1].name[-3:]):
            startnodename = MyWindow.nodes[startNodeIndex1].name[:-3]
           else:
            startnodename = MyWindow.nodes[startNodeIndex1].name
           txtN = "N"+startnodename+"=  {:.2f} kN"
           txtQ = "Q"+startnodename+"=  {:.2f} kN"
           txtM = "M"+startnodename+"=  {:.2f} kNm"


           if ("_" in MyWindow.nodes[endNodeIndex1].name[-3:]):
               endnodename = MyWindow.nodes[endNodeIndex1].name[:-3]
           else:
               endnodename = MyWindow.nodes[endNodeIndex1].name
           if ((startnodename.find("SPRING")==-1) and (endnodename.find("SPRING")==-1)):
               wholestring += (txtN.format(-MyWindow.localforces[0 * 3 + 0] / 1000.0) + " " + txtQ.format(
                   MyWindow.localforces[0 * 3 + 1] / 1000.0) + " " + txtM.format(-MyWindow.localforces[0 * 3 + 2] / 1000.0))
           else:
               wholestring += (txtN.format(-MyWindow.localforces[0 * 3 + 0] / 1000.0))
           wholestring += "\n"


           txtN = "N"+endnodename+"=  {:.2f} kN"
           txtQ = "Q"+endnodename+"=  {:.2f} kN"
           txtM = "M"+endnodename+"=  {:.2f} kNm"
           if ((startnodename.find("SPRING") == -1) and (endnodename.find("SPRING") == -1)):
               wholestring+=(txtN.format(MyWindow.localforces[1 * 3 + 0]/1000.0) + " " + txtQ.format(
                    -MyWindow.localforces[1 * 3 + 1]/1000.0) + " " + txtM.format(MyWindow.localforces[1 * 3 + 2]/1000.0))
           else:
               wholestring += (txtN.format(MyWindow.localforces[1 * 3 + 0] / 1000.0))
           wholestring += "\n"
           if abs(-MyWindow.localforces[0*3+0])>MyWindow.maxN:
               MyWindow.maxN=abs(-MyWindow.localforces[0*3+0])
           if abs(MyWindow.localforces[1 * 3 + 0]) > MyWindow.maxN:
               MyWindow.maxN = abs(MyWindow.localforces[1 * 3 + 0])
           if abs(MyWindow.localforces[0*3+1])>MyWindow.maxQ:
               MyWindow.maxQ=abs(MyWindow.localforces[0*3+1])
           if abs(MyWindow.localforces[1 * 3 + 1]) > MyWindow.maxQ:
               MyWindow.maxQ = abs(-MyWindow.localforces[1 * 3 + 1])
           if abs(-MyWindow.localforces[0*3+2])>MyWindow.maxM:
               MyWindow.maxM=abs(MyWindow.localforces[0*3+2])
           if abs(MyWindow.localforces[1 * 3 + 2]) > MyWindow.maxM:
               MyWindow.maxM = abs(-MyWindow.localforces[1 * 3 + 2])
           MyWindow.beamunit.append(Beamunit(beamname,-MyWindow.localforces[0 * 3 + 0],MyWindow.localforces[0 * 3 + 1],-MyWindow.localforces[0 * 3 + 2],MyWindow.localforces[1 * 3 + 0],-MyWindow.localforces[1 * 3 + 1],MyWindow.localforces[1 * 3 + 2]))

       #This is for the diagrams
       for e in range(len(MyWindow.beamunit)):
           if math.fabs(MyWindow.maxN)>1e-6!=0:
                MyWindow.beamunit[e].N1 /= MyWindow.maxN
                MyWindow.beamunit[e].N2 /= MyWindow.maxN
           else:
               MyWindow.beamunit[e].N1 =0
               MyWindow.beamunit[e].N2 =0
           if math.fabs(MyWindow.maxQ)>1e-6:
                MyWindow.beamunit[e].Q1 /= MyWindow.maxQ
                MyWindow.beamunit[e].Q2 /= MyWindow.maxQ
           else:
               MyWindow.beamunit[e].Q1 =0
               MyWindow.beamunit[e].Q2 = 0
           if math.fabs(MyWindow.maxM)>1e-6 :
             MyWindow.beamunit[e].M1 /= MyWindow.maxM
             MyWindow.beamunit[e].M2 /= MyWindow.maxM
           else:
             MyWindow.beamunit[e].M1 =0
             MyWindow.beamunit[e].M2 =0
       MyWindow.whol=wholestring
       #return False
       GLib.idle_add(destroywindow)

       return

    def showerror(self, wholestring):
        dialog1 = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                    Gtk.ButtonsType.OK, "Attention")
        dialog1.format_secondary_text(
            wholestring[5:])
        resp = dialog1.run()

        dialog1.destroy()
    def showresults(self,wholestring):
       MyWindow.textbuffer.set_text(wholestring)
       if MyWindow.notebook.get_n_pages()>0:
        for p1 in range(MyWindow.notebook.get_n_pages()):
           MyWindow.notebook.remove_page(0)
       MyWindow.notebook.append_page(MyWindow.layout1, Gtk.Label("Results"))
       MyWindow.notebook.append_page(MyWindow.layout5, Gtk.Label("Loads"))
       MyWindow.notebook.append_page(MyWindow.layout6, Gtk.Label("Reactions"))
       MyWindow.notebook.append_page(MyWindow.layout7, Gtk.Label("Displacements"))
       MyWindow.notebook.append_page(MyWindow.layout2, Gtk.Label("Moments"))
       MyWindow.notebook.append_page(MyWindow.layout3, Gtk.Label("Shear"))
       MyWindow.notebook.append_page(MyWindow.layout4, Gtk.Label("Axial"))
       MyWindow.notebook.set_current_page(MyWindow.current_page)
       MyWindow.printing.set_sensitive(True)
       MyWindow.resultstopdf.set_sensitive(True)
       MyWindow.textresultmenu.set_sensitive(True)
       MyWindow.copytoclipboard.set_sensitive(True)
       MyWindow.printtopdf.set_sensitive(True)
       if MyWindow.handler_id>0:
           MyWindow.layout2.disconnect(MyWindow.handler_id)
       MyWindow.handler_id = MyWindow.layout2.connect("draw", MyWindow.OnDrawlM)
       MyWindow.layout5.connect("draw", MyWindow.OnDrawlLoads)
       MyWindow.layout6.connect("draw", MyWindow.OnDrawlReactions)
       MyWindow.layout7.connect("draw", MyWindow.OnDrawDisplacements)

       MyWindow.layout3.connect("draw", MyWindow.OnDrawlQ)
       MyWindow.layout4.connect("draw", MyWindow.OnDrawlN)
       MyWindow.layout1.show()
       MyWindow.layout2.show()
       MyWindow.layout3.show()
       MyWindow.layout4.show()
       MyWindow.layout5.show()
       MyWindow.layout6.show()
       MyWindow.layout7.show()
       while Gtk.events_pending():

           Gtk.main_iteration()

       window.queue_allocate()



    def end_quit(self):
        tt=1



    def on_buttoncancel(self):
        MyWindow.solveexit=True
        #MyWindow.titl.set_title(MyWindow.windowtitle)

        #MyWindow.wi.destroy()
def app_main(sta):
    MyWindow.wi=Gtk.Window(default_height=50, default_width=200,title="Solving Static Frame", transient_for=window)
    MyWindow.wi.set_modal(True)
    grid = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL)
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL);
    box.pack_start(grid, False, False, 12);
 #   threading.threads_init()
    MyWindow.wi.connect("destroy", MyWindow.end_quit)
    MyWindow.progress = Gtk.ProgressBar(show_text=True)
    MyWindow.buttoncancel = Gtk.Button(label="Cancel")
    MyWindow.buttoncancel.connect("clicked", MyWindow.on_buttoncancel)
    MyWindow.buttoncancel.props.margin_top=10
    grid.add(MyWindow.progress)
    grid.add(MyWindow.buttoncancel)
    grid.attach(MyWindow.buttoncancel, 1,0, 20,20)
    box.add(grid)
    grid.props.margin = 10
    MyWindow.wi.add(box)



    #window.set_transient_for(MyWindow.wi)
    MyWindow.wi.show_all()

    MyWindow.wi.set_focus()
    thread = threading.Thread(target=MyWindow.readfile, args=[MyWindow, sta])
    thread.daemon = True
    thread.start()


def destroywindow():
    if (MyWindow.wi.get_property("visible")):
        MyWindow.wi.destroy()
#    MyWindow.solveexit = True


    MyWindow.solveexit = False
    if MyWindow.whol[0:5] == "Error":
            dialog1 = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR,
                                        Gtk.ButtonsType.OK, "Attention")
            dialog1.format_secondary_text(
                MyWindow.whol[5:])
            resp = dialog1.run()
            dialog1.destroy()
    if  (MyWindow.whol[0:5] != "Error") :
        MyWindow.solveexit = False
        if MyWindow.notebook.get_n_pages() > 0:
            for p1 in range(MyWindow.notebook.get_n_pages()):
                MyWindow.notebook.remove_page(0)

        MyWindow.showresults(MyWindow, MyWindow.whol)

        return False
    if len(MyWindow.whol)==0 or MyWindow.whol[0:5] == "Error" :
        MyWindow.cleartext.set_sensitive(True)
        MyWindow.Graph = DynamicArray()
        MyWindow.displacementsindex = []
        if MyWindow.whol[0:5] != "Error":
            MyWindow.layout2.disconnect(MyWindow.handler_id)
        MyWindow.handler_id=0
        MyWindow.displacements = []
        MyWindow.maxN = 0
        MyWindow.maxQ = 0
        MyWindow.maxM = 0
        #MyWindow.karray = np.zeros((3 * len(MyWindow.localnodes), 3 * len(MyWindow.localnodes)))
        MyWindow.results = np.zeros(3 * len(MyWindow.localnodes))
        MyWindow.fixedresults = np.zeros(3 * len(MyWindow.localnodes))
        MyWindow.beamunit=DynamicArray()

        for beamnameindex in range(0,len(MyWindow.beams)):
            MyWindow.beams[beamnameindex].N1 = 0
            MyWindow.beams[beamnameindex].Q1 = 0
            MyWindow.beams[beamnameindex].M1 = 0
            MyWindow.beams[beamnameindex].N2 = 0
            MyWindow.beams[beamnameindex].Q2 = 0
            MyWindow.beams[beamnameindex].M2 = 0
        MyWindow.show_frame(MyWindow)
    else:

        MyWindow.solveexit = False
        if MyWindow.notebook.get_n_pages() > 0:
            for p1 in range(MyWindow.notebook.get_n_pages()):
                MyWindow.notebook.remove_page(0)

        MyWindow.showresults(MyWindow, MyWindow.whol)

    #    MyWindow.initializevalues(MyWindow)
    return False
def prog(i):
    MyWindow.progress.set_fraction(i)

    #MyWindow.progress.set_text(str(i))
    return False
builder = Gtk.Builder()
#print(os.path.realpath(sys.argv[0][0:1+(sys.argv[0].rfind("/"))])+"/"+"GUInterface.glade")
builder.add_from_file(os.path.realpath(sys.argv[0][0:1+(sys.argv[0].rfind("/"))])+"/"+"GUInterface.glade")
#builder.add_from_file("GUInterface.glade")
window = builder.get_object("window1")
window.connect("destroy",Gtk.main_quit)
window = MyWindow()
Gtk.main()
