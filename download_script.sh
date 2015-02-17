#! /bin/bash

PARTIAL_URL="https://www.eeb.ucla.edu/seminars.php?id="
PAGE_ID=1
while [ $PAGE_ID -le 800 ]; do
	FULL_URL=$PARTIAL_URL:$PAGE_ID
	curl $FULL_URL > $PAGE_ID.html
	PAGE_ID=$((PAGE_ID+1))
done
