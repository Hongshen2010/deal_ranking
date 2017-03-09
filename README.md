Github repository:[deal_ranking](https://github.com/Hongshen2010/deal_ranking/blob/master/README.md)    

My project is a light-weight searchc engine for deal and discount imformation.    
The main function is returning the deal imformation based on input key words(queries).
The project contains two part. **First**, web crawling. **Second**, search result rendering and ranking.    
For the webpage crawling part, I used a python package called ***Scrapy*** to acheive this.
Scrapy is an open source web crawling module. It has many useful APIs for my project.   
First, I used scrapy to generate http requests in a generator. For webpages with ajax contents 
some costom setting will be used to define the ***xmlhttprequests*** to be sent.
        

```python
for url in urls:
    yield scrapy.Request(url = url, callback = self.parse)
```
        

After generating the requests, the next thing to do is parse the 
needed imformation from the webpages returned, for this project, the deal imformation (which 
may include item name, discount info, description and some links about it).   
Here, I used ***xpath parser*** module in Scrapy to do this. For example,   
The item names are stored in a certain span tag of some parent tag:
    
        

```python
'item': coupons.xpath('.//span[@class="notice_item"]/following-sibling::*/text()').extract()
```
    

As for the stoage, I put all the parsed imformation into a json file under Linux file system. 
The reason for this is json stores a list of javascript objects which can be converted into a 
list of dicts in python. Then all the information can be easily iterated and indexed.    
    
        
```JSON
[{"description": "Horchow offers Extra 25% Off Towel Sale. Deal ends 3/9 9:59.", "item": ["Towel Sale @ Horchow"],"imag": ["http://imgcache.dealmoon.com/fsvr.dealmoon.com/dealmoon/11e/6ec/3e9/044/bac/f76/d2c/9f1/f20/49c/2c.jpg_300_0_13_62cc.jpg"],"feature": [], "discount": "Extra 25% Off + Free Shipping","link": "http://www.dealmoon.com/exec/j/?d=610310" }]
```
        

So far, I have collected more than 3000 pieces of deals from a few websites.   
Since the rawly crawled data contains many dump words, I have to run several scripts to deal with it.  
Then remove the stop words from the files. 

For ranking the IR results, I will try simple tf*idf first. 
The raw data stored in several big .json files. Therefore, I need to split the single .json file into 
many small parts, recording the frequency of each word in each small file and then merge them together.   
When doing the counting I will use some stemming tools to reduce the vocabulary pool.
I am currently under the process of designing the data structure for this.    

I also made a simple demo to define the way of showing the search results. This demo is based on flask and sqlite.

Search result rendering, key word is dell. For here, I use the sql query to do this:   
```SQL
SELECT * From coupons WHERE item LIKE \'%' + ide + '%\'
```    
![alt text](https://github.com/Hongshen2010/deal_ranking/blob/master/2017-03-08%2022-02-21_dell.png =129x105)
