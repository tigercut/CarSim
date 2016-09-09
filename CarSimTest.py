#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file CarSimTest.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import ogata_lab


import Tkinter as tk

import cv2

from PIL import Image

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
carsimtest_spec = ["implementation_id", "CarSimTest", 
		 "type_name",         "CarSimTest", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "VenderName", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.debug", "0",
		 "conf.__widget__.debug", "text",
		 ""]
# </rtc-template>

##
# @class CarSimTest
# @brief ModuleDescription
#
#
class CarSimTest(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_status = ogata_lab.CarStatus(ogata_lab.CameraData(0,0,[]), ogata_lab.CameraData(0,0,[]), ogata_lab.CameraData(0,0,[]), RTC.Velocity3D(0,0,0, 0, 0, 0), RTC.AngularVelocity3D(0,0,0), RTC.Acceleration3D(0,0,0), RTC.AngularAcceleration3D(0,0,0))
		"""
		"""
		self._statusIn = OpenRTM_aist.InPort("status", self._d_status)
		self._d_simulator = ogata_lab.SimulatorStatus(RTC.Time(0,0), RTC.Pose3D(RTC.Point3D(0,0,0), RTC.Orientation3D(0,0,0)))
		"""
		"""
		self._simulatorIn = OpenRTM_aist.InPort("simulator", self._d_simulator)
		self._d_command = ogata_lab.CarCommand(RTC.Time(0,0), 0, 0 ,0)
		"""
		"""
		self._commandOut = OpenRTM_aist.OutPort("command", self._d_command)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  debug
		 - DefaultValue: 0
		"""
		self._debug = [0]
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("debug", self._debug, "0")
		
		# Set InPort buffers
		self.addInPort("status",self._statusIn)
		self.addInPort("simulator",self._simulatorIn)
		
		# Set OutPort buffers
		self.addOutPort("command",self._commandOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports

		self._received = False
		
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	#
	#	# @return RTC::ReturnCode_t
	#
	#	#
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onActivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#

	def animation(self):
                print "Animation"
                
                root.after(1000, self.animation)
                if not self._received:
                        return
                for i in range(178):
                        for j in range(178):
                                
                                lr = self._d_status.frontLeftCamera.pixels[(178 * i + j) * 3 + 0]
                                lg = self._d_status.frontLeftCamera.pixels[(178 * i + j) * 3 + 1]
                                lb = self._d_status.frontLeftCamera.pixels[(178 * i + j) * 3 + 2]

                                rr = self._d_status.frontRightCamera.pixels[(178 * i + j) * 3 + 0]
                                rg = self._d_status.frontRightCamera.pixels[(178 * i + j) * 3 + 1]
                                rb = self._d_status.frontRightCamera.pixels[(178 * i + j) * 3 + 2]
                               
                                cr = self._d_status.frontCenterCamera.pixels[(178 * i + j) * 3 + 0]
                                cg = self._d_status.frontCenterCamera.pixels[(178 * i + j) * 3 + 1]
                                cb = self._d_status.frontCenterCamera.pixels[(178 * i + j) * 3 + 2]
                                 
                                rl = ord(lr)
                                gl = ord(lg)
                                bl = ord(lb)

                                rr = ord(rr)
                                gr = ord(rg)
                                br = ord(rb)
                               
                                rc = ord(cr)
                                gc = ord(cg)
                                bc = ord(cb)

                                #print (rc, gc, bc)
                                image_ldata.put("#%02x%02x%02x" % (rl,gl,bl), (j, 177 - i))
                                image_rdata.put("#%02x%02x%02x" % (rr,gr,br), (j, 177 - i))
                                image_cdata.put("#%02x%02x%02x" % (rc,gc,bc), (j, 177 - i))

                                #cv2.flip(image_data,0)

                        canvas.update()
                        
	def onExecute(self, ec_id):
                # print "onExecute"
		if self._statusIn.isNew():
			self._d_status = self._statusIn.read()
			self._received = True
                        self._d_command.acceleratorPressMeter = 1
			self._commandOut.write()

		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	
#draw with TK
root = tk.Tk()
canvas = tk.Canvas(root, width = 600, height = 200)

image_cdata = tk.PhotoImage(width = 178, height = 178)
image_rdata = tk.PhotoImage(width = 178, height = 178)
image_ldata = tk.PhotoImage(width = 178, height = 178)

#print image_data
#canvas.create_image(200, 150, image = image_data)
canvas.create_image(300, 100 , image = image_cdata)
canvas.create_image(500, 100 , image = image_rdata)
canvas.create_image(100, 100 , image = image_ldata)

canvas.pack()

comp = None

def CarSimTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=carsimtest_spec)
    manager.registerFactory(profile,
                            CarSimTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    CarSimTestInit(manager)

    # Create a component
    global comp
    comp = manager.createComponent("CarSimTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager(True)
	root.after(1000, comp.animation)
        root.mainloop()

if __name__ == "__main__":
	main()

