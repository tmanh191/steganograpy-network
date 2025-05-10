cd /tool
sudo make
scp server /home/ubuntu
cd /home/ubuntu
./server -P 9999
