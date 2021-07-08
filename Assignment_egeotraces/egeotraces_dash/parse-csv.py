# any work with the data file
# make a nicer csv to pull from
import pandas as pd

# all of the parameters from the full data: 'Longitude [degrees_east]', 'Latitude [degrees_north]',
# 'PRESSURE [dbar]', 'DEPTH [m]', 'CTDTMP [deg C]', 'CTDSAL', 'SALINITY_D_CONC_BOTTLE', 'SALINITY_D_CONC_PUMP',
# 'SALINITY_D_CONC_FISH', 'SALINITY_D_CONC_UWAY', 'NITRATE_D_CONC_BOTTLE [umol/kg]', 'NITRATE_D_CONC_PUMP [umol/kg]',
# 'NITRATE_D_CONC_FISH [umol/kg]', 'NITRATE_D_CONC_UWAY [umol/kg]', 'NITRATE_LL_D_CONC_BOTTLE [umol/kg]',
# 'NITRATE_LL_D_CONC_FISH [umol/kg]', 'NO2+NO3_D_CONC_BOTTLE [umol/kg]', 'NO2+NO3_D_CONC_FISH [umol/kg]',
# 'Fe_D_CONC_BOTTLE [nmol/kg]', 'Fe_D_CONC_FISH [nmol/kg]', 'Fe_II_D_CONC_BOTTLE [nmol/kg]', 'Fe_II_D_CONC_FISH [nmol/kg]',
# 'Fe_S_CONC_BOTTLE [nmol/kg]', 'Fe_S_CONC_FISH [nmol/kg]'

# notes on which data was chosen and why

# sort by depth?
# put filtered data in a folder?


# read in original data
GA03_data = pd.read_csv("./data/GA03w.csv")
GIPY05_data = pd.read_csv("./data/GIPY05e.csv")
GP02_data = pd.read_csv("./data/GP02w.csv")
GIPY04_data = pd.read_csv("./data/GIPY04.csv")

headers = ['Station', 'Latitude', 'Longitude', 'Depth', 'Temperature', 'Salinity', 'Nitrate', 'Iron']

# make GA03 dataframe and csv
data = [GA03_data['Station'], GA03_data['Latitude [degrees_north]'], GA03_data['Longitude [degrees_east]'],
        GA03_data['DEPTH [m]'],
        GA03_data['CTDTMP [deg C]'], GA03_data['CTDSAL'], GA03_data['NITRATE_D_CONC_BOTTLE [umol/kg]'],
        GA03_data['Fe_D_CONC_BOTTLE [nmol/kg]']]
GA03 = pd.concat(data, axis=1, keys=headers)
# remove unwanted lons and lats
GA03 = GA03[((GA03.Longitude <= 360 - 60) & (GA03.Longitude >= 360 - 65)) | (GA03.Longitude >= 360 - 25)]
positions = []
for i in range(len(GA03)):
        lat = GA03['Latitude'].values[i]
        lon = GA03['Longitude'].values[i]
        if len(positions) == 0 or [lat, lon] != positions[-1]:
                positions.append([lat, lon])
for i in [0, 6]: #choosing specific profiles
        GA03 = GA03.drop(GA03[(GA03.Latitude == positions[i][0]) & (GA03.Longitude == positions[i][1])].index)
GA03.to_csv('GA03_filtered.csv', index=False)

# make GIPY05 dataframe and csv
data = [GIPY05_data['Station'], GIPY05_data['Latitude [degrees_north]'], GIPY05_data['Longitude [degrees_east]'],
        GIPY05_data['DEPTH [m]'],
        GIPY05_data['CTDTMP [deg C]'], GIPY05_data['CTDSAL'], GIPY05_data['NO2+NO3_D_CONC_BOTTLE [umol/kg]'],
        GIPY05_data['Fe_D_CONC_BOTTLE [nmol/kg]']]
GIPY05 = pd.concat(data, axis=1, keys=headers)
# remove unwanted lons and lats
GIPY05 = GIPY05[(GIPY05.Latitude >= -45) | (GIPY05.Latitude <= -65)]
positions = []
#stations = []
for i in range(len(GIPY05)):
        #station = GIPY05['Station'].values[i]
        lat = GIPY05['Latitude'].values[i]
        lon = GIPY05['Longitude'].values[i]
        if len(positions) == 0 or [lat, lon] != positions[-1]:
            positions.append([lat, lon])
            #stations.append(station)
#print(stations)
for i in [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 31, 33, 34]: #choosing specific profiles
        GIPY05 = GIPY05.drop(GIPY05[(GIPY05.Latitude == positions[i][0]) & (GIPY05.Longitude == positions[i][1])].index)
GIPY05.to_csv('GIPY05_filtered.csv', index=False)

# make GP02 dataframe and csv
data = [GP02_data['Station'], GP02_data['Latitude [degrees_north]'], GP02_data['Longitude [degrees_east]'],
        GP02_data['DEPTH [m]'],
        GP02_data['CTDTMP [deg C]'], GP02_data['CTDSAL'], GP02_data['NO2+NO3_D_CONC_BOTTLE [umol/kg]'],
        GP02_data['Fe_D_CONC_BOTTLE [nmol/kg]']]
GP02 = pd.concat(data, axis=1, keys=headers)
# remove unwanted lons and lats
GP02 = GP02[(GP02.Longitude <= 155) | (GP02.Longitude >= 180)]
positions = []
#stations = []
for i in range(len(GP02)):
        station = GP02['Station'].values[i]
        lat = GP02['Latitude'].values[i]
        lon = GP02['Longitude'].values[i]
        if len(positions) == 0 or [lat, lon] != positions[-1]:
            positions.append([lat, lon])
            #stations.append(station)
#print(stations)
for i in [0, 1, 7]: #choosing specific profiles
        GP02 = GP02.drop(GP02[(GP02.Latitude == positions[i][0]) & (GP02.Longitude == positions[i][1])].index)
GP02.to_csv('GP02_filtered.csv', index=False)

# make GIPY04 dataframe and csv
data = [GIPY04_data['Station'], GIPY04_data['Latitude [degrees_north]'], GIPY04_data['Longitude [degrees_east]'],
        GIPY04_data['DEPTH [m]'],
        GIPY04_data['CTDTMP [deg C]'], GIPY04_data['CTDSAL'], GIPY04_data['NITRATE_D_CONC_BOTTLE [umol/kg]'],
        GIPY04_data['Fe_D_CONC_BOTTLE [nmol/kg]']]
GIPY04 = pd.concat(data, axis=1, keys=headers)
# remove unwanted lons and lats
GIPY04 = GIPY04[(GIPY04.Latitude >= -45) | (GIPY05.Latitude <= -35)]
positions = []
stations = []
for i in range(len(GIPY04)):
        station = GIPY04['Station'].values[i]
        lat = GIPY04['Latitude'].values[i]
        lon = GIPY04['Longitude'].values[i]
        if len(positions) == 0 or [lat, lon] != positions[-1]:
            positions.append([lat, lon])
            stations.append(station)
print(stations)
for i in [0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,32,33,35,36,37,38,39,40,42,43,44,45,46,47,48,50,51,52,53]: #choosing specific profiles
        GIPY04 = GIPY04.drop(GIPY04[(GIPY04.Latitude == positions[i][0]) & (GIPY04.Longitude == positions[i][1])].index)
GIPY04.to_csv('GIPY04_filtered.csv', index=False)