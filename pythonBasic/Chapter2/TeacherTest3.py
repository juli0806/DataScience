hongID="881129-10668234"

base_index= hongID.index('-')
hongID1=hongID[:base_index]
hongID2=hongID[base_index+1:]
print(f"연월일 부분: {hongID1}")
print(f"숫자 부분: {hongID2}")
