import requests
import xmltodict
import re
from bs4 import BeautifulSoup


class VolusionError(Exception):
    pass


product_api = "http://www.lceperformance.com/net/WebService.aspx?Login=joshkogut@lcengineering.com&EncryptedPassword=37710E05D6FE636A842B6BF582F4A53B9A5DC17232F54BF3098720A14759E0C6&EDI_Name=Generic\Products&SELECT_Columns=p.LastModBy,p.LastModified,p.ProductCode,p.ProductName,pd.ProductDescription,pe.ProductPrice,pm.ExtInfo,pm.ProductFeatures,pm.TechSpecs"


def product_info():
    infos = []
    NextPage = True
    while NextPage:
        response = requests.get(product_api)
        soup = BeautifulSoup(response.text, features="xml")
        data = soup.find_all("Products")

        # data = xmltodict.parse(response.content)
        for product in data:
            info = {}
            for child in product.children:
                info[child.name] = child.text
            infos.append(info)

        """work =  data['xmldata']['Products']

		infos += work
		NextPage = len(work)>=100 and len(infos)<300
		print("%s products downloaded" % len(work))
		"""

    return infos


# TODO, map dict for each product
stock_api = "https://www.lceperformance.com/net/WebService.aspx?Login=joshkogut@lcengineering.com&EncryptedPassword=37710E05D6FE636A842B6BF582F4A53B9A5DC17232F54BF3098720A14759E0C6&Import=Update"


def update_stock(products):
    headers = {"Content-Type": "application/xml"}

    xml = '<?xml version="1.0" encoding="utf-8" ?><xmldata>'
    for code, stock, supplier, vendorsku in products:
        xml += "<Products>"
        xml += "	<ProductCode>%s</ProductCode>" % code
        xml += "	<StockStatus>%s</StockStatus>" % stock
        xml += (
            "	<ProductDescription_AbovePricing>by %s</ProductDescription_AbovePricing>"
            % supplier
        )
        xml += "	<ProductManufacturer>%s</ProductManufacturer>" % supplier
        xml += "	<Vendor_PartNo>%s</Vendor_PartNo>" % vendorsku
        xml += "</Products>"
    xml += "</xmldata>"
    r = requests.post(stock_api, data=xml, headers=headers)
    if r.status_code != 200:
        raise VolusionError("Server didn't return a 200")
    return r


# TODO, make functional
# stock_api = "https://www.lceperformance.com/net/WebService.aspx?Login=joshkogut@lcengineering.com&EncryptedPassword=37710E05D6FE636A842B6BF582F4A53B9A5DC17232F54BF3098720A14759E0C6&Import=Update"
def update_price(products):
    pass

    """headers = {'Content-Type':'application/xml'}

	xml = '<?xml version="1.0" encoding="utf-8" ?><xmldata>'
	for (code,stock,supplier, vendorsku) in products:
		xml += '<Products>'
		xml += '	<ProductCode>%s</ProductCode>' % code
		xml += '	<StockStatus>%s</StockStatus>' % stock
		xml += '	<ProductDescription_AbovePricing>by %s</ProductDescription_AbovePricing>' % supplier
		xml += '	<ProductManufacturer>%s</ProductManufacturer>' % supplier
		xml += '	<Vendor_PartNo>%s</Vendor_PartNo>' % vendorsku
		xml += '</Products>'
	xml += '</xmldata>'
	r =  requests.post( stock_api, data=xml, headers=headers )
	if r.status_code!=200:
		raise VolusionError("Server didn't return a 200")
	return r"""
