#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <port_number>"
    exit 1
fi

PORT=$1
./server -P "$PORT" -q 2>/dev/null | grep "sequence number" | awk '{if (NR==1) printf "%s", $NF; else printf ",%s", $NF} END {print ""}'
