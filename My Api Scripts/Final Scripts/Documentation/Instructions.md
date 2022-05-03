# How to Setup and Use PerfSonar
## by Jacob Clouse


##### A. Preliminary Information


Complete the following before going on to Step B.

Watch the full Setup Video Guide for PerfSonar by clicking on 
this link: https://learn.nsrc.org/perfsonar/what-is-perfsonar


Review installation options by clicking on 
this link: http://docs.perfsonar.net/install_options.html

—

##### B. Setting Up Your Server


You need to setup a Centos server in order to have access to the toolkit.
- Burn the Centos image to a disk or USB stick.
- Install the Centos image on bare metal (not in a VM).
- When setting up the Centos server, make sure that you create a custom user account and make it an Administrator.

**NOTE:** You can use other remote nodes to gather data, but you won’t be able to configure custom tests.

Once you are done installing the image:
- Connect the machine to the internet and boot it up.
- Login with your Administrator account.
- Configure SSH. Refer to the following to configure SSH on centos 7: https://phoenixnap.com/kb/how-to-enable-ssh-centos-7 
- After SSH is setup, remotely login via the terminal or Putty.

- Make sure the machine has a static IP address. Refer to the following guide: https://www.cyberciti.biz/faq/howto-setting-rhel7-centos-7-static-ip-configuration/


- Find the private IP address of the host computer:
    - While you are in the terminal, type ifconfig
    - If you are unsure which address it is, look for **‘eth0’** in the list (for Ethernet). Most private IP addresses start with **‘192.168’** for home networks or **‘10.0’** for larger enterprise networks.
    - Open up the web browser and enter in the IP address that you found previously. This should bring you to the PerfSonar web dashboard.


##### C. Setting Up Tests

To configure the testing nodes you want to test against, go to the Perfsonar web dashboard.
- Select ‘Private Dashboard’ in the top right hand corner.
- Login with the Administrator login that you set up during installation.
- If prompted, fill in information about the location of your node and your organization.


- Once you are logged in, click on the _‘Configure’_ option on the screen to proceed. 


Select the nodes you want to test against. 
- Review the online map of different PerfSonar nodes across the world at this link: http://stats.es.net/ServicesDirectory/ 
- To search for nodes using the online directory, refer to Perfsonar’s documentation: https://docs.perfsonar.net/manage_locating_hosts.html


Once you have located several hosts to test against, write down their hostnames and IP addresses in a separate document.


To configure a new test, click the ‘Config’ tab and select the kind of test you want to run.
The testing types are listed here: https://docs.perfsonar.net/pscheduler_ref_tests_tools.html


Enter the test duration, frequency, and the number of hosts you are testing against and their IPs. Then click on _‘Save’_ in the bottom right corner of the screen. 


You can run multiple types of tests, but make sure:
- Tests will not interfere with each other. 
- Your server is powerful enough to handle it (i.e., Do not try to run 35 tests on a Core 2 Duo from 2007).


##### D. Gathering Data


When your tests have been running for a good length of time, you can gather the data they have been collecting.
 
To view data for each host in your browser:
- Go to the web dashboard url, scroll down to where the hosts are listed, and click on the _‘Graph’_ option under the host you want to view.
- This displays a graph in a new browser tab which will illustrate the different test results that you have stored on your server.


You can download the data directly from the site as a JSON:
- Go to the home screen on the web dashboard, click on the ‘esmond’ dropdown menu, and click the ‘esmond link’ that has your hostname in it (e.g., ‘https://192.168.1.1/esmond/perfsonar/archive/’). 
- A new tab displays with all the JSON data for all the tests you are running and you will be using this  link later with Python to parse this data. 
- For now, click on the ‘JSON’ button in the top right to get the raw data in your browser.
- Copy and paste the data into a text file to view.


To parse the data obtained with Python, you will need to have the _'esmond'_ link that was discussed in the previous step. 
**NOTE:** that Perfsonar uses a REST API in order to access the database through this _‘esmond’_ link.
    (For more information, go to: https://docs.perfsonar.net/esmond_api_rest.html )
You can test GET requests to the API by using Postman (https://www.postman.com/ ). This will let you see what information you are getting back from it.

You can access the data with a few languages (i.e., JavaScript with the FetchAPI). Note that I:
* Choose Python since it was easy to set up and understand. 
* Used the 'requests' library and 'json' library to interact with the API.
* And was helped immensely by this youtube video / Python Tutorial: https://www.youtube.com/watch?v=9N6a-VLBa2I


Utilizing this method, you should be able to grab data from your own server and store it as a JSON file. You can also substitute the IP of your server with the IP of another node to query it for data.


##### E. Visualizing Data:


Once you have the data, use Exploratory to create graphs of the data.
For the Exploratory software link go to: https://exploratory.io/  
Sign up for a free account with your UAlbany email address.


**NOTE:** that you will need to parse the data beforehand in Python and only select the specific event types that you want on INDIVIDUAL hosts. For example, only select the throughput data going to one host in location A to graph. (If you query the default URL, you will get ALL the data for all hosts.) 

- Once you narrow it down enough, you can import into Exploratory by opening a new data set and importing a new JSON object.

- You can then adjust the X axis label, the Y axis label, the type of graph (most work with the 'histogram' type) and other settings. 

- After you publish, it will give you a URL to access your graph, but you have to be logged in to view it. You can also save data in the URL as a picture. 


##### F. Conclusion


PerfSonar enables you to gather, organize and display all of the data that you need. However, keep in mind PerfSonar has both strengths and weaknesses:

__PerfSonar has the following strengths:__
- It is highly customizable
- It is easy to administer and setup custom tests
- Has extensive documentation and is actively maintained

__PerfSonar has the following weaknesses:__
- There is quite a bit of setup involved which can intimidate new users
- The documentation, while extensive, can confusing at times
- Setting up and configuring a server correctly can be frustrating



