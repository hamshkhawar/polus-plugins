#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/scaled-nyxus-plugin:${version}