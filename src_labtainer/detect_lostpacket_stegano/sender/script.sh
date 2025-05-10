cd /tool
sudo make
scp client /home/ubuntu
cd /home/ubuntu
./client -D 192.168.1.20 -P 9999 -s `cat message.txt` -T 50
