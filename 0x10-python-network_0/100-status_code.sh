#!/bin/bash
# send a request and only show the status
curl -s -o /dev/null -I --w "%{http_code}" "$1"
