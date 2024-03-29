base-flask
==========

Base Flask project using Vagrant and Ansible to configure a VM

Requirements
============
* VirtualBox
* Ansible

Usage
=====
1. Clone this repo
2. Run this command:

        vagrant up

3. Connect to server with this command:

        vagrant ssh
        
4. After SSH'ing to server, enable project's virtual env:

        source /srv/venv/base-project/bin/activate
        
5. Run Flask project:

        cd /vagrant
        python app.py
6. Connect to application by browsing to this address: [http://localhost:8000](http://localhost:8000)

The directory where Vagrantfile is located will be linked to the /vagrant directory inside the VM. Modifications to the files in these linked directories will be visible from inside and outside of the VM.
