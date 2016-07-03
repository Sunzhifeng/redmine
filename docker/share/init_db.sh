#!/usr/bin/env bash

mysql -hlocalhost -P3306 -uroot -p123456 < /share/schema.sql
