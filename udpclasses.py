import numpy as np
import json

#This file is a translation to Python of enum.ts

#This class is catering to the event of precipitation
class Evt_precip:

    def __init__(self,serial_number,typee,hub_sn,evt, rec):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.evt = evt
        self.rec = rec
        self.unpacker()


    def unpacker(self):
        self.timeep = self.evt[0]

    def printme(self):
        #return "THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {}".format(self.serial_number, self.typee, self.hub_sn, self.timeep)
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {}".format(self.serial_number, self.typee, self.hub_sn, self.timeep))
        # data_set = {"SerialNumber": self.serial_number, "Type": self.typee, "Hub_Serial_Number": self.hub_sn, "Time_Epoch": self.timeep}
        # json_object = json.dumps(data_set)
        # return json_object

    def returnval(self):
        json_dict = {
            "serial_number": self.serial_number,
            "type": "evt_precip",
            "hub_sn": self.hub_sn, 
            "Time_Epoch": self.timeep,
            "rec": self.rec
            }
        return json_dict

#This class is catering to the event of Lightning Strike
class Evt_strike:

    def __init__(self,serial_number,typee,hub_sn,evt, rec):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.evt = evt
        self.rec = rec
        self.unpacker()

    def unpacker(self):
        self.timeep = self.evt[0]
        self.Distance = self.evt[1]
        self.Energy = self.evt[2]

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, Distance: {} meters, Energy: {}".format(self.serial_number, self.typee, self.hub_sn, self.timeep, self.Distance, self.Energy))
    
    def returnval(self):
        json_dict = {
            "serial_number": self.serial_number,
            "type": "evt_strike",
            "hub_sn": self.hub_sn, 
            "Time_Epoch": self.timeep,
            "Distance": self.Distance,
            "Energy": self.Energy,
            "rec": self.rec
            }
        return json_dict

#This class is catering to the event of High Winds
class Rapid_wind:

    def __init__(self,serial_number,typee,hub_sn,ob, rec):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.ob = ob
        self.rec = rec
        self.unpacker()
        self.transform_winddir()

    def unpacker(self):
        self.timeep = self.ob[0]
        self.windspeed = self.ob[1]
        self.winddirn = self.ob[2]

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, WindSpeed: {} m/sec, WindDirection: {} Degrees".format(self.serial_number, self.typee, self.hub_sn, self.timeep, self.windspeed, self.winddirn))
        
    def returnval(self):
        json_dict = {
            "serial_number": self.serial_number,
            "type": "rapid_wind",
            "hub_sn": self.hub_sn,
            "Time_Epoch": self.timeep,
            "Wind_Speed": self.windspeed,
            "Wind_Direction": self.winddirn,
            "rec": self.rec
            }
        return json_dict

    #Wind Direction has been flipped by 180Degrees because the weatherflow tempest unit was designed in the Northern
    #Hemisphere and we are using this device in the Southern Hemisphere.
    def transform_winddir(self):
        if self.winddirn > 180:
            self.winddirn = self.winddirn - 180
        elif self.winddirn < 180:
            self.winddirn = self.winddirn + 180
        elif self.winddirn == 0 or self.winddirn == 360:
            self.winddirn == 180
        elif self.winddirn == 180:
            self.winddirn == 0

