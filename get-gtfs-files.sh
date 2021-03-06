#!/bin/sh

OUTPUT_DIR="./gtfs-files"
rm -rf ${OUTPUT_DIR}
mkdir ${OUTPUT_DIR}
mkdir ${OUTPUT_DIR}/buses

declare -a buses=("SMBSC001")
declare -a nonbuses=("ferries" "lightrail" "nswtrains" "sydneytrains")

for bus in "${buses[@]}"
do
    mkdir ${OUTPUT_DIR}/buses/${bus}
    curl -H "Authorization: $API_AUTHORIZATION_TRANSPORT_NSW" https://api.transport.nsw.gov.au/v1/gtfs/schedule/buses/${bus} --output ${OUTPUT_DIR}/buses/${bus}/${bus}.zip
    unzip ${OUTPUT_DIR}/buses/${bus}/${bus}.zip -d ${OUTPUT_DIR}/buses/${bus}/
    find ${OUTPUT_DIR}/buses/${bus}/*txt -exec dos2unix {} \;
    python process-gtfs.py ${OUTPUT_DIR}/buses/${bus} bus
done

for nonbus in "${nonbuses[@]}"
do
    mkdir ${OUTPUT_DIR}/${nonbus}
    curl -H "Authorization: $API_AUTHORIZATION_TRANSPORT_NSW" https://api.transport.nsw.gov.au/v1/gtfs/schedule/${nonbus} --output ${OUTPUT_DIR}/${nonbus}/${nonbus}.zip
    unzip ${OUTPUT_DIR}/${nonbus}/${nonbus}.zip -d ${OUTPUT_DIR}/${nonbus}/
    find ${OUTPUT_DIR}/${nonbus}/*txt -exec dos2unix {} \;
    python process-gtfs.py ${OUTPUT_DIR}/${nonbus} ${nonbus}
done

