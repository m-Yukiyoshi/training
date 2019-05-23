#!/usr/bin/env python

from subprocess import call

for command in ("echo 1 > command1","echo 2 > command2","cat command* > merge"):
    call(command, shell=True)