#This class is catering to the event of Observing Air
class Obs_air:

    def __init__(self,serial_number,typee,hub_sn,obs,firmware_revision, rec):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.obs = obs
        self.firmware_revision = firmware_revision
        self.rec = rec
        self.unpacker()

    def unpacker(self):
        self.timeep = self.obs[0][0]
        self.stationpress = self.obs[0][1]
        self.airtemp = self.obs[0][2]
        self.relhumid = self.obs[0][3]
        self.lgtnstrike = self.obs[0][4]
        self.lgtnstrikedist_avg = self.obs[0][5]
        self.battery = self.obs[0][6]
        self.reportint = self.obs[0][7]
        
    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, Station Pressure: {} MB, Air Temp: {} C, Relative Humidity {} %, LightningStrikeCount {}, Lightning Strike Avg Distance {} Km, Battery {}, Report Interval {} Mins, Firmware Rev: {}".format(self.serial_number, self.typee, self.hub_sn, self.timeep, self.stationpress, self.airtemp, self.relhumid, self.lgtnstrike, self.lgtnstrikedist_avg, self.battery, self.reportint, self.firmware_revision))
    
    def returnval(self):
        json_dict = {
            "serial_number": self.serial_number,
            "type":"obs_air",
            "hub_sn": self.hub_sn,
            "Time_Epoch": self.timeep,
            "Station_Pressure": self.stationpress,
            "Air_Temperature": self.airtemp,
            "Relative_Humidity": self.relhumid,
            "Lightning_Strike_Count": self.lgtnstrike,
            "Lightning_Strike_Avg_Distance": self.lgtnstrikedist_avg,
            "Battery": self.battery,
            "Report_Interval": self.reportint,
            "firmware_revision": self.firmware_revision,
            "rec": self.rec
            }
        return json_dict

        #This class is catering to the event of Observing the Sky
class Obs_sky:

    def __init__(self,serial_number,typee,hub_sn,obs,firmware_revision, rec):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.obs = obs
        self.firmware_revision = firmware_revision
        self.rec =rec
        self.unpacker()
        self.transform_winddir()

    def unpacker(self):
        self.timeep = self.obs[0][0]
        self.illum = self.obs[0][1]
        self.ultravio = self.obs[0][2]
        self.rainAccum = self.obs[0][3]
        self.windLull = self.obs[0][4]
        self.windAvg = self.obs[0][5]
        self.windGust = self.obs[0][6]
        self.windDir = self.obs[0][7]
        self.battery = self.obs[0][8]
        self.reportint = self.obs[0][9]
        self.solarRad = self.obs[0][10]
        self.locrainAccum = self.obs[0][11]
        self.precipType = self.obs[0][12]
        self.windSampInt = self.obs[0][13]

    #Wind Direction has been flipped by 180Degrees because the weatherflow tempest unit was designed in the Northern
    #Hemisphere and we are using this device in the Southern Hemisphere.
    def transform_winddir(self):
        # if wind direction is greater than 180
        if self.windDir > 180:
            # remove 180 from wind dir
            self.windDir = self.windDir - 180
        # if wind direction is less than 180 
        elif self.windDir < 180:
            # add 180 to wind dir
            self.windDir = self.windDir + 180
        # if the wind is at 0/360
        elif self.windDir == 0 or self.windDir == 360:
            # set the dir to 180
            self.windDir == 180
        # if wind dir is 180
        elif self.windDir == 180:
            # set to 0/360
            self.windDir == 0

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, Illumination: {} Lux, UltraViolet: {} Index, Rain Accumulated: {} mm, Wind Lull: {} m/s, Wind Avg: {} m/s, Wind Gust: {} m/s, Wind Direction: {} Degrees, Battery: {} Volts, Report Interval: {} Minutes, Solar Radiation: {} W/m2, Local Day Rain Accumulation: {} mm, Precipitation Type: {}, Wind Sample Interval: {} secs, Firmware Version: {}".format(self.serial_number, self.typee, self.hub_sn, self.timeep, self.illum, self.ultravio, self.rainAccum, self.windLull, self.windAvg, self.windGust, self.windDir, self.battery, self.reportint, self.solarRad, self.locrainAccum, self.precipType, self.windSampInt, self.firmware_revision))

    def returnval(self):
        json_dict = {
            "serial_number": self.serial_number,
            "type":"obs_sky",
            "hub_sn": self.hub_sn, 
            "Epoch": self.timeep,
            "Illuminance": self.illum,
            "UV": self.ultravio, 
            "Accumulated": self.rainAccum,
            "Wind_Lull": self.windLull,
            "Wind_Avg": self.windAvg, 
            "Gust": self.windGust,
            "Wind_Direction": self.windDir,
            "Battery": self.battery, 
            "Interval": self.reportint,
            "Solar_Radiation": self.solarRad, 
            "Local_Day_Rain_Accumulation": self.locrainAccum,
            "Precipitation_Type": self.precipType, 
            "Wind_Sample_Interval": self.windSampInt,
            "firmware_revision": self.firmware_revision,
            "rec": self.rec
            }
        return json_dict

