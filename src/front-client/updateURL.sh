#!/bin/bash

#search for the file containing the url of back
file=`grep -rl http://localhost:5000 build`
#replace string
sed -i "s#http://localhost:5000#${BACKEND_URL}#g" $file