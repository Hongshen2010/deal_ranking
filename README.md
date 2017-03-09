Github repository:  [deal_ranking](https://github.com/Hongshen2010/deal_ranking/blob/master/README.md)    

My project is a light-weight searchc engine for deals and discount imformation.    
The main function is returning the deal imformation based on the key words(queries) input by the user.
The project contains two part.     
    
**First**, web crawling.     
**Second**, search result rendering and ranking.    
    
For the webpage crawling part, I used a python package called ***Scrapy*** to acheive this.
Scrapy is an open source web crawling module. It has many useful APIs for my project.   
First, I used scrapy to generate http requests in a generator. For webpages with ajax contents 
some costom setting will be used to define the ***xmlhttprequests*** to be sent.
        

```python
for url in urls:
    yield scrapy.Request(url = url, callback = self.parse)
```
        

After generating the requests, the next thing to do is parse the 
needed imformation from the returned responses. For this project, the deal imformation may include
item name, discount info, description and some links about it.   
Here, I used ***xpath parser*** module in Scrapy to do this. For example,   
For example, the item names are stored in a certain span tag of some parent tag:
    
        

```python
'item': coupons.xpath('.//span[@class="notice_item"]/following-sibling::*/text()').extract()
```
    

As for the data stoage, I put all the parsed imformation into several json files under Linux file system. 
The reason for choosing json is that json stores a list of javascript objects which can be converted into a 
list of dicts in python. Then all the information can be easily iterated and indexed.    
The following is an example of one piece of the parsed deals.    
    
        
```JSON
{
    "description": "Horchow offers Extra 25% Off Towel Sale. Deal ends 3/9 9:59.",     
    "item": ["Towel Sale @ Horchow"],    
    "imag": ["http://imgcache.dealmoon.com/fsvr.dealmoon.com/dealmoon/11e/6ec/3e9/044/bac/f76/d2c/9f1/f20/49 /2c.jpg_300_0_13_62cc.jpg"],    
    "feature": [],    
    "discount": "Extra 25% Off + Free Shipping",    
    "link": "http://www.dealmoon.com/exec/j/?d=610310" 
}
```
        

So far, I have collected about 3000 pieces of deals from a few websites which cover many categories.   
Since the rawly crawled data contains many dump words, I have to run several scripts to deal with it.  
Then remove the stop words from the files.    

For **ranking** the IR results, I will try simple **tf*idf** modle first.    
Since some pieces of deals may contain coupons codes in the des, such deals will appear in a more significant position than those without a
explicit coupon code.     
For example:

```JSON
{
    "description": "Sephora.com offers the Yves Saint Laurent Vinyl Cream Lip Stain 
                    via coupon code \"BARECLASSIC\".",
    "item": ["Yves Saint Laurent Volupt  Tint-in-Balm @ Sephora.com"],
    "imag": ["http://imgcache.dealmoon.com/fsvr.dealmoon.com/dealmoon/ec9/161/467/c0d/2b0/59e/f39/dae/8b3/102/14.jpg_300_0_13_73c0.jpg"],
    "feature": [],
    "discount": "$34",
    "link": "http://www.dealmoon.com/exec/j/?d=610026"
}
```
The raw data stored in several big .json files. Therefore, I need to split these big .json files into 
many small parts, recording the statistical information of each word in each small file and then merge them together.   
When doing the counting I will use some stemming tools to reduce the vocabulary pool.
I am currently under the process of designing the data structure for this process.    

I also made a simple demo to define the way of showing the search results. This demo is based on flask and sqlite.

Search result rendering, key word is dell. For here, I use the sql query to do this:    

```SQL
SELECT * From coupons WHERE item LIKE \'%' + ide + '%\'
```    

![alt text](https://github.com/Hongshen2010/deal_ranking/blob/master/2017-03-08%2022-02-21_dell.png?raw=true)
