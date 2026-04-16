#!/usr/bin/env bash

cd /home/joshua/infosite
source .venv/bin/activate

rm -f ./update-stock.log
python ./bigcommerce_inventory.py | tee ./update-stock.log