#This class is catering to the monitoring the Device Status
class Device_status:

    def __init__(self, serial_number, typee, hub_sn, timestamp, uptime,
                    voltage, firmware_revision, rssi, hub_rssi, sensor_status, debug, rec):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.timestamp = timestamp
        self.uptime = uptime
        self.voltage = voltage
        self.firmware_revision = firmware_revision
        self.rssi = rssi
        self.hub_rssi = hub_rssi
        self.sensor_status = sensor_status
        self.rec = rec
        self.debug = debug
        if self.debug == 0:
            self.debug = "Debugging is disabled"
        elif self.debug == 1:
            self.debug = "Debugging is enabled"

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_stamp: {} seconds, Uptime: {} Secs, Voltage: {} Volts, Firmware Rev: {}, RSSI: {}, HUB_RSSI: {}, Sensor Status: {}, Debug Flag: {}".format(self.serial_number, self.typee, self.hub_sn, self.timestamp, self.uptime, self.voltage, self.firmware_revision, self.rssi, self.hub_rssi, self.sensor_status, self.debug))

    def returnval(self):
        json_dict = {
            "type":"device_status",
            "serial_number": self.serial_number,
            "hub_sn": self.hub_sn,
            "timestamp": self.timestamp,
            "uptime": self.uptime,
            "voltage": self.voltage, 
            "firmware_revision":self.firmware_revision,
            "rssi": self.rssi,
            "hub_rssi": self.hub_rssi,
            "sensor_status": self.sensor_status,
            "debug": self.debug,
            "rec": self.rec
            }
        return json_dict

#This class is catering to the monitoring the Hub Status
class Hub_status:

    def __init__(self, serialnum, typee, firmwarerev, uptime,rssi, timestamp, resetflags, seq, fs,
                                radiostats, mqttstats, rec):
        self.serialnum = serialnum
        self.typee = typee
        self.firmwarerev = firmwarerev
        self.uptime = uptime
        self.rssi = rssi
        self.timestamp = timestamp
        self.resetflags = resetflags
        self.seq = seq
        self.fs = fs
        self.radiostats = radiostats
        self.mqttstats = mqttstats
        self.rec = rec
        self.unpacker()

    def unpacker(self):
        self.version = self.radiostats[0]
        self.rebootcount = self.radiostats[1]
        self.buserror = self.radiostats[2]
        
        if self.radiostats[3] == 0:
            self.radiopower = "OFF"
        if self.radiostats[3] == 1:
            self.radiopower = "ON"
        if self.radiostats[3] == 3:
            self.radiopower = "ACTIVE"

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, Up Time: {} Seconds, RSSI: {}, Time Stamp: {} Secs, Reset Flags: {}, Seq: {}, FS: {}, Radio Stats: {}, MQTT STATS: {}".format(self.serialnum, self.typee, self.uptime, self.rssi, self.timestamp, self.resetflags, self.seq, self.fs, self.radiostats, self.mqttstats))

    def returnval(self):
        json_dict = {
            "serial_number": self.serialnum,
            "type": "hub_status",
            "firmware_revision": self.firmwarerev,
            "uptime": self.uptime,
            "rssi": self.rssi,
            "timestamp": self.timestamp,
            "reset_flags": self.resetflags,
            "seq": self.seq,
            "fs": self.fs,
            "Version": self.version,
            "Reboot Count":self.rebootcount,
            "I2C Bus Error Count": self.buserror,
            "Radio_Power": self.radiopower,
            "MQTT_STATS": self.mqttstats,
            "rec": self.rec
            }
        return json_dict