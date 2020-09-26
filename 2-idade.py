#!/usr/bin/python3

from datetime import datetime

hoje = datetime.now()
nascimento = datetime(year=2007, month=12, day=6)
print((hoje-nascimento).days)
