#!/bin/bash

if [ -z "$BACKEND_URL" ]
then
  echo "[INFO]: no BACKEND_URL defined"
else
  echo "[INFO]: BACKEND_URL is set to ${BACKEND_URL}"
  for file in $(grep -rl http://localhost:5000 build)
  do
    echo "[INFO]: change is applied in "$file
    sed -i "s#http://localhost:5000#${BACKEND_URL}#g" $file
  done
fi

if [ -z "$HOMEPAGE_ROOT" ]
then
  echo "[INFO]: deployment is supposed to be at root level"
else
  echo "[INFO]: homepage root is set to ${HOMEPAGE_ROOT}"
  for file in $(grep -rl RootOfYourApp build)
  do
    echo "[INFO]: change is applied in "$file
    sed -i "s#RootOfYourApp#${HOMEPAGE_ROOT}#g" $file
  done
fi