# Weekly Assignment Instructions


### Overview

This assignment will provide an introduction to host-level security considerations, application security, and one of the tools you can use to monitor security around your host - wireshark!

### Learning Outcomes

You will learn about securing your host machine including updates, securely accessing it, and lowering its accessibility to the outside world.  You will also get experience with the host-based firewall and using Wireshark to monitor traffic between your host and other computers!  We will also be exploring a Linux VM with a Flask API you will be setting up via "Vagrant"!
    

### Instructions
1. **Review the following materials**:

   - [OS Security](https://cioinfluence.com/it-and-devops/review-of-secured-operating-system-windows-linux-macos-and-chromeos/)

        This article provides a solid overview of several of the popular Operating Systems and some of their security pros/cons.  Each one of these OS's is widely used and many corporate networks incorporate at least a couple (if not ALL) of them!  This means a good network security policy regarding multiple Operating Systems is imperative! 

   - [Hardening Linux Machines](https://tuxcare.com/blog/linux-system-hardening-top-10-security-tips/)

        This is a really good article outlining basic steps you should take to "harden" (make more secure) a computer running Linux!  We will be reviewing several aspects of this in our hands-on assignment for this week!

   - [Windows Hardening](https://spca.education/windows-11-hardening/)

        This provides an in-depth review of hardening a machine running Windows!  You will notice that many of these steps are similar to those of Linux. 

   - [What is a firewall?](https://usa.kaspersky.com/resource-center/definitions/firewall)

        This article from Kapersky is a great overview of what a firewall is!  We will be playing around with firewalls in Linux in your hands-on assignment for this week!

   - [Uncomplicated firewall - ufw](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)

        This article from Digital Ocean is a great resource for learning and using the "Uncomplicated Firewall" (ufw).  The Ubuntu-based Vagrant machine has ufw installed on it and in the hands-on lab we will be reviewing enabling it and opening ports so your applications will run!  Please note that this sits on top of iptables [Linux iptables](https://www.geeksforgeeks.org/iptables-command-in-linux-with-examples/) which is the tool that manages the host-based firewall on Linux!  While iptables are a lot more powerful and configurable ufw is a really simple tool for updating basic firewall rules.

   - [Windows Firewall](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/)

        Though we will be utilizing firewall tech in Linux this week many of these concepts exist within the Windows ecosystem too!  They just implement it slightly differently in their Windows Firewall application!

   - [Postman](https://www.postman.com/)

        This is a useful tool for testing REST APIs!  You can run any of your GET/POST/PUT/DELETE commands from a graphical User interface (GUI) and save them as a "collection".  I have included a collection which you can use to test this REST API and collect network traffic.

   - [Wireshark](https://www.wireshark.org/)
  
         Please download Wireshark as you will be utilizing this to read network traffic!

   - [Vagrant VMs](https://www.vagrantup.com/)

        This assignment will utilize a "Vagrant" virtual machine I have included in this repository.  You will also need [Virtualbox](https://www.virtualbox.org/) installed as your "Virtualization Provider".  Vagrant is a useful tool for software developers to share applications between themselves and not need to worry about different device configurations as they can develop their software on the same platform via the virtual machine!  Though Docker or other Containerization technologies are widely used today Vagrant is still useful when you need full OS functionality or (in our case) the ability to control other host-level configurations like the firewall!



3. **Complete the following tasks**:

   - Please be sure to install Virtualbox and Vagrant on your personal machines.  Virtualbox will be the default provider for the Vagrant VM I have setup for this assignment.  The Vagrant VM (configured in the Vagrantfile in this repository) contains a configuration for setting up a basic Ubuntu Linux VM and installing "Flask"(a Python web framework) and spinning up the basic REST API I have coded there.  

   - Please install Wireshark and Postman from the links above.  Once Wireshas has finished installing please start your "capture".  We will leave Wireshark listening to your network traffic through this assignment.

   - "Clone" this GitHub repository to your personal machine [Basic Cloning Instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

   - Once you have a local repository of this project on your personal machine navigate into it via a terminal (Mac/Linux) or Command-Line window (Windows) and run the following command which will spin-up the Ubuntu machine!

    ```bash
     vagrant up

    ```

   - Next please ssh into your Vagrant vm and run the following commands:

   ```bash
    vagrant ssh

    (you should be ssh'd into your machine)

    ifconfig

    (collect your IP address)
   ```

   Look for the line which gives your your IP address.  Should be something like: 192.168.X.X. 

   - Next let's validate the Flask API is running with:

   ```bash

   curl <Your IP address>:5000/students
   ```

   This should return a JSON list of students.  Assuming it does then your Fask API is running and returning data!  

   - Next run the following to exit your vagrant machine and go back to your personal machine.

   ```bash
   exit
   ```

   - Please open the collection in Postman and replace the "base_url" current variable under the collection header  with your IP address.  I.E. if your Vagrant machine IP address is 192.168.2.56 please replace http://127.0.0.1:5000 with http://192.168.2.56:5000 

   - Now that your IP address has been updated please try running the "Get Students" command in Postman.  What doyou get in response?  Probably nothing right?  Why would that be?  

   - use the "vagrant ssh" command in your terminal to go back into the Vagrant Ubuntu machine.  You were able to run the curl command before right?  Try running it again to validate the API is up and responsive.  If it is then we're likely dealing with a firewall issue!

   - Now we're going to enable the firewall.  Please run the following:

   ```bash

   sudo ufw allow 22/tcp
   sudo ufw allow 5000/tcp
   sudo ufw enable
   sudo ufw status
   ```

   this will enable ssh and the port that Flask is listening on and you should see them as allowed with the status command.  Please run "exit" to return to your personal host machine.

   - Next re-open Postman and try running the various commands listed there.  You can try logging in (not that it actually does much other than validate username/password).  If you don't see the password then how do you think you can find it?  Is it in any other command?  Also please try updating the JSON in the "Add Students" endpoint.  

   - Finally stop the capture on WireShark and save the output to a file.  To finish the assignment for this week please take your saved output and filter it down to all of the network traffic between your Host machine and the vagrant VM!  Upload that filtered .pcap file to Brightspace along with 250 to 500 words on your thoughts regarding the content captured (in the comments seciton!). was the port being closed important?  what other ports were opened and why?  What do you think some of the ossues were regarding the content sent back and forth to the API and potential issues regarding its "readability" for someone on your network listening?

   - To completely wipe your Vagrant VM you can run the following in your terminal:

   ```bash
   vagrant destroy
   ```
