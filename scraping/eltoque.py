import requests
from bs4 import BeautifulSoup

def main():
    url = "https://eltoque.com"
    
    sesion = requests.Session()
    response = sesion.get(url)
    
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
        
            table = soup.find("table", attrs={"class": "sc-672dda73-2 eeMZSu table table-borderless"})
            
            tbody = table.find_next("tbody")
            
            tr = tbody.find_all_next("tr")
            
            price_eur = tr[0].find_next("span", attrs={"class": "price-text"})
            price_usd = tr[1].find_next("span", attrs={"class": "price-text"})
            price_mlc = tr[2].find_next("span", attrs={"class": "price-text"})
            
            converted_price_eur = float(price_eur.text.split(" ")[0])
            converted_price_usd = float(price_usd.text.split(" ")[0])  
            converted_price_mlc = float(price_mlc.text.split(" ")[0])       
            
            print(f"EUR: {converted_price_eur}, USD: {converted_price_usd}, MLC: {converted_price_mlc}")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()