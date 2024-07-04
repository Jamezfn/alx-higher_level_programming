#!/bin/bash
# makes request to 0.0.0.0:5000/catch_me tht get message you got me!
curl -sL -x PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
