#!/usr/bin/env bash

IMAGE=cgsdfc/texlive2018:buaathesis
PROJECT_ROOT=/home/cgsdfc/deployment/GraduateDesign

docker run -it --rm \
    -v $PROJECT_ROOT:$PROJECT_ROOT \
    -w $PROJECT_ROOT \
    $IMAGE bash
