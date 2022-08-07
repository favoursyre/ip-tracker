# IP Tracker
## Disclaimer
This script is for educational purposes only, I don't endorse or promote it's illegal usage

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Languages](#languages)
4. [Installations](#installations)
5. [Usage](#usage)
6. [Run](#run)

## Overview

This script allows an attacker to locate the IP Address of a target geographically

## Features

- Gives a comprehensive details of the geographical location of the stipulated IP address

## Languages

- Python 3.9.7

## Installations

```shell
git clone https://github.com/favoursyre/ip-tracker.git && cd ip-tracker
```

```shell
pip install geopy
pip install geolite2
```

## Usage

```python
ip = None #Use this setup if you want to use the default public ip address of the target system
#OR
ip = r"104.243.35.168" #Use this setup to use a particular ip address

locate, country = locate(ip)
print(f"Country: {country}")
print("Location", locate)
```

## Run

```shell
python ip_tracker.py
```

![Result](https://drive.google.com/uc?export=download&id=1zZEkqhbaUTo8BslseKlxkRF0Me09aK6F)
