week_temperature={'월':25.5,'화':28.3,'수':33.2,'목':32.1,'금':17.3,'토':35.3,'일':33.3}

print("-"*60)
for key in week_temperature.keys():
    print(f"\t{key}",end="\t")
print()
print("-"*60)
for val in week_temperature.values():
    print(f"   {val}", end="\t")
print()
print("-" * 60)