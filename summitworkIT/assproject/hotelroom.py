import pymysql

class Room:
    #theRooms=[]
    def __init__(self,roomNum,bedType,smoking,rate, **args): ## **args to supply another argument if we want
        self.roomNum=roomNum
        self.bedType=bedType
        self.rate=rate
        self.occupantName="Not Occupied" # At the creation of the room
        self.smoking=smoking #{"s","n"}
        self.occupied=False
        #self.theRooms.append()

    def getBedType(self): #String
        return self.bedType
    def getSmoking(self):# char#{"s" or "n"}
        return self.smoking
    def getRoomNum(self):
        return self.roomNum
    def getRoomRate(self):
        return self.rate

    def getOccupant(self):
        return self.occupantName

    def setOccupied(self,occupied):
        self.occupied=occupied
    def setOccupant(self, occupantName):
        if occupantName!="Not occupied" or len(occupantName)==0:
            self.occupantName= occupantName
        else:
            self.occupantName ="Not occupied"

    def setRoomNum(self, roomNum):
        self.roomNum=roomNum

    def setBedType(self, bedType):
        self.bedType=bedType

    def setRate(self, rate):
        self.rate=rate

    def setSmoking(self, smoking):
        self.smoking=smoking
    def isOccupied(self):
        #Let suppose here that the room is occupied
        # so the occupant name is given and the length of the name
        # can not be 0. at least 2 chars
        self.occupied=False if self.occupantName=="not occupied" else True
        return self.occupied

    def __str__(self):
        print("Room Details are:\n")
        print("\nRoom Number:", self.roomNum, "\nOccupant name:", self.occupantName, "\nSmoking:", self.smoking, "\nBed Type:", self.bedType, "\nRate:", str(self.rate))
c= Room(5, "queen","s", 1)
print(c.__str__())
####################################################################
#           Database                      #
####################################################################

db = pymysql.connect("localhost","root","mypaaword","projecthotel")
cursor=db.cursor()

tableroom="""Create table room(
roomNum int(5),
bedType varchar(25),
smoking char(1),
rate double,
);"""
tablehotel="""Create table hotel(
name varchar(50), 
location varchar(50),
occupiedCnt int(5), 
numOfRooms int(5)
);"""
cursor.execute(tableroom)
db.commit()
cursor.execute(tablehotel)
#choicedb="use projecthotel"
# Insert a object room ceated
# Value for the room table
rnum=c.getRoomNum()
bt=c.getBedType()
sm=c.getSmoking()
rt=c.getRoomRate()
insertInroom="""insert into room(roomNum, bedType, smoking, rate) values(:rnum, :bt, :sm, :rt)"""
# Get all the rooms in the hotel: theRooms:[....]
selectallrooms="""select * from room; """
#
#cursor.execute()
selectallHotels="""select * from hotel; """
cursor.execute(selectallrooms)
db.commit()
fetchall=cursor.fetchall()
rr=[print(row) for row in fetchall ]

cursor.execute(selectallHotels)
db.commit()
fetchall=cursor.fetchall()
hh=[print(row) for row in fetchall]

##################################################################
##################################################################

class Hotel(Room):

    def __init__(self, theRooms, name, location,occupiedCnt, numOfRooms, **args):
        super().__init__(roomNum, bedType, smoking,rate)
        self.theRooms=theRooms
        self.name=name
        self.location=location
        self.occupiedCnt=occupiedCnt
        self.numOfRooms=numOfRooms

    def gettheRooms(self):
        selectallrooms = """select * from room; """
        #
        #selectallHotels = """select * from hotel; """
        mr = cursor.execute(selectallrooms)
        db.commit()
        fetchallrooms = cursor.fetchall()
        ##rr = [print(row) for row in fetchallrooms]
        return fetchallrooms

    def isFull(self):# boolean
        #g=lambda: self.theRooms
        if self.occupiedCnt==len(self.theRooms):
            return True
        return False
        # isfull=True
        # for room in self.theRooms:
        #     if room.occupied ==False: #
        #         isfull=False
        #         break
        #         return False
        #     return True

    #def countOccupied(self):

    def isEmpty(self): #boolean
        if self.occupiedCnt==0: # if the count is null
            return True
        return False


    def addRoom(self, roomnumber, bedtype, smoking, price):
        super().__init__(roomnumber, bedtype, smoking, price)
        self.gettheRooms().append(super.init(roomnumber, bedtype, smoking, price))

    def addReservation(self, occupantName, smoking, bedtype):

        for room in self.gettheRooms():
            if room.getSmoking()==self.smoking and room.getBedType()==self.bedtype and room.getOccupant()=="Not Occupied":
                 room.setOccupied(True)
                 room.setOccupant(self.occupantName)
                 print("Reservation made, ")
                 break
            else:
                 print("No reservation made, we do not have re room required")

    def __cancelReservation(self, occupantName):
        rnm=""
        for room in [ ro for ro in self.gettheRooms() if ro.getOccupant()!="Not Occupied"]:
            if room.getOccupant()==self.occupantName:
                print("Reservation successfully canceled")
                rnm=str(room.getRoomNum())
                break

            ##print("Reservation cancelation failled. No reservation with the given name: ", self.occupantName, " in the system")
            print("NOT_FOUND = -1")
        return rnm

    def findReservation(self, occupantName):
        occupiedrooms=[ro for ro in self.gettheRooms() if ro.getOccupant()!="Not Occupied"]
        index_room="NOT_FOUND"
        for room in occupiedrooms:
            if room.getOccupant()==self.occupantName:
                index_room=str(room.getRoomNum())
                break
        return index_room



    def printReservationList(self):
        for room in [ro for ro in self.gettheRooms() if ro.getOccupant()!="Not Occupied"]:
            #print("Room Number:", room.getRoomNum(), "\nOccupant name:", room.getOccupant(), "\nSmoking room:", room.getSmoking(),"\nBed Type:" "\nRate:", room.getRoomRate())

            return room.__str__(self)

        # Setters and getters methods for name and location
    def getName(self):
        return self.name

    def setName(self, theName):
        self.name = theName

    def getLocation(self):
        return self.location

    def setLocation(self, theLocation):
        self.location = theLocation

    def __str__(self):
        occupiedrooms=[ ro for ro in self.gettheRooms() if ro.getOccupant()!="Not Occupied"]

        print("Hotel Name :", self.getName(), "\nNumber of Rooms:", self.getRoomNum(), "\nNumber of occupied Rooms:",len(occupiedrooms), "\n\nRoom Details are:\n")
        for room in occupiedrooms:
            room.__str__()

    def getDailySales(self):
        salesamount=0
        occupiedrooms=[ro for ro in self.gettheRooms() if ro.getOccupant()!="Not Occupied"]

        for room in occupiedrooms:
            salesamount+room.getRoomRate()
        return salesamount


    def occupancyPercentage(self):
        occupiedrooms=[ ro for ro in self.gettheRooms() if ro.getOccupant()!="Not Occupied"]
        allTheRooms=self.gettheRooms()
        return str(round(len(occupiedrooms)/len(allTheRooms))*100,2)+"%"

    # Setters and getters methods for name and location
    def getName(self):
        return self.name

    def setName(self, theName):
        self.name=theName

    def getLocation(self):
        return self.location
    def setLocation(self, theLocation):
        self.location=theLocation

####################################################################
#           Database connection  day5 exercise                     #
####################################################################


