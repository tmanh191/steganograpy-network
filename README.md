## Cài đặt module từ GitHub và chạy Lab

Bước 1: Truy cập thư mục Labtainer Student
--------------------------------------------------
cd ~/labtainer/labtainer-student

Bước 2: Tải file imodule.tar từ GitHub
--------------------------------------------------
Cách 1: Dùng lệnh imodule
    imodule https://github.com/tmanh191/steganograpy-network/raw/main/imodule.tar

Cách 2: Dùng wget và giải nén thủ công
    wget https://github.com/tmanh191/steganograpy-network/raw/main/imodule.tar
    tar -xvf imodule.tar
    cp -r mmo_network_steg/ detect_mmo_stegano/ detect_lostpacket_stegano/ lp_network_steg/ ~/labtainer/trunk/labs/

Bước 3: Chạy bài Lab
--------------------------------------------------
labtainer -r
--------------------------------------------------
Hướng dẫn thực hành nằm trong thư mục docs của mỗi bài
