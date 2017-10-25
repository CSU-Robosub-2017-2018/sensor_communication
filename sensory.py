class getSensoryData():
    ##
    # @breif Defines incoming variables.
    def __init__(self):
        self.allData = [0] * 29  # multiplied by number of outputs

    ##
    # @brief Updates filtered IMU Data, x is forward/back, y left/right, z up/down
    def upDateData(self, imuData=[0] * 42):

        # IMU output

        # xyz acceleration, velocity, position
        self.allData[0] = imuData[0]  # x-direction acceleration (meter)
        self.allData[1] = imuData[1]  # y-direction acceleration (meter)
        self.allData[2] = imuData[2]  # z-direction acceleration (meter)

        self.allData[3] = imuData[3]  # x-direction velocity (meter/sec)
        self.allData[4] = imuData[4]  # y-direction velocity (meter/sec)
        self.allData[5] = imuData[5]  # z-direction velocity (meter/sec)

        self.allData[6] = imuData[6]  # x-direction position (meter/sec^2)
        self.allData[7] = imuData[7]  # y-direction position (meter/sec^2)
        self.allData[8] = imuData[8]  # z-direction position (meter/sec^2)

        # xyz rotation , rotation velocity, rotation acceleration
        self.allData[9] = imuData[9]  # x-axis rotation (radian)
        self.allData[10] = imuData[10]  # y-axis rotation radian)
        self.allData[11] = imuData[11]  # z-axis rotation (radian)

        self.allData[12] = imuData[12]  # x-axis rotation velocity (radian/sec)
        self.allData[13] = imuData[13]  # y-axis rotation velocity (radian/sec)
        self.allData[14] = imuData[14]  # z-axis rotation velocity (radian/sec)

        self.allData[15] = imuData[15]  # x-axis rotation acceleration (radian/sec^2)
        self.allData[16] = imuData[16]  # y-axis rotation acceleration (radian/sec^2)
        self.allData[17] = imuData[17]  # z-axis rotation acceleration (radian/sec^2)

        # Orientation from Quaternions  this is redundant information
        self.allData[18] = imuData[18]  # x-axis rotation (radian))
        self.allData[19] = imuData[19]  # y-axis rotation radian)
        self.allData[20] = imuData[20]  # z-axis rotation (radian)


        # self.allData[18] = imuData[18]  # x-direction magnetic (mGauss)
        # self.allData[19] = imuData[19]  # y-direction magnetic (mGauss)
        # self.allData[20] = imuData[20]  # z-direction magnetic (mGauss)


    ##
    # @brief Updates pressure sensor data, read in PSI
    def upDatePressureData(self, pressureData=[0] * 2):
        self.allData[21] = pressureData[0]  # Pressure sensor 1 Pascal
        self.allData[22] = pressureData[1]  # Pressure sensor 2 Pascal

    ##
    # @brief Makes yes / no based on camera readings, 1 for yes, 0 for no
    def upDateVisionData(self, visonData=[0] * 19):

        # Vision output

        # Color 3 bit number
			# 0 red
			# 1 green
			# 2 yellow
			# 3 blue
			# 4 white
			# 5 black
			# 6 orange
			# 7 imGoingToPunchOrenInTheFace
			
		#16 block direction
			#	# # # #
			#	# # # #
			#	# # # #
			#	# # # #
			#	should be a 1 by 16 array
			
		#size will be defined at a later date (need to do more test first)

        self.allData[23] = visonData[0]  # number of objects with a max of 3 objects

        # object 1
        self.allData[24] = visonData[1]  # 16 block direction 

        self.allData[25] = visonData[2]  # size

        self.allData[26] = visonData[3]  # circle

        self.allData[27] = visonData[4]  # line

        self.allData[28] = visonData[5]  # square

        self.allData[29] = visonData[6]  # Color

        # object 2
        self.allData[30] = visonData[7]  # 16 block direction

        self.allData[31] = visonData[8]  # size

        self.allData[32] = visonData[9]  # circle

        self.allData[33] = visonData[10]  # line

        self.allData[34] = visonData[11]  # square

        self.allData[35] = visonData[12]  # Color

        # object 3
        self.allData[36] = visonData[13]  # 16 block direction

        self.allData[37] = visonData[14]  # size

        self.allData[38] = visonData[15]  # circle

        self.allData[39] = visonData[16]  # line

        self.allData[40] = visonData[17]  # square

        self.allData[41] = visonData[18]  # Color


    def getAllData(self):
        return self.allData
