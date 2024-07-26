#Apache-Bot-Blocker
Apache-Bot-Blocker is an open-source project that provides a secure and efficient bot-blocking firewall implementation for websites using any server log such as Apache or Nginx HTTP server. This tool helps prevent malicious bot scraping, reducing system load, resource usage, and energy costs.


##Features

- Analyzes Apache server log files to identify potential malicious bots
- Uses reverse DNS and forward DNS methods to verify frequently visiting IPs
- Automatically adds non-verified IPs to an Iptables blacklist
- Helps improve website performance and security
- Free, non-third-party solution for business and website managers
- Conserves website resources by not requiring constant runtime
IMPORTANT: This blocking method is NOT live. This program is NOT meant to be constantly run on a live website. The code is configured so that the program will only be required to run once in a certain time period to be able to block the recurring bad bots after the initial run. To reiterate, this will not only accomplish the traditional blocking behavior of an anti-bad-bot program, but also do so without the need to constantly run the program, therein conserving your website's resources 

##Important Notes

Not a Live Blocking Method: This program is NOT meant to be constantly run on a live website. It is designed to be run periodically to block recurring bad bots after the initial run.

Resource Conservation: By not requiring constant runtime, this tool conserves your website's resources while still providing effective bot-blocking functionality.

##Key Details

Non-Third Party

This project does not require any external resources or tools besides built-in Python libraries. The bot blocker interacts directly with the Linux firewall to block identified malicious web-scraping bot IPs through the usage of Linux ip-rules commands.

RDS/FDS

The project utilizes both reverse DNS (RDS) and forward DNS (FDS) methods to combat against the potential of fake user-agent strings that point to reputable bots such as Google or Bing.

##Installation:

1) Install the package using pip:

       pip install apache_bot_blocker


##Configuration:

Editing the config.ini file

1. Locate the config.ini file in the package directory:

        pip show apache_bot_blocker

   Look for the "location" field in the output


2. Open the config.ini file with a text editor:

       nano /path/to/apache_bot_blocker/config.ini

3. To edit your web server log file (Nginx/Apache/other) preferences, input your preferences as such below:

       log_file_name = access_log
       log_file_path = /etc/httpd/logs/
       log_file_format = (?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\]
       timestamp_format = %%d/%%b/%%Y:%%H:%%M:%%S %%z

   **Important**: The 'ip' and 'timestamp' fields are mandatory in the REGEX log file pattern, otherwise the code will fail.  

##Editing Whitelist and Blacklist

1. Locate the whitelist and blacklist files in the same directory as config.ini.

       nano /path/to/apache_bot_blocker/whitelist.txt

   or

       nano /path/to/apache_bot_blocker/blacklist.txt


2. Add IP addresses to whitelist or blacklist, one per line:

       8.8.8.8
       8.8.4.4
       192.128.2.1

##Usage

1. After completing the configuration, run the bot blocker using the following command:

       run_bot_blocker


For more detailed information regarding linux commands, etc. please refer to 'documentation'