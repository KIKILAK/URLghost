#!/bin/bash
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"

echo -e "\n\n${greenColour} [+] instalando requirimentos necesarios... ${endColour}"
pip install -r requirements.txt