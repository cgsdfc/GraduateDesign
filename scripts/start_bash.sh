#!/usr/bin/env bash

IMAGE=dennis1f/sharelatex-texlive2018:latest
PROJECT_ROOT=/home/cgsdfc/deployment/GraduateDesign

docker run -it --rm \
    -v $PROJECT_ROOT:$PROJECT_ROOT \
    -w $PROJECT_ROOT \
    $IMAGE
