# Apache-Bot-Blocker
Apache-Bot-Blocker is a software project that focuses on creating secure bot-blocking firewall implementation for websites through the apache log. This project serves to prevent malicious bot scraping of your site, in order to decrease system load, resources, energy costs, etc. For further documentation, please refer to the 'documentation' folder


Having useless bots clog up your website resources can be a nuisance to deal with, especially for new developers and small website managers. These bots can deter your website's performance, causing multiple performance issues including customer/visitor displeasure, decreased website rankings, and more. This project presents a free access non-3rd party "bad" bot blocking tool for business/website managers.
It brings an efficient way of blocking "bad" bots from scraping your webpage. The program reads through and analyzes your most recent apache_log file through a series of visiting frequency conditions. After the analysis is done, the program will utilize reverse DNS and forward DNS methods to verify each IP that frequently visits your website. Lastly, each non-verified IP will be added to an Iptables blacklist where the IP will be removed from accessing your website.

IMPORTANT: This blocking method is NOT live. This program is NOT meant to be constantly run on a live website. The code is configured so that the program will only be required to run once in a certain time period to be able to block the recurring bad bots after the initial run. To reiterate, this will not only accomplish the traditional blocking behavior of an anti-bad-bot program, but also do so without the need to constantly run the program, therein conserving your website's resources 

DETAILS:

NON THIRD PARTY: This project does not incorporate any external resources or tools besides simple python libraries. The bot blocker interacts directly with the firewall to block any malicious web-scraping bots through the usage of linux ip-rules commands.

RDS/FDS: This project utilizes both reverse DNS and forward DNS methods to combat against the potential of fake user-agent strings that point to reputable bots such as Google or Bing. Since 

HOW TO USE:

1) Copy the Python source code into your preferred linux server directory. 
To access your linux remote server, cd into the location of your OpenSSH directory in the command line. Once there, ‘ssh’ into your remote server and run this command in the directory that you would like the file to be copied into. 

       pscp -r C:\path\to\your\folder username@remote_server_ip:/path/on/remote/server/

    Verify that your file is correctly copied by executing ‘ls’ in your command line, verify that you can now see the file name


2) Change to your APACHE_LOG file directory in your linux server
Your apache log should be located on the linux server that your website is hosted on. ‘cd’ into the directory that holds the file. For example, if my apache log file was located in the directory user/home/log, I would run the following command:

       cd /user/home/log

3) Run the “bad_bot_blocker.py” file from the src folder using this command while replacing 'filename' with your apache_log file name:

       python3 bad_bot_blocker.py 'apache_log' 




 
#todo: config file (location of log file, filename, format of log file, white/black list, good bot definition, frequency,  setup.py, use pip to install package, 