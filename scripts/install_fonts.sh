#!/usr/bin/env bash

PROJECT_FONTS_DIR=fonts
USER_FONTS_DIR=$HOME/.fonts

cp $PROJECT_FONTS_DIR/* $USER_FONTS_DIR

fc-cache -vf $USER_FONTS_DIR
