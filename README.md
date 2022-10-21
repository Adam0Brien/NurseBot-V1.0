# NurseBot-V1.0
# IoT solution for the medical industry


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
<img src="nursingBotDashboard.jpg" alt="Dashboard" style="width:820px;height:560px;" class="center">
</p>

# Proof of concept
As of right now (week 4) the wiring is very messy as its in the early stages but this will be reduced to a PCB in the comming weeks
<p align="center" Wiring Diagram >
<img src="nursingBotWiring.jpg" alt="Dashboard" style="width:800px;height:600px;" class="center">
</p>

# Week 5
<p>As of week 5 the lcd screen has been connected using i2c, so now the bme680 and the lcd screen are both using lcd on the same channel. This wont cause any problems because i2c is a shared bus, multiple devices are allowed, as long as no two devices share the dame i2c address.</p>
<p align="center" LCD Working >
<img src="lcd.jpg" alt="lcd" style="width:700px;height:600px;" class="center">
</p>




live readings
https://beebotte.com/dash/fc4e82f0-4599-11ed-aff5-19489407b7b2#.Y06nvnbMLD4
