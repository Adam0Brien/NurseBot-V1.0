# NurseBot-V1.0
# IoT solution for the medical industry

<p align="center" LDR >
<img src="img/nurseCap.png" alt="PCB" style="width:400px;height:250px;" class="center">
</p>

This project is an IoT solution to support the fast-paced medical industry, the main objective of this project is to make looking after new-born babies as easy as possible on nurses, 

The main function of this automated system is to take readings of the infant’s surroundings and report them to the cloud, it will also monitor the babies’ vital signs like its heartbeat and temperature
The following sensors are included in this design
<br>
•	BME 680 (for temperature, humidity and air quality
<br>
•	A pulse sensor to calculate the new-borns BPM and report to the cloud
<br>
•	A noise sensor that will detect if the baby is in distress, this will then send an automated text message to the on-duty nurse.
<br>


It is fully powered by a raspberry pi,and the full circuitry will be reduced to a PCB later on in order to reduce the overall size it will take up, the PCB also reduces the number of physical wires in the circuit which will in turn make it safer.


<br><br><br>
# Beebotte Dashboard
Below is the dashboard i created using Beebotte, It displays all vital signs/data of the child
<p align="center" Wiring Diagram >
<img src="img/nursingBotDashboard.jpg" alt="Dashboard" style="width:600px;height:460px;" class="center">
</p>

# Proof of concept
As of right now (week 4) the wiring is very messy as its in the early stages but this will be reduced to a PCB in the comming weeks
<p align="center" Wiring Diagram >
<img src="img/nursingBotWiring.jpg" alt="wiring" style="width:600px;height:400px;" class="center">
</p>

# Week 5
<p>As of week 5 the lcd screen has been connected using i2c, so now the bme680 and the lcd screen are both using lcd on the same channel. This wont cause any problems because i2c is a shared bus, multiple devices are allowed, as long as no two devices share the dame i2c address.</p>
<p align="center" LCD Working >
<img src="img/lcd.jpg" alt="lcd" style="width:500px;height:400px;" class="center">
</p>

# Week 6
<p>At the start of week 6 i added an LDR(light dependant resistor) to my circuit and connected it to the MCP3008 so i can find out what light level is present around the infant this will be monitoring.</p>
<p align="center" LDR >
<img src="img/LDR.jpg" alt="ldr" style="width:500px;height:400px;" class="center">
</p>
<br>
<br>
<p>Along with the LDR i also finished designing the schematic that will be used to make the PCB for this project, the goal here is to have a small board about the same size as the raspberry pi that will simply sit on top of it, similar to the Sense HAT</p>

<p align="center" LDR >
<img src="img/schematic.png" alt="schematic" style="width:509px;height:290px;" class="center">
</p>

<p align="center" LDR >
<img src="img/pcb.png" alt="PCB" style="width:400px;height:312px;" class="center">
</p>



# Week 9 (PCB Week)
<p>In week 9 the board arrived and was soldered together</p>
<p align="center" LDR >
<img src="img/board.jpg" alt="PCB" style="width:400px;height:400px;" class="center">
</p>

<p>Here is a comparison of the original wiring and the new PCB (Nurse Hat)</p>
<p align="center" LDR >
<img src="img/board-Comparison.jpg" alt="PCB" style="width:500px;height:300px;" class="center">
</p>


<p>The NurseHats I2C connections can also be used on a touch screen display,lcd screen (or any other I2C device) </p>
<p align="center" LDR >
<img src="img/touch-lcd.jpg" alt="PCB" style="width:400px;height:300px;" class="center">
</p>
<p align="center" LDR >
<img src="img/lcd-nurseHat.jpg" alt="PCB" style="width:500px;height:300px;" class="center">
</p>

live readings
https://beebotte.com/dash/fc4e82f0-4599-11ed-aff5-19489407b7b2#.Y06nvnbMLD4
