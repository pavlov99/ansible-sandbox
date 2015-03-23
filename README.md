# Configuration

You should have the following installed:
- [VirtualBox]
- [Vagrant]: see [Vagrant_installation] for how to install vagrant.
- [Ansible]: you can get ansible through *pip install ansible*.

[VirtualBox]:https://www.virtualbox.org
[Vagrant]:http://www.vagrantup.com/
[Vagrant_installation]:http://docs.vagrantup.com/v2/installation/index.html
[Ansible]:http://docs.ansible.com/

Install Ansible libraries (~2 min):

    $ make
    ansible-galaxy install --force --role-file=requirements.txt
    - downloading role 'timezone', owned by Stouts
    - downloading role from https://github.com/Stouts/Stouts.timezone/archive/2.0.1.tar.gz
    - extracting Stouts.timezone to ./provisioning/roles/Stouts.timezone
    - Stouts.timezone was installed successfully
      ...


After all the prerequisities met, you can boot an instant openstack developing environment (~45 min):

    $ vagrant up
    ==> default: Running provisioner: ansible...

# Deployment structure

    $ tree -L 3 /opt/<project>/
    /opt/<project>/
    ├── backend
    │   ├── current -> /opt/<project>/backend/releases/0.0.1
    │   └── releases
    │       └── 0.0.1
    ├── conf
    │   └── settings_web.py
    └── frontend
        ├── current -> /opt/<project>/frontend/releases/0.0.1
        └── releases
            └── 0.0.1

# Server Infrastructure

![alt server-configuration](../raw/develop/docs/images/server-configuration.png)

# Reference

- [how-to-make-vagrant-performance-not-suck]

[how-to-make-vagrant-performance-not-suck]:http://www.stefanwrobel.com/how-to-make-vagrant-performance-not-suck
