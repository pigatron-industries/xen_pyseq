#!/bin/bash

protoc -I=. --python_out=. ConfigMessage.proto
