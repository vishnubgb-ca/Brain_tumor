from extract_data import extract_data

def analyse():
   try:
      url = extract_data()
      print(url)
  except:
      print("Error")

analyse()
