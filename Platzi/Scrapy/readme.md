# Scrapy

To use the scrapy shell, we need navigate to the folder where we create the virtual environment. Then we write:

```python
scrapy shell "url"
```

Then we have the following available methods

```
scrapy
crawler
item
request
response
settings
spider
```

for example, if we apply the object `response`

```python
response.xpath('//h1/a/text()').get
```

we get the `h1` element inside the website

If we have several items, we apply the `getall()` method

```python
 response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
```

we get the encoding of the website by typing

```python
request.encoding
```

another examples

```
response.method
response.status
response.headers
response.body


```

