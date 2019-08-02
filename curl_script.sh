#! /bin/sh

SITE_BASE_URL="https://limitless-springs-53595.herokuapp.com"

echo "Logging in using the demo user credentials and fetching JWT token: \n"

# The demo username and password are hardcoded here so that we can give a demo
# of how to fetch a token using curl.
USERNAME="shiva"
PASSWORD="limitless-springs"

echo "username: $USERNAME"
echo "password: $PASSWORD"

token_res=`curl -s -X POST "$SITE_BASE_URL/api-token-auth/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"username\": \"$USERNAME\", \"password\": \"$PASSWORD\"}"`

token=`echo $token_res | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["token"])'`
echo "\ntoken: $token\n"

IFSC="ABHY0065001"
echo "Searching for bank with IFSC $IFSC\n"
search_with_ifsc_res=`curl -s -X GET "$SITE_BASE_URL/bank/ABHY0065001/" -H "accept: application/json" -H "Authorization: JWT $token"`

echo $search_with_ifsc_res | python -m json.tool


# Sample values for limit, offset, bank, city
limit=10
offset=0
bank="ABHYUDAYA COOPERATIVE BANK LIMITED"
city="MUMBAI"
search_with_name_and_city_res=`curl -G -s -X GET "$SITE_BASE_URL/bank/" -H "accept: application/json" \
                            --data-urlencode "bank_name=$bank" --data-urlencode "city=$city" \
                            --data-urlencode "offset=$offset" --data-urlencode "limit=$limit" \
                            -H "Authorization: JWT $token"`

echo "\n Searching with following data: limit=$limit offset=$offset bank=$bank city=$city\n"
echo $search_with_name_and_city_res | python -m json.tool


offset=10
echo "\n Now offset is 10. Data: limit=$limit offset=$offset bank=$bank city=$city\n"
search_with_name_and_city_res=`curl -G -s -X GET "$SITE_BASE_URL/bank/" -H "accept: application/json" \
                            --data-urlencode "bank_name=$bank" --data-urlencode "city=$city" \
                            --data-urlencode "offset=$offset" --data-urlencode "limit=$limit" \
                            -H "Authorization: JWT $token"`
echo $search_with_name_and_city_res | python -m json.tool

