import requests
from bs4 import BeautifulSoup
import pandas

base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
records = []

for page in range(0, 30, 10):

    print(base_url + str(page) + ".html")

    request = requests.get(
        base_url + str(page) + ".html",
        headers={
            "User-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
        },
    )
    content = request.content
    soup_data = BeautifulSoup(content, "html.parser")
    all_divs = soup_data.find_all("div", {"class": "propertyRow"})

    for item in all_divs:
        data = {
            "Address": item.find_all("span", {"class": "propAddressCollapse"})[0].text,
            "Locality": item.find_all("span", {"class": "propAddressCollapse"})[1].text,
            "Price": item.find("h4", {"class": "propPrice"})
            .text.replace("\n", "")
            .replace(" ", ""),
        }

        if item.find("span", {"class": "infoBed"}) is not None:
            data["Beds"] = item.find("span", {"class": "infoBed"}).find("b").text
        else:
            data["Beds"] = None

        if item.find("span", {"class": "infoSqFt"}) is not None:
            data["Area"] = item.find("span", {"class": "infoSqFt"}).find("b").text
        else:
            data["Area"] = None

        if item.find("span", {"class": "infoValueFullBath"}) is not None:
            data["Full Baths"] = (
                item.find("span", {"class": "infoValueFullBath"}).find("b").text
            )
        else:
            data["Full Baths"] = None

        if item.find("span", {"class": "infoValueHalfBath"}) is not None:
            data["Half Baths"] = (
                item.find("span", {"class": "infoValueHalfBath"}).find("b").text
            )
        else:
            data["Half Baths"] = None

        for column_group in item.find_all("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(
                column_group.find_all("span", {"class": "featureGroup"}),
                column_group.find_all("span", {"class": "featureName"}),
            ):
                if "Lot Size" in feature_group.text:
                    data["Lot Size"] = feature_name.text

        records.append(data)
data_frame = pandas.DataFrame(records)
data_frame.to_csv("all_output.csv")
