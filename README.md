# COVID-19 Prevention Kit

Story- 
As the world returns to a normal functioning, the chances of spreading of COVID-19 are increasing by the day. Thus, there is a huge need to ensure that we are taking ample amount of preventive measures and ensuring sanitation around us. This interface will help people in achieving this goal, and thus, making it safer for them to interact with the outer world, without the fear of getting infected by COVID-19.

Things Used in this Project-
Hardware Components: 
1. Bolt IoT Wi-Fi Module
2. IR Sensor Module(x2)
3. Breadboard
4. Jumper Wires
5. LEDs(x2)
6. Buzzer

Softwares, Apps and Online Services: 
1. Bolt IoT Android App
2. Bolt IoT Bolt Cloud
3. Telegram

Software Setup- 
STEP 1: Sign up/sign in to the Bolt IoT Cloud.
STEP 2: Link the Bolt device to Bolt Cloud using Bolt IoT Android App.
STEP 3: On the left-hand side tab on the Bolt Cloud, go to Products tab, and create a new Product.
STEP 4: Name your Product, choose the product type to be Output Device and the interface GPIO.
STEP 5: Now, go to the newly created Product and choose the "Configure this Device" icon.
STEP 6: Go to the Code tab and write the code for Smart Appliances Control, where we are creating a User Interface to interact with the Bolt Device, from the code section. Name the file and choose the extension to be html.
STEP 7: Save the Code and exit the Configuration Interface.
STEP 8: Now all you need to do is link your device to the product using the Link icon, after which you select your device displayed in the dialog.

Conclusion- 
As the system was put into operation once connected with power and connected with the cloud, the IR Sensor Data counts the number of people in the room, and when found to be more than 5, sends an alert through Telegram to the user and the Buzzer starts to go off, while the LED is lit.
