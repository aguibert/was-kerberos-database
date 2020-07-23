#!/bin/sh

echo "@AGG INSIDE START SCRIPT"

su oracle << EOF
echo "Username:"
whoami

echo "Initialize oracle user(s)"
echo password | okinit -f ORACLE

echo "List principles in key table: "
oklist -k -t /etc/krb5.keytab
EOF

echo "Make credential cache accessible"
chmod 777 /tmp/krb5cc_


