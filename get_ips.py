#!/usr/bin/env python
import requests
import csv

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
amazon_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "AMAZON"]
ec2_ips = [item for item in ip_ranges if item["service"] == "EC2"]

amazon_ips_ec2 = []

for ip in amazon_ips:
    for ec2_ip in ec2_ips:
        if ip == ec2_ip['ip_prefix'] and (ec2_ip['region'] == 'us-east-1' or ec2_ip['region'] == 'us-east-2'):
            amazon_ips_ec2.append(ip)

with open('amazon_ips_ec2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['IP Addresses'])
    for ip in amazon_ips_ec2:
        writer.writerow([ip])
