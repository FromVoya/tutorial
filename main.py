class Image:
    def __init__(self,width,height,background="."):
        self.__background=background
        self.__pixels={}
        self.__width=width
        self.__height=height
        self.__colour={self.__background}
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.width=width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, height):
        self.__height = height
    def __checkCoord(self,coord):
        if not isinstance(coord,tuple) or len(coord)!=2:
            raise KeyError("Значение точки должно быть двумерным кортежом")
        if not (0<=coord[0] < self.__width) or not (0<=coord[1]< self.__height):
            raise KeyError("Згачение координаты выходит за пределы изобржения")

    def __setitem__(self, coord, color):
        self.__checkCoord(coord)
        if color==self.__background:
            self.__pixels.pop(coord,None)
        else:
            self.__pixels[coord]=color
            self.__colour.add(color)
    def __getitem__(self, coord):
        self.__checkCoord(coord)
        return self.__pixels.get(coord,self.__background)



img=Image(20,4)
img[1,1]="*";img[2,1]="*";img[3,1]="*"
for y in range(img.height):
    for x in range(img.width):
        print(img[x,y],sep=" ",end=" ")
    print()