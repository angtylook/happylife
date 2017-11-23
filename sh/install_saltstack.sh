#! /bin/bash
# install saltstack minion usage:
# install_saltstack version master minion
curl -L https://bootstrap.saltstack.com -o bootstrap.sh
sudo bash bootstrap.sh stable ${1}
sudo echo "master: ${2}" > /etc/salt/minion.d/minion.conf
sudo echo "id: ${3}" >> /etc/salt/minion.d/minion.conf
sudo service salt-minion restart


