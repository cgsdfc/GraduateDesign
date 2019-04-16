#!/usr/bin/env bash

BIB_DB_PATH=bib_db

find $BIB_DB_PATH -name "*.bib" | wc -l
