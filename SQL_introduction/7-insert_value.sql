#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

read -p "Enter MySQL username: " mysql_user
read -sp "Enter MySQL password: " mysql_password
echo

mysql -h localhost -u "$mysql_user" -p"$mysql_password" -D "$1" << EOF
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
EOF

