import pandas as pd


def excel_to_array(file_path, sheet_name=None):
    try:
        # Read the Excel file into a pandas DataFrame
        if sheet_name:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(file_path)
        
        # Convert the DataFrame to a two-dimensional array (list of lists)
        array_data = df.values.tolist()
        
        return array_data
    except Exception as e:
        return str(e)

# Example usage:
file_path = 'Nauczyciele.xlsx'
sheet_name = 'Arkusz1'  # Replace with the name of your Excel sheet
temp = []
result = excel_to_array(file_path, sheet_name)
if isinstance(result, list):
    for row in result:
        # print(row)
        temp.append(row)
else:
    print(f"Error: {result}")

# lista.sort(key=lambda x: x[0])
lista = []
for i, x in enumerate(temp):
    if x[0] in [naucz[0] for naucz in lista]:
        for naucz in lista:
            if naucz[0] == x[0]:
                naucz[1].append(x[1])
    else:
        lista.append([x[0], [x[1]]])


# remove duplicates in lista
for i, x in enumerate(lista):
    for j, y in enumerate(lista):
        if i != j and x[0] == y[0]:
            lista.pop(j)

for i, x in enumerate(lista):
    print(i+1, x)

with open("lista.txt", "w", encoding='UTF-8') as f:
    for i, naucz in enumerate(lista):
        przedmioty = ""
        for przedmiot in naucz[1]:
            przedmioty += f"<li style='text-align: left;'>{przedmiot}</li>\n\t\t\t"

        string = f"""
<tr>
    <td style="text-align: center;"><strong>{i+1}.</strong></td>
    <td style="text-align: center;"><strong>{naucz[0]}</strong></td>
    <td>
        <ul>
            {przedmioty}
        </ul>
    </td>
</tr>"""
        
        f.write(string)