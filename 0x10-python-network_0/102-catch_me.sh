#!/bin/bash
# PUT METHOD is allowed
curl -sLX PUT -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
