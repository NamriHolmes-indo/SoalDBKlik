import requests
from bs4 import BeautifulSoup
import csv

def get_table_data(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')
    
    data_list = []

    for row in rows[1:]:
        columns = row.find_all('td')
        if len(columns) >= 6:  # Memastikan ada setidaknya 6 kolom
            no = columns[0].get_text(strip=True)
            kode_kemendagri = columns[1].get_text(strip=True)
            kabupaten = columns[2].get_text(strip=True)
            provinsi = columns[3].get_text(strip=True)
            ibu_kota = columns[4].get_text(strip=True)
            kecamatan_kelurahan_desa = columns[5].get_text(strip=True)
            
            data_list.append({
                'No': no,
                'Kode Kemendagri': kode_kemendagri,
                'Kabupaten': kabupaten,
                'Provinsi': provinsi,
                'Ibu Kota': ibu_kota,
                'Kecamatan/Kelurahan/Desa': kecamatan_kelurahan_desa
            })
    
    return data_list

def export_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

url = 'https://id.wikipedia.org/wiki/Daftar_kabupaten_di_Indonesia'
table_data = get_table_data(url)
for data in table_data:
    print(data)
export_to_csv(table_data, 'kabupaten_indonesia.csv')