#!/bin/bash

if [ -z "$BACKEND_URL" ]
then
  echo "[INFO]: no BACKEND_URL defined"
else
  echo "[INFO]: BACKEND_URL is set to ${BACKEND_URL}"
  #search for the file containing the url of back
  file=`grep -rl http://localhost:5000 src`
  #replace string
  sed -i "s#http://localhost:5000#${BACKEND_URL}#g" $file
fi

#add homepage (since app is not deployed at root level)
if [ -z "$HOMEPAGE" ]
then
  echo "[INFO]: deployment is supposed to be at root level"
else
  echo "[INFO]: homepage is set to ${HOMEPAGE}"
  lineCount=`cat package.json|wc -l`
  nbToKeep=`expr $lineCount - 1`
  head -$nbToKeep package.json > package.json
  echo "  ,\"homepage\": \"${HOMEPAGE}\"" >>package.json
  echo '}'>>package.json
fi