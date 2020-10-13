import csv 
          
field_names = ['un', 'ip'] 
          
credz = [
        {"un": "bender", "ip": "10.10.2.3"}, 
        {"un": "zoidberg", "ip": "10.10.2.5"},
        {"un": "fry", "ip": "10.10.2.4"}
        ]
          
with open('credz.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names) 
    writer.writeheader() 
    writer.writerows(credz) 
