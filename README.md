# Weathermaan  

## About the Project  
This is a command-line weather data analysis tool for Lahore.  
It reads daily weather data stored in `.txt` files and generates reports such as:  
- Highest & lowest temperature of a year  
- Monthly average temperature and humidity  
- Visual bar charts of daily temperatures  



## How it Works  
This program reads Lahore's weather data from text files and displays results based on the command you give.  


## How to Run  
python main.py <command> <year>
python main.py <command> <year/month>




## Commands  

- **`-a <year>`** → Shows the **highest temperature**, **lowest temperature**, and **highest humidity** for the year.  
   python main.py -a 2020
 

- **`-b <year/month>`** → Shows the **average highest temperature**, **average lowest temperature**, and **average humidity** for the month.  
  python main.py -b 2020/06
  

- **`-c <year/month>`** → Displays a **bar chart** of daily high and low temperatures   
   python main.py -c 2020/07
  

- **`-d <year/month>`** → Displays **combined high and low temperature bars** for each day on one line.  
  python main.py -d 2020/08




# Requirements  both for window and  Mac/Linux 

# Install all packages from `requirements.txt`  

pip install -r requirements.txt


# Install an individual package  

pip install <package-name>


**Example:**  

pip install colorama


# Virtual Environment Setup On Windows  

1. Create a Virtual Environment
  python -m venv .venv

2. Activate the Virtual Environment
  .venv\Scripts\Activate

3. Deactivate the Virtual Environment
  deactivate


# Virtual Environment Setup On Mac/Linux  

1. Create a Virtual Environment
  python3 -m venv .venv

2. Activate the Virtual Environment
  source .venv/bin/activate

3. Deactivate the Virtual Environment
  deactivate

