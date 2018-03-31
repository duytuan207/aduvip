#!/usr/bin/env bash


bin=$( dirname $0 )
cd $bin;
PING=`ping -c 3 $1 | grep '0 received' | wc -l`
echo $PING